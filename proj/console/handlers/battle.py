# -- coding: utf-8 --

import platform

from proj.runtime import context

from proj.entity import BattleEvent
from proj.entity import SkillType
from proj.entity.map import Shape

from proj.console import ui
from proj.console import format as fmt

from proj.console.handlers.person import profile


def battle_menu(ctrl):
    battle = ctrl.battle
    ret = [ui.menuitem("移动", goto=ctrl.move, validator=lambda x: not battle.moved[battle.current.id]),
           ui.menuitem("攻击", goto=ctrl.useskill, validator=lambda x: not battle.attacked[battle.current.id]),
           ui.menuitem("物品", goto=ctrl.useitem, validator=lambda x: not battle.itemed[battle.current.id]),
           ui.menuitem("状态", goto=ctrl.status),
           ui.menuitem("休息", goto=ctrl.rest, validator=lambda x: not battle.rested[battle.current.id]),
           ui.menuitem("撤销", goto=ctrl.reset, validator=lambda x: battle.reset)]
    return ret


def target_word(zhaoshi):
    if zhaoshi.shape.style == Shape.Point:
        return "目标"
    elif zhaoshi.shape.style in [Shape.BigSector, Shape.SmallSector]:
        return "起始方向"
    elif zhaoshi.shape.style == Shape.Line:
        return "方向"
    else:
        return "格子"


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


def handler_battle_start(ac):
    map = ac.battle.map
    if not ui.blankline():
        ui.echo()
    ui.warn("战斗开始！")
    ui.echo()
    ui.read("（回车继续）")
    ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_quit(ac):
    ui.echo()
    ui.echo("%s退下了。" % ac.subject.name)
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_map(ac):
    map = ac.battle.map
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot))
   

def handler_battle_finish_turn(ac):
    map = ac.battle.map
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_new_turn(ac):
    map = ac.battle.map
    map.window_center(ac.snapshot[ac.battle.current.id]["location"])
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot, show_events=True))
    ui.echo()
    ui.echo("轮到%s行动。" % ac.battle.current.name)
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_player(ac):
    map = ac.battle.map
    if ac.back:
        ui.echo()
        ui.map(map, entities=battle_person_handler(ac.snapshot))
    ui.cleanmenu()
    ui.menu(battle_menu(), title="请选择%s的行动方针：" % ac.battle.current.name, columns=2, width=15)


def handler_battle_move(ac):
    map = ac.battle.map
    map.window_center(ac.snapshot[ac.battle.current.id]["location"])
    if not ac.motivated or (not ac.battle.controllable() and len(ac.path) > 1):
        ui.echo()
        ui.map(map, entities=battle_person_handler(ac.snapshot, show_events=True))
        ui.echo()
        ui.echo("%s移动至%s。" % (ac.subject.name, ac.target))
        ui.echo()
        ui.read("（回车继续）")


def handler_battle_skill_scope(ac):
    map = ac.battle.map
    if ac.type == SkillType.Counter:
        ui.echo()
        ui.echo("%s发动反击！" % ac.subject.name)
        ui.echo()
        ui.read("（回车继续）")
    if ac.battle.current != ac.subject or not ac.battle.controllable():
        ui.echo()
        ui.echo("%s使出" % ac.subject.name + ui.rank(ac.skill.belongs, txt="【%s】" % ac.skill.belongs.name) + \
                "中的一式" + ui.rank(ac.skill, txt="【%s】" % ac.skill.name))
        ui.echo()
        if ac.type != SkillType.Counter and ac.battle.current != ac.subject:
            ui.read("（回车继续）")
        ui.map(map, entities=battle_person_handler(ac.snapshot), 
               coordinates=[{"positions": ac.scope, "color": "yellow"}], show_trace=False)
        #ui.echo()
        #ui.echo("%s使出" % ac.subject.name + ui.rank(ac.skill.belongs, txt="【%s】" % ac.skill.belongs.name) + \
        #        "中的一式" + ui.rank(ac.skill, txt="【%s】" % ac.skill.name))
        ui.echo()
        ui.read("（回车继续）")


