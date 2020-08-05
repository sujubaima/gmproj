# -- coding: utf-8 --

from proj.engine import Condition

from proj.runtime import context

class ScriptExecutedCondition(Condition):

    def check(self):
        return self.script in context.script_status and \
               self.label in context.script_status[self.script]
