from __future__ import division

import threading
import time
import importlib
import platform

from proj import options

from proj.engine.frame import Message
from proj.engine.frame import Action
from proj.engine.frame import Event
from proj.engine.frame import Order
from proj.engine.frame import Condition

from proj import data


def load_events():
    for e in dir(data.event):
        if not e.startswith("EVENT"):
            continue            
        Event(id=e, **getattr(data.events, e))
        
class MSGThread(threading.Thread):

    def run(self):
        while True:
            msg = Message.All.get()
            Message.handler(msg)
            if Message.All.empty():
                Message.empty.set()
                Message.nempty.clear()
            Message.nempty.wait()


class OrderThread(threading.Thread):
    
    def run(self):
        while True:
            order = Order.All.pop(0)
            if order.hub:
                Message.empty.wait()
                if len(Order.All) > 0 and not Order.All[0].hub:
                    order.finish()
                    continue
            #print(order.__class__)
            #if not order.eventless:
            #    while Event.pick() is not None:
            #        Message.empty.wait()
            order.solve()             
            if len(Order.All) == 0 or Order.All[0].hub:
                Order.empty.set()
            elif len(Order.All) == 0:
                Order.nempty.clear()
            Order.nempty.wait()
            
            
#class OrderHubThread(threading.Thread):
#
#    def run(self):
#        while True:
#            order = Order.Hubs.get()
#            Thread.synced.wait()
#            Order.All.put(order)
#            Order.empty.clear()
#            Order.nempty.set()           


def start():
    ods = importlib.import_module("proj.console.orders.world")
    ods.WorldProcessOrder()
    if options.MULTIPLE_THREAD:       
        oth = OrderThread(daemon=True)
        oth.start()
        mth = MSGThread()
        mth.run()
        #OrderHubThread().start()
        oth.join()
    else:
        Order.sync()
