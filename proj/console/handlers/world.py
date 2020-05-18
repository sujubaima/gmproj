# -- coding: utf-8 --

import sys
import platform

from proj import options

from proj.console import ui
from proj.console import format as fmt

from proj.console.orders.world import WorldProcessOrder
from proj.console.orders.world import WorldPlayerOrder
from proj.console.orders.world import WorldMovePositionOrder
from proj.console.orders.world import WorldTalkPositionOrder
from proj.console.orders.world import WorldGivePositionOrder
from proj.console.orders.world import WorldExplorePositionOrder
from proj.console.orders.world import WorldBuildPositionOrder
from proj.console.orders.world import WorldBuildOrder
from proj.console.orders.world import WorldTerranOrder
from proj.console.orders.world import WorldAttackPositionOrder
from proj.console.orders.world import WorldTalkOrder
from proj.console.orders.world import WorldRestOrder

from proj.console.orders.person import PersonItemChooseOrder
from proj.console.orders.person import PersonItemOrder

from proj.console.handlers.person import team_menu
from proj.console.handlers.person import item_menu

from proj.entity import Terran
from proj.entity import Map

from proj.runtime import context

last_timestamp = 0


system_menu = [ui.menuitem("事件", goto=lambda x: show_tasks()),
               ui.menuitem("情报", validator=lambda x: False),
               ui.menuitem("地图", goto=lambda x: show_thumbnail()),
               ui.menuitem("成就", validator=lambda x: False),
               ui.menuitem("存档", validator=lambda x: False),
               ui.menuitem("载入", validator=lambda x: False),
               ui.menuitem("退出", goto=lambda x: sys.exit(0))]


def world_menu(team):
    title = ui.colored("队员一览：%s队" % team.leader.name, color="yellow", attrs=["bold"])
    ret = [ui.menuitem("移动", goto=lambda x: WorldMovePositionOrder()),
           ui.menuitem("交谈", goto=lambda x: WorldTalkPositionOrder()),
           ui.menuitem("赠与", goto=lambda x: WorldGivePositionOrder()),
           ui.menuitem("探索", goto=lambda x: WorldExplorePositionOrder()),
           ui.menuitem("建设", goto=lambda x: WorldBuildPositionOrder()),
           ui.menuitem("攻击", goto=lambda x: WorldAttackPositionOrder()),
           ui.menuitem("休息", goto=lambda x: WorldRestOrder()),
           ui.menuitem("队伍", goto=lambda x: ui.menu(member_menu(), title=title, 
                                                      goback=True, backmethod=lambda: WorldPlayerOrder())),
           ui.menuitem("系统", goto=lambda x: ui.menu(system_menu, columns=2, width=15,
                                                      goback=True, backmethod=lambda: WorldPlayerOrder()))]
    return ret
              
              
def build_menu(person, pos): 
    bmenu = [ui.menuitem("建造建筑", goto=lambda x: ui.menu(buildings_menu(person, pos), goback=True)),
             ui.menuitem("拆除建筑", goto=lambda x: ui.menu(buildings_menu(person, pos), goback=True)),
             ui.menuitem("改造地形", goto=lambda x: ui.menu(terran_menu(person, pos), goback=True))]
    return bmenu


def terran_menu(person, pos):
    tmenu = [ui.menuitem("草地", goto=lambda x: WorldTerranOrder(subject=person, position=pos, terran=Terran.one("TERRAN_GRASS"))),
             ui.menuitem("树林", goto=lambda x: WorldTerranOrder(subject=person, position=pos, terran=Terran.one("TERRAN_FOREST"))),
             ui.menuitem("水域", goto=lambda x: WorldTerranOrder(subject=person, position=pos, terran=Terran.one("TERRAN_WATER"))),
             ui.menuitem("山地", goto=lambda x: WorldTerranOrder(subject=person, position=pos, terran=Terran.one("TERRAN_MOUNTAIN")))]
    return tmenu


def buildings_menu(person, pos):
    bmenu = []
    return bmenu


def show_thumbnail():
    ui.echo()
    ui.thumbnail(map=context.PLAYER.team.scenario, entities=team_info(context.PLAYER.team.scenario))
    ui.echo()
    ui.read("（回车继续）")
    

def show_tasks(back=False):
    if back:
        ui.popmenu()
    ui.menu(task_menu(), title="请选择查看的事件：", goback=True)
    

def task_method(x):
    context.tasks_status[x[0]] = False
    ui.menu([], title="事件：%s" % x[0], inpanel=x[1], shownone=False, goback=True, backmethod=lambda: show_tasks(back=True))


def task_menu():
    tmenu = []
    for t in context.tasks_index:
        tlist = context.tasks[t]
        bold = context.tasks_status[t]
        tmenu.append(ui.menuitem(t, value=(t, tlist), bold=bold, goto=task_method))
    return tmenu


def member_menu():
    team = context.PLAYER.team
    ret = []
    for m in team.members:
        title = lambda x: ui.colored("当前队员：%s" % x.name, color="yellow", attrs=["bold"])
        ret.append(ui.menuitem(m.name, value=m, 
                               goto=lambda x: ui.menu(team_menu(x), title=title(x), goback=True, columns=4, width=15)))
    return ret


