# -- coding: utf-8 --
import math
import random
import importlib

from proj.entity.common import Entity
from proj.entity.effect import Effect
from proj.entity.effect import ExertEffect
from proj.entity.effect import Status
from proj.entity.map import Shape


class SuperSkill(Entity):

    All = {}

    def handle(self, k, v):
        if k == "nodes":
            effectlib = importlib.import_module("proj.entity.effect")
            ret = []
            for ntpl in v:
                nd = SkillNode()
                effects = ntpl["functions"]
                for effe in effects:
                    tp = effe["type"]
                    effeobj = eval("effectlib.%sEffect" % tp)(belongs=self, **effe)
                    status = Status(effects=[effeobj])
                    nd.effects.append(ExertEffect(exertion=status)) 
                nd.belongs = self
                if "next" in ntpl:
                    nd.next.extend(ntpl["next"])
                nd.name = ntpl["name"]
                nd.description = ntpl.get("description")
                nd.exp = ntpl.get("exp", 0)
                if "tags" in ntpl:
                    nd.tags.update(ntpl["tags"].split(","))
                if "required" in ntpl:
                    nd.required.extend(ntpl["required"])
                ret.append(nd) 
            setattr(self, k, ret)
        else:
            setattr(self, k, v)

    def finish(self):
        for idx, nd in enumerate(self.nodes):
            for n in nd.next:
                self.nodes[n].previous.append(idx)
        SuperSkill.All[self.id] = self
    
    def initialize(self):
        self.name = None
        self.nodes = []
        self.skills = []
        self.effects = []
        self.effects_battle = []

    def add(self, node):
        self.nodes.append(itm)
        itm.belongs = self
        itm.rank = self.rank
        return self
        
    def check_required(self, person, req):
        attr = getattr(person, req["attrname"])
        lower, upper = req["range"][1:-1].split(",")
        lower = int(lower) if len(lower) > 0 else 0
        upper = int(upper) if len(upper) > 0 else 100
        if req["range"].startswith("("):
            lowerfunc = lambda x: x > lower
        else:
            lowerfunc = lambda x: x >= lower
        if req["range"].endswith(")"):
            upperfunc = lambda x: x < upper
        else:
            upperfunc = lambda x: x <= upper
        return lowerfunc(attr) and upperfunc(attr)

    def learn(self, person, idx):
        for effe in self.nodes[idx].effects:
            effe.work(person, objects=[person])
        person.learned.add(self.nodes[idx].id)
            
    def learn_status(self, person, idx):
        node = self.nodes[idx]
        if node.id in person.learned:
            return 0
        for t in node.tags:
            if not t.startswith("SKILL_"):
                continue
            sk = Skill.one(t)
            if sk in person.skills + person.skills_inner:
                return 0
        can_learn = True
        for req in node.required:
            if not self.check_required(person, req):
                can_learn = False
                break
        for p in node.previous:
            if self.learn_status(person, p) != 0:
                can_learn = False
                break
        return 1 if can_learn else -1


class SkillNode(Entity):

   def initialize(self):
       self.name = None
       self.description = ""
       self.belongs = None
       self.next = []
       self.previous = []
       self.effects = []
       self.tags = set()
       self.required = []
       self.rank = 0
       
   def learn(self, person):
       for effe in self.effects:
           effe.work(person, objects=[person])
       person.learned.add(self.id)


class Skill(Entity):

    blockmap = {"Seep": 0, "Swap": 1, "Emit": 2}

    @staticmethod
    def damage():
        pass

    @staticmethod
    def recover():
        pass

    @staticmethod
    def injury():
        pass

    @staticmethod
    def poison():
        pass

    def handle(self, k, v):
        if k == "shape":
            vsplit = v.split(",")
            ssplit = vsplit[0].split(".")
            if len(ssplit) == 1:
                block = 1
            else:
                block = Skill.blockmap[ssplit[1]]
            shp = eval("Shape.%s" % ssplit[0])
            pt = int(vsplit[1])
            sc = int(vsplit[2])
            if len(vsplit) == 4:
                ms = int(vsplit[3])
                setattr(self, k, Shape(shp, pt, sc, ms, block=block))
            else:
                setattr(self, k, Shape(shp, pt, sc, block=block))
        elif k == "effects":
            ret = []
            for etpl in v:
                effeobj = Effect.fromjson(etpl)
                ret.append(effeobj)
            setattr(self, k, ret)
        elif k == "style":
            sty = set()
            sty.update(v.split(","))
            setattr(self, k, sty)
            setattr(self, "tags", sty)
        else:
            setattr(self, k, v)

    def initialize(self):

        self.name = None
        self.rank = 0
        self.belongs = None 
        self.power = 0
        self.mp = 0
        self.yinyang = 0
        self.cd = 0
        self.style = None
        self.shape = Shape(Shape.Point, 1, 0)
        self.targets = "Enemies"
        self.effects = []

        self.use_on_scene = False

    def effect(self, effe):
        self.effects.append(effe)

    #def exerteffect(self, exertion, target=None):
    #    self.effects.append(ExertEffect(exertion=exertion, target=target))
        
    def work(self, subject, objects=[], **kwargs):
        phase = kwargs.get("phase", None)
        for effe in self.effects:
            if phase is None or phase & effe.phase != 0: 
                effe.work(subject, objects=objects, source=self, **kwargs)

    def leave(self, p, subject, objects=[], **kwargs):
        for effe in self.effects:
            effe.leave(subject, objects=objects, source=self, **kwargs)
            
