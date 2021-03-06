#-- coding: utf-8 --
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj import entity
from proj.entity import Person
from proj.entity import Map
from proj.entity import Terran
from proj.entity import Team
from proj.entity import Item

from proj import engine
from proj.engine import script

from proj import console
from proj import data
from proj.console import ui

from proj.runtime import context

print("\n初始化引擎中……")
engine.init()
console.init()
print("\n载入数据中……")
entity.init()

if __name__ == "__main__":
    pa = Person.one("PERSON_PLAYER")
    pb = Person.one("PERSON_SONG_TIANYONG")
    pc = Person.one("PERSON_XIE_HUI")
    pd = Person.one("PERSON_ZHAO_SHENJI")
    pe = Person.one("PERSON_CHEN_TINGZHI")

    pa.add_item(Item.one("ITEM_DIAOGAN"), 1)
    pa.add_item(Item.one("ITEM_LIANDAO"), 1)
    pa.add_item(Item.one("ITEM_SHOUFU"), 1)

    m = Map.one("MAP_SUZHOUCHENG")
    team_a = Team()
    team_a.include(pa)
    team_a.leader = pa
    team_a.scenario = m
    
    team_b = pd.team
    team_b.targets.append((0, (69, 34)))

    context.map = m
    context.PLAYER = pa
    context.teams[team_a.id] = team_a
    context.teams[team_b.id] = team_b

    #m.locate(team_a, (12, 37))
    tmploc = pe.team.location
    m.locate(team_a, (tmploc[0], tmploc[1] + 1))

    m.window_center(m.location(team_a))
    
    script.run(data.scripts.SCRIPT_INITIALIZE_1, subject=pa, object=pc)
    script.run(data.scripts.SCRIPT_INITIALIZE_2, subject=pa, object=pc)

    engine.start()
