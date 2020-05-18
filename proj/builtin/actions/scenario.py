# -- coding: utf-8 --

from proj.engine import Action
from proj.engine import Message as MSG


__all__ = ['ConversationAction', 'AcquireItemAction']

class SearchAction(Action):

    def initialize(self):
        self.subject = None
        self.scene = None

    def do(self):
        ret = []
        #for k, v in self.scene.objects.items():
        #    if v[1]:
        #        continue
        #    ri = random.randint(1, 100)
        #    if ri < v[1]:
        #        retobj.append(k)
        #        v[1] = True
        for k, v in self.scene.items.items():
            if v[1] == 0:
                continue
            ri = random.randint(1, 100)
            if ri <= v[0]:
                if v[2] is not None:
                    q = random.randint(*v[2])
                else:
                    q = 1
                ret.append((k, q))
                v[1] -= q
        #self.subject.gain(retitem)
        if len(ret) == 0:
            MSG(style=MSG.Show, text="你什么也没有找到。")
        else:
            for itm in ret:
                AcquireAction(subject=self.subject, item=itm[0], quantity=itm[1]).do()


class ConversationAction(Action):

    def initialize(self):
        self.conv = None

    def do(self):
        MSG(style=MSG.Conversation, conv=self.conv)


class AcquireItemAction(Action):

    def initialize(self):
        self.subject = None
        self.item = None
        self.quantity = None
        self.showmsg = True

    def do(self):
        self.subject.add_item(self.item, quantity=self.quantity)
        if self.showmsg:
            Message(style=Message.AcquireItem, item=self.item, quantity=self.quantity)


class DropAction(Action):
    pass


class MakeAction(Action):
    pass


class DamageAction(Action):
    pass


class KillAction(Action):
    pass


class CancelOrderAction(Action):

    def do(self):
        context.Order = None
        Order.All.pop()


class ProcessAction(Action):

    def initialize(self):
        self.period = None
