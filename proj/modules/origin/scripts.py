# -- coding: utf-8 --

from proj import entity
from proj.entity import Person
from proj.entity import Map
from proj.entity import Team

from proj import console

from proj import engine

from proj.runtime import context
from proj.runtime import saveload


def start(loadfile=None):
    
    print("引擎初始化中……\n")
    console.init()
    print("游戏数据载入中……\n")
    entity.init()
    print("世界构建中……\n")
    context.init()

    m = Map.one("MAP_SUZHOUCHENG")
    player = Person.one("PERSON_PLAYER")

    team_player = Team()
    team_player.include(player)
    team_player.leader = player
    team_player.scenario = m

    context.map = m
    context.PLAYER = player
    context.teams[team_player.id] = team_player

    m.locate(team_player, (18, 27))

    m.window_center(m.location(team_player))

    if loadfile is not None:
        print("存档文件加载中……\n")
        saveload.load(loadfile)
    engine.init()
    engine.start()
