# -- coding: utf-8 --
from __future__ import division

import math
import random

from proj.entity.constants import EquipPosition
from proj.entity.common import Entity
from proj.entity.skill import Superskill
from proj.entity.item import Item
from proj.entity.recipe import Recipe
from proj.entity.team import Team
from proj.entity.effect import Status
from proj.entity.force import Force

from proj.utils import Exponential


class Person(Entity):

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
        elif k in set(["dongjing", "gangrou", "zhipu", "yinyang", 
                       "neigong", "boji", "jianfa", "daofa", "changbing", "anqi", "qimen"]):
            self.tmpdict["tpl_%s" % k] = v
        elif k in set(["hp_max", "mp_max", "attack", "defense", "motion", "speed", 
                       "counter_rate", "dodge_rate", "critical_rate", "anti_damage_rate", "hit_rate"]):
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
        for k in set(["dongjing", "gangrou", "zhipu", "yinyang",
                       "neigong", "boji", "jianfa", "daofa", "changbing", "anqi", "qimen",
                       "hp_max_", "mp_max_", "attack_", "defense_", "motion_", "speed_",
                       "counter_rate_", "dodge_rate_", "critical_rate_", "anti_damage_rate_", "hit_rate_"]):
            tpl_key = "tpl_%s" % k
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

        # 灵动值：影响时序速度、闪避率与移动步数
        # 沉静值：影响基础防御与命中率
        self.dongjing = 0

        # 刚猛值：影响基础攻击
        # 柔易值：影响反击率与暴击伤害
        self.gangrou = 0

        # 颖悟值：影响武学修炼速度、暴击率与医疗能力
        # 朴拙值：影响气血因子与休息回复率
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

        self.move_style = "move"

        # 外伤值
        self.injury = 0
        # 内伤值
        self.wound = 0
        # 风毒值
        self.poison_hp = 0
        # 瘀毒值
        self.poison_mp = 0
        # 饥饿值
        self.hunger = 0
        # 疲劳值
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
        self.movitivity = set(["TERRAN_BLANK", "TERRAN_ROAD", "TERRAN_GRASS", "TERRAN_FLOWER_RED", "TERRAN_FLOWER_YELLOW"
                               "TERRAN_HILL", "TERRAN_FOREST", "TERRAN_DESERT", "TERRAN_SNOW", "TERRAN_CLOUD"])
        self.locativity = set(["TERRAN_BLANK", "TERRAN_ROAD", "TERRAN_GRASS", "TERRAN_FLOWER_RED", "TERRAN_FLOWER_YELLOW", 
                               "TERRAN_HILL", "TERRAN_FOREST", "TERRAN_DESERT", "TERRAN_SNOW", "TERRAN_CLOUD"])

        # 命中率
        #self.register("hit_rate", middle=0.96, upper=1.15)
        self.register("hit_rate", middle=1, upper=1.04, base=0.94)
        # 闪避率
        self.register("dodge_rate", middle=1, upper=1.5, base=0.04)
        # 反击率
        self.register("counter_rate", middle=1, upper=1.5, base=0.04)
        # 拆招率
        self.register("anti_damage_rate", middle=1, upper=1.5, base=0.04)
        # 拆招减伤
        self.register("anti_damage", middle=0.7, upper=0.85)
        # 暴击率
        self.register("critical_rate", middle=1, upper=1.5, base=0.04)
        # 暴击伤害
        self.register("critical_damage", lower=1.15, upper=1.75)
        # 休息回复率
        self.register("hp_recover_rate", middle=0.1, upper=0.2)
        self.register("mp_recover_rate", middle=0.1, upper=0.2)
        # 医疗效果
        self.register("rescue_rate", middle=1, upper=2)
        # 伤病抗性
        self.register("anti_injury_rate", lower=0.75, middle=1)
        self.register("anti_wound_rate", lower=0.75, middle=1)
        # 中毒抗性
        self.register("anti_poison_rate", lower=0.75, middle=1)
        # 基础攻击加成
        self.register("attack", middle=1, upper=1.5, base=200)
        # 基础防御加成
        self.register("defense", middle=1, upper=2, base=200)
        # HP加成
        #self.register("hp_rate", middle=1, upper=1.4)
        self.register("hp_max", middle=1, upper=1.4, base=1000)
        # MP加成
        #self.register("mp_rate", middle=1, upper=1.2)
        self.register("mp_max", middle=1, upper=1.2, base=400)
        # 移动力
        #self.register("motion", lower=1, middle=3, upper=5.6, base=0)
        self.register("motion", lower=1.9, middle=3.5, upper=5.1, base=-1)
        # 时序速度
        self.register("speed", middle=1, upper=1.6, base=160)
        # 经验获取效率
        self.register("study_rate", middle=1, upper=1.5)
        # 背包大小
        self.register("weight_max", middle=30, upper=60)
        self.register("volume_max", middle=60, upper=120)
        # 阴阳加成系数
        self.register("yinyang_rate", middle=1, upper=1.5)

        self.hp = self.hp_limit
        self.mp = self.mp_limit
        
        self.conversation = None

    def register(self, name, lower=None, upper=None, middle=None, degree=50, base=1):
        setattr(self, "%s_exp" % name, Exponential(lower=lower, upper=upper, middle=middle, degree=degree, base=1))
        setattr(self, "%s_" % name, base)
        setattr(self, "%s_factor_" % name, 1)

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
    def hp_max(self):
        return int(self.hp_max_ * self.hp_max_factor_ * round(self.hp_max_exp.value(-1 * self.zhipu), 4))

    @property
    def mp_max(self):
        return int(self.mp_max_ * math.pow(1.01, self.neigong) * self.mp_max_factor_ * round(self.mp_max_exp.value(-1 * self.zhipu), 4))

    @property
    def hp_limit(self):
        return max(1, int(self.hp_max - self.injury))

    @property
    def mp_limit(self):
        return max(1, int(self.mp_max - self.wound))

    @property
    def attack_base(self):
        #return int(self.attack_ * self.attack_rate)
        return int(self.attack_ * self.attack_factor_ * round(self.attack_exp.value(self.gangrou), 4))

    @property
    def defense_base(self):
        #return int(self.defense_ * self.defense_rate)
        return int(self.defense_ * self.defense_factor_ * round(self.defense_exp.value(-1 * self.dongjing), 4))

    @property
    def hit_rate(self):
        #return self.hit_rate_ * round(self.hit_rate_exp.value(-1 * self.dongjing), 4)
        return self.hit_rate_ * self.hit_rate_factor_ * round(self.hit_rate_exp.value(-1 * self.gangrou), 4)

    @property
    def dodge_rate(self):
        return self.dodge_rate_ * self.dodge_rate_factor_ * round(self.dodge_rate_exp.value(self.dongjing), 4) * self.equip_ratio
        #return self.dodge_rate_ * round(self.dodge_rate_exp.value(-1 * self.gangrou), 4) * self.equip_ratio

    @property
    def counter_rate(self):
        #return self.counter_rate_ * round(self.counter_rate_exp.value(-1 * self.gangrou), 4)
        return self.counter_rate_ * self.counter_rate_factor_ * round(self.counter_rate_exp.value(-1 * self.dongjing), 4)
        
    @property
    def anti_damage_rate(self):
        return self.anti_damage_rate_ * self.anti_damage_rate_factor_ * round(self.anti_damage_rate_exp.value(self.zhipu), 4)
        
    @property
    def anti_damage(self):
        return self.anti_damage_ * round(self.anti_damage_exp.value(self.gangrou), 4)
        #return self.counter_rate_ * round(self.counter_rate_exp.value(-1 * self.dongjing), 4)

    @property
    def critical_rate(self):
        #return self.critical_rate_ * round(self.critical_rate_exp.value(self.zhipu), 4)
        return self.critical_rate_ * self.critical_rate_factor_ * round(self.critical_rate_exp.value(self.zhipu), 4)

    @property
    def critical_damage(self):
        return self.critical_damage_ * round(self.critical_damage_exp.value(self.gangrou), 4)

    @property
    def hp_recover_rate(self):
        return self.hp_recover_rate_ * round(self.hp_recover_rate_exp.value(-1 * self.zhipu), 4)

    @property
    def mp_recover_rate(self):
        return self.mp_recover_rate_ * round(self.mp_recover_rate_exp.value(-1 * self.zhipu), 4)

    #@property
    #def attack_rate(self):
    #    return self.attack_rate_ * round(self.attack_rate_exp.value(self.gangrou), 4)
  
    #@property
    #def defense_rate(self):
    #    return self.defense_rate_ * round(self.defense_rate_exp.value(-1 * self.dongjing), 4)

    #@property
    #def hp_rate(self):
    #    return self.hp_rate_ * round(self.hp_rate_exp.value(-1 * self.zhipu), 4)
        
    #@property
    #def mp_rate(self):
    #    return self.mp_rate_ * round(self.mp_rate_exp.value(-1 * self.zhipu), 4)

    @property
    def rescue_rate(self):
        return self.rescue_rate_ * round(self.rescue_rate_exp.value(self.zhipu), 4)

    @property
    def anti_injury(self):
        return self.anti_injury_rate_ * round(self.anti_injury_rate_exp.value(-1 * self.gangrou), 4)

    @property
    def anti_wound(self):
        return self.anti_wound_rate_ * round(self.anti_wound_rate_exp.value(self.gangrou), 4)

    @property
    def anti_poison(self):
        return self.anti_poison_rate_ * round(self.anti_poison_rate_exp.value(self.dongjing), 4)

    @property
    def motion(self):
        return int((self.motion_ + self.motion_exp.value(self.dongjing)) * self.equip_ratio)

    @property
    def speed(self):
        return round(self.speed_ * self.speed_factor_ * round(self.speed_exp.value(self.dongjing), 4) * self.equip_ratio)

    @property
    def study_rate(self):
        return self.study_rate_ * round(self.study_rate_exp.value(self.zhipu), 4)

    @property
    def weight_max(self):
        return self.weight_max_ * round(self.weight_max_exp.value(self.gangrou), 4)

    @property
    def volume_max(self):
        return self.volume_max_ * round(self.volume_max_exp.value(self.gangrou), 4)

    @property
    def equip_ratio(self):
       return 1 if self.weight_equip == 0 else min(1, self.equip_max / self.weight_equip)

    @property
    def equip_max(self):
        return self.weight_max * 2 / 3
        
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
        return round(self.yinyang_rate_exp.value(yinyang * value), 4)

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
