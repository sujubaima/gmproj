#-- coding: utf-8 --
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj.entity import Person
from proj.entity import Map
from proj.entity import Terran
from proj.entity import Team

from proj import engine

#from proj.builtin.actions import WorldMoveAction

from proj import console
from proj.console import ui
from proj.console.orders import WorldProcessOrder

from proj.runtime import context

console.init()

if __name__ == "__main__":
    pa = Person.one("PERSON_PLAYER")
    pb = Person.one("PERSON_SONG_TIANYONG")
    pc = Person.one("PERSON_XIE_HUI")
    pd = Person.one("PERSON_ZHAO_SHENJI")

    #m = Map(x=120, y=80, window_x=7, window_y=7)
    #m.set_terran([(0, 0), (1, 0),
    #              (0, 1), (1, 1), (2, 1),(3, 1), (4, 1), 
    #              (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)], Terran.Water)
    #m.set_terran([(5, 4), (6, 4), 
    #              (4, 5), (5, 5), (6, 5),
    #              (6, 6), (7, 6), (8, 6)], Terran.Forest)
    #m.set_terran([(3, 6), (4, 6), 
    #              (3, 7)], Terran.Hill)
    #m.set_terran([(3, 4), (4, 4),
    #              (2, 5), 
    #              (2, 6), (5, 6)], Terran.Mountain)
    #m.set_object([(3, 5)], "少林寺")

    #ct = (1, 16)

    m = Map.one("MAP_SUZHOUCHENG")
    #m_world = Map.one("MAP_WORLD")
    team_a = Team()
    #team_b = Team()
    team_a.include(pa)
    team_a.leader = pa
    team_a.scenario = m
    #team_b.include(pb, pc)
    #team_b.leader = pb
    #team_b.scenario = m
    
    team_b = pd.team
    team_b.target = (69, 34)
    #print(team_b.scenario)

    context.map = m
    context.PLAYER = pa
    context.teams[team_a.id] = team_a
    context.teams[team_b.id] = team_b

    m.locate(team_a, (12, 37))
    #m.locate(team_a, (26, 18))
    #m.locate(team_a, (23, 14))
    #m.locate(team_b, (5, 5))

    m.window_center(m.location(team_a))

    #WorldMoveAction(subject=team_b, target=(3, 6)).do()
    #context.timestamp += 1000

    #WorldProcessOrder()
    
    engine.start()
