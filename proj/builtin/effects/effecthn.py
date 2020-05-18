# -- coding: utf-8 --

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


# 含颦            
class HanPinEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        sts_count = 0
        pc_sts = []
        if self.level == 1:
            sts_tpl = "STATUS_HANPIN_ANONYMOUS"
        else:
            sts_tpl = "STATUS_HANPIN_ANONYMOUS_DA"
        for sts in subject.status:
            if sts.name is not None and sts.style == 0:
                sts_count += 1
            if sts.tpl_id == sts_tpl:
                pc_sts.append(sts)
        if sts_count > len(pc_sts):
            for i in range(sts_count - len(pc_sts)):
                sts = Status.template(sts_tpl)
                subject.status.append(sts)
                sts.work(subject)
        elif sts_count < len(pc_sts):
            for sts in pc_sts[0: len(pc_sts) - sts_count]:
                sts.leave(subject)


# 化瘀
class HuaYuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs.get("battle", None)
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_factor = self.factor(subject)
        for obj in objects:
            poison_recover = min(obj.poison_mp, int(self.level * effe_factor))
            obj.poison_mp -= poison_recover
            if battle is not None and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self,
                    details={"object": obj.name, "poison_recover": poison_recover})


# 回春
class HuiChunEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_factor = self.factor(subject)
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            recover = common.random_gap(int(self.level * effe_factor), 0.025)
            recover = max(0, recover - obj.poison_hp)
            obj.hp_delta += recover
            #obj.correct()
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name, "recover": recover})


# 接骨
class JieGuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs.get("battle", None)
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        effe_factor = self.factor(subject)
        for obj in objects:
            injury_recover = min(obj.injury, int(self.level * effe_factor))
            obj.injury -= injury_recover
            if battle is not None and not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self,
                    details={"object": obj.name, "injury_recover": injury_recover})


# 精武
class JingWuEffect(Effect):

    phase = BattlePhase.AfterDamage

    skill_style = ""

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_on = False
        for obj in battle.sequence[-1]["action"].objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            if self.skill_style not in battle.sequence[-1]["action"].skill.style:
                continue
            effe_on = True
            hp_enhance = int(obj.hp_delta * 0.01 * self.level)
            mp_enhance = int(obj.mp_delta * 0.01 * self.level)
            #old_delta = obj.hp_delta
            obj.hp_delta += hp_enhance
            obj.mp_delta += mp_enhance
            #obj.correct()
            #if obj.hp_delta != old_delta:
            #    battle.event(obj, BattleEvent.HPDamaged)["value"] += obj.hp_delta - old_delta
        if not battle.silent and effe_on:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"enhance": "%s%%" % self.level})


# 惧武
class JuWuEffect(Effect):

    phase = BattlePhase.AfterDamage

    skill_style = ""

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        if subject not in objects:
            return
        if self.skill_style not in battle.sequence[-1]["action"].skill.style:
            return
        hp_enhance = int(subject.hp_delta * 0.01 * self.level)
        mp_enhance = int(subject.mp_delta * 0.01 * self.level)
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"enhance": "%s%%" % self.level})


# 绝影
class JueYingEffect(Effect):

    phase = BattlePhase.BeforeAttack

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
        #old_dire = battle.map.direction(suj_loc, obj_loc)
        old_dire = (obj.direction + 3) % 6
        tmp_locs = []
        for pt in battle.map.circle(obj_loc, 1):
            if not battle.map.can_stay(subject, pt):
                continue
            new_dire = battle.map.direction(obj_loc, pt)
            dire_diff = abs(new_dire - old_dire)
            tmp_locs.append((pt, 1 if dire_diff == 5 else dire_diff))
        tmp_locs.sort(key=lambda x: x[1])
        target = tmp_locs[0][0]
        battle.moved[subject.id] = False
        BattleMoveAction(showmsg=False, active=False,
                         battle=battle, subject=subject, target=target,
                         path=[target, suj_loc]).do()
        #battle.redirect(subject, [obj], obj_loc, battle.sequence[-1]["action"].skill)
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"subject": subject.name,
                                                                         "object": obj.name})


