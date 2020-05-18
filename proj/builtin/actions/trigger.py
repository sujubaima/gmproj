# -- coding: utf-8 --

from proj.engine import Action
from proj.engine import Event

__all__ = ['EventSwitchAction', 'EventSwitchOnAction', 'EventSwitchOffAction']

class EventSwitchAction(Action):

    def do(self):
        Event.get(self.event).turn(self.state)
      

class EventSwitchOnAction(Action):

    def do(self):
        Event.get(self.event).turn("on")      
        
        
class EventSwitchOffAction(Action):

    def do(self):
        Event.get(self.event).turn("off")   