# -- coding: utf-8 --

import random
import importlib

from proj.entity import Effect
from proj.entity import Status
from proj.entity import BattleEvent
from proj.entity import BattlePhase
from proj.entity import common
from proj.entity import SkillType
from proj.entity.effect import ExertEffect

from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction

from proj.engine import Message as MSG


# 拔狗牙
class BaGouYaEffect(ExertEffect):

    def initialize(self):
        super(BaGouYaEffect, self).initialize()
        sts_tpl = "STATUS_QIWU"
        self.exertion = Status.template(sts_tpl)
        self.description_ = "以此技能发动反击时，" + self.description_

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if battle.sequence[-1]["action"].type != SkillType.Counter:
            return
        if subject != battle.sequence[-1]["action"].subject:
            return
        super(BaGouYaEffect, self).work(subject, objects=objects, **kwargs)


# 捕风
class BuFengEffect(Effect):

    phase = BattlePhase.BeforeDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        sub_loc = battle.map.location(subject)
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            obj_loc = battle.map.location(obj)
            obj_distance = battle.map.distance(sub_loc, obj_loc)
            dire = battle.map.direction(sub_loc, obj_loc)
            obj_tgt = sub_loc
            while obj_tgt != obj_loc and not battle.map.can_stay(obj, obj_tgt):
                obj_tgt = battle.map.neighbour(obj_tgt, dire)
            current_distance = battle.map.distance(obj_tgt, sub_loc)
            if obj_tgt != obj_loc and current_distance < obj_distance:
                BattleMoveAction(showmsg=False, active=False,
                                 battle=battle, subject=obj, target=obj_tgt,
                                 path=[obj_tgt, obj_loc]).do()
                MSG(style=MSG.Effect, subject=subject, effect=self, 
                    details={"object": obj.name})


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
                    MSG(style=MSG.Effect, subject=subject, effect=self, 
                        details={"object": obj.name, "equip": equip.name, "equip_rank": equip.rank})


# 打狗头
class DaGouTouEffect(ExertEffect):

    def initialize(self):
        super(DaGouTouEffect, self).initialize()
        sts_tpl = "STATUS_ZHENSHE"
        self.exertion = Status.template(sts_tpl)
        self.targetstr = ("目标及其相邻敌方单位", "其")

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        new_objects = []
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            obj_loc = battle.map.location(obj)
            for loc in battle.map.circle(obj_loc, 1):
                p = battle.map.loc_entity.get(loc, None)
                if p is None or battle.is_friend(subject, p) or p in new_objects:
                    continue
                new_objects.append(obj)
        super(DaGouTouEffect, self).work(subject, objects=new_objects, **kwargs)


# 端狗窝
class DuanGouWoEffect(Effect):

    phase = BattlePhase.AfterDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects)== 0:
            objects = battle.sequence[-1]["action"].objects
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            obj.hp_delta = int(obj.hp_delta * (1 + 0.1 * len(objects)))
            obj.mp_delta = int(obj.hp_delta * (1 + 0.1 * len(objects)))



# 飞电
class FeiDianEffect(ExertEffect):

    def initialize(self):
        super(FeiDianEffect, self).initialize()
        sts_tpl = "STATUS_XUNJI"
        self.exertion = Status.template(sts_tpl)
        self.description_ = "若攻击未命中或被闪避，" + self.description_
        self.targets = "Subject"

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_on = False
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                effe_on = True
                break
        if effe_on:
            super(FeiDianEffect, self).work(subject, objects=[subject], **kwargs)


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


# 攻气
class GongQiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_factor = self.factor(subject)
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            effect_on = True
            mp_drain = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * self.level * effe_factor)
            mp_drain = max(mp_drain, -1 * obj.mp)
            obj.mp_delta += mp_drain
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"mp_drain": -1 * mp_drain})


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
