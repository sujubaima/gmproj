# -- coding: utf-8 --
from __future__ import division

import math
import random

from proj.entity.constants import EquipPosition
from proj.entity.common import Entity
from proj.entity.common import HyperAttr
from proj.entity.skill import Superskill
from proj.entity.item import Item
from proj.entity.recipe import Recipe
from proj.entity.team import Team
from proj.entity.effect import Status
from proj.entity.force import Force

from proj.utils import Exponential


class Person(Entity):

    ATTR_SET = set(["dongjing", "gangrou", "zhipu", "yinyang",
                    "neigong", "boji", "jianfa", "daofa", "changbing", "anqi", "qimen",
                    "hp_max", "mp_max", "attack", "defense", "motion", "speed",
                    "counter_rate", "dodge_rate", "critical_rate", "anti_damage_rate", "hit_rate"])

    def handle(self, k, v):
        if k == "tags":
            self.tags.update(v.split(","))
        elif k == "force":
            self.force = Force.one(v)
        elif k == "superskills":
            ret = []
            for stpl in v:
                self.superskills[stpl["id"]] = stpl["learn"]
        elif k == "items":
            items = []
            items_quantity = {}
            for itpl in v:
                it = Item.one(itpl["id"])
                if "Equip" in it.tags or "Skillbook" in it.tags:
                    for idx in range(itpl["quantity"]):
                        it = Item.template(itpl["id"])
                        self.add_item(it, 1)
                    if "durability" in itpl:
                        it.durability_current = itpl["durability"]
                    if "position" in itpl:
                        if "tpl_equipment" not in self.tmpdict:
                            self.tmpdict["tpl_equipment"] = []
                        pos = eval("EquipPosition.%s" % itpl["position"])
                        self.tmpdict["tpl_equipment"].append((it, pos))
                else:
                    self.add_item(it, itpl["quantity"])
        elif k == "equipment":
            ret = [None] *5
            self.tmpdict["tpl_equipment"] = []
            for eqpl in v:
                eq = Item.template(eqpl["id"])
                pos = eval("EquipPosition.%s" % eqpl["position"])
                self.tmpdict["tpl_equipment"].append((eq, pos))
                self.add_item(eq, 1)
        elif k == "running":
            ss = Superskill.one(v["id"])
            self.running = ss
        elif k == "studying":
            ss, nd = v.split("-")
            self.studying = Superskill.one(ss).nodes[nd]
        elif k == "recipes":
            for rtpl in v:
                self.recipes.append(Recipe.one(rtpl["id"]))
        elif k == "status":
            for st in v:
                self.status.append(Status.template(st["id"]))
        elif k in Person.ATTR_SET:
            self.tmpdict["tpl_%s_" % k] = v
        else:
            setattr(self, k, v)

    def finish(self):
        for ssid, learnlist in self.superskills.items():
            ss = Superskill.one(ssid)
            if learnlist == "All":
                learnlist = range(len(ss.nodes))
            for n in learnlist:
                ss.learn(self, n)
        for k in Person.ATTR_SET:
            tpl_key = "tpl_%s_" % k
            if tpl_key in self.tmpdict:
                setattr(self, k, self.tmpdict.pop(tpl_key))
        if "tpl_equipment" in self.tmpdict:
            for eq, pos in self.tmpdict.pop("tpl_equipment"):
                #print(self.name, eq.name)
                eq.work(self, position=pos)
        if self.running is not None:
            self.run(self.running)
        if self.skill_counter is not None and isinstance(self.skill_counter, dict):
            for sk in self.skills:
                if sk.tpl_id == self.skill_counter["id"]:
                    self.skill_counter = sk
                    break
        for st in self.status:
            if st.phase & 1 != 0 and not st.worked:
                st.work(self, objects=[self])
        if self.team is None:
            self.team = Team()
            self.team.include(self)
        if self.id not in Entity.Instances:
            self.hp = self.hp_limit
            self.mp = self.mp_limit
    
    def initialize(self):

        self.firstname = ""
        self.lastname = ""
        self.sex = 0
        self.showname = None
        self.force = None
        self.title = None
        self.tags = set()

        self.boji = 0
        self.jianfa = 0
        self.daofa = 0
        self.changbing = 0
        self.qimen = 0
        self.anqi = 0
        
        self.neigong = 0

        self.yinyang = 0

        self.dongjing = 0
        self.gangrou = 0
        self.zhipu = 0

        #self.hp_ = 1000
        #self.mp_ = 100
        #self.mp_ = 400
        self.hp_delta = 0
        self.mp_delta = 0

        self.hp_recover_rate_inferior = 0.5
        self.mp_recover_rate_inferior = 0.5

        #self.attack_ = 250
        #self.defense_ = 250

        self.direction = 1
        self.process = 0

        self.injury = 0
        self.wound = 0
        self.poison_hp = 0
        self.poison_mp = 0
        self.hunger = 0
        self.fatigue = 0
        
        self.visible = True

        self.team = None
        self.force = None
        self.battle = None
        self.group = None
        self.group_ally = 0
        self.path = []

        self.skills = []
        self.skills_equipped = [None] * 6
        self.skills_inner = []
        self.skill_counter = None

        self.superskills = {}
        self.studying = None
        self.learned = set()
        self.exp = 0

        self.recipes = []

        self.lands = []
        
        self.equipment = [None] * 5
        self.items = []
        self.quantities = {}
        self.vice_enable = False
        self.weight = 0
        self.volume = 0
        self.weight_equip = 0

        self.status = []

        # 该角色的ZOC范围与ZOC量
        self.zoc_scope = 1
        self.zoc_value = 99
        self.movitivity = set(["TERRAN_BLANK", "TERRAN_ROAD", "TERRAN_GRASS", 
                               "TERRAN_FLOWER_RED", "TERRAN_FLOWER_YELLOW"
                               "TERRAN_HILL", "TERRAN_FOREST", "TERRAN_DESERT", 
                               "TERRAN_SNOW", "TERRAN_CLOUD"])
        self.locativity = set(["TERRAN_BLANK", "TERRAN_ROAD", "TERRAN_GRASS", 
                               "TERRAN_FLOWER_RED", "TERRAN_FLOWER_YELLOW", 
                               "TERRAN_HILL", "TERRAN_FOREST", "TERRAN_DESERT", 
                               "TERRAN_SNOW", "TERRAN_CLOUD"])

        self.hp = self.hp_limit
        self.mp = self.mp_limit
        
        self.conversation = None

    def exp_multi(self, name, attr, attrfac=1, output=None):
        prop_locked = getattr(self, "%s_locked" % name)        
        if prop_locked is not None:
            return prop_locked
        prop_base = getattr(self, "%s_" % name)
        #prop_delta = getattr(self, "%s_delta_" % name)
        prop_factor = getattr(self, "%s_factor_" % name)
        prop_exp = getattr(self, "%s_exp_" % name)
        attrval = getattr(self, attr)
        ret = prop_base * prop_factor * round(prop_exp.value(attrfac * attrval), 4)
        if output is None:
            return ret
        else:
            return output(ret)

    def exp_add(self, name, attr, attrfac=1, output=None):
        prop_locked = getattr(self, "%s_locked" % name)
        if prop_locked is not None:
            return prop_locked
        prop_base = getattr(self, "%s_" % name)
        #prop_delta = getattr(self, "%s_delta_" % name)
        prop_factor = getattr(self, "%s_factor_" % name)
        prop_exp = getattr(self, "%s_exp_" % name)
        attrval = getattr(self, attr)
        ret = prop_base + prop_factor * round(prop_exp.value(attrfac * attrval), 4)
        if output is None:
            return ret
        else:
            return output(ret)

    def random(self, total=90, attrs=["boji", "jianfa", "daofa",
                                      "changbing", "anqi", "qimen"]):
        tmplist = []
        lft = total
        ceil = 30
        floor = 1
        for i in range(len(attrs) - 1):
            p = random.randint(floor, min(ceil, lft, lft - len(attrs) + i + 1))
            lft -= p
            tmplist.append(p)
        if lft > 30:
            tmplist.append(30)
            lft = lft - 30
            for i in range(30 * len(tmplist)):
                i = i % len(tmplist)
                if tmplist[i] >= 30:
                    continue
                tmplist[i] += 1
                lft -= 1
                if lft == 0:
                    break
        else:
            tmplist.append(lft)
        for i in range(len(attrs)):
            setattr(self, attrs[i], tmplist[i])
        self.yinyang = random.randint(-49, 49)
        self.dongjing = random.randint(-49, 49)
        self.gangrou = random.randint(-49, 49)
        self.zhipu = random.randint(-49, 49)

    @property
    def name(self):
        if self.showname:
            return self.showname
        else:
            return self.firstname + self.lastname

    @property
    def hp_limit(self):
        return max(1, int(self.hp_max - self.injury))

    @property
    def mp_limit(self):
        return max(1, int(self.mp_max - self.wound))

    @property
    def equip_max(self):
        return self.weight_max * 2 / 3

    @property
    def inner_superskills(self):
        tmp = set()
        for skill_inner in self.skills_inner:
            if skill_inner.belongs.tpl_id in tmp:
                continue
            tmp.add(skill_inner.belongs.tpl_id)
        return list(tmp)
        
    def already(self, status, exertor=None, source=None):
        ret = None
        for s in self.status:
            if s.tpl_id is not None and s.tpl_id == status.tpl_id and \
               (exertor is None or s.exertor == exertor) and \
               (source is None or s.source == source):
                ret = s
                break
        return ret

    def correct(self, poison=True):
        if self.hp + self.hp_delta < 0:
            self.hp_delta = -1 * self.hp
        if self.mp + self.mp_delta < 0:
            self.mp_delta = -1 * self.mp
        if self.hp + self.hp_delta > self.hp_limit and self.hp_delta > 0:
            self.hp_delta = max(self.hp_limit - self.hp, 0)
        if self.mp + self.mp_delta > self.mp_limit and self.mp_delta > 0:
            self.mp_delta = max(self.mp_limit - self.mp, 0)

    def special(self, attr):
        if attr == "Dong":
            return self.dongjing
        elif attr == "Jing":
            return -1 * self.dongjing
        elif attr == "Gang":
            return self.gangrou
        elif attr == "Rou":
            return -1 * self.gangrou
        elif attr == "Zhi": 
            return self.zhipu
        elif attr == "Pu":
            return -1 * self.zhipu

    def yinyang_rate(self, yinyang):
        if yinyang == 0:
            value = 50 - abs(self.yinyang)
        else:
            value = self.yinyang
        return round(self.yinyang_effect_exp_.value(yinyang * value), 4)

    def minus_item(self, item, quantity=1):
        self.quantities[item.tpl_id] -= quantity
        self.weight -= item.weight * quantity
        self.volume -= item.volume * quantity
        if self.quantities[item.tpl_id] <= 0:
            self.quantities.pop(item.tpl_id)
            self.items.remove(item)
        elif "Equip" in item.tags or "Skillbook" in item.tags:
            self.items.remove(item)

    def add_item(self, item, quantity=1):
        if item.tpl_id not in self.quantities:
            self.quantities[item.tpl_id] = 0
        if item not in self.items:
            self.items.append(item)
        self.quantities[item.tpl_id] += quantity
        self.weight += item.weight * quantity
        self.volume += item.volume * quantity

    def equip_off(self, item, pos):
        self.equipment[pos] = None
        if item.double_hand:
            self.equipment[1 - pos] = None
        self.weight_equip -= item.weight
        #self.add_item(item)

    def equip_on(self, item, pos):
        self.equipment[pos] = item
        if item.double_hand:
            self.equipment[1 - pos] = item
        self.weight_equip += item.weight
        #if item.tpl_id in self.quantities:
        #    self.minus_item(item)
            
    def run(self, superskill):
        for ins in self.skills_inner:
            if ins.belongs.tpl_id != superskill.tpl_id:
                continue
            ins.work(self, objects=[self])
            
    def unrun(self, superskill):
        for ins in self.skills_inner:
            if ins.belongs.tpl_id != superskill.tpl_id:
                continue
            ins.leave(self, objects=[self])

    def remove_skill(self, skill):
        self.skills.remove(skill)
        if skill in self.skills_equipped:
            self.skills_equipped.remove(skill)
            self.skills_equipped.append(None)
        if self.counter_skill == skill:
            self.counter_skill = None


