# -- coding: utf-8 --

import platform

from proj.runtime import context

from proj.entity import BattleEvent
from proj.entity.map import Shape

from proj.console import ui
from proj.console import format as fmt
from proj.console.orders import BattlePlayerOrder
from proj.console.orders import BattleMovePositionOrder
from proj.console.orders import BattleSkillChooseOrder
from proj.console.orders import BattleItemChooseOrder
from proj.console.orders import BattlePersonChooseOrder
from proj.console.orders import BattleRestOrder
from proj.console.orders import BattleResetOrder

from proj.console.handlers.person import profile


def battle_menu(battle=None):
    if battle is None:
        battle = context.PLAYER.battle
    ret = [ui.menuitem("移动", goto=lambda x: BattleMovePositionOrder(), validator=lambda x: not battle.moved[battle.current.id]),
           ui.menuitem("攻击", goto=lambda x: BattleSkillChooseOrder(), validator=lambda x: not battle.attacked[battle.current.id]),
           ui.menuitem("物品", goto=lambda x: BattleItemChooseOrder(), validator=lambda x: not battle.itemed[battle.current.id]),
           ui.menuitem("状态", goto=lambda x: BattlePersonChooseOrder()),
           #ui.menuitem("日志", validator=lambda x: False),
           ui.menuitem("休息", goto=lambda x: BattleRestOrder()),
           ui.menuitem("撤销", goto=lambda x: BattleResetOrder(), validator=lambda x: battle.reset)]
    return ret


def item_menu(battle=None):
    if battle is None:
        battle = context.PLAYER.battle
    smenu = []
    for itm in battle.current.items:
        if itm in battle.current.equipment:
            continue
        mitem = ui.menuitem(ui.rank(itm) + "（剩余：%s）" % battle.current.quantities[itm.tpl_id], value=itm)
        smenu.append(mitem)
    return smenu
    

def skill_menu(battle=None):
    if battle is None:
        battle = context.PLAYER.battle
    smenu = []
    skill_ava = battle.skill_available(battle.current)
    for itm in battle.current.skills:
        zcd = battle.skill_cd(battle.current, itm)
        if zcd > 0:
            mitem = ui.menuitem("%s：%s（还需等待%s回合）" % \
                                (itm.belongs.name, itm.name, zcd), validator=lambda x: False, value=itm)
        elif itm in skill_ava:
            comments = [ui.skill(itm)]
            skill_str = "%s：%s" % (ui.rank(itm.belongs), ui.rank(itm))
            for effe in itm.effects:
                comments.append(ui.effect(effe))
            mitem = ui.menuitem(skill_str, comments=comments, value=itm)
        else:
            mitem = ui.menuitem("%s：%s" % (itm.belongs.name, itm.name) + \
                                "〈你未装备合适的武器〉", validator=lambda x: False, value=itm)
        smenu.append(mitem)
    return smenu


def person_menu(battle=None):
    if battle is None:
        battle = context.PLAYER.battle
    pmenu = []
    for p in battle.all:
        if p in battle.dead:
            pitem = ui.menuitem("%s（已退场）" % p.name, validator=lambda x: False, value=p)
        else:
            pitem = ui.menuitem(p.name, value=p, goto=lambda x: profile(x))
        pmenu.append(pitem)
    return pmenu


def target_word(zhaoshi):
    if zhaoshi.shape.style == Shape.Point:
        return "目标"
    elif zhaoshi.shape.style in [Shape.BigSector, Shape.SmallSector]:
        return "起始方向"
    elif zhaoshi.shape.style == Shape.Line:
        return "方向"
    else:
        return "格子"


def validate_position(pos, valid_pos, can_on_person, battle=None):
    if battle is None:
        battle = context.PLAYER.battle
    x, y = pos.split()
    x = int(x)
    y = int(y)
    real_pos = battle.map.point_to_real((x, y))
    #if not can_on_person and real_pos in battle.map.loc_entity:
    #    return None
    if real_pos not in valid_pos:
        return None
    return real_pos
    

