# -- coding: utf-8 --

import sys
import itertools

from proj.engine import Control
from proj.engine import Message as MSG

from proj.entity import Recipe
from proj.entity import Item
from proj.entity import Person

from proj.runtime import context

from proj.builtin.actions import PersonItemTransferAction


class PipeControl(Control):
    """
    将一组控件连成管道，形成上下游级联关系
    """
    def initialize(self):
        super(PipeControl, self).initialize()
        self.pipeline = []
        self.pipestack = []
        self.valves = []
        self.optionals = []

    def run(self):
        ks = None
        vs = None
        oks = None
        ovs = None
        control = None
        idx = 0
        while len(self.pipeline) > 0 or len(ks) != len(vs):
            # 回退上一个控件
            if control is not None and len(ks) != len(vs):
                if control.breakon:
                    break
                self.pipeline.insert(0, (control, ks, oks))
                control, ks, oks = self.pipestack.pop()
                if ks is not None:
                    if len(self.pipestack) == 1:
                        ks_i = 0
                        oks_i = 0
                    else:
                        ks_i = len(self.pipestack[-1][1])
                        oks_i = len(self.pipestack[-1][2])
                    for k in ks[ks_i:] + oks[oks_i:]:
                        setattr(control, k, None)
                        setattr(self, k, None)
            # 前进下一个控件
            else:
                self.pipestack.append((control, ks, oks))
                control, keys, optionals = self.pipeline.pop(0)
                if ks is not None and vs is not None:
                    for k, v in zip(ks + oks, vs + ovs):
                        setattr(control, k, v) 
                        setattr(self, k, v)
                ks = keys
                oks = optionals
            if control is None:
                break
            control.run()
            vs = []
            ovs = []
            for k in oks:
                v = getattr(control, k, None)
                ovs.append(v)
            for k in ks:
                v = getattr(control, k, None)
                if v is None:
                    break
                else:
                    vs.append(v)
        if control is not None and len(ks) == len(vs):
            for k, v in zip(ks + oks, vs + ovs):
                setattr(control, k, v)
                setattr(self, k, v)

    def pipe(self, control, valves=None, optionals=None, breakon=False):
        if valves is None:
            valves = []
        if optionals is None:
            optionals = []
        control.breakon = breakon
        self.valves = self.valves + valves
        self.optionals = self.optionals + optionals
        self.pipeline.append((control, self.valves, self.optionals))
        return self


class BranchControl(Control):

    def launch(self):
        MSG(style=MSG.BranchControl, control=self)

    @Control.listener
    def select(self, label_idx):
        self.label, self.idx = label_idx
        context.executed(self.name, self.label) 
        self.close()


class EnsureControl(Control):
    """
    确认控件
    """
    def launch(self):
        MSG(style=MSG.EnsureControl, control=self)

    @Control.listener
    def input(self, sure):
        if sure:
            self.sure = True
        self.close()


class PositionSelectControl(Control):
    """
    基础的位置选择控件
    """
    @staticmethod
    def validator(map, pos, valid_pos, can_on_person):
        x, y = pos.split()
        x = int(x)
        y = int(y)
        real_pos = map.point_to_real((x, y))
        if not can_on_person and real_pos in map.loc_entity:
            return None
        if real_pos not in valid_pos:
            return None
        return real_pos

    def launch(self):
        MSG(style=MSG.PositionSelectControl, control=self)

    @Control.listener
    def select(self, pos):
        self.target = pos
        self.close()
        

class PersonSelectControl(Control):
    """
    基础的人物选择控件
    """
    def initialize(self):
        super(PersonSelectControl, self).initialize()
        self.canskip = True

    def launch(self):
        MSG(style=MSG.PersonSelectControl, control=self)

    @Control.listener
    def select(self, person):
        self.person = person
        self.close()


class PersonSelectMultipleControl(Control):
    """
    人物多选控件
    """ 
    def initialize(self):
        super(PersonSelectMultipleControl, self).initialize()
        self.canskip = True

    def launch(self):
        MSG(style=MSG.PersonSelectMultipleControl, control=self)

    @Control.listener
    def select(self, persons):
        self.persons = persons
        self.close()


