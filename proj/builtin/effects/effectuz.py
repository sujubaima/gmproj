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
 
 
# 无畏            
class WuWeiEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        if battle.current == subject:
            return
        max_damage = None
        if len(battle.sequence) > 1:
            for seq in battle.sequence[-2::-1]:
                if seq["current"] == subject:
                    break
                if not isinstance(seq["action"], BattleSkillAction):
                    continue
                if subject == seq["action"].subject:
                    continue
                if battle.is_friend(subject, seq["action"].subject):
                    continue
                if subject not in seq["action"].objects or \
                   "results" not in seq or subject.id not in seq["results"] or \
                   BattleEvent.ACTMissed in seq["results"][subject.id]:
                    continue
                max_damage = seq["results"][subject.id][BattleEvent.HPDamaged]["value"]
                #print(seq["action"], seq["action"].subject.name, max_damage)
                break
        if max_damage is not None and subject.hp_delta < max_damage:
            subject.hp_delta = max_damage
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self)    
            

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
            battle.additions.insert(0, add_ac)
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, 
                    details={"object": battle.sequence[-1]["action"].subject.name})


# 卸劲
class XieJinEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return 
        if subject.hp + subject.hp_delta <= 0:
            return
        effe_factor = self.factor(subject)
        mp_trans = int(battle.event(subject, BattleEvent.HPDamaged)["value"] * self.level * 0.01 * effe_factor)
        mp_trans = max(-1 * subject.mp, mp_trans)
        if mp_trans != 0:
            subject.hp_delta -= mp_trans
            subject.mp_delta += mp_trans
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"mp_trans": -1 * mp_trans})


# 虚耗
class XuHaoEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        subject.mp_delta *= 2


# 虚晃
class XuHuangEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        if len(objects) == 0:
            objects = battle.sequence[-1]["action"].objects
        for obj in objects:
            #if battle.event(obj, BattleEvent.ACTMissed) is not None:
            #    continue
            dire = random.sample([d for d in range(0, 6) if d != obj.direction], 1)[0]
            obj.direction = dire
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self, details={"object": obj.name})


# 薰风
class XunFengEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        #if len(battle.sequence) == 0 or subject != battle.sequence[-1]["action"].subject:
        #    return
        if battle.current != subject:
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


# 浴血
class YuXueEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject == battle.sequence[-1]["action"].subject:
            return
        if subject not in battle.sequence[-1]["action"].objects:
            return
        if battle.event(subject, BattleEvent.ACTMissed) is not None:
            return
        base_damage = battle.event(subject, BattleEvent.HPDamaged)["value"]
        effe_factor = self.factor(subject)
        sub_loc = battle.map.location(subject)
        for loc in battle.map.circle(sub_loc, 2):
            obj = battle.map.loc_entity.get(loc, None)
            if obj is None or not battle.is_enemy(subject, obj):
                continue
            hp_delta = common.random_gap(base_damage * 0.01 * self.level * effe_factor, 0.025)
            obj.hp_delta += hp_delta
            if not battle.silent:
                MSG(style=MSG.Effect, subject=subject, effect=self,
                details={"object": obj.name, "hp_delta": -1 * hp_delta})


# 云剑
class YunJianEffect(ExertEffect):

    def initialize(self):
        super(YunJianEffect, self).initialize()
        sts_tpl = "STATUS_YUNJIAN_ANONYMOUS"
        self.exertion = Status.template(sts_tpl)

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        target = battle.sequence[-1]["action"].target
        stash_key = "YunJianStash"
        if stash_key not in battle.map.stash:
            battle.map.stash[stash_key] = {}
        locations = []
        for loc in battle.map.circle(target, 2, mr=0):
            grid = battle.map.xy[loc[0]][loc[1]]
            if grid.object is not None:
                continue
            if not loc in battle.map.stash[stash_key]:
                battle.map.stash[stash_key][loc] = grid.terran
                new_terran = Terran.template("TERRAN_CLOUD")
                new_terran.tpl_id = grid.terran.tpl_id
                grid.terran = new_terran
            locations.append(loc)
        super(YunJianEffect, self).work(subject, objects=objects,
                                        status_attr={"locations": locations}, **kwargs)


class YunJianAnonymousEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        status = kwargs["status"]
        jy_sts = []
        for sts in subject.status:
            if sts.tpl_id == status.tpl_id:
                jy_sts.append(sts)
        if len(jy_sts) > 1 and jy_sts[0] != status:
            return
        stash_key = "YunJianStash"
        p = battle.current
        if battle.is_friend(subject, p):
            return
        p_loc = battle.map.location(p)
        if stash_key not in battle.map.stash or \
           p_loc not in battle.map.stash[stash_key]:
            return
        hp_delta = int(subject.attack_base * 0.75)
        p.hp_delta -= hp_delta
        if not battle.silent:
            MSG(style=MSG.Effect, subject=subject, effect=self,
                details={"object": p.name, "hp_delta": hp_delta})

    def leave(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        status = kwargs["status"]
        stash_key = "YunJianStash"
        loc_set = set()
        for sts in subject.status:
            if sts != status and sts.tpl_id == status.tpl_id:
                loc_set.update(sts.locations)
        for loc in status.locations:
            if loc not in loc_set:
                grid = battle.map.xy[loc[0]][loc[1]]
                old_terran = battle.map.stash[stash_key].pop(loc)
                grid.terran = old_terran
       

# 震慑
class ZhenSheEffect(Effect):

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
            if obj != status.exertor:
                continue
            obj.hp_delta = int(obj.hp_delta * 0.8)
            obj.mp_delta = int(obj.mp_delta * 0.8)


# 驻颜
class ZhuYanEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        battle = kwargs["battle"]
        if subject != battle.sequence[-1]["action"].subject:
            return
        subject.mp_delta = 0


# 醉意
class ZuiYiEffect(Effect):

    pass
