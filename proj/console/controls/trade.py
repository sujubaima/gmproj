# -- coding: utf-8 --

import sys
import itertools

from proj.console import ui

from proj import data

from proj.engine import Message as MSG
from proj.engine import Control

from proj.entity import Item
from proj.entity import Recipe

from proj.console.controls.common import PipeControl
from proj.console.controls.common import RecipeSelectControl
from proj.console.controls.common import ItemSelectControl
from proj.console.controls.common import ItemQuantitySelectControl
from proj.console.controls.common import PersonSelectControl

from proj.builtin.actions import PersonItemTransferAction
from proj.builtin.actions import PersonItemAction
from proj.builtin.actions import PersonRecipeAction
from proj.builtin.actions import PersonItemBuyAction
from proj.builtin.actions import PersonItemSellAction
from proj.builtin.actions import PersonItemAcquireAction
from proj.builtin.actions import PersonItemLostAction
from proj.builtin.actions import PersonEquipStrengthenAction
from proj.builtin.actions import TeamItemTransferAction



class TradeControl(Control):

    def launch(self):
        MSG(style=MSG.TradeControl, control=self)

    @Control.listener
    def buy(self, arg):
        item_title = "请选择要购买的物品："
        quantity_text = "请输入要购买的数量："
        control = PipeControl()
        control.pipe(BuyItemSelectControl(buyer=self.subject, seller=self.object,
                         persons=[self.object], title=item_title), valves=["item"])
        control.pipe(BuyItemQuantitySelectControl(buyer=self.subject, seller=self.object,
                         text=quantity_text), valves=["quantity"])
        control.run()
        if control.item is not None and control.quantity is not None:
            PersonItemBuyAction(subject=self.subject, object=self.object, 
                item=control.item, quantity=control.quantity).do() 
        self.launch()

    @Control.listener
    def sell(self, arg):
        item_title = "请选择要出售的物品："
        quantity_text = "请输入要出售的数量："
        control = PipeControl()
        control.pipe(SellItemSelectControl(buyer=self.object, seller=self.subject,
                         persons=self.subject.team.members, title=item_title), valves=["item"])
        control.pipe(SellItemQuantitySelectControl(buyer=self.subject, seller=self.object,
                         text=quantity_text), valves=["quantity"])
        control.run()
        if control.item is not None and control.quantity is not None:
            PersonItemSellAction(subject=self.subject, object=self.object, 
                item=control.item, quantity=control.quantity).do()
        self.launch()

    @Control.listener
    def make(self, arg):
        recipe_title = "请选择要制作的配方："
        control = RecipeSelectControl(persons=self.subject.team.members + [self.object],
                      title=recipe_title)
        control.run()
        if control.person is not None and control.recipe is not None:
            products = PersonRecipeAction(subject=control.person, persons=self.subject.team.members,
                           recipe=control.recipe).do()
            if control.person not in self.subject.team.members and len(products) > 0:
                TeamItemTransferAction(team=self.subject.team, object=control.person,
                    item=Item.one("ITEM_MONEY"), quantity=25).do()
                control = PersonSelectControl(persons=self.subject.team.members)
                control.run()
                PersonItemTransferAction(subject=self.person, object=control.person,
                    item=products[0][0], quantity=products[0][1]).do()
        self.launch()

    @Control.listener
    def repair(self, arg):
        item_title = "请选择你要修理的物品："
        control = PipeControl()
        control.pipe(RepairItemSelectControl(person=self.subject, fixer=self.object, 
                         persons=self.subject.team.members, title=item_title), valves=["item"])
        control.pipe(RepairRecipeSelectControl(fixer=self.object,
                         persons=self.subject.team.members), valves=["recipe"])
        control.run()
        if control.recipe is not None:
            PersonRecipeAction(subject=self.subject, persons=self.subject.team.members, 
                recipe=control.recipe).do()
            money = control.recipe.tmpdict.get("money", 0) + 25
            TeamItemTransferAction(team=self.subject.team, object=self.object,
                item=Item.one("ITEM_MONEY"), quantity=money).do()
            control.item.durability_current = control.item.durability
            MSG(style=MSG.PersonEquipRepair, item=control.item)
        self.launch()

    @Control.listener
    def strengthen(self, arg):
        item_title = "请选择你要强化的物品："
        inlay_title = "请选择你要强化的部位："
        material_title = "请选择你要用于强化的材料："
        control = PipeControl()
        control.pipe(StrengthenItemSelectControl(person=self.subject, another=self.object, 
                         persons=self.subject.team.members, title=item_title), valves=["item"])
        control.pipe(ItemInlaySelectControl(subject=self.subject, object=self.object,
                         title=inlay_title), valves=["position", "tags"])
        control.pipe(StrengthenMaterialSelectControl(persons=self.subject.team.members,
                         title=material_title), valves=["inlay"])
        control.run()
        if control.inlay is not None:
            PersonEquipStrengthenAction(subject=self.subject, equip=control.item,
                item=control.inlay, position=control.position).do()    
        self.launch()


