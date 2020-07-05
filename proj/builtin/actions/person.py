# -- coding: utf-8 --

import importlib

from proj import options
from proj import data

from proj.runtime import context

from proj.engine import Action
from proj.engine import Order
from proj.engine import Message as MSG

from proj.entity import Person
from proj.entity import Item

from proj.engine import script


class PersonConversationAction(Action):
    """
    人物对话
    """
    def initialize(self):
        self.idx = 0

    def process_conversation(self):
        orders = importlib.import_module("proj.console.orders")
        while self.idx < len(self.conversation):
            line = self.conversation[self.idx]
            if line["style"] == "Speak":
                context.spoken(self.conversation_name, self.idx)
                if "sentences" not in line:
                    PersonSpeakAction(talker=line["talker"], subject=self.subject, object=self.object, 
                                      content=line["content"]).do()
                else:
                    for setence in line["sentences"]:
                        PersonSpeakAction(talker=sentence["talker"], subject=self.subject, object=self.object,
                                          content=sentence["content"]).do()
            elif line["style"] == "Script":
                if "scripts" in line:
                    script.run(line["scripts"])
                else:
                    script.run([line])
            elif line["style"] == "Conditions":
                final_result = script.conditions(line["conditions"])
                rststr = str(final_result).lower()
                if rststr in line["result"]:
                    self.idx = line["result"][rststr]
                else:
                    self.idx += 1   
                continue                    
            elif line["style"] == "Branch":
                MSG(style=MSG.PersonDialogBranch, subject=self.subject,
                    conversation=self.conversation, branches=line["branches"], 
                    name=self.conversation_name).callback = self.callback
                break
            if "next" in line:
                self.idx = line["next"]
            else:
                self.idx += 1  
            if line.get("breaking", False):
                return
            if line.get("interrupting", False):
                eval("orders.WorldTalkOrder")(subject=self.subject, object=self.object, 
                                              conversation=self.conversation_name, idx=self.idx, hub=True)
                return             
        if self.idx >= len(self.conversation):
            context.timeflow(1)
            PersonSpeakAction(talker=None, content=None).do()

    def do(self):
        conversations = importlib.import_module("%s.scripts" % options.DATA_PATH)
        conversplit = self.conversation.split(",")
        if len(conversplit) > 1:
            self.idx = int(conversplit[1])
        self.conversation_name = conversplit[0]
        self.conversation = getattr(conversations, conversplit[0])
        self.process_conversation()

    def callback(self, idx):
        self.idx = idx
        self.process_conversation()
        
        
class PersonSessionAction(Action):

    def do(self):
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

    def do(self):
        if self.talker is None:
            pass
        #elif len(self.talker) == 0:
        #    self.talker = None
        #elif self.talker.startswith("{") and self.talker.endswith("}"):
            # self.talker = Person.one(self.talker[1:-1])
        # elif self.talker.startswith("[") and self.talker.endswith("]"):
            # teamstr, condstr = self.talker[1:-1].split("|")
            # team = Team.one(teamstr) 
            # cond = {}
            # for cstr in condstr.split(","):
                # ck, cv = cstr.split("=")
                # cond[ck] = cv 
            # self.talker = self.pick(team, **cond)
        # else:
            # self.talker = eval("self.%s" % self.talker)
        MSG(style=MSG.PersonSpeak, talker=self.talker, content=self.content)
        

class PersonChangeConversationAction(Action):
    """
    修改人物对话
    """
    def do(self):
        self.person.conversation = self.conversation
        
        
class PersonConversationAddBranchAction(Action):
    """
    人物对话增加分支
    """
    def do(self):
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
    def do(self):
        conversations = importlib.import_module("%s.dialogs" % options.DATA_PATH)
        conversation = getattr(conversations, self.conversation)
        conversation[self.master]["branches"].remove(self.branch)
        
        
