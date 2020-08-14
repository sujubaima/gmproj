# -- coding: utf-8 --

from proj import options

from proj.runtime import context

from proj.console import ui

from proj.console.handlers.common import team_info
from proj.console.handlers.common import item_menu


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


def world_menu(ctrl):
    title = ui.byellow("队员一览：%s队" % ctrl.team.leader.name)
    ret = [ui.menuitem("移动", goto=ctrl.move),
           ui.menuitem("交谈", goto=ctrl.talk),
           #ui.menuitem("赠与"),
           ui.menuitem("探索", goto=ctrl.explore),
           #ui.menuitem("建设"),
           ui.menuitem("攻击", goto=ctrl.attack),
           ui.menuitem("休息", goto=ctrl.rest),
           ui.menuitem("地图", goto=ctrl.thumbnail),
           ui.menuitem("队伍", goto=ctrl.teaminfo),
           ui.menuitem("系统", goto=ctrl.system)]
    return ret


def handler_scenario_control(ctrl):
    scenario = ctrl.scenario
    ui.cleanmenu()
    recenter(ctrl.team)
    if not ui.blankline():
        ui.echo()
    ui.echo("当前回合：%s" % context.timestamp)
    ui.echo()
    ui.map(scenario, entities=team_info(ctrl), coordinates=[{"positions": context.guide, "color": "yellow"}], show_trace=True)
    ui.menu(world_menu(ctrl), title="请选择你的行动方针：", macros=ctrl.macs, columns=4, width=15)


def handler_explore_tool_select_control(ctrl):
    i_menu = item_menu(ctrl)
    i_menu.insert(0, ui.menuitem("徒手", value=(None, ctrl.team.leader), goto=ctrl.select))
    ui.menu(i_menu, title=ui.byellow(ctrl.title),
            goback=True, backmethod=ctrl.close)


def handler_scenario_change_control(ctrl):
    map = ctrl.team.scenario
    ui.map(map, entities=team_info(ctrl), show_trace=True)
    ui.echo()
    ret = ui.sure(ctrl.text)
    ctrl.input(ret)


def handler_rest_control(ctrl):
    ui.echo()
    ui.map(ctrl.team.scenario, entities=team_info(ctrl), show_trace=True)
    ui.echo()
    ret = ui.sure("你已经休息过了一段时间，是否继续休息？")
    ctrl.input(ret)


def handler_thumbnail_control(ctrl):
    if not ui.blankline():
        ui.echo()
    ui.thumbnail(map=ctrl.scenario, entities=team_info(ctrl))
    ui.echo()
    ui.read("（回车继续）")
    ctrl.close()
