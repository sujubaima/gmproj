# -- coding: utf-8 --

import importlib

from proj import options
from proj import data

from proj.runtime import context

from proj.engine import Action
from proj.engine import Message as MSG

from proj.entity import Person
from proj.entity import Item

from proj.engine import script


class PersonSessionAction(Action):

    def take(self):
        for sentence in self.sentences:
            PersonSpeakAction(talker=sentence.get("talker", None), subject=self.subject, object=self.object,
                              content=sentence["content"]).do()


class PersonSpeakAction(Action):
    """
    人物说话
    """
    def pick(self, team, **kwargs):
        ret = None
        for m in team.members:
            all_match = True
            for k, v in kwargs.items():
                if getattr(m, k, None) != v:
                    all_match = False
                    break
            if all_match:
                ret = m
                break
        return ret

    def take(self):
        if self.talker is None:
            pass
        MSG(style=MSG.PersonSpeak, action=self)
        

class PersonChangeConversationAction(Action):
    """
    修改人物对话
    """
    def take(self):
        self.person.conversation = self.conversation
        
        
class PersonConversationAddBranchAction(Action):
    """
    人物对话增加分支
    """
    def take(self):
        conversations = importlib.import_module("%s.dialogs" % options.DATA_PATH)
        conversation = getattr(conversations, self.conversation)
        if self.branch not in conversation[self.master]["branches"]:
            if self.position is not None:
                conversation[self.master]["branches"].insert(self.position, self.branch)
            else:
                conversation[self.master]["branches"].append(self.branch)
        
        
class PersonConversationRemoveBranchAction(Action):
    """
    人物对话删除分支
    """
    def take(self):
        conversations = importlib.import_module("%s.dialogs" % options.DATA_PATH)
        conversation = getattr(conversations, self.conversation)
        conversation[self.master]["branches"].remove(self.branch)
        
        
class PersonConversationChangeContentAction(Action):
    """
    人物对话删除分支
    """
    def take(self):
        conversations = importlib.import_module("%s.dialogs" % options.DATA_PATH)
        conversation = getattr(conversations, self.conversation)
        conversation[self.index]["content"] = self.content
        
        
class PersonItemTransferAction(Action):

    def initialize(self):
        self.bag = True

    def take(self):
        position = -1
        for idx, equip in enumerate(self.subject.equipment):
            if equip == self.item:
                position = idx
                break
        if position >= 0:
            PersonEquipOffAction(subject=self.subject, position=position).do()
        self.subject.minus_item(self.item, quantity=self.quantity)
        if self.bag:
            self.object.add_item(self.item, quantity=self.quantity)
        MSG(style=MSG.PersonItemTransfer, action=self)

        
class PersonItemAction(Action):

    def take(self):
        self.item.work(self.subject, objects=[self.object])
        context.timeflow(1)


class PersonItemSellAction(Action):

    def take(self):
        PersonItemTransferAction(subject=self.subject, object=self.object,
                                 item=self.item, quantity=self.quantity).do()
        TeamItemTransferAction(team=self.object.team, object=self.subject,
                               item=Item.one("ITEM_MONEY"), quantity=int(self.item.money * 0.4) * self.quantity).do()


class PersonItemBuyAction(Action):

    def take(self):
        PersonItemTransferAction(subject=self.object, object=self.subject,
                                 item=self.item, quantity=self.quantity).do()
        TeamItemTransferAction(team=self.subject.team, object=self.object,
                               item=Item.one("ITEM_MONEY"), quantity=self.item.money * self.quantity).do()


class PersonItemAcquireAction(Action):

    def take(self):
        self.subject.add_item(self.item, quantity=self.quantity)
        MSG(style=MSG.PersonItemAcquire, action=self)


class PersonItemLostAction(Action):

    def take(self):
        position = -1 
        for idx, equip in enumerate(self.subject.equipment):
            if equip == self.item:
                position = idx
                break
        if position >= 0:
            PersonEquipOffAction(subject=self.subject, position=position).do()
        self.subject.minus_item(self.item, quantity=self.quantity)
        MSG(style=MSG.PersonItemLost, action=self)
        
        
class PersonLearnRecipeAction(Action):

    def take(self):
        if self.recipe not in self.subject.recipes:
            self.subject.recipes.append(self.recipe)
        MSG(style=MSG.PersonRecipeLearn, action=self)
        
        
class PersonStudySkillAction(Action):

    def take(self):
        if self.node == self.subject.studying:
            return
        self.subject.exp = 0
        self.subject.studying = self.node


class PersonEquipOffAction(Action):

    def take(self):
        if self.subject.equipment[self.position] is not None:
            self.subject.equipment[self.position].leave(self.subject)
        

class PersonEquipOnAction(Action):
   
    def take(self):
        if self.subject.equipment[self.position] is not None:
             self.subject.equipment[self.position].leave(self.subject)
        self.equip.work(self.subject, position=self.position)
        
        
class PersonTaskUpdateAction(Action):

    def take(self):
        self.task = getattr(data.task, self.task)
        if self.task not in context.tasks:
            context.tasks[self.task] = []
            context.tasks_index.insert(0, self.task)
        for content in self.contents:
            content = getattr(data.task, content) 
            if content not in context.tasks[self.task]:
                 context.tasks[self.task].append(content)
        context.tasks_index.remove(self.task)
        context.tasks_index.insert(0, self.task)
        context.tasks_status[self.task] = True
        MSG(style=MSG.PersonTaskUpdate, action=self)
        
        
class PersonAttitudeChangeAction(Action):

    def take(self):
        if self.subject.id not in context.attitudes:
            context.attitudes[self.subject.id] = {}
        if self.object.id not in context.attitudes[self.subject.id]:
            context.attitudes[self.subject.id][self.object.id] = 50
        context.attitudes[self.subject.id][self.object.id] += self.delta
        MSG(style=MSG.PersonAttitudeChange, action=self)
        
        
class PersonRecipeAction(Action):

    def take(self):
        products = self.recipe.work(subject=self.subject, persons=self.persons)
        context.timeflow(1)
        return products


class PersonEquipStrengthenAction(Action):

    def take(self):
        equip_pos = -1
        if self.equip in self.subject.equipment:
            equip_pos = self.subject.equipment.index(self.equip)
            self.equip.leave(self.subject)
        new_tpl = self.equip.tpl_id + ",%s-%s" % (self.position, self.item.tpl_id)
        new_equip = Item.template(new_tpl)
        new_equip.durability_current = self.equip.durability_current
        Item.register(new_equip)
        if equip_pos != -1:
            new_equip.work(self.subject, position=equip_pos)
        PersonItemLostAction(subject=self.subject, item=self.equip, quantity=1).do()
        PersonItemLostAction(subject=self.subject, item=self.item, quantity=1).do()
        PersonItemAcquireAction(subject=self.subject, item=new_equip, quantity=1).do()


class TeamItemTransferAction(Action):

    def take(self):
        for m in self.team.members:
            if self.quantity == 0:
                break
            if self.item.tpl_id in m.quantities:
                q = min(self.quantity, m.quantities[self.item.tpl_id])
                PersonItemTransferAction(subject=m, object=self.object, item=self.item, quantity=q).do()
                self.quantity -= q