# 离魂 
class LiHunEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.current:
            return
        pool = []
        for i in range(battle.map.x):
            for j in range(battle.map.y):
                #if (i, j) not in battle.map.loc_entity and \
                if battle.map.can_stay(subject, (i, j)):
                    pool.append((i, j))
        pos = random.sample(pool, 1)[0]
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"pos": pos})
        BattleMoveAction(motivated=False, battle=battle,
                         subject=subject, target=pos,
                         path=[pos, battle.map.location(subject)]).do()
        battle.moved[subject.id] = True


# 连击
class LianJiEffect(Effect):

    influence = "Dong"

    phase = BattlePhase.AfterSettlement

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        effe_ratio = self.factor(subject) * self.level * 0.01
        if not common.if_rate(effe_ratio):
            return
        skill = battle.sequence[-1]["action"].skill
        target = battle.sequence[-1]["action"].target
        scope = battle.sequence[-1]["action"].scope
        newobjs = []
        for pt in scope:
            q = battle.map.loc_entity.get(pt, None)
            if q is not None and q.hp > 0 and battle.skill_accept(skill, subject, q):
                newobjs.append(q)
        if len(newobjs) == 0:
            return
        add_ac = BattleSkillAction(subject=subject, battle=battle,
                                   skill=skill, target=target, scope=scope,
                                   objects=newobjs)
        battle.sequence[-1]["action"].additions.insert(0, add_ac)
        battle.attacked[subject.id] = False
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self)


# 连枝（获取增益）
class LianZhiBuffEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        obj_loc = battle.sequence[-1]["action"].target
        obj = battle.map.loc_entity.get(obj_loc, None)
        if obj is None:
            return
        candidates = []
        for sts in obj.status:
            if sts.name is not None and sts.style == 1 and subject.already(sts) is None:
                candidates.append(sts)
        if len(candidates) == 0:
            return
        final_sts = random.sample(candidates, 1)[0]
        ee = ExertEffect(exertion=final_sts, showmsg=False, turns=max(2, final_sts.leftturn))
        ee.work(subject=subject, objects=[subject], **kwargs)
        MSG(style=MSG.Effect, subject=subject, effect=self, 
            details={"object": obj.name, "status": "【%s】" % final_sts.name})


# 连枝（施加负面）
class LianZhiDebuffEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        obj_loc = battle.sequence[-1]["action"].target
        obj = battle.map.loc_entity.get(obj_loc, None)
        if obj is None:
            return
        candidates = []
        for sts in subject.status:
            if sts.name is not None and sts.style == 0 and obj.already(sts) is None:
                candidates.append(sts)
        if len(candidates) == 0:
            return
        final_sts = random.sample(candidates, 1)[0]
        ee = ExertEffect(exertion=final_sts, showmsg=False, turns=max(2, final_sts.leftturn))
        ee.work(subject=subject, objects=[obj], **kwargs)
        MSG(style=MSG.Effect, subject=subject, effect=self, 
            details={"object": obj.name, "status": "【%s】" % final_sts.name})


# 连枝
class LianZhiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        Effect.template("EFFECT_LIANZHI_BUFF").work(subject, objects=objects, **kwargs)
        Effect.template("EFFECT_LIANZHI_DEBUFF").work(subject, objects=objects, **kwargs)


# 逆脉（攻击） 
class NiMaiAttackEffect(Effect):

    phase = BattlePhase.AfterDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        if common.if_rate(0.5):
            hp_damage = max(subject.mp_delta, -1 * battle.sequence[-1]["action"].skill.mp)
            subject.mp_delta -= hp_damage
            subject.hp_delta += hp_damage
            subject.wound -= hp_damage * 0.3
            #subject.correct()
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self)


# 逆脉（防御）
class NiMaiDefenseEffect(Effect):

    phase = BattlePhase.AfterDamage

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        if common.if_rate(0.5):
            mp_damage = max(subject.hp_delta, -1 * (subject.mp + subject.mp_delta))
            subject.mp_delta += mp_damage
            subject.hp_delta -= mp_damage
            subject.wound -= mp_damage * 0.3
            #subject.correct()
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self)
