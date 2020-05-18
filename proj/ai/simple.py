# -- coding: utf-8 --
from __future__ import division

import time
import random
import math

from proj.entity.map import Shape
from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction
from proj.builtin.actions import BattleItemAction
from proj.builtin.actions import BattleRestAction


def huichun(p, q):
    score = 0
    if q.hp / q.hp_max <= 0.3:
        score += max(3500, q.hp_max - q.hp)
        if p == q:
            score += 1000
    return score
    

class SimpleAI(object):

    EFFECT_MAP = {"EFFECT_HUICHUN": huichun,
                  "EFFECT_HUICHUN_DA": huichun,
                  "EFFECT_HUICHUN_XIAO": huichun}

    def __init__(self, battle):
        self.battle = battle
        self.move_scope = []
        self.connections = {}
        self.loc_clc_map = {}
        self.object_info = []
        self.person_info = []

    def skill_ranges(self, zhaoshies):
        max_attack_range = {"Friends": -1, "Enemies": -1}
        min_attack_range = {"Friends": 99, "Enemies": 99}
        for zhaoshi in zhaoshies:
            if zhaoshi.shape is None:
                continue
            tmp_range = zhaoshi.shape.attack_range()
            keylist = []
            if zhaoshi.targets != "Friends":
                keylist.append("Enemies")
            if zhaoshi.targets != "Enemies":
                keylist.append("Friends")
            for tkey in keylist:
                if max_attack_range[tkey] < tmp_range[1]:
                    max_attack_range[tkey] = tmp_range[1]
                if min_attack_range[tkey] > tmp_range[0]:
                    min_attack_range[tkey] = tmp_range[0]
        max_attack_range["All"] = max(max_attack_range["Friends"], max_attack_range["Enemies"])
        min_attack_range["All"] = min(min_attack_range["Friends"], min_attack_range["Enemies"])
        return max_attack_range, min_attack_range

    def person_in_scope(self, q_info, attack_range, attack_angle, attack_block, person_angle):
        q_angle = person_angle
        if q_angle < 0:
            q_angle += math.pi * 2
        if q_info[2] > attack_range[1] or q_info[2] < attack_range[0] or q_angle > attack_angle:
            return False
        in_scope = True
        min_d = attack_range[1]
        for blk in self.object_info:
            if blk[2] < min_d:
                min_d = blk[2]
            if attack_block == 1 and q_angle >= blk[3] and q_info[2] >= min_d:
                in_scope = False
                break
            elif attack_block == 2 and q_angle - math.pi / 180  == blk[3] and q_info[2] >= blk[2]:
                in_scope = False
                break
        return in_scope
        

    def do(self, p):
        if not self.battle.silent:
            self.move_scope, self.connections = self.battle.map.move_scope(p, style=p.move_style)

            self.person_info = []
            self.object_info = []

            # 记录所有的遮挡物信息
            for i in range(self.battle.map.x):
                for j in range(self.battle.map.y):
                    if self.battle.map.xy[i][j].object is not None:
                        self.object_info.append([(i, j), 0, 0, 0, self.battle.map.xy[i][j].object])

            # 记录所有的人物信息
            for q in self.battle.alive:
                ploc = self.battle.map.location(q)
                self.person_info.append([ploc, 0, 0, 0, q])

        maybe = self.consider(p)
        max_score = -1
        submaybe = []

        for may, score in maybe:
            if score > max_score:
                max_score = score
                submaybe[:] = []
        for may, score in maybe:
            if score == max_score:
                submaybe.append(may)
        idx = random.randint(0, len(submaybe) - 1)
        for ac in submaybe[idx]:
            if not self.battle.silent and isinstance(ac, BattleSkillAction):
                ac.scope = self.battle.map.shape(ac.ploc, ac.target, ac.skill.shape)
        return submaybe[idx]

    def consider(self, p):
        maybe = []
        maybe = self.do_emergency(p)
        if len(maybe) > 0:
            return maybe
        if self.battle.silent:
            clist = [self.do_attack_silent, self.do_item_silent, self.do_rest]
        else:
            clist = [self.do_attack, self.do_item, self.do_rest]
        for func in clist:
            m = func(p)
            if m is not None:
                for sm in m:
                    maybe.append(sm)
        return maybe

    def do_emergency(self, p):
        ret = []
        equip_a = p.equipment[0]
        skills_ava = self.battle.skill_available(p, check_cd=False)
        if equip_a is None and len(skills_ava) == 0:
            for itm in p.items:
                if "Weapon" in itm.tags:
                    tgt = self.battle.map.location(p)
                    ret.append(([BattleItemAction(subject=p, battle=self.battle, target=tgt, 
                                                  item=itm, objects=[p], scope=[tgt])], 10000))
        return ret
        
    def do_attack_silent(self, p):
        can_do = []
        if self.battle.attacked[p.id]:
            zhaoshies = []
        else:
            zhaoshies = self.battle.skill_available(p)
        for zhaoshi in zhaoshies:               
            q = random.sample(self.battle.enemies(p), 1)[0]
            qloc = self.battle.map.entity_loc[q.id]
            score = 0
            if zhaoshi.power > 0:
                score += zhaoshi.power * (min(1, 1 if zhaoshi.mp == 0 else p.mp / zhaoshi.mp))
            else:
                for effe in zhaoshi.effects:
                    if effe.tpl_id not in SimpleAI.EFFECT_MAP:
                        continue
                    score += SimpleAI.EFFECT_MAP[effe.tpl_id](p, q)
            if score == 0:
                continue
            action_list = [BattleSkillAction(subject=p, battle=self.battle, target=qloc, counter=False,
                                             skill=zhaoshi, objects=[q], scope=[qloc])]
            can_do.append((action_list, score))
        return can_do

    def do_attack(self, p):
        if self.battle.moved[p.id]:
            move_scope = []
        else:
            move_scope = self.move_scope
        can_do = []
        tmp_min_distance = 100
        tmp_loc = None
        if self.battle.attacked[p.id]:
            zhaoshies = []
        else:
            zhaoshies = self.battle.skill_available(p)
        max_attack_range, min_attack_range = self.skill_ranges(zhaoshies)

        for loc in move_scope + [self.battle.map.location(p)]:
            # 更新所有人物与遮挡物相对于行动者的向量与距离
            for ele in self.object_info + self.person_info:
                if ele[-1] == p:
                    ele[0] = loc
                eleloc = ele[0]
                #ele[1] = self.battle.map.vector(loc, eleloc)
                ele[2] = self.battle.map.distance(loc, eleloc) 

            at_least_one = False
            for q_info in self.person_info:
                tmp_distance = q_info[2]
                q = q_info[-1]
                if self.battle.is_enemy(p, q):                    
                    if tmp_distance < tmp_min_distance:
                        tmp_min_distance = tmp_distance
                        tmp_loc = loc
                    at_least_one = at_least_one or (tmp_distance <= max_attack_range["Enemies"] and \
                                                    tmp_distance >= min_attack_range["Enemies"])
                else:
                    at_least_one = at_least_one or (tmp_distance <= max_attack_range["Friends"] and \
                                                    tmp_distance >= min_attack_range["Friends"])

            if not at_least_one:
                continue

            for zhaoshi in zhaoshies:
                if (loc, zhaoshi.shape.scope, zhaoshi.shape.msputter) not in self.loc_clc_map:
                    self.loc_clc_map[(loc, zhaoshi.shape.scope, zhaoshi.shape.msputter)] = \
                      self.battle.map.shape_scope(loc, zhaoshi.shape) 
                cset = self.loc_clc_map[(loc, zhaoshi.shape.scope, zhaoshi.shape.msputter)]
                #cset = self.battle.map.circle(loc, 1, mr=max(1, zhaoshi.shape.msputter))

                # 计算所有人物与遮挡物相对于行动者X方位向量的偏移角
                for ele in self.object_info + self.person_info:
                    if ele[-1] == p:
                        continue
                    ele[3] = self.battle.map.angle(loc, (loc[0] + 1, loc[1]), ele[0]) 
                for scope in cset:
                    score = 0
                    ## 计算所有人物与遮挡物相对于行动者技能目标的偏移角
                    #for ele in self.object_info + self.person_info:
                    #    if ele[-1] == p or loc == scope:
                    #        continue
                    #    ele[3] = self.battle.map.angle(loc, scope, ele[0])
                    if zhaoshi.shape == Shape.Point and zhaoshi.sputter > 0:
                        attack_range = [0, zhaoshi.sputter]
                        attack_angle = math.pi * 2
                        scope_angle = None
                    else:
                        attack_range = zhaoshi.shape.attack_range(distance=self.battle.map.distance(loc, scope))
                        attack_angle = zhaoshi.shape.attack_angle()
                        if loc != scope:
                            scope_angle = self.battle.map.angle(loc, (loc[0] + 1, loc[1]), scope)
                        else:
                            scope_angle = 0
                    attack_block = zhaoshi.shape.block

                    self.object_info.sort(key=lambda x: x[3])
                    ql = []
                    for q_info in self.person_info:
                        if scope_angle is not None:
                            person_angle = q_info[3] - scope_angle
                        else:
                            person_angle = self.battle.map.angle(scope, (scope[0] + 1, scope[1]), q_info[0])
                        if not self.person_in_scope(q_info, attack_range, attack_angle, attack_block, person_angle):
                            continue
                        q = q_info[-1]
                        if not self.battle.skill_accept(zhaoshi, p, q):
                            continue
                        ql.append(q)
                        if zhaoshi.power > 0:
                            score += zhaoshi.power * (min(1, 1 if zhaoshi.mp == 0 else p.mp / zhaoshi.mp))
                        else:
                            for effe in zhaoshi.effects:
                                if effe.tpl_id not in SimpleAI.EFFECT_MAP:
                                    continue
                                score += SimpleAI.EFFECT_MAP[effe.tpl_id](p, q)
                    if score == 0:
                        continue
                    action_list = [BattleMoveAction(subject=p, battle=self.battle, target=loc, scope=move_scope, 
                                                    path=self.battle.map.move_trace(loc, self.battle.map.location(p), self.connections)),
                                   BattleSkillAction(subject=p, battle=self.battle, target=scope, counter=False,
                                                     skill=zhaoshi, objects=ql, ploc=loc, scope=[])]
                    can_do.append((action_list, score)) 
        if len(can_do) == 0:
            can_do.append(([BattleMoveAction(subject=p,
                                             battle=self.battle,
                                             target=tmp_loc, 
                                             scope=move_scope, 
                                             path=self.battle.map.move_trace(tmp_loc, self.battle.map.location(p), self.connections)),
                            BattleRestAction(subject=p, battle=self.battle)], int(p.mp_limit * p.mp_recover_rate_inferior)))
        return can_do

    def do_item_silent(self, p):  
        can_do = []    
        if self.battle.itemed[p.id]:
            items = []
        else:
            items = p.items
        for item in items:
            q = random.sample(self.battle.enemies(p), 1)[0]
            qloc = self.battle.map.entity_loc[q.id]
            score = 0
            for effe in item.effects:
                if effe.tpl_id not in SimpleAI.EFFECT_MAP:
                    continue
                score += SimpleAI.EFFECT_MAP[effe.tpl_id](p, q)
            if score == 0:
                continue
            action_list = [BattleItemAction(subject=p, battle=self.battle, target=qloc, 
                                            item=item, objects=[q], scope=[qloc])]
            can_do.append((action_list, score)) 
        return can_do
     
    def do_item(self, p):                 
        if self.battle.moved[p.id]:
            move_scope = []
        else:
            move_scope = self.move_scope
        can_do = []
        tmp_min_distance = 100
        tmp_loc = None
        if self.battle.itemed[p.id]:
            items = []
        else:
            items = p.items
        max_attack_range, min_attack_range = self.skill_ranges(items)
        for loc in move_scope + [self.battle.map.location(p)]:
            # 更新所有人物与遮挡物相对于行动者的向量与距离
            for ele in self.object_info + self.person_info:
                if ele[-1] == p:
                    ele[0] = loc
                eleloc = ele[0]
                ele[2] = self.battle.map.distance(loc, eleloc)

            at_least_one = False
            for q_info in self.person_info:
                tmp_distance = q_info[2]
                q = q_info[-1] 
                if self.battle.is_enemy(p, q):
                    if tmp_distance < tmp_min_distance:
                        tmp_min_distance = tmp_distance
                        tmp_loc = loc
                    at_least_one = at_least_one or (tmp_distance <= max_attack_range["Enemies"] and \
                                                    tmp_distance >= min_attack_range["Enemies"])
                else:
                    at_least_one = at_least_one or (tmp_distance <= max_attack_range["Friends"] and \
                                                    tmp_distance >= min_attack_range["Friends"])

            if not at_least_one:
                continue

            for item in items:
                if item.shape is None:
                    continue
                if (loc, item.shape.scope, item.shape.msputter) not in self.loc_clc_map:
                    self.loc_clc_map[(loc, item.shape.scope, item.shape.msputter)] = \
                      self.battle.map.shape_scope(loc, item.shape)
                cset = self.loc_clc_map[(loc, item.shape.scope, item.shape.msputter)]
                for scope in cset:
                    score = 0
                    if item.shape == Shape.Point and item.sputter > 0:
                        attack_range = [0, item.sputter]
                        attack_angle = math.pi * 2
                        scope_angle = None
                    else:
                        attack_range = item.shape.attack_range(distance=self.battle.map.distance(loc, scope))
                        attack_angle = item.shape.attack_angle()
                        if loc != scope:
                            scope_angle = self.battle.map.angle(loc, (loc[0] + 1, loc[1]), scope)
                        else:
                            scope_angle = 0
                    attack_block = item.shape.block

                    self.object_info.sort(key=lambda x: x[3])
                    ql = []
                    for q_info in self.person_info:
                        if scope_angle is not None:
                            person_angle = q_info[3] - scope_angle
                        else:
                            person_angle = self.battle.map.angle(scope, (scope[0] + 1, scope[1]), q_info[0])
                        if not self.person_in_scope(q_info, attack_range, attack_angle, attack_block, person_angle):
                            continue
                        q = q_info[-1]
                        if q is None or not self.battle.skill_accept(item, p, q):
                            continue
                        ql.append(q)
                        for effe in item.effects:
                            if effe.tpl_id not in SimpleAI.EFFECT_MAP:
                                continue
                            score += SimpleAI.EFFECT_MAP[effe.tpl_id](p, q)
                    if score == 0:
                        continue
                    action_list = [BattleMoveAction(subject=p, battle=self.battle, target=loc, scope=move_scope, 
                                                    path=self.battle.map.move_trace(loc, self.battle.map.location(p), connections)),
                                   BattleItemAction(subject=p, battle=self.battle, target=scope, 
                                                    item=item, objects=ql, scope=zshape)]
                    can_do.append((action_list, score)) 
        return can_do

    def do_rest(self, p):
        return [([BattleRestAction(subject=p, battle=self.battle)], int(p.mp_limit * p.mp_recover_rate))]