def handler_battle_skill(ac):
    map = ac.battle.map
    if len(ac.objects) == 0:
        ui.echo()
        ui.echo("攻击范围内无目标！")
        ui.read()
    elif ac.critical:
        if not ui.blankline():
            ui.echo()
        criticaltxt = ac.subject.criticaltxt
        if criticaltxt is None:
            criticaltxt = "接我这招！"
        ui.echo(ui.colored("%s：%s" % (ac.subject.name, criticaltxt), color="yellow", attrs=["bold"]))
        ui.read()
    for obj in ac.anti_list:
        if not ui.blankline():
            ui.echo()
        antitxt = "可惜，这一招已经被我看破了！"
        ui.echo(ui.colored("%s：%s" % (obj.name, antitxt), color="yellow", attrs=["bold"]))
        ui.read()
    ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_item_scope(ac):
    map = ac.battle.map
    if ac.battle.current != ac.subject or not ac.battle.controllable():
        ui.echo()
        ui.map(map, entities=battle_person_handler(ac.snapshot), 
               coordinates=[{"positions": ac.scope, "color": "yellow"}], show_trace=False)
        ui.echo()     
        fstr = "%s使用了物品" % ac.subject.name
        ui.echo(fstr + ui.colored(ui.rank(ac.item, txt="【%s】" % ac.item.name)))
        ui.echo()
        ui.read("（回车继续）")


def handler_battle_item(ac):
    map = ac.battle.map
    if len(ac.objects) == 0:
        ui.echo()
        ui.echo("使用范围内无目标！")
    ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_battle_rest(ac):
    map = ac.battle.map
    ui.echo()
    ui.map(map, entities=battle_person_handler(ac.snapshot, show_events=True))
    ui.echo()
    ui.read("（回车继续）")


def handler_effect(ac):
    if ac.effect.name is None:
        return
    effe_details = ac.details
    if effe_details is None:
        effe_details = {}
    for k, v in effe_details.items():
        if "%s_rank" % k in effe_details:
            e_rank = effe_details["%s_rank" % k]
            effe_details[k] = ui.colored("【%s】" % v, color=ui.rankcolor(e_rank), attrs=["bold"])
    if not ui.blankline():
        ui.echo()
    ui.echo("%s发动了" % ac.subject.name + \
            ui.effectname(ac.effect, txt="【%s】" % ac.effect.name) + "效果，%s。" % \
            ac.effect.text.format(**effe_details))
    ui.read()
            
            
def handler_battle_finish(ac):
    ui.echo()
    result = "胜利" if ac.result else "失败"
    ui.warn("战斗%s！" % result)
    ui.echo()
    for p, exp in ac.explist:
        ui.echo("%s获得了%s点经验。" % (p.name, exp))
        ui.echo()
    for p, node in ac.nodelist:
        ui.echo("%s已经习得了技能%s：%s。" % (p.name, ui.rank(node.belongs), ui.rank(node)))
        ui.echo()
    for p, item, quantity in ac.itemlist:
        ui.echo("%s获得了%s×%s。" % (p.name, ui.rank(item), quantity))
        ui.echo()
    ui.read("（回车继续）")


def handler_battle_finish_silent(ac):
    if not ui.blankline():
        ui.echo()
    ui.warn("传闻：在一场对决中，%s被%s击败了。" % (ac.teamloser.leader.name, ac.teamwinner.leader.name))
    ui.read()


def handler_battle_map_control(ctrl):
    map = ctrl.battle.map
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ctrl.snapshot))


def handler_battle_control(ctrl):
    map = ctrl.battle.map
    if not ui.blankline():
        ui.echo()
    ui.map(map, entities=battle_person_handler(ctrl.snapshot))
    ui.cleanmenu()
    ui.menu(battle_menu(ctrl), title="请选择%s的行动方针：" % ctrl.battle.current.name, 
            macros=ctrl.macs, columns=2, width=15)
   

def handler_battle_pos_select_control(ctrl):
    map = ctrl.battle.map
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctrl.snapshot),
           coordinates=[{"positions": ctrl.positions, "color": "green"}], show_trace=False)
    ui.echo()
    rt = ui.read("%s（绿色表示可移动格子，坐标用空格分隔，输入#back可返回）：" % ctrl.text,
                 handler=ctrl.validator)
    ui.echo()
    if ctrl.ensure:
        surert = ui.sure(ctrl.ensure_text)
        if not surert:
            rt = None
    ctrl.select(rt)


def handler_battle_scope_control(ctrl):
    map = ctrl.battle.map
    ui.echo()
    ui.map(map, entities=battle_person_handler(ctrl.snapshot),
           coordinates=[{"positions": ctrl.scope, "color": "yellow"}], show_trace=False)
    ui.echo()
    rt = ui.sure("黄色为作用范围，是否确认")
    ctrl.input(rt)


def handler_battle_sequence(ctrl):
    if not ui.blankline():
        ui.echo()
    ret = []
    for p in [ctrl.battle.current] + ctrl.acseq:
        if ctrl.battle.is_friend(ctrl.battle.current, p):
            ret.append(ui.colored(p.name, color="cyan", attrs=["bold"]))
        else:
            ret.append(ui.colored(p.name, color="red", attrs=["bold"]))
    ui.echo("当前行动顺序如下：")
    ui.echo()
    ui.echo("->".join(ret))
    ui.echo()
    ui.read("（回车继续）")
    ctrl.launch()
