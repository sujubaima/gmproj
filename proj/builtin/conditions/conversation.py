# -- coding: utf-8 --

from proj.engine import Condition

from proj.runtime import context

class ConversationSpokenCondition(Condition):

    def check(self):
        return self.conversation in context.conversation_status and \
               self.index in context.conversation_status[self.conversation]