class BuyItemSelectControl(ItemSelectControl):

    def launch(self):
        self.person = self.buyer
        super(BuyItemSelectControl, self).launch()

    def filter(self, item):
        if item.tpl_id == "ITEM_MONEY":
            return 2
        total_money = 0
        for m in self.buyer.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        return 0 if item.money <= total_money else 1


class SellItemSelectControl(ItemSelectControl):

    def launch(self):
        self.person = self.buyer
        super(SellItemSelectControl, self).launch()

    def filter(self, item):
        if item.tpl_id == "ITEM_MONEY":
            return 2
        if len(item.tags & self.buyer.tags) == 0:
            return 2
        total_money = 0
        for m in self.buyer.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        return 0 if item.money <= total_money else 1


class RepairItemSelectControl(ItemSelectControl):

    def filter(self, item):
        if "Equip" in item.tags and item.durability_current != item.durability:
            return 0
        else:
            return 2


class StrengthenItemSelectControl(ItemSelectControl):

    def filter(self, item):
        if "Equip" in item.tags and len(item.inlays) > 0:
            return 0
        else:
            return 2


class BuyItemQuantitySelectControl(ItemQuantitySelectControl):

    def launch(self):
        self.person = self.seller
        super(BuyItemQuantitySelectControl, self).launch()

    def qrange(self):
        total_money = 0
        if "Equip" in self.item.tags:
            return [1, 1]
        for m in self.buyer.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        maxcount = total_money // item.money
        return [1, min(maxcount, self.seller.quantity[item.tpl_id])]


class SellItemQuantitySelectControl(ItemQuantitySelectControl):

    def launch(self):
        self.person = self.seller
        super(SellItemQuantitySelectControl, self).launch()

    def qrange(self):
        if "Equip" in self.item.tags:
            return [1, 1]
        total_money = 0
        for m in self.buyer.team.members:
            total_money += m.quantities.get("ITEM_MONEY", 0)
        maxcount = total_money // item.money
        return [1, min(maxcount, self.seller.quantities[item.tpl_id])]


class RepairRecipeSelectControl(RecipeSelectControl):

    def launch(self):
        self.title = "请选择你的修理方案："
        self.sub = True
        recipe_id = "RECIPE_%s" % self.item.tpl_id[5:]
        recipe_id = recipe_id.split(",")[0]
        if getattr(data.recipes, recipe_id, None) is not None:
            recipe = Recipe.one(recipe_id)
        item_ratio = 1 - self.item.durability_current / self.item.durability
        money_recipe = Recipe()
        money_recipe.tmpdict["money"] = max(1, int(self.item.money * item_ratio))
        self.recipes = [(self.fixer, money_recipe)]
        if recipe is not None and recipe.regular:
            self.recipes.append((self.fixer, recipe.repair(item_ratio)))
        elif recipe is not None:
            sub_recipes = self.subrecipes(recipe)
            self.recipes.extend([(self.fixer, rcp.repair(item_ratio)) for rcp in sub_recipes])
        super(RepairRecipeSelectControl, self).launch()


class ItemInlaySelectControl(Control):

    def launch(self):
        MSG(style=MSG.ItemInlaySelectControl, control=self)

    @Control.listener
    def select(self, inlay):
        if self.tags is None:
            self.tags = self.item.inlays[inlay]["accept"] 
        else:
            self.tags = self.tags & self.item.inlays[inlay]["accept"]
        self.position = inlay
        self.close()


class StrengthenMaterialSelectControl(ItemSelectControl):

    def filter(self, item):
        if len(item.tags & self.tags) != 0:
            return 0
        else:
            return 2

    @Control.listener
    def select(self, owneritem):
        if owneritem is not None:
            item, owner = owneritem
        else:
            item = None
            owner = None
        self.owneritem = owneritem
        self.inlay = item
        self.owner = owner
        self.close()