def person_attr(name, attr, lower=None, upper=None, middle=None, degree=50, base=1, func=None, output=None):
    if attr.startswith("-"):
        attr = attr[1:]
        attrfac = -1
    else:
        attrfac = 1
    setattr(Person, "%s_exp_" % name, Exponential(lower=lower, upper=upper, middle=middle, degree=degree, base=1))
    setattr(Person, "%s_" % name, base)
    setattr(Person, "%s_factor_" % name, 1)
    #setattr(Person, "%s_delta_" % name, 0)
    if func is None:
        func = Person.exp_multi
    prop = property(fget=lambda x: func(x, name, attr, attrfac, output),
                    fset=lambda x, y: setattr(x, "%s_" % name, y))
    setattr(Person, name, prop)


def _person_attr(name, attr, lower=None, upper=None, middle=None, degree=50, base=1, func=None, output=None):
    if attr.startswith("-"):
        attr = attr[1:]
        attrfac = -1
    else:
        attrfac = 1
    exp = Exponential(lower=lower, upper=upper, middle=middle, degree=degree, base=1)
    hyper = HyperAttr(base)
    setattr(Person, "%s_" % name, hyper)
    setattr(Person, "%s_exp_" % name, exp)
    if func is None:
        func = Person.exp_multi
    prop = property(fget=lambda x: func(x, name, attr, attrfac, output),
                    fset=lambda x, y: setattr(x, "%s_" % name, y))
    setattr(Person, name, prop)


