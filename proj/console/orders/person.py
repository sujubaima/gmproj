# -- coding: utf-8 --

import sys
import itertools

from proj.console import ui

from proj import data

from proj.engine import Message as MSG
from proj.engine import Order

from proj.entity import Person
from proj.entity import Item
from proj.entity import Recipe

from proj.runtime import context

from proj.builtin.actions import PersonStudySkillAction
from proj.builtin.actions import PersonItemTransferAction
from proj.builtin.actions import PersonItemAction
from proj.builtin.actions import PersonEquipOffAction
from proj.builtin.actions import PersonEquipOnAction
from proj.builtin.actions import PersonRecipeAction
from proj.builtin.actions import PersonItemBuyAction
from proj.builtin.actions import PersonItemSellAction
from proj.builtin.actions import PersonItemAcquireAction
from proj.builtin.actions import PersonItemLostAction
from proj.builtin.actions import PersonEquipStrengthenAction
from proj.builtin.actions import TeamItemTransferAction


class PersonItemChooseOrder(Order):

    def initialize(self):
        self.orderarg = {}

    def carry(self):
        if self.persons is None:
            self.persons = [self.subject]
        if self.order is not None:
            filter = self.order.item_filter
        else:
            filter = self.filter
        MSG(style=MSG.PersonItemChoose, subject=self.subject, object=self.object, 
            persons=self.persons, filter=filter, action=self.order.action, tags=self.tags, 
            showmoney=self.order.showmoney, moneystyle=self.order.moneystyle, order=self.order, back=self.back).callback = self.callback

    def callback(self, itemsub):
        if itemsub is not None:
            item, subject = itemsub
            self.subject = subject
        else:
            item = None
        if item is not None and self.quantity is None:
            PersonItemQuantityOrder(item=item, subject=self.subject, object=self.object, 
                                    order=self.order, candidates=self.candidates,
                                    orderarg=self.orderarg)
        elif item is not None and (self.subject is None or self.object is None):
            PersonItemObjectOrder(item=item, subject=self.subject, object=self.object,
                                  quantity=self.quantity, order=self.order, candidates=self.candidates,
                                  orderarg=self.orderarg)
        elif item is not None:
            self.order(subject=self.subject, object=self.object, 
                       quantity=self.quantity, item=item, **self.orderarg) 


class PersonItemQuantityOrder(Order):

    def initialize(self):
        self.orderarg = {}

    def carry(self):
        MSG(style=MSG.PersonItemQuantity, 
            subject=self.subject, object=self.object, item=self.item,
            action=self.order.action, qrange=self.order.quantity_range, 
            filter=self.order.quantity_filter).callback=self.callback
                                                          
    def callback(self, quantity):                              
        if quantity is not None and (self.subject is None or self.object is None):                               
            PersonItemObjectOrder(subject=self.subject, item=self.item, object=self.object,
                                  quantity=quantity, order=self.order, candidates=self.candidates,
                                  orderarg=self.orderarg)
        elif quantity is not None:                                             
            self.order(subject=self.subject, object=self.object, 
                       quantity=quantity, item=self.item, **self.orderarg) 


class PersonItemObjectOrder(Order):

    def initialize(self):
        self.orderarg = {}

    def carry(self):
        MSG(style=MSG.PersonItemObject, subject=self.subject, 
            candidates=self.candidates, action=self.order.action).callback = self.callback

    def callback(self, person):
        if person is not None and self.subject is None:
            self.subject = person
        elif person is not None:
            self.object = person
        if person is not None and (self.subject is None or self.object is None):
            PersonItemObjectOrder(subject=self.subject, object=self.object, item=self.item, 
                                  quantity=quantity, order=self.order, candidates=self.candidates,
                                  orderarg=self.orderarg)  
        elif person is not None and self.item is None:
            PersonItemChooseOrder(subject=self.subject, persons=self.persons, object=object, 
                                  order=self.order, orderarg=self.orderarg)
        elif person is not None:
            self.order(subject=self.subject, object=self.object, 
                       quantity=self.quantity, item=self.item, **self.orderarg)
            

class PersonItemBaseOrder(Order):

    action = ""
    
    showmoney = False
    
    moneystyle = 0

    @classmethod
    def quantity_filter(cls, p, q, item, quantity):
        qrange = cls.quantity_range(p, q, item)
        return quantity >= qrange[0] and quantity <= qrange[1]
 
    @classmethod
    def quantity_range(cls, p, q, item):
        return [1, sys.maxsize]

    @classmethod
    def person_filter(cls, p, q, item):
        return True

    @classmethod
    def item_filter(cls, p, q, item, tags):
        return 0


