# -- coding: utf-8 --

from proj.runtime import context

from proj.core.event import Event
from proj.core.action import ConversationAction
from proj.core.action import AcquireAction


from proj.modules.lite import dialogs

Event(name="Event_1", active=True)

def run_event_1(self):
    ConversationAction(conv=dialogs.START).do()

Event.get("Event_1").enhance("run", run_event_1)

# ------------------------------------------------

Event(name="Event_2")

def run_event_2(self):
    ConversationAction(conv=dialogs.START_2).do()
    AcquireAction(subject=context.PLAYER, item="《射雕心法》", quantity=1).do()
    Event.get("Event_3").turn("on")

Event.get("Event_2").enhance("run", run_event_2)

# ------------------------------------------------

Event(name="Event_3")

def run_event_3(self):
    ConversationAction(conv=dialogs.START_3).do()
    Event.get("Event_4").turn("on")

Event.get("Event_3").enhance("run", run_event_3)

# ------------------------------------------------

Event(name="Event_4")

def run_event_4(self):
    ConversationAction(conv=dialogs.START_4).do()
    Event.get("Event_5").turn("on")
    Event.get("Event_6").turn("on")

Event.get("Event_4").enhance("run", run_event_4)

# ------------------------------------------------

Event(name="Event_5")

def run_event_5(self):
    ConversationAction(conv=dialogs.START_5).do()

def condition_event_5(self):
    return Event.get("Event_2").triggered

Event.get("Event_5").enhance("run", run_event_5)
Event.get("Event_5").enhance("condition", condition_event_5)

# ------------------------------------------------

Event(name="Event_6")

def run_event_6(self):
    ConversationAction(conv=dialogs.VAN_MEET_1).do()
    Event.get("Event_5").turn("off")

Event.get("Event_6").enhance("run", run_event_6)