person_attr("hit_rate", attr="-gangrou", middle=1, upper=1.04, base=0.94)
person_attr("dodge_rate", attr="dongjing", middle=1, upper=1.5, base=0.04)
person_attr("counter_rate", attr="-dongjing", middle=1, upper=1.5, base=0.04)
person_attr("anti_damage_rate", attr="zhipu", middle=1, upper=1.5, base=0.04)
person_attr("anti_damage", attr="-gangrou", middle=0.7, upper=0.85)
person_attr("critical_rate", attr="zhipu", middle=1, upper=1.5, base=0.04)
person_attr("critical_damage", attr="gangrou", lower=1.15, upper=1.75)
person_attr("hp_recover_rate", attr="-zhipu", middle=0.1, upper=0.2)
person_attr("mp_recover_rate", attr="-zhipu", middle=0.1, upper=0.2)
person_attr("rescue_rate", attr="zhipu", middle=1, upper=2)
person_attr("anti_injury", attr="-gangrou", lower=0.75, middle=1)
person_attr("anti_wound", attr="-gangrou", lower=0.75, middle=1)
person_attr("anti_poison_rate", attr="-dongjing", lower=0.75, middle=1)
person_attr("attack", attr="gangrou", middle=1, upper=1.4, base=200, output=int)
person_attr("defense", attr="-dongjing", middle=1, upper=2, base=200, output=int)
person_attr("hp_max", attr="-zhipu", middle=1, upper=1.4, base=1000, output=int)
person_attr("mp_max", attr="-zhipu", middle=1, upper=1.2, base=400, output=int)
person_attr("motion", attr="dongjing", lower=1.9, middle=3.5, upper=5.1, base=-1, func=Person.exp_add, output=int)
person_attr("speed", attr="dongjing", middle=1, upper=1.5, base=160, output=int)
person_attr("study_rate", attr="zhipu", middle=1, upper=1.5)
person_attr("weight_max", attr="gangrou", middle=30, upper=60)
person_attr("volume_max", attr="gangrou", middle=60, upper=120)
person_attr("yinyang_effect", attr="yinyang", middle=1, upper=1.5)


if __name__ == "__main__":
    from proj.data import person
    import time
    t1 = time.time()
    p = Person.one("PERSON_2")
    q = Person.one("PERSON_3")
    t2 = time.time()
    o = Person.one("PERSON_2")
    print(p.tpl_id, p.id)
    for s in p.skills:
        print(s.name)
