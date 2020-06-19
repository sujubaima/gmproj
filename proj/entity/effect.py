# -- coding: utf-8 --
import importlib
import math
import copy

from proj.engine import Message as MSG

from proj.entity.common import Entity
from proj.entity.constants import BattleEvent
from proj.entity.constants import BattlePhase
from proj.entity.constants import StatusAcceptType
from proj.entity.constants import StatusOverType
from proj.entity.constants import AttrText

from proj.utils import Exponential
from proj.utils import if_rate


class InfluentedEntity(Entity):

    influence = None

    factor_lower = None
    factor_middle = None
    factor_upper = None

    def finish(self):
        super(InfluentedEntity, self).finish()
        if self.influence is not None:
            self.factor_exp = Exponential(lower=self.factor_lower,
                                          middle=self.factor_middle,
                                          upper=self.factor_upper)
    
    def factor(self, person, reverse=False):
        if self.influence is None:
            return 1
        elif reverse:
            return self.factor_exp.value(-1 * person.special(self.influence))
        else:
            return self.factor_exp.value(person.special(self.influence)) 


class Effect(InfluentedEntity):

    All = {}

    phase = BattlePhase.AfterAttack

    influence = None

    factor_lower = None
    factor_middle = None
    factor_upper = None

    #ratio_lower = None
    #ratio_middle = None
    #ratio_upper = None
    
    @classmethod
    def fromjson(cls, etpl):
        tp = etpl["id"]
        #tpsplit = tp.split(".")
        #if tpsplit[0] == "EXERT" and len(tpsplit) == 3:
        #    status = Status(effects=[Effect.template(tpsplit[2])])
        #    effeobj = ExertEffect(exertion=status, **etpl)
        #    effeobj.exertion.leftturn = etpl.get("turns", -1)
        #elif tpsplit[0] == "EXERT":
        #    effeobj = ExertEffect(exertion=Status.template(tpsplit[1]), **etpl)
        #    effeobj.exertion.leftturn = etpl.get("turns", -1)
        #else:
        #    effeobj = Effect.template(tp)
        if tp.startswith("EXERT."):
            status = Status.template(tp[6:])
            effeobj = ExertEffect(exertion=status, **etpl)
            effeobj.exertion.leftturn = etpl.get("turns", -1)
        else:
            effeobj = Effect.template(tp)
        effe_id = effeobj.id
        effeobj.load(**etpl)
        effeobj.id = effe_id
        return effeobj

    def finish(self):
        super(Effect, self).finish()
        if self.phase is not None and not isinstance(self.phase, int):
            vsplit = self.phase.split(",")
            flag = 0
            for vs in vsplit:
                flag = flag | eval("BattlePhase.%s" % vs)
            self.phase = flag
        Effect.All[self.name] = self

    def initialize(self):
        self.id = None
        self.name = None
        self.text = ""
        self.style = 0

        self.level = 1

    # 如果是战斗中发动效果，objects为空，battle为当前战斗实例
    # 如果非战斗中发动效果，battle为空
    def work(self, subject, objects=[], **kwargs):
        pass

    def leave(self, subject, objects=[], **kwargs):
        pass


