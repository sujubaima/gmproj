# -- coding: utf-8 --

import random
import importlib

from proj.entity import Effect
from proj.entity import Status
from proj.entity import BattleEvent
from proj.entity import BattlePhase
from proj.entity import common
from proj.entity.effect import ExertEffect

from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction

from proj.engine import Message as MSG


# 尝胆
class ChangDanEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if battle.sequence[-1]["action"].skill.targets == "Friends":
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        sts_tpl = "STATUS_CHANGDAN_ANONYMOUS"
        sts = Status.template(sts_tpl)
        subject.status.append(sts)
        sts.work(subject)


# 除械
class ChuXieEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            if obj.equipment[0] is None:
                continue
            if self.equip_style in obj.equipment[0].tags:
                equip = obj.equipment[0]
                equip.leave(obj)
                if not battle.silent:
                    MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name,
                                                                                 "equip": equip.name,
                                                                                 "equip_rank": equip.rank})


class FeiXingEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        pass

# 分断     
class FenduanEffect(Effect):

    phase = BattlePhase.BeforeDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        status = kwargs["status"]
        objs = []
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        for obj in objects:
            if obj.already(status, exertor=subject) is not None:
                objs.append(obj)
                if not battle.silent:
                    MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name})
        for obj in objs:
            objects.remove(obj)
            if obj.id in battle.sequence[-1]["results"]:
                battle.sequence[-1]["results"].pop(obj.id)


# 风毒
class FengDuEffect(Effect):

    from_damage = True

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_factor = self.factor(subject)
        effe_ratio = 1
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            poison_hp = 0
            if not self.from_damage:
                poison_hp = int(-1 * effe_factor * self.level * obj.anti_poison)
            else:
                poison_hp = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * effe_factor * self.level * obj.anti_poison)
            obj.poison_hp -= poison_hp
            if poison_hp != 0 and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name, "poison_hp": -1 * poison_hp})


# 复元
class FuYuanEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.current:
            return
        effelib = importlib.import_module("proj.builtin.effect")
        effelib.HuiChunEffect(level=self.level).work(subject, objects=objects, **kwargs)
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self)


# 罡风
class GangFengEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        for skill in subject.skills:
            if self.skill_style not in skill.style:
                continue
            skill.shape.sputter += 1

    def leave(self, subject, objects=[], **kwargs):
        for skill in subject.skill_style:
            if self.skill_style not in skill.style:
                continue
            skill.shape.sputter -= 1


# 刚劲
class GangJinEffect(Effect):

    from_damage = True

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_factor = self.factor(subject)
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            injury = 0
            if not self.from_damage:
                injury = int(-1 * effe_factor * self.level * obj.anti_injury)
            else:
                injury = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * self.level * effe_factor * obj.anti_injury)
            obj.injury -= injury
            if injury != 0 and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"injury": -1 * injury, "object": obj.name})


# 蛊惑
class GuhuoEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        status = kwargs["status"]
        if "group_ally" not in subject.stash:
            subject.stash["group_ally"] = subject.group_ally
        subject.group_ally = status.exertor.group_ally

    def leave(self, subject, objects=[], **kwargs):
        status = kwargs["status"]
        check_sts = True
        for sts in subject.status:
            if sts.tpl_id == status.tpl_id and sts != status:
                check_sts = False
                break
        if check_sts:
            subject.group_ally = subject.stash["group_ally"]
