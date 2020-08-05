# -- coding: utf-8 --

from proj.engine import Action
from proj.engine import Event

from proj.runtime import context


class EventSwitchAction(Action):

    def take(self):
        Event.get(self.event).turn(self.state, context.timestamp_)
      

class EventSwitchOnAction(Action):

    def take(self):
        Event.get(self.event).turn("on", context.timestamp_)      
        
        
class EventSwitchOffAction(Action):

    def take(self):
        Event.get(self.event).turn("off", context.timestamp_)   
