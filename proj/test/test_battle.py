# -- coding: utf-8 --

import os
import sys
import threading

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj.entity import Battle
from proj.entity import Item
from proj.entity import Person
from proj.entity import Map
from proj.entity import Team
from proj.entity import Status

from proj.builtin.actions import BattleStartAction

from proj import console
from proj.console import ui

from proj import engine

from proj.runtime import context


console.init()


if __name__ == "__main__":
    p_lx = Person.one("PERSON_PLAYER")
    p_wpf = Person.one("PERSON_WAN_PENGFEI")

    # 百兵堂
    p_sty = Person.one("PERSON_SONG_TIANYONG")
    p_xh = Person.one("PERSON_XIE_HUI")
    p_jl = Person.one("PERSON_JU_LIU")

    # 长生坛
    p_zsj = Person.one("PERSON_ZHAO_SHENJI")

    # 东厂
    p_tw = Person.one("PERSON_TIAN_WEI")

    # 华山派
    p_yl = Person.one("PERSON_YANG_LEI")

    # 幽冥宫
    p_qcb = Person.one("PERSON_QI_CHENGBAI")
    p_yqf = Person.one("PERSON_YING_QINGFENG")
    
    # 九溪派
    p_zrb = Person.one("PERSON_ZHU_RUBI")    
    p_yq = Person.one("PERSON_YU_QI")
    p_hy = Person.one("PERSON_HE_YUE")
    p_msq = Person.one("PERSON_MU_SHUANGQING")
    
    # 北辰派
    p_ctz = Person.one("PERSON_CHEN_TINGZHI")
    p_ly = Person.one("PERSON_LUO_YI")
    
    # 青袍会
    p_zbs = Person.one("PERSON_ZHONG_BUSU")
    p_lw = Person.one("PERSON_LI_WAN")

    # 少林寺
    p_jy = Person.one("PERSON_JUE_YIN")
    p_jc = Person.one("PERSON_JUE_CHENG")
    p_pk = Person.one("PERSON_PENG_KUAN")

    # 武当派
    p_zys = Person.one("PERSON_ZHANG_YINSONG")
    p_lpf = Person.one("PERSON_LI_PEIFENG")

    # 丐帮
    p_lcy = Person.one("PERSON_LI_CANGYING")
    p_xfl = Person.one("PERSON_XING_FEILONG")
    p_hyx = Person.one("PERSON_HONG_YUANXIANG")
    
    # 峨眉派
    p_rwh = Person.one("PERSON_RAN_WUHUA")
    p_cg = Person.one("PERSON_CI_GUANG")

    # 甲螺
    p_ld = Person.one("PERSON_LI_DAN")
    p_ysq = Person.one("PERSON_YAN_SIQI")

    # 巨阙门
    p_gzq = Person.one("PERSON_GENG_ZHUQIAO")
    p_sjy = Person.one("PERSON_SHI_JINGYAN")

    # 密宗
    p_snrd = Person.one("PERSON_SUONAN_RAODAN")
    
    
    m1 = Map.one("MAP_BTL_BAIBINGTANGZONGDUO")
    m2 = Map.one("MAP_BTL_YOUMINGGONGSHANXIA")
    m3 = Map.one("MAP_BTL_GRASSLAND_BIG")
    m4 = Map.one("MAP_SUZHOUCHENG_BTL")
    m5 = Map.one("MAP_JIUXIPAI_BTL")
    m6 = Map.one("MAP_SHAOLINSI_BTL")

    team_shaolin = Team(label="少林寺")
    team_wudang = Team(label="武当派")
    team_gaibang = Team(label="丐帮")
    team_emei = Team(label="峨眉派")
    team_youminggong = Team(label="幽冥宫")
    team_huairen = Team()
    team_beichenpai = Team(label="北辰派")
    team_jiuxipai = Team(label="九溪派")
    team_baibingtang = Team(label="百兵堂")
    team_jialuozu = Team(label="甲螺组")
    team_juquemen = Team(label="巨阙门")
    team_caiji = Team()
    
    team_shaolin.include(p_jy, p_jc, p_snrd)
    team_wudang.include(p_zys, p_lpf)
    team_gaibang.include(p_xfl, p_lcy)
    team_emei.include(p_rwh, p_cg)
    team_huairen.include(p_tw, p_zsj)
    team_youminggong.include(p_qcb, p_yqf)
    team_baibingtang.include(p_sty, p_xh, p_jl)
    team_jialuozu.include(p_ld, p_ysq)
    team_juquemen.include(p_gzq, p_sjy)
    team_beichenpai.include(p_ctz, p_ly)
    team_jiuxipai.include(p_msq, p_hy, p_yq, p_zrb)
    team_caiji.include(p_lx, p_wpf)

    ui.echo()
    ui.warn("欢迎测试本游戏的战斗系统，windows下建议控制台字体调成黑体，谢谢！")
    ui.echo()

    ac = ui.menu([ui.menuitem(team_shaolin.label, value=team_shaolin),
                  ui.menuitem(team_wudang.label, value=team_wudang),
                  ui.menuitem(team_gaibang.label, value=team_gaibang),
                  ui.menuitem(team_emei.label, value=team_emei),
                  ui.menuitem(team_youminggong.label, value=team_youminggong),
                  ui.menuitem(team_juquemen.label, value=team_juquemen),
                  ui.menuitem(team_beichenpai.label, value=team_beichenpai),
                  ui.menuitem(team_jiuxipai.label, value=team_jiuxipai),], title="请选择参战的阵营：",
                  multiple=True, multiple_range=[2, 2])

    team_a = ac[0]
    team_b = ac[1]

    context.teams[team_a.id] = team_a
    context.teams[team_b.id] = team_b
    
    ac = ui.menu([ui.menuitem(team_a.label, value=team_a.leader),
                  ui.menuitem(team_b.label, value=team_b.leader),
                  ui.menuitem("观战而已", value=None)], title="请选择你想控制的阵营：")

    if ac == "观战而已":
        context.PLAYER = None
    else:
        context.PLAYER = ac

    ac = ui.menu([ui.menuitem(m6.name, value=m6),
                  ui.menuitem(m4.name, value=m4),
                  ui.menuitem(m1.name, value=m1),
                  ui.menuitem(m2.name, value=m2),
                  #ui.menuitem(m3.name, value=m3),
                  ui.menuitem(m5.name, value=m5)], title="请选择测试用的地图：")

    BattleStartAction(map=ac, groups=[team_a.members, team_b.members]).do()
   
    engine.start()