class Status(InfluentedEntity):

    @classmethod
    def template(cls, tpl_id):
        if tpl_id.startswith("LAMBDA."):
            status = Status(effects=[Effect.template(tpl_id.split(".")[1])])
            status.tpl_id = tpl_id
            return status 
        else:
            return super(Status, cls).template(tpl_id)
        
    def handle(self, k, v):
        if k == "phase":
            vsplit = v.split(",")
            flag = 0
            for vs in vsplit:
                flag = flag | eval("BattlePhase.%s" % vs)
            setattr(self, k, flag)
        elif k == "functions":
            ret = []
            for efpl in v:
                #effeobj = Effect.template(efpl["id"])
                #effe_id = effeobj.id
                #effeobj.load(**efpl)
                #effeobj.id = effe_id
                effeobj = Effect.fromjson(efpl)
                ret.append(effeobj)
            setattr(self, "effects", ret)
        elif k == "overtype":
            tp = eval("StatusOverType.%s" % v)
            setattr(self, k, tp)
        elif k == "accepttype":
            tp = eval("StatusAcceptType.%s" % v)
            setattr(self, k, tp)
        elif k == "text":
            self.text_ = v
        else:
            setattr(self, k, v)

    def initialize(self):
        self.name = None
        self.source = None
        self.exertor = None
        self.style = 0

        self.effects = []

        self.phase = 1
        self.startturn = -1
        self.leftturn = -1
        self.forever = False
        self.countable = False

        self.worked = False

        self.ratio = 1

        self.text_ = None

        self.accepttype = StatusAcceptType.Different
        self.overtype = StatusOverType.Prolong

    def finish(self):
        super(Status, self).finish()
        self.countable = self.countable or self.name is not None

    def work(self, subject, objects=[], **kwargs):
        if self.influence is not None:
            ratio = self.ratio * self.factor(subject)
            if not if_rate(ratio):
                return 
        for effe in self.effects:
            effe.work(subject, objects=objects, status=self, **kwargs)
        if not self.worked:
            self.worked = True

    def leave(self, subject, objects=[], **kwargs):
        for effe in self.effects:
            effe.leave(subject, objects=objects, status=self, **kwargs)
        subject.status.remove(self)
            
    def clone(self):
        if self.tpl_id is not None:
            sts = Status.template(self.tpl_id)
        else:
            sts = Status(name=self.name, style=self.style, effects=self.effects, description=self.description)
        sts.phase = self.phase
        sts.tpl_id = self.tpl_id
        sts.overtype = self.overtype
        sts.accepttype = self.accepttype
        sts.ratio = self.ratio
        sts.influence = self.influence
        sts.factor_lower = self.factor_lower
        sts.factor_middle = self.factor_middle
        sts.factor_upper = self.factor_upper
        sts.factor_exp = self.factor_exp
        return sts

    def accept(self, tgt):
        st = tgt.already(self, exertor=self.exertor, source=self.source)
        if self.accepttype == StatusAcceptType.Unover:
            ac = False 
        elif self.accepttype == StatusAcceptType.Different:
            ac = st is None
        elif self.accepttype == StatusAcceptType.Overlap:
            ac = True
        if ac and self.overtype == StatusOverType.Prolong and st is not None:
            st.exertor = self.exertor
            st.source = self.source
            if st.leftturn <= self.leftturn:
                st.leftturn = self.leftturn + 1
            ac = False
        return ac
        
    @property
    def text(self):
        if self.text_ is not None:
            return self.text_
        ret = []
        for effe in self.effects:
            ret.append(effe.text)
        return "；".join(ret)


class ExertEffect(Effect):

    TargetFunc = {"Enemies": lambda battle, subject: battle.enemies(subject),
                  "Friends": lambda battle, subject: battle.friends(subject),
                  "Subject": lambda battle, subject: [battle.sequence[-1]["action"].subject],
                  "Objects": lambda battle, subject: [obj for obj in battle.sequence[-1]["action"].objects \
                                                          if battle.event(obj, BattleEvent.ACTMissed) is None]}
                                                           
    def initialize(self):                                  
        super(ExertEffect, self).initialize()              
        self.targets = "Objects"
        self.targetstr = None
        self.exertor = "Subject"
        self.exertion = None
        self.text_ = "对{object}施加了{status}状态"
        self.description_ = "对{targetstr}施加{status}状态"
        self.style = None
        self.base_ratio = 1
        self.showmsg = True
        
    def handle(self, k, v):
        if k == "exertion" and isinstance(v, str):
            self.exertion = Status.template(v)
        else:
            setattr(self, k, v)

    def finish(self):
        super(ExertEffect, self).finish()
        if self.targetstr is None and self.targets == "Subject":
            self.targetstr = ("自身", "自身")
        elif self.targetstr is None:
            self.targetstr = ("目标", "其")
        if self.exertion is not None:
            if self.tpl_id is None:
                self.tpl_id = "EXERT.%s" % self.exertion.tpl_id
            if self.name is None:
                self.name = self.exertion.name
            if self.description is None and self.exertion.name is not None:
                self.description = self.description_.format(targetstr=self.targetstr[0], status=self.exertion.name)
                #self.description += "，使%s%s" % (self.targetstr, self.exertion.description)
                self.description += "，使%s%s" % (self.targetstr[1], self.exertion.description)
                self.text = self.text_ + "；{text}"
            if self.style is None:
                self.style = self.exertion.style
        
    def work(self, subject, objects=[], **kwargs):
        ratio = self.factor(subject) * self.base_ratio
        if not if_rate(ratio):
            return
        battle = kwargs.get("battle", None)
        source = kwargs.get("source", None)
        if battle is None and len(objects) == 0:
            objects = [subject]
        elif len(objects) == 0:
            objects = ExertEffect.TargetFunc[self.targets](battle, subject)
        for tgt in objects:
            #if not if_rate(ratio):
            #    continue
            exertion = self.exertion.clone()
            exertion.exertor = subject
            if source is not None:
                exertion.source = source
            if self.turns is not None:
                exertion.leftturn = self.turns
            if not exertion.accept(tgt):
                continue
            if battle is not None:
                exertion.startturn = battle.turnidx
            status_attr = kwargs.get("status_attr", None)
            if status_attr is not None:
                for attrk, attrv in status_attr.items():
                    setattr(exertion, attrk, attrv)
            tgt.status.append(exertion)
            if exertion.phase & 1 != 0:
                if "status" in kwargs:
                    kwargs.pop("status")
                exertion.work(tgt, objects=objects, **kwargs)
            if self.showmsg and battle is not None and not battle.silent and exertion.name is not None:
                detail_map = {"subject": subject.name, "object": tgt.name, "status": exertion.name}
                if exertion.phase & 1 != 0:
                    detail_map["text"] = exertion.text.format(**detail_map)
                else:
                    detail_map["text"] = "%s%s" % (tgt.name, self.exertion.description)
                MSG(style=MSG.Effect, subject=subject, effect=self, 
                    details=detail_map)
                #for effe in exertion.effects:
                #    effe.work(tgt, objects=objects, status=exertion, **kwargs)
        
    def leave(self, subject, objects=[], **kwargs):
        source = kwargs.get("source", None)
        sts = []
        for st in subject.status:
            if st.source == source:
                sts.append(st)
        for exertion in sts:
            exertion.leave(subject, objects=objects, **kwargs)
            #subject.status.remove(exertion) 
            #Status.remove(exertion)


