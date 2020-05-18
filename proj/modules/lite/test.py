from proj.runtime import context

from proj.core.person import Person
from proj.core.event import Event
from proj.core.order import Order
from proj.core.action import Action

from proj.console import control as inter
from proj.console import interscene
from proj.console import engine

from proj.modules.lite import events

from proj.modules.lite.data import scenes

context.PLAYER = Person(xing="L", ming="X") 
context.SCENARIO = scenes.SCENE_1_1

while True:
    while Event.pick() is not None:
        #while not Action.empty():
        #    Action.handle()
        console.loop()
    Order.handle()
    #while not Action.empty():
    #    Action.handle()
    console.loop()
    interscene.scene()
