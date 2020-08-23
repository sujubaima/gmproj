import random
import math
import uuid
import importlib


from proj import data


class Entity(object):

    Templates = {}

    Instances = {}
    
    @staticmethod
    def remove(obj):
        if obj.tpl_id in Entity.Templates:
            Entity.Templates[obj.tpl_id].remove(obj)
        if obj.id in Entity.Instances:
            Entity.Instances.pop(obj.id)  

    @classmethod
    def _remove(cls, obj):
        if cls in Entity.Templates and \
           obj.tpl_id in Entity.Templates[cls]:
            Entity.Templates[cls][obj.tpl_id].remove(obj)
        if cls in Entity.Instances and \
           obj.id in Entity.Instances[cls]:
            Entity.Instances[cls].pop(obj.id)      

    @classmethod
    def template(cls, tpl_id):
        tpl = eval("data.%s.%s" % (cls.__name__.lower(), tpl_id))
        if "class" in tpl:
            if "module" in tpl:
                tmp = importlib.import_module(tpl["module"])
            cls = eval("tmp.%s" % tpl["class"])
        ret = cls(tpl_id=tpl_id, **tpl)
        #ret.tpl_id = tpl_id
        #ret.load(**tpl)
        return ret
        
    @classmethod
    def one(cls, tpl_id):
        if tpl_id not in Entity.Templates:
            Entity.Templates[tpl_id] = []
        if len(Entity.Templates[tpl_id]) == 0:
            obj = cls.template(tpl_id)
            Entity.Templates[tpl_id].append(obj)
            Entity.Instances[obj.id] = obj
        return Entity.Templates[tpl_id][0]

    @classmethod
    def register(cls, obj):
        tpl_id = obj.tpl_id
        if tpl_id not in Entity.Templates:
            Entity.Templates[tpl_id] = []
        Entity.Templates[tpl_id].append(obj)
        Entity.Instances[obj.id] = obj

    @staticmethod
    def get(cls, obj_id):
        return Entity.Instances.get(obj_id, None)

    @classmethod
    def _get(cls, obj_id):
        if cls not in Entity.Instances:
            return None
        return Entity.Instances[cls][obj_id]

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid1())
        self.tpl_id = None

        self.locked = set()
        self.stash = {}
        self.tmpdict = {}

        self.initialize()
        self.load(**kwargs)
        #if len(kwargs) != 0:
        #    self.finish()

    def load(self, **kwargs):
        for k, v in kwargs.items():
            self.handle(k, v)
        #if len(kwargs) != 0:
        self.finish()
        
    def handle(self, k, v):
        setattr(self, k, v)

    def initialize(self):
        pass

    def finish(self):
        pass        

    def __getattr__(self, k):
        return None


class HyperAttr(object):

    def __init__(self, base, delta=0, factor=1, type=None, fval=None):
        self.base = base
        self.delta = delta
        self.factor = factor
        if type is None:
            self.type = lambda x: x
        else:
            self.type = type
        if fval is None:
            self.fval = lambda: self.type((self.base + self.delta) * self.factor)
        else:
            self.fval = lambda: self.type(fval(self))

    def __call__(self):
        return self.fval()


def random_gap(base, gap):
    if base >= 0:
        return random.randint(int(base * (1 - gap)), int(base * (1 + gap)))
    else:
        return random.randint(int(base * (1 + gap)), int(base * (1 - gap)))


def if_rate(ratio):
    return random.randint(1, 10000) <= ratio * 10000