class PersonItemOrder(PersonItemBaseOrder):

    action = "使用"

    def carry(self):
        PersonItemAction(subject=self.subject, object=self.object, item=self.item).do()
        
       
class PersonItemTransferOrder(PersonItemBaseOrder):

    action = "转移"

    @classmethod
    def quantity_range(cls, p, q, item):
        return [1, p.quantities[item.tpl_id]]

    def carry(self):
        PersonItemTransferAction(subject=self.subject, object=self.object, item=self.item, quantity=self.quantity).do()


class PersonItemPresentOrder(PersonItemBaseOrder):

    action = "赠予"

    @classmethod
    def quantity_range(cls, p, q, item):
        return [1, p.quantities[item.tpl_id]]

    def carry(self):
        PersonItemPresentAction(subject=self.subject, object=self.object, item=self.item, quantity=self.quantity, bag=False).do()


class PersonBuyOrder(PersonItemBaseOrder):

    action = "购买"
    
    showmoney = True
    
    moneystyle = 0

    @classmethod
    def quantity_range(cls, p, q, item):
        total_money = 0
        for m in q.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        maxcount = total_money // item.money
        return [1, maxcount]

    @classmethod
    def item_filter(cls, p, q, item, tags):
        if item.tpl_id == "ITEM_MONEY":
            return 2
        total_money = 0
        for m in q.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        return 0 if item.money <= total_money else 1

    def carry(self):
        PersonItemBuyAction(subject=self.subject, object=self.object, item=self.item, quantity=self.quantity).do()
        PersonTradeOrder(subject=self.object, object=self.subject)
    
    
class PersonSellOrder(PersonItemBaseOrder):

    action = "出售"
    
    showmoney = True
    
    moneystyle = 1

    @classmethod
    def quantity_range(cls, p, q, item):
        return [1, q.quantities[item.tpl_id]]

    @classmethod
    def item_filter(cls, p, q, item, tags):
        if item.tpl_id == "ITEM_MONEY":
            return False
        total_money = 0
        for m in q.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        return 0 if item.money <= total_money else 1
    
    def carry(self):
        PersonItemSellAction(subject=self.subject, object=self.object, item=self.item, quantity=self.quantity).do()
        PersonTradeOrder(subject=self.subject.team.leader, object=self.object)
    
    
class PersonMakeOrder(Order):
    pass        
        
        
class PersonStudySkillOrder(Order):

    def carry(self):
        backmethod = lambda: PersonItemChooseOrder(subject=self.subject, 
                                                   quantity=1, candidates=self.subject.team.members, 
                                                   order=PersonItemOrder, back=True)
        MSG(style=MSG.PersonStudySkill, superskill=self.superskill, subject=self.subject, backmethod=backmethod).callback = self.callback

    def callback(self, node):
        if node is not None:
            PersonStudySkillAction(subject=self.subject, node=node).do()            
        
        
class PersonTradeOrder(Order):

    def carry(self):
        MSG(style=MSG.PersonTrade, subject=self.subject, object=self.object)
        
        
class PersonEquipmentOrder(Order):

    def initialize(self):
        self.fromon = False
        self.fromoff = False

    def carry(self):
        MSG(style=MSG.PersonEquipment, subject=self.subject, fromon=self.fromon, fromoff=self.fromoff)
    
    
class PersonEquipOffOrder(Order):

    def carry(self):
        PersonEquipOffAction(subject=self.subject, position=self.position).do()
        PersonEquipmentOrder(subject=self.subject, fromoff=True)
        
        
class PersonEquipOnOrder(PersonItemBaseOrder):

    @classmethod
    def item_filter(cls, p, q, item, tags):
        if len(item.tags & tags) > 0 and item not in p.equipment:
            return 0
        else:
            return 2

    def carry(self):
        PersonEquipOnAction(subject=self.subject, position=self.position, equip=self.item).do()
        PersonEquipmentOrder(subject=self.subject, fromon=True) 


class PersonSkillOrder(Order):

    def initialize(self):
        self.fromon = False
        self.fromoff = False

    def carry(self):
        MSG(style=MSG.PersonSkill, subject=self.subject, fromon=self.fromon, fromoff=self.fromoff)


