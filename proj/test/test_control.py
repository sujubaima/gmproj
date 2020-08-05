# -- coding: utf-8 --

import os
import sys
import time
import threading

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj import engine
from proj.engine import Control
from proj.engine import Message as MSG

from proj.console.controls import PipeControl
from proj.console.controls import TradeControl
from proj.console.controls import ScenarioControl
from proj.console.controls import TimeflowControl

#from proj.console.controls import ItemSelectControl
#from proj.console.controls import SkillSelectControl

from proj import console

from proj.entity import Person
from proj.entity import Map

from proj.runtime import context


class TestControlA(Control):

    def launch(self):
        self.text = "controlA"
        self.wait = True
        MSG(style=MSG.ControlTest).control = self
        print("LaunchedA")

    @Control.listener
    def hook(self):
        print("hookA")
        TestControlB().run()
        self.close()
        print("CloseA")

class TestControlB(Control):

    def launch(self):
        self.text = "controlB"
        self.wait = True
        MSG(style=MSG.ControlTest).control = self
        print("LaunchedB")

    @Control.listener
    def hook(self):
        print("hookB")
        TestControlC().run()
        self.close()
        print("CloseB")


class TestControlC(Control):

    def launch(self):
        self.text = "controlC"
        self.wait = True
        MSG(style=MSG.ControlTest).control = self
        print("LaunchedC")

    @Control.listener
    def hook(self):
        print("HookC")
        self.close()
        print("CloseC")


console.init()
engine.init()


if __name__ == "__main__":
    p_player = Person.one("PERSON_PLAYER")
    p_sty = Person.one("PERSON_SONG_TIANYONG")
    p_dtj = Person.one("PERSON_DING_TIEJIANG_SUZHOU")
    m_world = Map.one("MAP_SUZHOUCHENG")
    m_world.locate(p_player.team, (12, 37))
    p_player.team.include(p_sty)
    p_player.team.scenario = m_world
    context.PLAYER = p_player
    
    control = TradeControl(subject=p_player, object=p_dtj)
    #control = TestControlA() 
    #control = SkillControl(subject=p_player)
    #control = EquipmentControl(subject=p_player)
    #control = PipeControl()
    #control.pipe(SkillSelectControl(subject=p_player, type=0), keys=["skill"])\
    #       .pipe(ItemSelectControl(subject=p_player, object=p_player, quantity=1), keys=["item"])
    #control = ScenarioControl(subject=p_player.team, scenario=m_world)
    #control = TimeflowControl()
    bth = threading.Thread(target=control.run, daemon=True)
    bth.start()

    mth = engine.MSGThread()
    #mth.start()
    #mth.join()
    mth.run()
