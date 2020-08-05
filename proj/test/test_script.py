# -- coding: utf-8 --

import os
import sys
import time

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj import data

from proj.runtime import context

from proj import console

from proj import engine
from proj.engine import script

from proj.entity import Person
from proj.entity import Map

console.init()


if __name__ == "__main__":
    player = Person.one("PERSON_PLAYER")
    map = Map.one("MAP_SUZHOUCHENG")
    time_1 = time.time()
    script.run(data.scripts.SCRIPT_WANPENGFEI_1, timeflow=1, 
               subject=Person.one("PERSON_PLAYER"), 
               object=Person.one("PERSON_WAN_PENGFEI"))
    #script.run2(data.scripts.SCRIPT_WANPENGFEI_TEST, timeflow=1,
    #            subject=player,
    #            object=Person.one("PERSON_WAN_PENGFEI"))
    time_2 = time.time()
    print(time_2 - time_1)
    engine.start()