class PersonAddSkillEffect(Effect):
    """
    允许角色习得某技能
    """
    def work(self, subject, objects=[], **kwargs):
        sllib = importlib.import_module("proj.entity.skill")
        skill = sllib.Skill.template(self.skill)
        if skill.belongs is None:
            skill.belongs = self.belongs
        else:
            skill.belongs = sllib.SuperSkill.one(skill.belongs)
        skill.rank = skill.belongs.rank
        subject.skills.append(skill)
        for idx, sk in enumerate(subject.skills_equipped):
            if sk is None:
                subject.skills_equipped[idx] = skill
                break
        if len(subject.skills) > 1 and subject.skills[0].tpl_id == "SKILL_WANGBAQUAN_1":
            subject.remove_skill(subject.skills[0])
        

    def leave(self, subject, objects=[], **kwargs):
        sllib = importlib.import_module("proj.entity.skill")
        for skill in subject.skills:
            if skill.tpl_id == self.skill:
                break
        subject.remove(skill)
        sllib.Skill.remove(skill)
        
        
class PersonAddInnerSkillEffect(Effect):
    """
    允许角色习得某技能
    """
    def work(self, subject, objects=[], **kwargs):
        sllib = importlib.import_module("proj.entity.skill")
        skill = sllib.Skill.template(self.skill)
        if skill.belongs is None:
            skill.belongs = self.belongs
        skill.rank = skill.belongs.rank
        subject.skills_inner.append(skill)

    def leave(self, subject, objects=[], **kwargs):
        sllib = importlib.import_module("proj.entity.skill")
        for skill in subject.skills_inner:
            if skill.tpl_id == self.skill:
                break
        subject.skills_inner.remove(skill)
        sllib.Skill.remove(skill)


class EntityChangeAttributeEffect(Effect):

    def finish(self):
        super(EntityChangeAttributeEffect, self).finish()
        self.attrs = copy.deepcopy(self.attrs)

    def modify(self, subject, reverse=False, **kwargs):
        status = kwargs.get("status", None)
        for attr in self.attrs:
            attrname = attr["name"]
            if "value" in attr:
                if reverse:
                    if attr.get("locked", False):
                        subject.locked.remove(attrname)
                    if attrname not in subject.locked:
                        newattr = subject.stash[attrname]
                        setattr(subject, attrname, newattr)
                else:
                    newattr = attr["value"]
                    if attrname not in subject.locked:
                        oldattr = getattr(subject, attrname)
                        subject.handle(attrname, newattr)
                    subject.stash[attrname] = oldattr
                    if attr.get("locked", False):
                        subject.locked.add(attrname)
            elif "delta" in attr:
                delta = (-1 * attr["delta"]) if reverse else attr["delta"]
                #print(subject.name, attr, delta)
                if attrname not in subject.locked:
                    oldattr = getattr(subject, attrname)
                    newattr = oldattr + delta
                    setattr(subject, attrname, newattr)
                    if status is not None and status.countable:
                        deltaname = "delta_%s" % attrname
                        subject.stash[deltaname] = subject.stash.get(deltaname, 0) + delta 
                if attrname in subject.stash:
                    subject.stash[attrname] += delta
            elif "ratio" in attr:
                ratio = attr["ratio"]
                #print(subject.name, attr, ratio)
                if attrname not in subject.locked:
                    oldattr = getattr(subject, attrname)
                    newattr = oldattr / ratio if reverse else oldattr * ratio
                    setattr(subject, attrname, newattr)
                    if status is not None and status.countable:
                        rationame = "ratio_%s" % attrname
                        if reverse:
                            subject.stash[rationame] = subject.stash.get(rationame, 1) / ratio
                        else:
                            subject.stash[rationame] = subject.stash.get(rationame, 1) * ratio
                if attrname in subject.stash:
                    if reverse:
                        subject.stash[attrname] /= ratio
                    else:
                        subject.stash[attrname] *= ratio

    def work(self, subject, objects=[], **kwargs):
        self.modify(subject, **kwargs)

    def leave(self, subject, objects=[], **kwargs):
        self.modify(subject, reverse=True, **kwargs)

    
