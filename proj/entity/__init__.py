from proj import data

from proj.entity.constants import BattleEvent
from proj.entity.constants import BattleGroup
from proj.entity.constants import BattlePhase
from proj.entity.constants import AttrText
from proj.entity.constants import SkillType
from proj.entity.person import Person
from proj.entity.map import Map
from proj.entity.map import MapGrid
from proj.entity.map import Terran
from proj.entity.map import Element
from proj.entity.map import Shape
from proj.entity.skill import Skill
from proj.entity.skill import Superskill
from proj.entity.battle import Battle
from proj.entity.effect import Effect
from proj.entity.effect import Status
from proj.entity.force import Force
from proj.entity.common import Entity
from proj.entity.common import HyperAttr
from proj.entity.item import Item
from proj.entity.recipe import Recipe
from proj.entity.team import Team
from proj.entity.force import Force


def init():
    for m in dir(data.map):
        if not m.startswith("MAP"):
            continue
        Map.one(m)
    for f in dir(data.force):
        if not f.startswith("FORCE"):
            continue
        Force.one(f)
    for p in dir(data.person):
        if not p.startswith("PERSON"):
            continue
        Person.one(p)