def battle_person_handler(snapshot, show_events=False):

    retlist = []

    for p in snapshot.values():
        if not p["visible"]:
            continue
        ret = {"location": None,
               "contents": [None, None, None],
               "trace": None}
        ret["location"] = p["location"]

        # 处理标题文本
        #if "current" in p and platform.system() == "Linux":
        if "current" in p:
            ret["contents"][0] = ui.colored(p["name"], 
                                            color="grey",
                                            on_color="on_%s" % ui.GROUP_COLOR[p["group"]])
        #elif "current" in p:
        #    ret["contents"][0] = ui.colored(p["name"], 
        #                                    on_color="on_%s" % ui.GROUP_COLOR[p["group"]], 
        #                                    attrs=["bold"])
        else:
            ret["contents"][0] = ui.colored(p["name"], 
                                            color=ui.GROUP_COLOR[p["group"]], 
                                            attrs=["bold"])
        ret["contents"][0] += fmt.vaka["direction"][str(p["direction"])] 

        # 处理HP文本
        if BattleEvent.HPChanged in p["events"]:
            hp_delta = p["events"][BattleEvent.HPChanged]["value"]
        else:
            hp_delta = 0
        if not show_events and hp_delta != 0:
            qcolor = "green" if p["poison_hp"] > 0 else None
            ret["contents"][1] = "%s：%s" % (fmt.aka["hp"], ui.colored(str(p["hp"] - hp_delta), color=qcolor))
            #ret["contents"][1] = str(p["hp"] - hp_delta)
        else:
            qcolor = "green" if p["poison_hp"] > 0 else None
            ret["contents"][1] = "%s：%s" % (fmt.aka["hp"], ui.colored(str(p["hp"]), color=qcolor))
            #ret["contents"][1] = str(p["hp"])
        if show_events and hp_delta != 0:
            qcolor = "red" if hp_delta < 0 else "green"
            showstr = hp_delta if hp_delta < 0 else "+%s" % hp_delta
            ret["contents"][1] += ui.colored("(%s)" % showstr, color=qcolor, attrs=["bold"])
        elif show_events and BattleEvent.ACTMissed in p["events"]:
            ret["contents"][1] += ui.colored("(miss)", color="yellow", attrs=["bold"])
        else:
            qcolor = "red" if p["injury"] > 0 else None
            ret["contents"][1] += "/" + ui.colored(str(p["hp_limit"]), color=qcolor)

        # 处理MP文本
        if BattleEvent.MPChanged in p["events"]:
            mp_delta = p["events"][BattleEvent.MPChanged]["value"]
        else:
            mp_delta = 0
        if not show_events and mp_delta != 0:
            ncolor = "green" if p["poison_mp"] > 0 else None
            ret["contents"][2] = "%s：%s" % (fmt.aka["mp"], ui.colored(str(p["mp"] - mp_delta), color=ncolor))
            #ret["contents"][2] = str(p["mp"] + mp_delta)
        else:
            ncolor = "green" if p["poison_mp"] > 0 else None
            ret["contents"][2] = "%s：%s" % (fmt.aka["mp"], ui.colored(str(p["mp"]), color=ncolor))
            #ret["contents"][2] = str(p["mp"])
        if show_events and mp_delta != 0:
            showstr = mp_delta if mp_delta < 0 else "+%s" % mp_delta
            ret["contents"][2] += ui.colored("(%s)" % showstr, color="blue", attrs=["bold"])
        else:
            ncolor = "red" if p["wound"] > 0 else None
            ret["contents"][2] += "/" + ui.colored(str(p["mp_limit"]), color=ncolor)

        # 处理路径
        if BattleEvent.PositionMoved in p["events"]:
            ret["trace"] = p["events"][BattleEvent.PositionMoved]["trace"]
        retlist.append(ret)
    return retlist


def handler_battle_start(ctx):
    map = ctx.battle.map
    if not ui.blankline():
        ui.echo()
    ui.warn("战斗开始！")
    ui.echo()
    ui.read("（回车继续）")
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_quit(ctx):
    ui.echo()
    ui.echo("%s退下了。" % ctx.subject.name)
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_map(ctx):
    map = ctx.battle.map
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons))
   

