from __future__ import division

import os
import sys
import threading
import time
import importlib
import platform
import signal

from proj.engine.frame import Message
from proj.engine.frame import Action
from proj.engine.frame import Control
from proj.engine.frame import Event
from proj.engine.frame import Condition
from proj.engine.script import JsonScript

from proj import data


running = False


def init():
    for e in dir(data.event):
        if not e.startswith("EVENT"):
            continue            
        Event(id=e, **getattr(data.events, e))
        

class MSGThread(threading.Thread):

    def run(self):
        global running
        while running:
            msg = Message.All.get()
            Message.handler(msg)
            if Message.All.empty():
                Message.empty.set()


def signal_handler(signal, frame):
    stop(trace=True)


def stop(trace=False):
    global running
    running = False
    for ctrl in Control.All[::-1]:
        ctrl.close()
    Control.thpool.shutdown(wait=False)
    print("")
    sys.exit()


def start():
    global running
    signal.signal(signal.SIGINT, signal_handler)
    running = True
    ctrls = importlib.import_module("proj.console.controls.timeflow")
    control = ctrls.TimeflowControl()
    #bth = threading.Thread(target=control.run, daemon=True)
    #bth.start()
    Control.thpool.submit(control.run)
    mth = MSGThread()
    mth.run()
