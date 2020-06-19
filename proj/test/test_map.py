# -- coding: utf-8 --

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj.entity import Map
from proj.entity import Person

if __name__ == "__main__":
    map = Map.one("MAP_TEST_ASTAR")
    person = Person.one("PERSON_PLAYER")
    for steps in [-1, 1, 2, 3, 4]:
        #startpt = (4, 2)
        startpt = (0, 2)
        endpt = (6, 2)
        last = None
        map.pathblocked = set()
        print("Steps: %s, StartPos: %s, Destination: %s" % (steps, startpt, endpt))
        while startpt != endpt:
            rst = map.connect_dynamic(startpt, endpt, person, last=last, steps=steps)
            print(rst)
            startpt = rst[0]
            last = rst[1]