class PersonRecipeChooseOrder(Order):

    def subrecipes(self, recipe):
        tags = {}
        tag_quantity = {}
        for k, v in recipe.materials:
            if isinstance(k, str):
                tags[k] = []
                tag_quantity[k] = v
        for tag in tags:
            for itm in self.subject.items:
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
            recipes.append(r)
        return recipes

    def carry(self):
        if self.persons is None:
            self.persons = [self.subject]
        if self.candidates is None:
            self.candidates = [self.subject]
        MSG(style=MSG.PersonRecipeChoose, subject=self.subject, 
            persons=self.persons, candidates=self.candidates, sub=False, filter=self.filter).callback = self.callback
        
    def callback(self, recipe):
        if recipe is not None:
            if recipe.regular:
                PersonRecipeOrder(subject=self.subject, persons=self.persons, recipe=recipe)
            else:
                recipes = self.subrecipes(recipe)
                MSG(style=MSG.PersonRecipeEnsure, subject=self.subject, persons=self.persons, recipes=recipes).callback = self.callback
            
            
class PersonRecipeOrder(Order):

    def carry(self):
        products = PersonRecipeAction(subject=self.subject, persons=self.persons, recipe=self.recipe).do()
        if self.subject not in self.persons and len(products) > 0:
            TeamItemTransferAction(team=self.persons[0].team, object=self.subject, item=Item.one("ITEM_MONEY"), quantity=25).do()
            PersonItemObjectOrder(subject=self.subject, item=products[0][0], quantity=products[0][1],
                                  candidates=self.persons, order=PersonItemTransferOrder)
            PersonTradeOrder(subject=self.persons[0].team.leader, object=self.subject, hub=True)


class PersonSkillOffOrder(Order):

    def carry(self):
        if self.position == -1:
            self.skill_counter = None
        else:
            self.subject.skills_equipped[self.position] = None
        PersonSkillOrder(subject=self.subject, fromoff=True)


class PersonSkillOnOrder(Order):

    def carry(self):
        MSG(style=MSG.PersonSkillChoose, subject=self.subject).callback = self.callback
    
    def callback(self, skill):
        if skill is not None:
            if self.position == -1:
                self.skill_counter = skill
            else:
                self.subject.skills_equipped[self.position] = skill
            PersonSkillOrder(subject=self.subject, fromon=True)
        else:
            PersonSkillOrder(subject=self.subject, fromoff=True)
 

class PersonEquipInlayChooseOrder(PersonItemBaseOrder):

    def carry(self):
        MSG(style=MSG.PersonEquipInlayChoose, subject=self.subject, object=self.object, item=self.item)


class PersonEquipStrengthenOrder(PersonItemBaseOrder):

    def carry(self):
        PersonEquipStrengthenAction(subject=self.subject, equip=self.equip, item=self.item, position=self.position).do()
        PersonTradeOrder(subject=self.subject.team.leader, object=self.object)
        
        
class PersonEquipRepairRecipeOrder(PersonItemBaseOrder, PersonRecipeChooseOrder):

    def carry(self):
        recipe_id = "RECIPE_%s" % self.item.tpl_id[5:]
        recipe_id = recipe_id.split(",")[0]
        if getattr(data.recipes, recipe_id, None) is not None:
            recipe = Recipe.one(recipe_id)
        item_ratio = 1 - self.item.durability_current / self.item.durability
        money_recipe = Recipe()
        money_recipe.extensions["money"] = max(1, int(self.item.money * item_ratio))
        recipes = [money_recipe]
        if recipe is not None and recipe.regular:
            recipes.append(recipe.repair(item_ratio))             
        elif recipe is not None:
            sub_recipes = self.subrecipes(recipe)
            recipes.extend([rcp.repair(item_ratio) for rcp in sub_recipes])
        MSG(style=MSG.PersonRecipeChoose, subject=self.object, 
            persons=self.persons, title="请选择你的修理方案", sub=True, recipes=recipes).callback = self.callback
            
    def callback(self, recipe):
        if recipe is not None:
            PersonRecipeAction(subject=self.subject, persons=self.persons, recipe=recipe).do()
            money = recipe.extensions.get("money", 0) + 25
            TeamItemTransferAction(team=self.subject.team, object=self.object, item=Item.one("ITEM_MONEY"), quantity=money).do()
            self.item.durability_current = self.item.durability
            MSG(style=MSG.PersonEquipRepair, item=self.item)
            
class PersonEquipRepairOrder(PersonItemBaseOrder):

    def carry(self):
        ratio = self.item.durability_current / self.item.durability
        self.item.durability_current = self.item.durability
        TeamItemTransferAction(team=self.subject.team, object=self.object, item=Item.one("ITEM_MONEY"), quantity=int(self.item.money * ratio)).do()
        MSG(style=MSG.PersonEquipRepair, subject=self.subject, item=self.item)
        