def handler_battle_finish_turn(ctx):
    map = ctx.battle.map
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_new_turn(ctx):
    map = ctx.battle.map
    map.window_center(ctx.persons[ctx.battle.current.id]["location"])
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons, show_events=True))
    ui.echo()
    ui.echo("轮到%s行动。" % ctx.subject.name)
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_player(ctx):
    map = ctx.battle.map
    if ctx.back:
        ui.echo()
        ui.map(map, entities=battle_person_handler(ctx.persons))
    ui.cleanmenu()
    ui.menu(battle_menu(), title="请选择%s的行动方针：" % ctx.battle.current.name, columns=2, width=15)


def handler_battle_move_position(ctx):
    map = ctx.battle.map 
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons), 
           coordinates=ctx.positions, coordinate_color="green")
    ui.echo()
    rt = ui.read("请输入你想要移动的格子坐标（绿色表示可移动格子，坐标用空格分隔，输入#back可返回）：",
                    handler=lambda x: validate_position(x, ctx.positions, False))
    ui.echo()
    return rt


def handler_battle_move_ensure(ctx):
    map = ctx.battle.map
    ui.echo()
    #ui.map(map, entities=ctx.persons, coordinates=ctx.trace, coordinate_color="blue")
    ui.map(map, entities=battle_person_handler(ctx.persons))
    ui.echo()
    rt = ui.sure("移动完成，是否确认")
    ui.echo()
    return rt


def handler_battle_move_start(ctx):
    pass


def handler_battle_move_finish(ctx):
    map = ctx.battle.map
    map.window_center(ctx.persons[ctx.battle.current.id]["location"])
    if not ctx.motivated or (not ctx.battle.controllable() and len(ctx.path) > 1):
        ui.echo()
        #ui.map(map, entities=ctx.persons, coordinates=ctx.path, coordinate_color="blue")
        ui.map(map, entities=battle_person_handler(ctx.persons, show_events=True))
        ui.echo()
        ui.echo("%s移动至%s。" % (ctx.subject.name, ctx.target))
        ui.echo()
        ui.read("（回车继续）")


def handler_battle_skill_choose(ctx):
    if ctx.back:
        rt = ui.backmenu()
    else:
        rt = ui.menu(skill_menu(), title="请选择你要使用的招式：", goback=True,
                     backmethod=lambda: BattlePlayerOrder(battle=ctx.battle, back=True))
    return rt


def handler_battle_skill_position(ctx):
    map = ctx.battle.map
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons), 
           coordinates=ctx.positions, coordinate_color="green", show_trace=False)
    ui.echo()
    ret = ui.read("请输入你想要作用的%s（绿色表示可指定的%s，坐标用空格分隔，输入#back可返回）：" % \
                    (target_word(ctx.skill), target_word(ctx.skill)),
                    handler=lambda x: validate_position(x, ctx.positions, True))
    ui.echo()
    return ret


def handler_battle_skill_ensure(ctx):
    map = ctx.battle.map
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons), 
           coordinates=ctx.scope, coordinate_color="yellow", show_trace=False)
    ui.echo()
    rt = ui.sure("黄色为作用范围，是否确认")
    return rt


def handler_battle_skill_start(ctx):
    map = ctx.battle.map
    if ctx.counter:
        ui.echo()
        ui.echo("%s发动反击！" % ctx.subject.name)
        ui.echo()
        ui.read("（回车继续）")
    if ctx.battle.current != ctx.subject or not ctx.battle.controllable():
        ui.echo()
        ui.echo("%s使出" % ctx.subject.name + ui.rank(ctx.skill.belongs, txt="【%s】" % ctx.skill.belongs.name) + \
                "中的一式" + ui.rank(ctx.skill, txt="【%s】" % ctx.skill.name))
        ui.echo()
        if not ctx.counter and ctx.battle.current != ctx.subject:
            ui.read("（回车继续）")
        ui.map(map, entities=battle_person_handler(ctx.persons), 
               coordinates=ctx.scope, coordinate_color="yellow", show_trace=False)
        #ui.echo()
        #ui.echo("%s使出" % ctx.subject.name + ui.rank(ctx.skill.belongs, txt="【%s】" % ctx.skill.belongs.name) + \
        #        "中的一式" + ui.rank(ctx.skill, txt="【%s】" % ctx.skill.name))
        ui.echo()
        ui.read("（回车继续）")