def person_menu(point, map, include_self=False):
    ret = []
    team = map.loc_entity[point]
    for m in team.members:
        if m == context.PLAYER and not include_self:
            continue
        ret.append(ui.menuitem(m.name, value=m)) 
    return ret


def validate_position(pos, valid_pos, can_on_person, map=None):
    if map is None:
        map = context.PLAYER.team.scenario
    x, y = pos.split()
    x = int(x)
    y = int(y)
    real_pos = map.point_to_real((x, y))
    if not can_on_person and real_pos in map.loc_entity:
        return None
    if real_pos not in valid_pos:
        return None
    return real_pos

def team_info(map):

    retlist = []

    for loc, entity in map.loc_entity.items():
        ret = {"location": None,
               "contents": ["", "", ""],
               "trace": [],
               "player": False}
        ret["location"] = map.entity_loc[entity.id]

        if len(entity.members) == 1:
            title = entity.leader.name 
        else:
            title = "%s队" % entity.leader.name
        # 处理标题文本
        #if entity.leader.player and platform.system() == "Linux":
        if entity.leader.player:
            ret["player"] = True
            ret["contents"][0] = ui.colored(title,
                                            color="grey",
                                            on_color="on_cyan")
        #elif entity.leader.player:
        #    ret["player"] = True
        #    ret["contents"][0] = ui.colored(title,
        #                                    on_color="on_cyan",
        #                                    attrs=["bold"])
        else:
            ret["contents"][0] = ui.colored(title,
                                            color="cyan",
                                            attrs=["bold"])
        #ret["contents"][0] += fmt.vaka["direction"][str(entity.direction)]
        if entity.battle is not None:
            ret["contents"][1] += ui.colored("（战斗中）", color="yellow", attrs=["bold"])

        # 处理路径
        if entity.last_move + context.duration() > context.timestamp and len(entity.path) > 1:
            ret["trace"].extend(entity.path)
        retlist.append(ret)
    last_timestamp = context.timestamp
    return retlist
    
    
def _recenter(team):
    t_loc = team.scenario.location(team)
    t_map = team.scenario
    new_center_x = t_map.center_x
    if t_loc[0] - t_map.window_start_x < options.MOTION_SCENARIO:
        new_center_x = max(0, t_map.center_x - options.MOTION_SCENARIO + t_loc[0] - t_map.window_start_x)
    elif t_map.window_start_x + t_map.window_x - t_loc[0] < options.MOTION_SCENARIO + 1:
        new_center_x = min(t_map.center_x + options.MOTION_SCENARIO + 1 - \
                           t_map.window_start_x - t_map.window_x + t_loc[0], t_map.x - 1)
    new_center_y = t_map.center_y
    if t_loc[1] - t_map.window_start_y < options.MOTION_SCENARIO:
        new_center_y = max(0, t_map.center_y - options.MOTION_SCENARIO + t_loc[1] - t_map.window_start_y)
    elif t_map.window_start_y + t_map.window_y - t_loc[1] < options.MOTION_SCENARIO + 1:
        new_center_y = min(t_map.center_y + options.MOTION_SCENARIO + 1 - \
                           t_map.window_start_y - t_map.window_y + t_loc[1], t_map.y - 1)
    if new_center_x != t_map.center_x or new_center_y != t_map.center_y:
        team.scenario.window_center((new_center_x, new_center_y))
        
        