class ItemSelectControl(Control):
    """
    基础的物品选择控件
    """
    def finish(self):
        super(ItemSelectControl, self).finish()
        self.tags_orig = self.tags
        self.persons_orig = self.persons 

    def macros(self):
        macs = {}
        descs = {}
        if self.persons is not None:
            for p in self.persons:
                pkey = "#people." + p.tpl_id[7:].lower()
                macs[pkey] = self.showperson
                descs[pkey] = "只列出%s物品" % p.name
        macs["#people.all"] = self.resetperson
        descs["#people.all"] = "列出所有人物品"
        for tag, desc in Item.AllTags.items():
            ikey = "#item." + tag.lower()
            macs[ikey] = self.showtag
            descs[ikey] = "只列出%s" % desc
        macs["#item.all"] = self.resettag
        descs["#item.all"] = "列出所有物品"
        return macs, descs

    def showtag(self, tag):
        tag = tag[6:].capitalize()
        self.tags = set()
        if self.tags_orig is not None:
            for t in self.tags_orig:
                self.tags.add(t)
        else:
            self.tags = set()
        self.tags.add(tag)
        self.items = None
        self.launch()

    def showperson(self, person):
        person = Person.one("PERSON_" + tag[8:].upper())
        self.persons = [person]
        self.launch()

    def resettag(self, macro):
        self.tags = self.tags_
        self.items = None
        self.launch()

    def resetperson(self, macro):
        if self.persons_ is not None:
            self.persons = self.persons_
        self.launch()

    def filter(self, item):
        if self.tags is not None and len(item.tags & self.tags) == 0:
            return 2
        return 0

    def validator(self, item):
        return True

    def prepare(self):
        if self.persons is None and self.person is not None:
            self.persons = [self.person]
        if self.items is None:
            self.items = []
            for p in self.persons:
                for itm in p.items:
                    if self.filter is not None:
                        status = self.filter(itm)
                    else:
                        status = 0
                    if status == 2:
                        continue
                    self.items.append((itm, p, status==0))

    def launch(self):
        self.prepare()
        MSG(style=MSG.ItemSelectControl, control=self)

    @Control.listener
    def select(self, itemsub):
        if itemsub is not None:
            item, owner = itemsub
        else:
            item = None
            owner = None
        self.owneritem = itemsub
        self.item = item
        self.owner = owner
        self.close()


class ItemQuantitySelectControl(Control):

    def validator(self, quantity):
        quantity = int(quantity)
        return quantity <= self.range[1] and quantity >= self.range[0]

    def qrange(self):
        if "Equip" in self.item.tags:
            return [1, 1]
        return [1, self.person.quantities[self.item.tpl_id]] 
 
    def launch(self):
        self.range = self.qrange()
        MSG(style=MSG.ItemQuantitySelectControl, control=self)

    @Control.listener
    def select(self, quantity):
        self.quantity = quantity
        self.close()


class SkillSelectControl(Control):

    def launch(self):
        MSG(style=MSG.SkillSelectControl, control=self)

    @Control.listener
    def select(self, skill):
        self.skill = skill
        self.close()


class PersonStatusControl(Control):

    def launch(self):
        MSG(style=MSG.PersonStatusControl, control=self)


class RecipeSelectControl(Control):

    def filter(self, recipe):
        if self.tags is None or len(recipe.tags & self.tags) > 0:
            return 0
        else:
            return 2

    def subrecipes(self, recipe):
        tags = {}
        tag_quantity = {}
        for k, v in recipe.materials:
            if isinstance(k, str):
                tags[k] = []
                tag_quantity[k] = v
        for tag in tags:
            for p in self.persons:
                for itm in p.items:
                    if tag in itm.tags:
                        tags[tag].append(itm)
        finaltags = {}
        finalset = {}
        for tag, taglist in tags.items():
            finaltags[tag] = []
            finalset[tag] = set()
            for com in itertools.combinations(taglist, tag_quantity[tag]):
                keymap = {}
                for k in com:
                    if k.tpl_id not in keymap:
                        keymap[k.tpl_id] = 0
                    keymap[k.tpl_id] += 1
                key = ",".join(["%s-%s" % (k, keymap[k]) for k in sorted(list(keymap.keys()))])
                if key not in finalset[tag]:
                    finaltags[tag].append(keymap)
                    finalset[tag].add(key)
        recipes = []
        for com in itertools.product(*list(finaltags.values())):
            r = Recipe()
            r.name = recipe.name
            r.effects = recipe.effects
            r.tags = recipe.tags
            for rmk, rmv in recipe.materials:
                if not isinstance(rmk, str):
                    r.materials.append((rmk, rmv))
            for cm in com:
                for cmk, cmv in cm.items():
                    r.materials.append((Item.one(cmk), cmv))
            recipes.append((self.person, r))
        return recipes

    def launch(self):
        if self.persons is None:
            self.persons = [self.person]
        if self.recipes is None:
            self.recipes = []
            for p in self.persons:
                for rec in p.recipes:
                    self.recipes.append((p, rec))
        MSG(style=MSG.RecipeSelectControl, control=self)

    @Control.listener
    def select(self, ownerrecipe):
        if ownerrecipe is not None:
            self.person, self.recipe = ownerrecipe
            if not self.recipe.regular:
                subrecipe_title = "该配方存在多种可选方案，请选择要使用的方案："
                recipes = self.subrecipes(self.recipe)
                control = RecipeSelectControl(person=self.person, persons=self.persons, recipes=recipes, 
                    title=subrecipe_title, sub=True)
                control.run()
                self.person, self.recipe = control.person, control.recipe
        if self.person is None or self.recipe is None:
            self.launch()
        else:
            self.close()
