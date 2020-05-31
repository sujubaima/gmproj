# -- coding: utf-8 --

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj.entity import Battle
from proj.entity import Item
from proj.entity import Person
from proj.entity import Map
from proj.entity import Team
from proj.entity import Status

from proj.builtin.actions import BattleStartAction

from proj.console.orders import WorldProcessOrder

from proj import console
from proj.console import ui

from proj import engine

from proj.runtime import context


console.init()


if __name__ == "__main__":
    p_lx = Person.one("PERSON_PLAYER")
    p_wpf = Person.one("PERSON_WAN_PENGFEI")
    p_sty = Person.one("PERSON_SONG_TIANYONG")
    p_xh = Person.one("PERSON_XIE_HUI")
    p_jl = Person.one("PERSON_JU_LIU")
    p_zsj = Person.one("PERSON_ZHAO_SHENJI")
    p_tw = Person.one("PERSON_TIAN_WEI")
    p_yl = Person.one("PERSON_YANG_LEI")
    p_yqf = Person.one("PERSON_YING_QINGFENG")
    
    p_zrb = Person.one("PERSON_ZHU_RUBI")    
    p_yq = Person.one("PERSON_YU_QI")
    p_hy = Person.one("PERSON_HE_YUE")
    p_msq = Person.one("PERSON_MU_SHUANGQING")
    
    p_ctz = Person.one("PERSON_CHEN_TINGZHI")
    p_ly = Person.one("PERSON_LUO_YI")
    p_sjy = Person.one("PERSON_SHI_JINGYAN")
    
    p_zbs = Person.one("PERSON_ZHONG_BUSU")
    p_lw = Person.one("PERSON_LI_WAN")

    p_jy = Person.one("PERSON_JUE_YIN")
    p_jc = Person.one("PERSON_JUE_CHENG")

    p_zys = Person.one("PERSON_ZHANG_YINSONG")
    p_lpf = Person.one("PERSON_LI_PEIFENG")

    p_lcy = Person.one("PERSON_LI_CANGYING")
    p_xfl = Person.one("PERSON_XING_FEILONG")
    
    p_rwh = Person.one("PERSON_RAN_WUHUA")
    
    
    m1 = Map.one("MAP_BTL_BAIBINGTANGZONGDUO")
    m2 = Map.one("MAP_BTL_YOUMINGGONGSHANXIA")
    m3 = Map.one("MAP_BTL_GRASSLAND_BIG")
    m4 = Map.one("MAP_SUZHOUCHENG_BTL")
    m5 = Map.one("MAP_JIUXIPAI_BTL")
    m6 = Map.one("MAP_SHAOLINSI_BTL")


    #o.direction = -4
    #o.move_style = "flydown"

    team_a = Team()
    team_b = Team()
    #team_a.include(p_zrb, p_wpf, p_sty, p_xh, p_yl)
    #team_b.include(p_zsj, p_tw, p_jl, p_yqf)

    #team_a.include(p_msq, p_hy, p_yq, p_zrb, p_jy)
    #team_b.include(p_zys, p_wpf, p_sjy, p_ly, p_ctz)
    team_a.include(p_rwh)
    team_b.include(p_jc)

    context.teams[team_a.id] = team_a
    context.teams[team_b.id] = team_b

    ui.echo()
    ui.warn("欢迎测试本游戏的战斗系统，windows下建议控制台字体调成黑体，谢谢！")
    ui.echo()
    
    ac = ui.menu([ui.menuitem("%s队" % team_a.leader.name, value=team_a.leader),
                  ui.menuitem("%s队" % team_b.leader.name, value=team_b.leader),
                  ui.menuitem("观战而已", value=None)], title="请选择你想控制的队伍：")

    if ac == "观战而已":
        context.PLAYER = None
    else:
        context.PLAYER = ac

    ac = ui.menu([ui.menuitem(m6.name, value=m6),
                  ui.menuitem(m4.name, value=m4),
                  ui.menuitem(m1.name, value=m1),
                  ui.menuitem(m2.name, value=m2),
                  ui.menuitem(m3.name, value=m3),
                  ui.menuitem(m5.name, value=m5)], title="请选择测试用的地图：")
    #b = interbtl.battle(ac, [p, q, g], [o])

    BattleStartAction(map=ac, groups=[team_a.members, team_b.members]).do()
    #context.timestamp += 1
   
    WorldProcessOrder()

    engine.start(events=False)
