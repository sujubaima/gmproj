# -- coding: utf-8 --

import importlib
import random

from proj.entity import Effect
from proj.entity import Status
from proj.entity import BattleEvent
from proj.entity import BattlePhase
from proj.entity import common
from proj.entity.effect import ExertEffect

from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction

from proj.engine import Message as MSG

# 悟招
class WuShenEffect(Effect):

    phase = BattlePhase.Finish

    skill_style = ""

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject.id not in battle.exps:
            return
        if subject.studying is not None and skill_style in subject.studying.belongs.tags:
            battle.exps[subject.id] *= 2


# 吸髓
class XiSuiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effect_on = False
        effe_factor = self.factor(subject)
        total_drain = 0
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            effect_on = True
            mp_drain = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * self.level * effe_factor)
            mp_drain = max(mp_drain, -1 * obj.mp)
            subject.mp_delta -= mp_drain
            obj.mp_delta += mp_drain
            #if obj.hp + obj.hp_delta > 0:
            #    obj.hp_delta -= min(-1 * obj.hp_delta, mp_drain)
            total_drain += mp_drain
        #subject.correct()
        if not battle.silent and effect_on:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"mp_drain": -1 * total_drain})


# 吸血
class XiXueEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effect_on = False
        effe_factor = self.factor(subject)
        total_drain = 0
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            effect_on = True
            hp_drain = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * self.level * effe_factor)
            subject.hp_delta -= hp_drain
            total_drain += hp_drain
        #subject.correct()
        if not battle.silent and effect_on:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"hp_drain": -1 * total_drain})


# 先机
class XianJiEffect(Effect):

    influence = "Jing"

    ratio_upper = 0.5
    ratio_middle = 0.25

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        #effe_ratio = self.ratio(subject)
        effe_ratio = 1
        if not common.if_rate(effe_ratio):
            return
        if subject.skill_counter is not None:
            p_tgt = battle.map.location(subject)
            q_tgt = battle.map.location(battle.sequence[-1]["action"].subject)
            if not battle.skill_ava(subject, subject.skill_counter):
                return
            counter_range = battle.map.shape_scope(p_tgt, subject.skill_counter.shape)
            if q_tgt not in counter_range:
                return
            #dis = battle.map.distance(s_tgt, p_tgt)
            #counter_range = subject.skill_counter.shape.attack_range()
            #if counter_range[0] >= dis or counter_range[1] < dis:
            #    return
            add_ac = BattleSkillAction(subject=subject, battle=battle,
                                       skill=subject.skill_counter, target=q_tgt, scope=[q_tgt],
                                       objects=[battle.sequence[-1]["action"].subject])
            battle.sequence[-1]["action"].additions.insert(0, add_ac)
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": battle.sequence[-1]["action"].subject.name})


# 卸劲
class XieJinEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject not in battle.sequence[-1]["action"].objects:
            return
        effe_factor = self.factor(subject)
        mp_trans = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * self.level * 0.1 * effe_factor)
        subject.hp_delta += mp_trans
        subject.mp_delta -= mp_trans
        #MSG(style=MSG.Effect, subject=subject, effect=self, details={"mp_trans": mp_trans})


# 薰风
class XunFengEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if len(battle.sequence) == 0 or subject != battle.sequence[-1]["action"].subject:
            return
        effelib = importlib.import_module("proj.builtin.effects")
        plist = []
        sub_loc = battle.map.location(subject)
        for pt in battle.map.circle(sub_loc, 2, mr=0):
            p = battle.map.loc_entity.get(pt, None)
            if p is None or not battle.is_friend(subject, p):
                continue
            plist.append(p)
        effelib.QuFengEffect(level=self.level).work(subject, objects=plist, **kwargs)
        effelib.HuaYuEffect(level=self.level).work(subject, objects=plist, **kwargs)
        if battle is not None and not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"poison_recover": self.level})


# 移花
class YiHuaEffect(Effect):

    phase = BattlePhase.BeforeDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        obj_loc = battle.sequence[-1]["action"].target
        obj = battle.map.loc_entity.get(obj_loc, None)
        if obj is None:
            return
        suj_loc = battle.map.location(subject)
        battle.map.remove(subject)
        battle.map.remove(obj)
        if not battle.map.can_stay(subject, obj_loc) or not battle.map.can_stay(obj, suj_loc):
            battle.map.locate(subject, suj_loc)
            battle.map.locate(obj, obj_loc)
            return
        battle.map.locate(subject, obj_loc)
        battle.map.locate(obj, suj_loc)
        battle.moved[subject.id] = False
        BattleMoveAction(active=False, showmsg=False, battle=battle, subject=subject, target=obj_loc,
                         path=[obj_loc, suj_loc]).do()
        BattleMoveAction(active=False, showmsg=False, battle=battle, subject=obj, target=suj_loc,
                         path=[suj_loc, obj_loc]).do()
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"subject": subject.name,
                                                                         "object": obj.name})


# 益气
class YiQiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs.get("battle", None)
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_factor = self.factor(subject)
        for obj in objects:
            wound_recover = min(obj.wound, int(self.level * effe_factor))
            obj.wound -= wound_recover
            if battle is not None and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self,
                    details={"object": obj.name, "wound_recover": wound_recover})


# 瘀毒
class YuDuEffect(Effect):

    influence = "Zhi"

    from_damage = True

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_factor = self.factor(subject)
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            poison_mp = 0
            if not self.from_damage:
                poison_mp = int(-1 * effe_factor * self.level * obj.anti_poison)
            else:
                poison_mp = int(battle.event(obj, BattleEvent.HPDamaged)["value"] * 0.01 * effe_factor * self.level * obj.anti_poison)
            obj.poison_mp -= poison_mp
            if poison_mp != 0 and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name, "poison_mp": -1 * poison_mp})