def recenter(team):
    t_loc = team.scenario.location(team)
    t_map = team.scenario
    new_start_x = t_map.window_start_x
    if t_loc[0] - t_map.window_start_x < options.MOTION_SCENARIO:
        new_start_x = max(0, t_loc[0] - options.MOTION_SCENARIO)
    elif t_map.window_start_x + t_map.window_x - t_loc[0] < options.MOTION_SCENARIO + 1:
        new_start_x = min(options.MOTION_SCENARIO + 1 - t_map.window_x + t_loc[0], t_map.x - t_map.window_x)
    new_start_y = t_map.window_start_y
    if t_loc[1] - t_map.window_start_y < options.MOTION_SCENARIO:
        new_start_y = max(0, t_loc[1] - options.MOTION_SCENARIO)
    elif t_map.window_start_y + t_map.window_y - t_loc[1] < options.MOTION_SCENARIO + 1:
        new_start_y = min(options.MOTION_SCENARIO + 1  - t_map.window_y + t_loc[1], t_map.y - t_map.window_y)
    if new_start_x != t_map.window_start_x or new_start_y != t_map.window_start_y:
        team.scenario.window_center((new_start_x + t_map.window_x // 2, 
                                     new_start_y + t_map.window_y // 2))


def handler_world_map(ctx):
    ui.echo()
    ui.map(ctx.map, entities=team_info(ctx.map), show_trace=ctx.show_trace)
    ui.echo()
    ui.read("（回车继续）")
    ui.echo()


def handler_world_player(ctx):
    map = ctx.map
    ui.cleanmenu()
    recenter(ctx.subject)
    ui.echo()
    ui.echo("当前回合：%s" % context.timestamp)
    ui.echo()
    ui.map(map, entities=team_info(ctx.map), show_trace=True)
    ui.menu(world_menu(ctx.subject), title="请选择你的行动方针：", columns=5, width=15)


def handler_world_move_position(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map),
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    rt = ui.read("请输入你想要移动的格子坐标（绿色表示可移动格子，坐标用空格分隔，输入#back可返回）：",
                 handler=lambda x: validate_position(x, ctx.positions, False))
    ui.echo()
    return rt


def handler_world_clash(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map), show_trace=True)
    ui.echo()
    ui.warn("移动过程中发生路径冲突，移动已中断！")
    ui.echo()
    ui.read("（回车继续）")
    ui.menu(world_menu(ctx.subject), title="请选择你的行动方针：", columns=5, width=15)


def handler_world_talk_position(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map),
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    rt = ui.read("请输入你想要对话的对象坐标（绿色表示可交谈范围，坐标用空格分隔，输入#back可返回）：",
                 handler=lambda x: validate_position(x, ctx.positions, True))
    ui.echo()
    return rt


def handler_world_talk_object(ctx):
    map = ctx.map
    if ctx.pos not in map.loc_entity:
        ui.warn("该坐标下无可交谈对象！")
        ui.echo()
        ui.read("（回车继续）")
        return None
    pmenu = person_menu(ctx.pos, map)
    if len(pmenu) > 1:
        rt = ui.menu(pmenu, title="请选择你要交谈的角色：", goback=True, backmethod=lambda: None)
        ui.echo()
    else:
        rt = pmenu[0].value
    return rt


def handler_world_build_position(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map),
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    rt = ui.read("请输入你想要建设的格子（绿色表示可建设范围，坐标用空格分隔，输入#back可返回）：",
                 handler=lambda x: validate_position(x, ctx.positions, True))
    return rt


def handler_world_build_plan(ctx):
    ui.menu(build_menu(ctx.subject, ctx.position), goback=True, title="请选择你的建设方案：", backmethod=lambda: WorldPlayerOrder())

    
def handler_world_give_position(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map),
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    while True:
        rt = ui.read("请输入你想要赠予的对象坐标（绿色表示可赠予范围，坐标用空格分隔，输入#back可返回）：",
                     handler=lambda x: validate_position(x, ctx.positions, True))
        if rt is not None and rt not in map.loc_entity:
            ui.warn("该坐标下无可赠予对象！")
        else:
            break
        ui.echo()
    return rt
    
    
def handler_world_give_object(ctx):
    map = ctx.map
    if ctx.pos not in map.loc_entity:
        ui.warn("该坐标下无可赠予对象！")
        ui.echo()
        ui.read("（回车继续）")
        return None
    ui.echo()
    pmenu = person_menu(ctx.pos, map)
    if len(pmenu) > 1:
        rt = ui.menu(pmenu, title="请选择你要赠予的角色：", goback=True, backmethod=lambda: None)
    else:
        rt = pmenu[0].value
    return rt


def handler_world_explore_position(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map),
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    rt = ui.read("请输入你想要探索的格子（绿色表示可探索范围，坐标用空格分隔，输入#back可返回）：",
                 handler=lambda x: validate_position(x, ctx.positions, True))
    ui.echo()
    return rt


def handler_world_explore_tool(ctx):
    itm_menu = [ui.menuitem("徒手", value="")]
    itm_menu.extend(item_menu(ctx.subject.members, None, filter=ctx.filter, show_forbidden=False))
    if len(itm_menu) == 1:
        ret = item_menu[0].value
    else:
        ret = ui.menu(itm_menu, title="以下工具可用于该地块探索：", goback=True)
    return ret


def handler_world_attack_position(ctx):
    map = ctx.map
    ui.echo()
    ui.map(map, entities=team_info(ctx.map),
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    rt = ui.read("请输入你想要攻击的对象坐标（绿色表示可攻击范围，坐标用空格分隔，输入#back可返回）：",
                 handler=lambda x: validate_position(x, ctx.positions, True))
    ui.echo()
    return rt


def handler_world_attack_ensure(ctx):
    ret = ui.sure(ui.colored("动手之前要想清楚，是否进行攻击？", color="yellow", attrs=["bold"]))
    return ret
    
    
def handler_world_scenario_change_ensure(ctx):
    target = ctx.team.scenario.transport_locs[ctx.team.location]
    target = Map.one(target).name
    map = ctx.team.scenario
    ui.map(map, entities=team_info(map), show_trace=True)
    ui.echo()
    ret = ui.sure("当前地块可通往%s，是否前往？" % target)
    return ret
    
    
def handler_world_rest(ctx):
    ui.echo()
    ui.map(ctx.map, entities=team_info(ctx.map), show_trace=True)
    ui.echo()
    ret = ui.sure("你已经休息过了一段时间，是否继续休息？")
    return ret
