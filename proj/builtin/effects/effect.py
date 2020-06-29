# -- coding: utf-8 --

import random

from proj.entity import Effect
from proj.entity import Status
from proj.entity import BattleEvent
from proj.entity import BattlePhase
from proj.entity import AttrText
from proj.entity import common
from proj.entity.effect import ExertEffect
from proj.entity.effect import PersonChangeAttributeEffect

from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction

from proj.engine import Message as MSG

            
class DoubleExertEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        ee = ExertEffect(exertion=Status.one(self.status))
        if self.turns is not None:
            ee.turns = self.turns
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            ee.work(subject=subject, objects=[obj], **kwargs)
            ee.work(subject=obj, objects=[subject], **kwargs)


class BattlePersonChangeAttributeEffect(PersonChangeAttributeEffect):
    """
    修改角色属性
    """
    def work(self, subject, objects=[], **kwargs):
        status = kwargs.get("status", None)
        if status is not None and status.exertor is not None:
            effe_factor = self.factor(status.exertor)
            if subject != status.exertor:
                sub_factor = self.factor(subject, reverse=True)
            else:
                sub_factor = 1
            txtlist = []
            for attr in self.attrs:
                if "delta" in attr:
                    attr["delta"] = attr["delta"] * effe_factor * sub_factor
                    if attr["delta"] > 0:
                        txtlist.append("%s的%s增加了%s" % (subject.name, 
                                                           AttrText.get(attr["name"], attr["name"]), 
                                                           attr["delta"]))
                    else:
                        txtlist.append("%s的%s减少了%s" % (subject.name, 
                                                           AttrText.get(attr["name"], attr["name"]), 
                                                           -1 * attr["delta"]))
                if "ratio" in attr:
                    attr["ratio"] = round(attr["ratio"] * effe_factor * sub_factor, 2)
                    if attr["ratio"] > 1:
                        txtlist.append("%s的%s提升了%s%%" % (subject.name, 
                                                             AttrText.get(attr["name"], attr["name"]), 
                                                             int(100 * (attr["ratio"] - 1))))
                    else:
                        txtlist.append("%s的%s降低了%s%%" % (subject.name, 
                                                             AttrText.get(attr["name"], attr["name"]), 
                                                             int(100 * (1 - attr["ratio"]))))
            self.text = "；".join(txtlist)
        self.modify(subject, **kwargs)


class TraficabilityEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        if self.mode == "Stay":
            subject.locativity.add(self.terran)
        subject.movitivity.add(self.terran)

    def leave(self, subject, objects=[], **kwargs):
        if self.mode == "Stay":
            subject.locativity.discard(self.terran)
        subjec.movitivity.discard(self.terran)
