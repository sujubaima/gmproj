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


# 盘根
class PanGenEffect(Effect):

    phase = BattlePhase.BeforeAttack

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(battle.sequence) > 1 and \
           isinstance(battle.sequence[-2]["action"], BattleMoveAction) and \
           battle.sequence[-2]["action"].subject == subject:
            return
        debuffs = []
        for sts in subject.status:
            if sts.name is not None and sts.style == 0:
                debuffs.append(sts)
        if len(debuffs) == 0:
            return
        chosen = random.sample(debuffs, 1)[0]
        chosen.leave(subject)
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"status": chosen.name})


# 清风拂山岗
class QingFengFuShanGangEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_factor = self.factor(subject)
        for obj in objects:
            if battle.is_friend(subject, obj):
                continue
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            wound = -1 * int(obj.defense_base * effe_factor * obj.anti_wound)
            obj.wound -= wound
            if wound != 0 and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"wound": -1 * wound, "object": obj.name})
            

# 驱风
class QuFengEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs.get("battle", None)
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_factor = self.factor(subject)
        for obj in objects:
            poison_recover = min(obj.poison_hp, int(self.level * effe_factor))
            obj.poison_hp -= poison_recover
            if battle is not None and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self,
                    details={"object": obj.name, "poison_recover": poison_recover})



# 却步
class QueBuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_factor = self.factor(subject)
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            #process = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * self.level * effe_factor)
            process = int(self.level * effe_factor)
            process = -1 * common.random_gap(process, 0.025)
            obj.process += process
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"process": -1 * process, "object": obj.name})


# 柔劲
class RouJinEffect(Effect):

    from_damage = True

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_factor = self.factor(subject)
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            wound = 0
            if not self.from_damage:
                wound = int(-1 * effe_factor * self.level * obj.anti_wound)
            else:
                wound = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * effe_factor * self.level * obj.anti_wound)
            obj.wound -= wound
            if wound != 0 and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"wound": -1 * wound, "object": obj.name})


# 神准
class ShenZhunEffect(Effect):

    phase = BattlePhase.BeforeDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        for obj in battle.alive:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                battle.remove_event(obj, BattleEvent.ACTMissed)
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self)


# 太极劲
class TaiJiJinEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        for skill in subject.skills:
            if not skill.tpl_id.startswith("SKILL_TAIJI"):
                continue
            if skill.power != 0:
                skill.power += 99

    def leave(self, subject, objects=[], **kwargs):
        for skill in subject.skills:
            if not skill.tpl_id.startswith("SKILL_TAIJI"):
                continue
            if skill.power != 0:
                skill.power -= 99



# 同归  
class TongGuiEffect(Effect):

    phase = BattlePhase.AfterDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        status = kwargs["status"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            if obj.already(status, exertor=subject) is not None:
                obj.hp_delta *= 2
                obj.mp_delta *= 2
                if not battle.silent:
                    MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name})


# 同心
class TongXinEffect(Effect):

    phase = BattlePhase.AfterDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        for obj in objects:
            sts_count = 0
            for sts in obj.status:
                if subject.already(sts) is not None:
                    sts_count += 1
            if sts_count == 0:
                continue
            obj.hp_delta = int(obj.hp_delta * (1 + 0.01 * self.level * sts_count))
            obj.mp_delta = int(obj.mp_delta * (1 + 0.01 * self.level * sts_count))
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name})


# 偷盗
class TouDaoEffect(Effect):

    phase = BattlePhase.BeforeDamage

    base_rate = 0.5

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        for obj in battle.sequence[-1]["action"].objects:
            if len(obj.items) == 0:
                self.battle.add_event(q, BattleEvent.ACTMissed)
                continue
            itm = random.sample(obj.items, 1)[0]
            if itm.tpl_id == "ITEM_MONEY":
                quantity = random.randint(1, obj.quantities[itm.tpl_id])
            else:
                quantity = 1
            effe_ratio = self.base_rate * self.factor(subject) * math.pow(2, -1 * itm.rank)
            if common.if_rate(effe_ratio):
                obj.minus_item(itm, quantity)
                subject.add_item(itm, quantity)
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name,
                                                                             "item": itm.name,
                                                                             "item_rank": itm.rank,
                                                                             "quantity": quantity})
            else:
                self.battle.add_event(q, BattleEvent.ACTMissed)


# 退敌
class TuiDiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        for obj in battle.sequence[-1]["action"].objects:
            pass
        MSG(style=MSG.Effect, subject=subject, effect=self)


# 吞吴
class TunWuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        beaten = False
        for obj in objects:
            if obj.hp == 0:
                beaten = True
                break
        if beaten:
            effelib = importlib.import_module("proj.builtin.effects")
            effelib.QuFengEffect(level=self.level).work(subject, objects=[subject], **kwargs)
            effelib.HuaYuEffect(level=self.level).work(subject, objects=[subject], **kwargs)
            effelib.JieGuEffect(level=self.level).work(subject, objects=[subject], **kwargs)
            effelib.YiQiEffect(level=self.level).work(subject, objects=[subject], **kwargs)
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self)
