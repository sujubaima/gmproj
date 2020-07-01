# -- coding: utf-8 --

import random
import math
import importlib

from proj.entity import Effect
from proj.entity import Status
from proj.entity import BattleEvent
from proj.entity import BattlePhase
from proj.entity import Terran
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


# 豪气干云
class HaoQiGanYunEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        hit = False
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                hit = True
                break
        sts_tpl = "STATUS_HAOQIGANYUN_ANONYMOUS"
        if hit:
            sts = Status.template(sts_tpl)
            subject.status.append(sts)
            sts.work(subject)


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


# 换骨
class HuanGuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if battle.turnidx > self.level:
            return
        old_sts = None
        sts_tpl = "STATUS_HUANGU_ANONYMOUS"
        for sts in subject.status:
            if sts.tpl_id == sts_tpl:
                old_sts = sts
        if old_sts is not None:
            old_sts.leave(subject) 
        sts = Status.template(sts_tpl)
        sts.effects[0].attrs = [{"name": "counter_rate_", "delta": 0.01 * battle.turnidx},
                                {"name": "critical_rate_", "delta": 0.01 * battle.turnidx},
                                {"name": "dodge_rate_", "delta": 0.01 * battle.turnidx},
                                {"name": "anti_damage_rate_", "delta": 0.01 * battle.turnidx}]
        subject.status.append(sts)
        sts.work(subject)


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


# 金刚不坏
class JinGangBuHuaiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if battle.is_friend(subject, battle.sequence[-1]["action"].subject):
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        effe_factor = self.factor(subject)
        effe_ratio = 0.2 * effe_factor
        if subject.hp_delta < 0 and common.if_rate(effe_ratio):
            subject.hp_delta = -1
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self)


# 禁用
class JinYongEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        for ac in self.action.split(","):
            if ac == "Move":
                sts_map = battle.moved
            elif ac == "Attack":
                sts_map = battle.attacked
            elif ac == "Item":
                sts_map = battle.itemed
            elif ac == "Rest":
                sts_map = battle.rested
            sts_map[subject.id] = True


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
            obj.hp_delta += hp_enhance
            obj.mp_delta += mp_enhance
        if not battle.silent and effe_on:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"enhance": "%s%%" % self.level})


# 击退
class JiTuiEffect(Effect):

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
            obj_tgt = battle.map.neighbour(obj_loc, dire)
            #print(obj.name, obj_loc, obj_tgt)
            if not battle.map.on_map(obj_tgt) or not battle.map.can_stay(obj, obj_tgt):
                continue
            current_distance = battle.map.distance(obj_tgt, sub_loc)
            if obj_tgt != obj_loc and current_distance > obj_distance:
                BattleMoveAction(showmsg=False, active=False,
                                 battle=battle, subject=obj, target=obj_tgt,
                                 path=[obj_tgt, obj_loc]).do()
                MSG(style=MSG.Effect, subject=subject, effect=self,
                    details={"object": obj.name})


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
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        hp_enhance = int(subject.hp_delta * 0.01 * self.level)
        mp_enhance = int(subject.mp_delta * 0.01 * self.level)
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, details={"enhance": "%s%%" % self.level})


# 涓流
class JuanLiuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        for skill in subject.skills:
            skill.stash["mp"] = skill.mp
            skill.mp = int(skill.mp * 0.8)

    def leave(self, subject, objects=[], **kwargs):
        for skill in subject.skills:
            skill.mp = skill.stash.pop("mp")


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
            if not battle.map.is_on_map(pt) or not battle.map.can_stay(subject, pt):
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
        battle.attacked[subject.id] = False
        add_ac = BattleSkillAction(subject=subject, battle=battle,
                                   skill=skill, target=target, scope=scope,
                                   objects=newobjs)
        battle.additions.append(add_ac)
        #battle.attacked[subject.id] = False
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self)


# 连枝（获取增益）
class LianZhiBuffEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        #if battle.event(subject, BattleEvent.ACTMissed) is not None:
        #    return
        obj_loc = battle.sequence[-1]["action"].target
        obj = battle.map.loc_entity.get(obj_loc, None)
        if obj is None:
            return
        if battle.event(obj, BattleEvent.ACTMissed) is not None:
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
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, 
                details={"object": obj.name, "status": "【%s】" % final_sts.name})


# 连枝（施加负面）
class LianZhiDebuffEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        #if battle.event(subject, BattleEvent.ACTMissed) is not None:
        #    return
        obj_loc = battle.sequence[-1]["action"].target
        obj = battle.map.loc_entity.get(obj_loc, None)
        if obj is None:
            return
        if battle.event(obj, BattleEvent.ACTMissed) is not None:
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
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, 
                details={"object": obj.name, "status": "【%s】" % final_sts.name})


