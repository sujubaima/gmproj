# -- coding: utf-8 --

import os
import sys
import random

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj import entity
from proj.entity import Person
from proj.entity import HyperAttr

from proj.runtime import context

if __name__ == "__main__":
    #pa = Person()
    #pa.gangrou = random.randint(-50, 50)
    #pa.dongjing = random.randint(-50, 50)
    #pa.zhipu = random.randint(-50, 50)
    #pb = Person()
    #pa.gangrou = random.randint(-50, 50)
    #pa.dongjing = random.randint(-50, 50)
    #pa.zhipu = random.randint(-50, 50)

    # ""
    # "p1: 动%s 静%s 刚%s 柔%s 智%s 朴%s" % (50 + pa.dongjing, 50 - pa.dongjing, 50 + pa.gangrou, 50 - pa.gangrou, 50 + pa.zhipu, 50 - pa.zhipu)
    # "p2: 动%s 静%s 刚%s 柔%s 智%s 朴%s" % (50 + pb.dongjing, 50 - pb.dongjing, 50 + pb.gangrou, 50 - pb.gangrou, 50 + pb.zhipu, 50 - pb.zhipu)
    # ""

    #def expect(x, y):
    #    e1 = (x.attack_rate / y.defense_rate) / 100 * (x.hit_rate / 100 * (1 - y.dodge_rate / 100)) * ((1 - x.critical_rate / 100) + x.critical_damage / 100 * x.critical_rate / 100)
    #    e2 = (y.attack_rate / x.defense_rate) / 100 * (y.hit_rate / 100 * (1 - x.dodge_rate / 100)) * ((1 - y.critical_rate / 100) + y.critical_damage / 100 * y.critical_rate / 100) * 0.5
    #    e3 = e1 * (1 - y.counter_rate / 100) + (e2 - e1) * y.counter_rate / 100
    #    e4 = e3 * x.speed / (x.speed + y.speed)
    #    return e4

    #ea = expect(pa, pb)
    #eb = expect(pb, pa)
    # ea, eb
    # ea * pa.hp_rate / (ea * pa.hp_rate + eb * pb.hp_rate), eb * pb.hp_rate / (ea * pa.hp_rate + eb * pb.hp_rate)
    # ""

    #p = Person()
    #print("灵动\t沉静\t刚猛\t柔易\t颖悟\t朴拙\t命中\t闪避\t反击\t破绽\t破绽伤害\t回复\t医治加成\t攻击加成\t防御加成\tHP加成\t移动力\t时序速度\t经验获得\n")
    #for i in range(-50, 51, 5):
    #    p.gangrou = 0
    #    p.dongjing = i
    #    p.zhipu = 0
    #    print("%s%%\t%s%%\t%s%%\t%s%%\t%s%%\t%s%%\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % \
    #          (50 + p.dongjing, 50 - p.dongjing, 50 + p.gangrou, 50 - p.gangrou, 50 + p.zhipu, 50 - p.zhipu, 
    #           p.hit_rate, p.dodge_rate, p.counter_rate, p.critical_rate, p.critical_damage,
    #           p.hp_recover_rate, p.rescue_rate, p.attack_rate, p.defense_rate, p.hp_rate, p.motion, p.speed, p.study_rate))
    entity.init()
    context.init()

    p1 = Person.one("PERSON_ZHANG_YINSONG")
    p2 = Person.one("PERSON_JUE_CHENG")
    #rel1 = context.relationship("person", p1, p2)
    #rel2 = context.relationship("person", p2, p1)
    #print(rel1, rel2)
    print(p1.dodge_rate, p2.dodge_rate)
    print(p1.attack, p2.defense)
    p1.abc = HyperAttr(5, delta=0.5, factor=1.2, type=int, fval=lambda self: self.base + self.delta)
    print(p1.abc())
    print(getattr(p1.__class__, "dodge_rate"))