class PersonConversationChangeContentAction(Action):
    """
    人物对话删除分支
    """
    def do(self):
        conversations = importlib.import_module("%s.dialogs" % options.DATA_PATH)
        conversation = getattr(conversations, self.conversation)
        conversation[self.index]["content"] = self.content
        
        
class PersonItemTransferAction(Action):

    def initialize(self):
        self.bag = True

    def do(self):
        self.subject.minus_item(self.item, quantity=self.quantity)
        if self.bag:
            self.object.add_item(self.item, quantity=self.quantity)
        MSG(style=MSG.PersonItemTransfer, subject=self.subject, object=self.object, item=self.item, quantity=self.quantity)

        
class PersonItemAction(Action):

    def do(self):
        self.item.work(self.subject, objects=[self.object])
        context.timeflow(1)


class PersonItemSellAction(Action):

    def do(self):
        PersonItemTransferAction(subject=self.subject, object=self.object,
                                 item=self.item, quantity=self.quantity).do()
        TeamItemTransferAction(team=self.object.team, object=self.subject,
                               item=Item.one("ITEM_MONEY"), quantity=self.item.money * 0.4 * self.quantity).do()


class PersonItemBuyAction(Action):

    def do(self):
        PersonItemTransferAction(subject=self.subject, object=self.object,
                                 item=self.item, quantity=self.quantity).do()
        TeamItemTransferAction(team=self.object.team, object=self.subject,
                               item=Item.one("ITEM_MONEY"), quantity=self.item.money * self.quantity).do()


class PersonItemAcquireAction(Action):

    def do(self):
        self.subject.add_item(self.item, quantity=self.quantity)
        MSG(style=MSG.PersonItemAcquire, subject=self.subject, item=self.item, quantity=self.quantity)


class PersonItemLostAction(Action):

    def do(self):
        self.subject.minus_item(self.item, quantity=self.quantity)
        MSG(style=MSG.PersonItemLost, subject=self.subject, item=self.item, quantity=self.quantity)
        
        
class PersonLearnRecipeAction(Action):

    def do(self):
        if self.recipe not in self.subject.recipes:
            self.subject.recipes.append(self.recipe)
        MSG(style=MSG.PersonRecipeLearn, subject=self.subject, recipe=self.recipe)
        
        
class PersonStudySkillAction(Action):

    def do(self):
        if self.node == self.subject.studying:
            return
        self.subject.exp = 0
        self.subject.studying = self.node


class PersonEquipOffAction(Action):

    def do(self):
        if self.subject.equipment[self.position] is not None:
            self.subject.equipment[self.position].leave(self.subject)
        

class PersonEquipOnAction(Action):
   
    def do(self):
        if self.subject.equipment[self.position] is not None:
             self.subject.equipment[self.position].leave(self.subject)
        self.equip.work(self.subject, position=self.position)
        
        
class PersonTaskUpdateAction(Action):

    def do(self):
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
        MSG(style=MSG.PersonTaskUpdate, task=self.task)
        
        
class PersonAttitudeChangeAction(Action):

    def do(self):
        if self.subject.id not in context.attitudes:
            context.attitudes[self.subject.id] = {}
        if self.object.id not in context.attitudes[self.subject.id]:
            context.attitudes[self.subject.id][self.object.id] = 50
        context.attitudes[self.subject.id][self.object.id] += self.delta
        MSG(style=MSG.PersonAttitudeChange, subject=self.subject, object=self.object, delta=self.delta)
        
        
class PersonRecipeAction(Action):

    def do(self):
        products = self.recipe.work(subject=self.subject, persons=self.persons)
        context.timeflow(1)
        return products


class PersonEquipStrengthenAction(Action):

    def do(self):
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

    def do(self):
        for m in self.team.members:
            if self.quantity == 0:
                break
            if self.item.tpl_id in m.quantities:
                q = min(self.quantity, m.quantities[self.item.tpl_id])
                PersonItemTransferAction(subject=m, object=self.object, item=self.item, quantity=q).do()
                self.quantity -= q
