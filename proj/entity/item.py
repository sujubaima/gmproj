# -- coding: utf-8 --

from proj.engine import Message as MSG

from proj.entity.common import Entity
from proj.entity.map import Shape
from proj.entity.effect import Status
from proj.entity.effect import ExertEffect
from proj.entity.effect import Effect


class Item(Entity):

    @classmethod
    def template(cls, tpl_id):
        tplsplit = tpl_id.split(",")
        raw_ent = super(Item, cls).template(tplsplit[0])
        raw_ent.tpl_id = tpl_id
        for addition in tplsplit[1:]:
            pos, item = addition.split("-")
            pos = int(pos)
            item = Item.one(item)
            raw_ent.effects.extend(item.effects)
            raw_ent.inlays[pos]["filled"] = item
            raw_ent.rank = item.rank
            if len(item.tags & raw_ent.inlays_prefix) > 0:
                raw_ent.prefix = item.name
            else:
                raw_ent.prefix = "定制"
            raw_ent.money += item.money
        return raw_ent
    
            
    def handle(self, k, v):
        if k == "effects":
            ret = []
            for func in v:
                effeobj = Effect.fromjson(func)
                ret.append(effeobj)
            setattr(self, k, ret)
        elif k == "shape":
            vsplit = v.split(",")
            shp = eval("Shape.%s" % vsplit[0])
            pt = int(vsplit[1])
            sc = int(vsplit[2])
            if len(vsplit) == 4:
                ms = int(vsplit[3])
                setattr(self, k, Shape(shp, pt, sc, ms))
            else:
                setattr(self, k, Shape(shp, pt, sc))
        elif k == "tags":
            self.tags.update(v.split(","))
        elif k == "inlays":
            for line in v:
               vtags = set()
               vtags.update(line["accept"].split("|"))
               self.inlays.append({"name": line["name"], "accept": vtags})
        elif k == "inlays_prefix":
            self.inlays_prefix.update(v.split("|"))
        elif k == "name":
            setattr(self, "name_", v)
        elif k == "durability":
            self.durability = v
            self.durability_current = v
        else:
            setattr(self, k, v)

    @property
    def name(self):
        return self.prefix + self.name_

    def initialize(self):
        self._name = None
        self.prefix = ""
        #self.style = None
        self.tags = set()
        self.inlays = []
        self.inlays_prefix = set()

        self.usable = True
        self.battle_only = False

        self.weight = 1.0
        self.volume = 1.0
        self.money = 0

        self.deposable = True
        self.consumable = True
        
        self.double_hand = False

        self.effects = []
        self.shape = None

        self.targets = None
        
        self.durability = 1
        self.durability_current = 1

    def work(self, subject, objects=[], **kwargs):
        if "Equip" in self.tags:
            pos = kwargs.get("position", None)
            if pos is None:
                pos = self.pos()           
            if subject.equipment[pos] is not None and subject.equipment[pos].double_hand:
                subject.equipment[pos].leave(subject)
            if pos == 0 and subject.equipment[pos] is not None:
                pos = 1
            if pos == 1 and self.double_hand:
                pos = 0
            if subject.equipment[pos] is not None:
                subject.equipment[pos].leave(subject)
            if self.double_hand and subject.equipment[1 - pos] is not None:
                subject.equipment[1 - pos].leave(subject)
            if pos != 1 or subject.vice_enable:
                for effe in self.effects:
                    effe.work(subject, objects=[subject], source=self, **kwargs)
            subject.equip_on(self, pos)
            if "battle" in kwargs:
                MSG(style=MSG.PersonItemEquip, subject=subject, item=self)    
        else:
            for effe in self.effects:
                effe.work(subject, objects=objects, source=self, **kwargs)
            if "Medicine" in self.tags:
                subject.minus_item(self)

    def leave(self, subject, objects=[], **kwargs):
        if "Equip" in self.tags:
            pos = subject.equipment.index(self)
            if pos != 1 or self.double_hand or subject.vice_enable:
                for effe in self.effects:
                    effe.leave(subject, objects=objects, source=self, **kwargs)
            subject.equip_off(self, pos)

    def with_tag(self, tag):
        return tag in self.tags

    def pos(self):
        taglist = ["Weapon", None, "Armor", "Shoes", "ounament"]
        for i in range(len(taglist)):
            if taglist[i] in self.tags:
                break
        return i