def handler_battle_skill_finish(ctx):
    map = ctx.battle.map
    if len(ctx.objects) == 0:
        ui.echo()
        ui.echo("攻击范围内无目标！")
        ui.read()
    elif ctx.critical:
        if not ui.blankline():
            ui.echo()
        criticaltxt = ctx.subject.criticaltxt
        if criticaltxt is None:
            criticaltxt = "接我这招！"
        ui.echo(ui.colored("%s：%s" % (ctx.subject.name, criticaltxt), color="yellow", attrs=["bold"]))
        ui.read()
    for obj in ctx.anti_list:
        if not ui.blankline():
            ui.echo()
        antitxt = "可惜，这一招已经被我看破了！"
        ui.echo(ui.colored("%s：%s" % (obj.name, antitxt), color="yellow", attrs=["bold"]))
        ui.read()
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_item_choose(ctx):
    if ctx.back:
        rt = ui.backmenu()
    else:
        rt = ui.menu(item_menu(), title="请选择你要使用的物品：", goback=True,
                     backmethod=lambda: BattlePlayerOrder(battle=ctx.battle, back=True))
    return rt


def handler_battle_item_start(ctx):
    map = ctx.battle.map
    if ctx.battle.current != ctx.subject or not ctx.battle.controllable():
        ui.echo()
        ui.map(map, entities=battle_person_handler(ctx.persons), 
               coordinates=ctx.scope, coordinate_color="yellow", show_trace=False)
        ui.echo()     
        fstr = "%s使用了物品" % ctx.subject.name
        ui.echo(fstr + ui.colored(ui.rank(ctx.item, txt="【%s】" % ctx.item.name)))
        ui.echo()
        ui.read("（回车继续）")


def handler_battle_item_finish(ctx):
    map = ctx.battle.map
    if len(ctx.objects) == 0:
        ui.echo()
        ui.echo("使用范围内无目标！")
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_person_choose(ctx):
    ui.menu(person_menu(), title="请选择你要查看的角色：", goback=True, 
            backmethod=lambda: BattlePlayerOrder(battle=ctx.battle, back=True))

def handler_battle_rest_start(ctx):
    pass


def handler_battle_rest_finish(ctx):
    map = ctx.battle.map
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctx.persons, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_effect(ctx):
    if ctx.effect.name is None:
        return
    effe_details = ctx.details
    if effe_details is None:
        effe_details = {}
    for k, v in effe_details.items():
        if "%s_rank" % k in effe_details:
            e_rank = effe_details["%s_rank" % k]
            effe_details[k] = ui.colored("【%s】" % v, color=ui.rankcolor(e_rank), attrs=["bold"])
    if not ui.blankline():
        ui.echo()
    ui.echo("%s发动了" % ctx.subject.name + \
            ui.effectname(ctx.effect, txt="【%s】" % ctx.effect.name) + "效果，%s。" % \
            ctx.effect.text.format(**effe_details))
    ui.read()
            
            
def handler_battle_finish(ctx):
    ui.echo()
    result = "胜利" if ctx.result else "失败"
    ui.warn("战斗%s！" % result)
    ui.echo()
    for p, exp in ctx.explist:
        ui.echo("%s获得了%s点经验。" % (p.name, exp))
        ui.echo()
    for p, node in ctx.nodelist:
        ui.echo("%s已经习得了技能%s：%s。" % (p.name, ui.rank(node.belongs), ui.rank(node)))
        ui.echo()
    for p, item, quantity in ctx.itemlist:
        ui.echo("%s获得了%s×%s。" % (p.name, ui.rank(item), quantity))
        ui.echo()
    ui.read("（回车继续）")


def handler_battle_finish_silent(ctx):
    if not ui.blankline():
        ui.echo()
    ui.warn("传闻：在一场对决中，%s被%s击败了。" % (ctx.loser.leader.name, ctx.winner.leader.name))
    ui.read()
