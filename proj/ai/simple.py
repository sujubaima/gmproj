# -- coding: utf-8 --
from __future__ import division

import time
import random
import math
import copy

from proj.entity import SkillType
from proj.entity.map import Shape
from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction
from proj.builtin.actions import BattleItemAction
from proj.builtin.actions import BattleRestAction


def huichun(p, q, effe, battle):
    score = 0
    if q.hp / q.hp_max <= 0.3:
        score += max(3500, q.hp_max - q.hp)
        if p == q:
            score += 1000
    return score


def mohewuliang(p, q, effe, battle):
    if effe.level < battle.turnidx:
        power = 750 + 125 * (2 - effe.level)
        return power * min(1, p.mp / power * 0.4)
    else:
        return 1
    

class SimpleAI(object):

    EFFECT_MAP = {"EFFECT_HUICHUN": huichun,
                  "EFFECT_HUICHUN_DA": huichun,
                  "EFFECT_HUICHUN_XIAO": huichun,
                  "EFFECT_MOHEWULIANG": mohewuliang,
                  "EFFECT_MOHEWULIANG_DA": mohewuliang,
                  "EFFECT_MOHEWULIANG_XIAO": mohewuliang,}

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

    def angle_in_sector(self, start, end, angle):
        angle_beyond = start > end
        if not angle_beyond and (angle < start or angle > end):
            return False
        if angle_beyond and angle < start and angle > end:
            return False
        return True

    def person_in_scope(self, q_info, attack_range, attack_angle, attack_block, person_angle, scope_angle, distance_function):
        if scope_angle is None:
            scope_angle = 0
        q_distance = distance_function(q_info)
        q_angle = person_angle
        a_angle = attack_angle + scope_angle
        angle_beyond = False
        if a_angle > math.pi * 2:
            a_angle -= math.pi * 2
            angle_beyond = True
        if q_distance > attack_range[1] or q_distance < attack_range[0]:
            return False
        #if not angle_beyond and (q_angle < scope_angle or q_angle > a_angle):
        #    return False
        #if angle_beyond and q_angle > a_angle and q_angle < scope_angle:
        #    return False
        if not self.angle_in_sector(scope_angle, a_angle, q_angle):
            return False
        in_scope = True
        min_d = attack_range[1]
        for blk in self.object_info:
            b_distance = distance_function(blk)
            b_angle = blk[3]
            if b_distance < attack_range[0] or b_distance > attack_range[1]:
                continue
            #if not angle_beyond and (b_angle < scope_angle or b_angle > a_angle):
            #    continue
            #if angle_beyond and b_angle > a_angle and b_angle < scope_angle:
            #    continue
            if not self.angle_in_sector(scope_angle, a_angle, b_angle):
                continue
            if b_distance < min_d:
                min_d = b_distance
            if attack_block == 1 and self.angle_in_sector(scope_angle, q_angle, b_angle) and q_info[2] >= min_d:
                in_scope = False
                break
            elif attack_block == 2 and q_angle == b_angle and q_info[2] >= b_distance:
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
            if self.battle.silent:
                continue
            if isinstance(ac, BattleSkillAction) or isinstance(ac, BattleItemAction):
                ac.scope = self.battle.map.shape(ac.ploc, ac.target, ac.skill.shape)
                #print(ac.debug_info)
                #print(ac.person_info)
                #print(ac.object_info)
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

    def do_skill_silent(self, p, skills, isitem=False):
        if isitem:
            theaction = BattleItemAction
        else:
            theaction = BattleSkillAction
        can_do = []
        for skill in skills:
            q = random.sample(self.battle.enemies(p), 1)[0]
            qloc = self.battle.map.entity_loc[q.id]
            score = 0
            if not isitem and skill.power > 0:
                score += skill.power * (min(1, 1 if skill.mp == 0 else p.mp / skill.mp))
            for effe in skill.effects:
                if effe.tpl_id not in SimpleAI.EFFECT_MAP:
                    continue
                score += SimpleAI.EFFECT_MAP[effe.tpl_id](p, q, effe, self.battle)
            if score == 0:
                continue
            action_list = [theaction(subject=p, battle=self.battle, target=qloc, type=SkillType.Normal,
                                     skill=skill, objects=[q], scope=[qloc])]
            can_do.append((action_list, score))
        return can_do
        
    def do_skill(self, p, skills, isitem=False, with_default=True):
        if isitem:
            theaction = BattleItemAction
        else:
            theaction = BattleSkillAction
        if self.battle.moved[p.id]:
            move_scope = []
        else:
            move_scope = self.move_scope
        can_do = []
        tmp_min_distance = 100
        tmp_locs = []
        max_attack_range, min_attack_range = self.skill_ranges(skills)

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
                        tmp_locs = [loc]
                    elif tmp_distance == tmp_min_distance:
                        tmp_locs.append(loc)
                    at_least_one = at_least_one or (tmp_distance <= max_attack_range["Enemies"] and \
                                                    tmp_distance >= min_attack_range["Enemies"])
                else:
                    at_least_one = at_least_one or (tmp_distance <= max_attack_range["Friends"] and \
                                                    tmp_distance >= min_attack_range["Friends"])

            if not at_least_one:
                continue

            for skill in skills:
                if (loc, skill.shape.scope, skill.shape.msputter) not in self.loc_clc_map:
                    self.loc_clc_map[(loc, skill.shape.scope, skill.shape.msputter)] = \
                      self.battle.map.shape_scope(loc, skill.shape)
                cset = self.loc_clc_map[(loc, skill.shape.scope, skill.shape.msputter)]

                # 计算所有人物与遮挡物相对于行动者X方位向量的偏移角
                for ele in self.object_info + self.person_info:
                    if ele[-1] == p:
                        continue
                    ele[3] = self.battle.map.angle(loc, (loc[0] + 1, loc[1]), ele[0])
                for scope in cset:
                    score = 0
                    #test_scope = self.battle.map.shape(loc, scope, skill.shape)
                    if skill.shape.style == Shape.Point and skill.shape.sputter > 0:
                        attack_range = [0, skill.shape.sputter]
                        attack_angle = math.pi * 2 + math.pi / 180
                        scope_angle = None
                        distance_function = lambda x: self.battle.map.distance(scope, x[0])
                    else:
                        attack_range = skill.shape.attack_range(distance=self.battle.map.distance(loc, scope))
                        attack_angle = skill.shape.attack_angle() + math.pi / 180
                        if loc != scope:
                            scope_angle = self.battle.map.angle(loc, (loc[0] + 1, loc[1]), scope)
                        else:
                            scope_angle = 0
                        distance_function = lambda x: x[2]
                    attack_block = skill.shape.block

                    self.object_info.sort(key=lambda x: x[3])
                    ql = []
                    for q_info in self.person_info:
                        q = q_info[-1]
                        if not self.battle.skill_accept(skill, p, q):
                            continue
                        if scope_angle is not None:
                            #person_angle = q_info[3] - scope_angle
                            person_angle = q_info[3]
                        else:
                            if q_info[0] != scope:
                                person_angle = self.battle.map.angle(scope, (scope[0] + 1, scope[1]), q_info[0])
                            else:
                                person_angle = 0
                        if not self.person_in_scope(q_info, attack_range, attack_angle, attack_block, person_angle, scope_angle, distance_function):
                            #if p.tpl_id == "PERSON_RAN_WUHUA" and q != p and self.battle.map.location(q) in test_scope:
                            #    print(loc, scope, q.name, q_info, attack_range, attack_angle, attack_block, person_angle, scope_angle)
                            continue
                        #if p.tpl_id == "PERSON_CI_GUANG" and q != p and self.battle.map.location(q) not in test_scope:
                        #    print(loc, scope, q.name, q_info, attack_range, attack_angle, attack_block, person_angle, scope_angle)
                        ql.append(q)
                        if not isitem and skill.power > 0:
                            score += skill.power * (min(1, 1 if skill.mp == 0 else p.mp / skill.mp))
                        for effe in skill.effects:
                            if effe.tpl_id not in SimpleAI.EFFECT_MAP:
                                continue
                            score += SimpleAI.EFFECT_MAP[effe.tpl_id](p, q, effe, self.battle)
                    #debug_info = [attack_range, attack_angle, attack_block, scope, scope_angle, loc]
                    #object_info = [(obj[0], obj[2], obj[3]) for obj in self.object_info]
                    #person_info = [(obj[0], obj[2], obj[3]) for obj in self.person_info]
                    if score == 0:
                        #if p.tpl_id == "PERSON_CHEN_TINGZHI":
                        #    print(skill.name, scope)
                        #    print(debug_info)
                        #    print(person_info)
                        #    print(object_info)
                        continue

                    action_list = [BattleMoveAction(subject=p, battle=self.battle, target=loc, scope=move_scope,
                                                    path=self.battle.map.move_trace(loc, self.battle.map.location(p), self.connections)),
                                   theaction(subject=p, battle=self.battle, target=scope, type=SkillType.Normal,
                                             skill=skill, item=skill, objects=ql, ploc=loc, scope=[])]
                                             #debug_info=debug_info, person_info=person_info, object_info=object_info)]
                    can_do.append((action_list, score))
        if len(can_do) == 0 and len(tmp_locs) > 0 and with_default:
            tmp_loc = random.sample(tmp_locs, 1)[0]
            move_default = BattleMoveAction(subject=p, battle=self.battle, target=tmp_loc, scope=move_scope,
                                             path=self.battle.map.move_trace(tmp_loc, self.battle.map.location(p), self.connections))
            rest_default = BattleRestAction(subject=p, battle=self.battle)
            if self.battle.rested[p.id]:
                list_default = [move_default]
            else:
                list_default = [move_default, rest_default]
            can_do.append((list_default, min(250, int(p.mp_limit * p.mp_recover_rate_inferior))))
        return can_do

    def do_attack(self, p):
        if self.battle.attacked[p.id]:
            zhaoshies = []
        else:
            zhaoshies = self.battle.skill_available(p)
        return self.do_skill(p, zhaoshies)

    def do_item(self, p):
        if self.battle.itemed[p.id]:
            items = []
        else:
            items = [itm for itm in p.items if itm.shape is not None]
        return self.do_skill(p, items, isitem=True, with_default=False)

    def do_attack_silent(self, p):
        if self.battle.attacked[p.id]:
            zhaoshies = []
        else:
            zhaoshies = self.battle.skill_available(p)
        return self.do_skill_silent(p, zhaoshies)
    
    def do_item_silent(self, p):  
        can_do = []    
        if self.battle.itemed[p.id]:
            items = []
        else:
            items = [itm for itm in p.items if itm.shape is not None]
        return self.do_skill_silent(p, items, isitem=True)
     
    def do_rest(self, p):
        if self.battle.rested[p.id]:
            return []
        else:
            return [([BattleRestAction(subject=p, battle=self.battle)], min(250, int(p.mp_limit * p.mp_recover_rate)))]
