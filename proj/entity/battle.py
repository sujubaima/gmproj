# -- coding: utf-8 --

from __future__ import division

import random
import math
import importlib
import uuid
import time

from proj import options

from proj.entity.effect import Status
from proj.entity.person import Person
from proj.entity.map import Shape
from proj.entity.constants import BattleGroup
from proj.entity.constants import BattlePhase
from proj.entity.constants import BattleEvent
from proj.entity.constants import SkillStyle
from proj.entity import common

from proj.runtime import context


class Battle(object):

    @classmethod
    def one(cls, tpl_id):
        plib = importlib.import_module("proj.entity.person")
        return plib.Person.one(tpl_id[7:]).team.battle

    def __init__(self, map, groups, allies=None, death=False, silent=False):
        self.id = uuid.uuid1()

        self.silent = False if silent is None else silent
        self.death = False if death is None else death

        self.alive = []
        self.dead = []
        self.all = []

        self.exps = {}
        
        self.map = map
        self.auto = False
        self.current = None
        self.moved = {}
        self.attacked = {}
        self.itemed = {}
        
        self.turnidx = 0

        self.phase = None

        self.sequence = []

        self.cdmap = {}

        self.groups = groups

        self.extensions = {}
       
        if allies is None:
            self.allies = []
        else:
            self.allies = allies

        self.update_group_ally()

        ridx = options.USE_AI.rfind(".")
        mod_name = options.USE_AI[:ridx]
        cls_name = options.USE_AI[ridx + 1:]
        ai_cls = importlib.import_module(mod_name)
        self.ai = getattr(ai_cls, cls_name)(self)
        #self.ai = SimpleAI(self)

        for g in self.groups:
            self.alive.extend(g)
            self.all.extend(g)
            for p in g:
                p.group = g
                p.group_ally = self.group_allies[self.groups.index(p.group)]
                #p.battle = self

    def update_group_ally(self):
        self.group_allies = [int(math.pow(2, idx)) for idx in range(len(self.groups))]

        if len(self.allies) == 0:
            self.allies.extend([[idx] for idx in range(len(self.groups))])

        for idx, ally in enumerate(self.allies):
            tmp = 0
            for gidx in ally:
                tmp = tmp | int(math.pow(2, gidx))
            for gidx in ally:
                self.group_allies[gidx] = self.group_allies[gidx] | tmp

    def start(self):
        for p in self.alive:
            p.battle = self
            p.team.battle = self
            p.hp = p.hp_limit
            p.mp = p.mp_limit
        for j in [0, 1]:
            for idx, p in enumerate(self.groups[j]):
                loc_x, loc_y = self.map.start_locs[j][idx]
                self.map.locate(p, (loc_x, loc_y))
                #p.direction = self.map.direction(self.map.entity_loc[p.id], 
                #                                 self.map.center_point(self.map.start_locs[1 - j]))
        for p in self.alive:
            enemies_locs = []
            for ene in self.enemies(p):
                if ene.id not in self.map.entity_loc:
                    continue
                enemies_locs.append(self.map.location(ene))
            p.direction = self.map.direction(self.map.location(p), self.map.center_point(enemies_locs))
            self.moved[p.id] = False
            self.attacked[p.id] = False
            self.itemed[p.id] = False
        
    def finish(self):
        teamset = set()
        exp_total = 0
        friend_count = 0
        for p in self.all:
            if p.team.id not in teamset:
                p.team.battle = None
                p.team.result = self.result(p.team)
                teamset.add(p.team.id)
            if p.group_ally & context.PLAYER.group_ally:
                exp_total += int(round(10 * math.pow(1.008, p.neigong + p.boji + p.jianfa +
                                                     p.daofa + p.changbing + p.qimen + p.anqi)))
                friend_count += 1
        for p in self.all:
            if p.team == context.PLAYER.team:
                self.exps[p.id] == exp_total * p.study_rate // friend_count
        #self.reset_delta()
        #self.status_work(BattlePhase.Finish)
        #self.deal()
        for p in self.all:
            p.battle = None
            for sts in p.status:
                if sts.leftturn >= 0:
                    sts.leave(p, battle=self)

    def start_turn(self):
        itm = self.pick()
        self.current = itm
        self.update_skill()
        self.moved[itm.id] = False
        self.attacked[itm.id] = False
        self.itemed[itm.id] = False
        self.reset = False
        self.turnidx += 1
        #self.status_work(BattlePhase.StartTurn)
        return itm
        
    def finish_turn(self):
        self.update_status()
        #self.update_skill()
        #self.update_alive()
        
    def append_group(self, group, allies=[]):
        self.groups.append(group)
        self.update_group_ally()

    def pick(self):
        min = (None, 1000)
        for itm in self.alive:
            ctime = (1000 - itm.process) / itm.speed
            if ctime < min[1]:
                min = (itm, ctime)
        for itm in self.alive:
            if itm == min[0]:
                itm.process = -1 * max(0, itm.fatigue - 500)
            else:
                itm.process += int(min[1] * itm.speed)
        return min[0]

    def quit(self, person):
        self.alive.remove(person)
        self.dead.append(person)
        self.map.remove(person)
        for sts in person.status:
            if sts.leftturn >= 0:
                sts.leave(person, battle=self)
        
    def controllable(self):
        #return True
        return context.PLAYER is not None and \
               self.current.group == context.PLAYER.group and \
               "group_ally" not in self.current.stash

    def snapshot(self, record_event=True):
        ret = {}
        for p in self.alive:
            if context.PLAYER is not None:
                group = 0 if self.is_friend(p, context.PLAYER) else 1
            else:
                group = self.group_allies.index(p.group_ally)
            p_dict = {"name": p.name,
                      "visible": p.visible,
                      "location": self.map.entity_loc[p.id],
                      "group": group,
                      "direction": p.direction,
                      "hp": p.hp,
                      "mp": p.mp,
                      "hp_limit": p.hp_limit,
                      "mp_limit": p.mp_limit,
                      "injury": p.injury,
                      "wound": p.wound,
                      "poison_mp": p.poison_mp,
                      "poison_hp": p.poison_hp,
                      "events": {}}
            if p == self.current:
                p_dict["current"] = True
            if record_event and len(self.sequence) > 0 and p.id in self.sequence[-1]["results"]:
                p_dict["events"].update(self.sequence[-1]["results"][p.id])
            ret[p.id] = p_dict
        return ret

    def event(self, p, evt):
        if p.id in self.sequence[-1]["results"] and evt in self.sequence[-1]["results"][p.id]:
            return self.sequence[-1]["results"][p.id][evt]
        else:
            return None

    def add_event(self, q, evt, **kwargs):
        if q.id in self.sequence[-1]["results"]:
            e_dict = self.sequence[-1]["results"][q.id]
        else:
            e_dict = {}
        e_dict[evt] = {}
        for k, v in kwargs.items():
            e_dict[evt][k] = v
        self.sequence[-1]["results"][q.id] = e_dict

    def remove_event(self, q, evt):
        if q.id not in self.sequence[-1]["results"]:
            return
        self.sequence[-1]["results"][q.id].pop(evt)

    def redirect(self, p, plist, tgt, skill):
        x, y = tgt
        if self.map.entity_loc[p.id] != tgt:
            p.direction = self.map.direction(self.map.entity_loc[p.id], (x, y))
            if skill.shape.style == Shape.BigSector:
                # p.direction = p.direction * 2
                p.direction = p.direction + 1
            elif skill.shape.style == Shape.SmallSector:
                # p.direction = p.direction * 2
                p.direction = p.direction + 1
        # if abs(p.direction) > 4:
        #    p.direction = p.direction * -1 // 8
        p.direction = p.direction % 6
        for q in plist:
            if self.is_friend(p, q):
                continue
            dire = self.map.direction(self.map.entity_loc[p.id], self.map.entity_loc[q.id])
            #q.direction = -1 * dire
            q.direction = (dire + 3) % 6
       
    def enemies(self, p):
        ret = []
        for q in self.alive:
            if self.is_enemy(p, q):
                ret.append(q)
        return ret

    def friends(self, p):
        ret = []
        for q in self.alive:
            if self.is_friend(p, q):
                ret.append(q)
        return ret

    def is_enemy(self, p, q):
        return p.group_ally & q.group_ally == 0

    def is_friend(self, p, q):
        return p.group_ally & q.group_ally != 0

    def skill_accept(self, skill, p, q):
        if skill.targets == "Enemies":
            return self.is_enemy(p, q)
        elif skill.targets == "Friends":
            return self.is_friend(p, q)
        else:
            return True

    def update_status(self):
        #for p in self.alive:
        p = self.current
        if p is None:
            return
        for st in p.status:
            if st.startturn == self.turnidx:
                continue
            if st.leftturn >= 0:
                st.leftturn -= 1
            if st.leftturn != 0:
                continue
            st.leave(p, battle=self)
            #Status.remove(st)

    def update_skill(self):
        p = self.current
        if p.id not in self.cdmap:
            return
        for k, v in self.cdmap[p.id].items():
            if v == 0:
                continue
            self.cdmap[p.id][k] = v - 1

    def skill_cd(self, p, skill):
        if p.id not in self.cdmap:
            return 0
        if skill.id not in self.cdmap[p.id]:
            return 0
        return self.cdmap[p.id][skill.id]

    def action(self, person):
        while not self.moved[person.id] or \
              not self.attacked[person.id] or \
              not self.itemed[person.id]:
            #t1 = time.time()
            ai_list = self.ai.do(person)
            #t2 = time.time()
            #print("ai", t2 - t1)
            for ai_ac in ai_list:
                yield ai_ac

    def update_alive(self):
        for person in self.alive:
            if person.hp == 0:
                self.alive.remove(person)
                self.dead.append(person)
                self.map.remove(person)

    def finished(self):
        l = None
        for p in self.alive:
            if l is None:
                l = p.group_ally
            if p.group_ally != l:
                return False
        return True

    def result(self, team):
        return team.members[0].group_ally == self.alive[0].group_ally

    def reset_delta(self):
        for p in self.alive:
            p.hp_delta = 0
            p.mp_delta = 0

    def status_work(self, phase):
        self.phase = phase
        for p in self.alive:
            for s in p.status:
                if s.phase & phase == 0:
                    continue
                s.work(p, battle=self)
                
    def getskillattr(self, obj, name):
        v = getattr(obj, name, None)
        if v is None:
            v = getattr(obj, "qimen")
        return v

    def calculate_weapon(self, skill, p, q):
        if skill.double_weapon is None:
            sty = set([SkillStyle.Boji])
            if p.equipment[0] is not None:
                sty.update(p.equipment[0].tags)
            sty = (sty & skill.style).pop().lower()
            vp = self.getskillattr(p, sty)
            vq = self.getskillattr(q, sty)
        else:
            sty_a = set([SkillStyle.Boji])
            sty_b = set([SkillStyle.Boji])
            if p.equipment[0] is not None:
                sty_a.update(p.equipment[0].tags)
            if p.equipment[1] is not None:
                sty_b.update(p.equipment[1].tags)
            sty_a = (sty_a & skill.style).pop().lower()
            sty_b = (sty_b & skill.style).pop().lower()
            vp = (self.getskillattr(p, sty_a) + self.getskillattr(p, sty_b)) // 2
            vq = (self.getskillattr(q, sty_a) + self.getskillattr(q, sty_b)) // 2
        return vp, vq
                
    def damage(self, skill, p, q):
        should_critical = common.if_rate(p.critical_rate)
        should_anti_damage = common.if_rate(q.anti_damage_rate)
        if skill.power == 0:
            return 0, 0, should_critical, False
        mp_rate = 1 if skill.mp == 0 else max(1, -1 * p.mp_delta / skill.mp)
        real_attack = p.attack_base
        real_defense = q.defense_base
        #vp = getattr(p, skill.style.lower())
        #vq = getattr(q, skill.style.lower())
        vp, vq = self.calculate_weapon(skill, p, q) 
        #real_attack += (skill.power + 250) * math.pow(1.005, vp) * math.pow(1.002, p.neigong)
        attack_dire = self.map.direction(self.map.location(p), self.map.location(q))       
        if attack_dire == q.direction:
            dire_ratio = 1.5
        elif attack_dire == (q.direction + 1) % 6 or attack_dire == (q.direction + 5) % 6:
            dire_ratio = 1.2
        else:
            dire_ratio = 1
        act_neigong_p = int(p.neigong * (p.mp_limit / p.mp_max))
        act_neigong_q = int(q.neigong * (q.mp_limit / q.mp_max))
        real_attack += skill.power * mp_rate * math.pow(1.005, vp) * math.pow(1.002, act_neigong_p) * p.yinyang_rate(skill.yinyang)
        #real_attack_base = real_attack
        #real_attack_skill = int(skill.power * math.pow(1.005, vp) * math.pow(1.002, p.neigong) * p.yinyang_rate(skill.yinyang))
        #real_attack = int(math.sqrt(real_attack_base * real_attack_skill) * mp_rate)
        real_defense *= math.pow(1.005, vq) * math.pow(1.002, act_neigong_q) * max(1, q.yinyang_rate(skill.yinyang))
        real_attack -= max(p.hunger - 500, 0)
        real_attack = int(real_attack * 0.6)
        real_defense = int(real_defense * 0.6)
        #real_attack = int(real_attack * 1.4)
        #real_defense = int(real_defense / 1.4)
        #print(p.name, q.name, real_attack, real_defense)
        hp_damaged = common.random_gap(real_attack, 0.025) - common.random_gap(real_defense, 0.025)
        mp_damaged = 0
        if hp_damaged <= 0:
            hp_damaged = 1
        hp_damaged *= dire_ratio
        #should_critical = common.if_rate(p.critical_rate)
        #should_anti_damage = common.if_rate(q.anti_damage_rate)
        if should_critical:
            #hp_damaged = hp_damaged * p.critical_damage
            hp_damaged = hp_damaged * 1.8
        if should_anti_damage:
            #hp_damaged = max(1, hp_damaged * 0.5)
            hp_damaged = max(1, hp_damaged * q.anti_damage)
        return int(hp_damaged), int(mp_damaged), should_critical, should_anti_damage

    def check_weapon_before(self, p, skill):
        equip_a = p.equipment[0]
        equip_b = p.equipment[1]
        if skill.double_weapon is not None:
            equip_b.leave(p)
            p.vice_enable = True
            equip_b.work(p, position=1)
        else:
            if equip_a is None or len(skill.style & equip_a.tags) == 0:
                if equip_a is not None:
                    equip_a.leave(p)
                if equip_b is not None and equip_a != equip_b:
                    equip_b.leave(p)
                    equip_b.work(p)
                if equip_a is not None:
                    equip_a.work(p, position=1)
                
    def check_weapon_after(self, p, skill):
        if skill.double_weapon is not None:
            equip_b = p.equipment[1]
            equip_b.leave(p)
            p.vice_enable = False
            equip_b.work(p, position=1)

    def start_cd(self, p, skill, cd=None):
        if p.id not in self.cdmap:
            self.cdmap[p.id] = {}
        if skill.id not in self.cdmap[p.id]:
            self.cdmap[p.id][skill.id] = 0
        skill_cd = 0
        if cd is not None:
            skill_cd = cd
        elif skill.cd != 0:
            skill_cd = skill.cd
        if skill_cd > 0: 
            self.cdmap[p.id][skill.id] += skill_cd + 1
            
    def skill_ava(self, p, skill):
        if skill.double_weapon is not None:
            if p.equipment[0] is None or p.equipment[1] is None:
                return False
            should_pass = True
            cset = set()
            cset.update(p.equipment[0].tags)
            cset.update(p.equipment[1].tags)
            if (skill.double_weapon[0] in p.equipment[0].tags and \
                skill.double_weapon[1] in p.equipment[1].tags) or \
               (skill.double_weapon[0] in p.equipment[1].tags and \
                skill.double_weapon[1] in p.equipment[0].tags):
                shoud_pass = False
            return not should_pass
        elif SkillStyle.Boji not in skill.style:
            should_pass = True
            for equip in p.equipment[:2]:
                if equip is not None and len(skill.style & equip.tags) != 0:
                    should_pass = False
                    break
            return not should_pass
        else:
            return True

    def skill_available(self, p, check_cd=True):
        ret = []
        if p.id not in self.cdmap:
            self.cdmap[p.id] = {}
        equip = p.equipment[0]
        for skill in p.skills:
            if skill.double_weapon is not None:
                if p.equipment[0] is None or p.equipment[1] is None:
                    continue
                should_pass = True
                cset = set()
                cset.update(p.equipment[0].tags)
                cset.update(p.equipment[1].tags)
                if (skill.double_weapon[0] in p.equipment[0].tags and \
                    skill.double_weapon[1] in p.equipment[1].tags) or \
                   (skill.double_weapon[0] in p.equipment[1].tags and \
                    skill.double_weapon[1] in p.equipment[0].tags):
                    should_pass = False
                if should_pass:
                    continue
            elif SkillStyle.Boji not in skill.style:
                should_pass = True
                for equip in p.equipment[:2]:
                    if equip is not None and len(skill.style & equip.tags) != 0:
                        should_pass = False
                        break
                if should_pass:
                    continue
            if skill.id not in self.cdmap[p.id]:
                self.cdmap[p.id][skill.id] = 0
            if not check_cd or self.cdmap[p.id][skill.id] == 0:
                ret.append(skill)
        return ret

    def real_motion(self, p):
        zoc = 0
        for x, y in self.map.circle(self.map.entity_loc[p.id], 1):
            if self.map.xy[x][y].person is not None:
                zoc += 1
        ret = p.base_motion - zoc
        if ret < 0:
            ret = 0
        return ret

    def deal(self, persons=None):
        if persons is None:
            persons = self.alive
        if not isinstance(persons, list):
            persons = [persons]
        for p in persons:
            if p.hp_delta == 0 and p.mp_delta == 0:
                continue
            p.correct()
            p.hp += p.hp_delta
            p.mp += p.mp_delta
            self.add_event(p, BattleEvent.HPChanged, value=p.hp_delta)
            self.add_event(p, BattleEvent.MPChanged, value=p.mp_delta)
