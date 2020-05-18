# -- coding: utf-8 --

from proj.engine import Message as MSG

from proj.entity.common import Entity
from proj.entity.item import Item
from proj.entity.effect import Effect

class Recipe(Entity):
    
    def handle(self, k, v):
        if k == "materials":
            for mv in v:
                if "tag" in mv:
                    self.materials.append((mv["tag"], mv.get("quantity", 1)))
                    self.regular = False
                else:
                    self.materials.append((Item.one(mv["id"]), mv.get("quantity", 1)))
        elif k == "effects":
            for effe in v:
                effe_obj = Effect.fromjson(effe)
                self.effects.append(effe_obj)
        elif k == "tags":
            self.tags.update(v.split(","))
        else:
            setattr(self, k, v)

    def initialize(self):
        self.tags = set()
        self.materials = []
        self.effects = []
        self.regular = True
        
    def check(self, subjects):
        ret = True
        quantities = {}
        items = []
        for sub in subjects:
            quantities.update(sub.quantities)
            items.extend(sub.items)
        for m, quantity in self.materials:
            if isinstance(m, Item):
                if m.tpl_id not in quantities:
                    ret = False
                    break
                if quantities[m.tpl_id] < quantity:
                    ret = False
                    break
            else:
                tag_quantity = 0
                for itm in items:
                    if m in itm.tags:
                        tag_quantity += 1
                if tag_quantity < quantity:
                    ret = False
                    break
        return ret

    def work(self, subject, objects=[], **kwargs):
        persons = kwargs["persons"]
        if self.name is not None:
            MSG(style=MSG.Show, text="%s开始制作配方%s" % (subject.name, self.name), wait=True)
        for m, quantity in self.materials:
            for p in persons:
                if m.tpl_id in p.quantities and p.quantities[m.tpl_id] >= quantity:
                    sub = p
                    break
            sub.minus_item(m, quantity=quantity)
            MSG(style=MSG.PersonItemLost, subject=sub, item=m, quantity=quantity)
        products = []
        for effe in self.effects:
            effe.work(subject, objects=objects, products=products, **kwargs)
        return products
        
    def repair(self, ratio):
        rcp = Recipe()
        rcp.tags = self.tags
        for m, quantity in self.materials:
            new_q = int(quantity * ratio)
            if new_q == 0:
                continue
            rcp.materials.append((m, new_q))
        if len(rcp.materials) > 0:
            return rcp
        else:
            return None
