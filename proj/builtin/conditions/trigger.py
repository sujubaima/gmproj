# -- coding: utf-8 --

from proj.engine import Condition

from proj.runtime import context


class EventActiveCondition(Condition):

    def check(self):
        return self.event.active
        
        
class EventTriggeredCondition(Condition):

    def check(self):
        return self.event.triggered
        
        
class EventActiveTimeCondition(Condition):

    def check(self):
        return context.timestamp > self.active_time + self.duration