# 连枝
class LianZhiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        Effect.template("EFFECT_LIANZHI_BUFF").work(subject, objects=objects, **kwargs)
        Effect.template("EFFECT_LIANZHI_DEBUFF").work(subject, objects=objects, **kwargs)


# 流光
class LiuGuangEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if battle.current != subject:
            return
        mp_delta = int(subject.mp_limit * 0.06)
        subject.mp_delta -= mp_delta
        plist = []
        sub_loc = battle.map.location(subject)
        for loc in battle.map.circle(sub_loc, 2):
            p = battle.map.loc_entity.get(loc, None)
            if p is None or not battle.is_friend(subject, p):
                continue
            plist.append(p) 
        for p in plist:
            if p.mp == p.mp_limit:
                continue
            p.mp_delta += int(mp_delta / len(plist))
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": p.name})


# 美人如玉
class MeiRenRuYuEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        for obj in objects:
            if battle.event(obj, BattleEvent.ACTMissed) is not None:
                continue
            if obj.sex != 0:
                continue
            obj.hp_delta = int(obj.hp_delta * 1.3)
            obj.mp_delta = int(obj.mp_delta * 1.3)


# 明月照大江
class MingYueZhaoDaJiangEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if battle.is_friend(subject, battle.sequence[-1]["action"].subject):
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        attacker = battle.sequence[-1]["action"].subject
        counter_base = round(1 + attacker.attack_base / 400, 2)
        effelib = importlib.import_module("proj.builtin.effects")
        sts_tpl = "STATUS_MINGYUEZHAODAJIANG_ANONYMOUS"
        sts = Status.template(sts_tpl)
        sts.effects[0].attrs = [{"name": "counter_rate_factor_", "ratio": counter_base}]
        subject.status.append(sts)
        sts.work(subject)

class MingYueZhaoDaJiangLeaveEffect(Effect):
      
    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if battle.is_friend(subject, battle.sequence[-1]["action"].subject):
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        sts_tpl = "STATUS_MINGYUEZHAODAJIANG_ANONYMOUS"
        for sts in subject.status:
            if sts.tpl_id != sts_tpl:
                continue
            sts.leave(subject)


# 迷形
class MiXingEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        attacker = battle.sequence[-1]["action"].subject
        attacker.direction = (attacker.direction + 3) % 6
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self, 
                details={"attacker": attacker.name, "subject": subject.name})


# 摩诃无量
class MoHeWuLiangEffect(Effect):

   phase = BattlePhase.AfterDamage

   def work(self, subject, objects=[], **kwargs):
       battle = kwargs["battle"]
       if subject != battle.sequence[-1]["action"].subject:
           return
       if len(objects) == 0:
           objects = battle.sequence[-1]["action"].objects
       #damagelist = [-1]
       damagelist = []
       for seq in battle.sequence:
           if not isinstance(seq["action"], BattleSkillAction):
               continue
           if seq["action"].skill.tpl_id.startswith("SKILL_MOHEWULIANGZHANG"):
               continue
           if "results" not in seq:
               continue
           for objdict in seq["results"].values():
               if BattleEvent.HPDamaged not in objdict:
                   continue
               hp_damaged = objdict[BattleEvent.HPDamaged]["value"]
               if hp_damaged < 0:
                   damagelist.append(hp_damaged)
       damagelist.sort()
       idx = self.level
       #damage_base = damagelist[self.level] if len(damagelist) >= self.level + 1 else -1
       if len(damagelist) == 0:
           damage_base = -1
       else:
           damage_base = damagelist[min(len(damagelist) - 1, self.level)]
       mp_base = min(-1, int(damage_base * 0.3))
       skill_ability = battle.calculate_weapon(battle.sequence[-1]["action"].skill, subject, subject)[0]
       mp_skill = -1 * int(mp_base * math.pow(1.004, 100 - subject.neigong) * math.pow(1.004, 100 - skill_ability))
       damage_base = int(damage_base * min(1, subject.mp / mp_skill))
       subject.mp_delta -= min(mp_skill, subject.mp)
       for obj in objects:
           if battle.event(obj, BattleEvent.ACTMissed) is not None:
                return
           actual_damage = damage_base
           obj.hp_delta += actual_damage


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
            subject.wound -= int(hp_damage * 0.5)
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
            subject.wound -= int(mp_damage * 0.5)
            #subject.correct()
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self)