class PersonChangeAttributeEffect(EntityChangeAttributeEffect):
    pass


class PersonSkillChangeAttributeEffect(EntityChangeAttributeEffect):
    """
    修改技能属性
    """

    def choose(self, subject):
        skill = None
        for s in subject.skills + subject.skills_inner:
            if s.tpl_id == self.skill:
                skill = s
                break
        return skill

    def work(self, subject, objects=[], **kwargs):
        skill = self.choose(subject)
        self.modify(skill, **kwargs)

    def leave(self, subject, objects=[], **kwargs):
        skill = self.choose(subject)
        self.modify(skill, reverse=True, **kwargs)


class PersonSkillEffectChangeAttributeEffect(EntityChangeAttributeEffect):
    
    def choose(self, subject):
        skill = None
        for s in subject.skills + subject.skills_inner:
            if self.skill is not None and s.tpl_id == self.skill:
                skill = s
                break
        effect = None
        for idx, e in enumerate(skill.effects):
            if (self.effect is not None and e.tpl_id == self.effect) or \
               (self.index is not None and idx == self.index):
                effect = e
                break
        return effect

    def work(self, subject, objects=[], **kwargs):
        effect = self.choose(subject)
        self.modify(effect, **kwargs)

    def leave(self, subject, objects=[], **kwargs):
        effect = self.choose(subject)
        self.modify(effect, reverse=True, **kwargs)
        
        
class EntityAddEffectEffect(Effect):

    def work(self, subject, objects=[], **kwargs):
        effeobj = Effect.fromjson(self.effect)
        subject.effects.append(effeobj)

    def leave(self, subject, objects=[], **kwargs):
        for effe in subject.effects:
            if effe.tpl_id == self.effect["id"]:
                break
        subject.effects.remove(effe)
        Effect.remove(effe)


class PersonSkillAddEffectEffect(Effect):
    """
    增加技能效果
    """
    def work(self, subject, objects=[], **kwargs):
        for s in subject.skills + subject.skills_inner:
            if s.tpl_id == self.skill:
                skill = s
                break
        effeobj = Effect.fromjson(self.effect)
        skill.effects.append(effeobj)

    def leave(self, subject, objects=[], **kwargs):
        for s in subject.skills + subject.skills_inner:
            if s.tpl_id == self.skill:
                skill = s
                break
        for effe in skill.effects:
            if effe.tpl_id == self.effect["id"]:
                break
        skill.effects.remove(effe)
        Effect.remove(effe)
        
        
class PersonSkillRemoveEffectEffect(PersonSkillAddEffectEffect):

    def work(self, subject, objects=[], **kwargs):
        super(PersonSkillRemoveEffectEffect, self).leave(subject, objects, **kwargs)
        
    def leave(self, subject, objects=[], **kwargs):
        super(PersonSkillRemoveEffectEffect, self).work(subject, objects, **kwargs)


class SkillStudyEffect(Effect):
    """
    开始修炼技能
    """
    def work(self, subject, objects=[], **kwargs):
        person = objects[0]
        sllib = importlib.import_module("proj.entity.skill")
        odlib = importlib.import_module("proj.console.orders")
        superskill = sllib.SuperSkill.one(self.superskill)
        odlib.PersonStudySkillOrder(subject=person, superskill=superskill)

    def leave(self, subject, objects=[], **kwargs):
        subject.studying = None
        
        
class ItemMakeEffect(Effect):

    def initialize(self):
        super(ItemMakeEffect, self).initialize()
        self.quantity = 1
        self.rate = 0.6

    def handle(self, k, v):
        olib = importlib.import_module("proj.entity.item")
        if k == "item":
            self.item = olib.Item.one(v)
        else:
            setattr(self, k, v)

    def work(self, subject, objects=[], **kwargs):
        products = kwargs["products"]
        ratio_f = 0
        for recipe in subject.recipes:
            if len(self.item.tags & recipe.tags) > 0:
                ratio_f += 1
        alib = importlib.import_module("proj.builtin.actions")
        if if_rate(self.rate * math.pow(1.004, ratio_f)):
            alib.PersonItemAcquireAction(subject=subject, item=self.item, quantity=self.quantity).do()
            products.append((self.item, self.quantity))
        else:
            alib.PersonSpeakAction(talker=None, content="配方制作失败！").do()
