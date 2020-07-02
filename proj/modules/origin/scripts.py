# -- coding: utf-8 --

from proj.entity import Person
from proj.entity import Map
from proj.entity import Team

from proj import console

from proj import engine

from proj.runtime import context

console.init()

def start():
    m = Map.one("MAP_SUZHOUCHENG")
    player = Person.one("PERSON_PLAYER")

    team_player = Team()
    team_player.include(player)
    team_player.leader = player
    team_player.scenario = m

    context.map = m
    context.PLAYER = player
    context.teams[team_player.id] = team_player

    m.locate(team_player, (12, 37))

    m.window_center(m.location(team_player))

    engine.start()
