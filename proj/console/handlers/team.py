# -- coding: utf-8 --

from proj.console import ui


def team_menu(ctrl):
    ret = [ui.menuitem("状态", goto=ctrl.status),
           ui.menuitem("物品", goto=ctrl.item),
           ui.menuitem("技能", goto=ctrl.skill),
           ui.menuitem("装备", goto=ctrl.equip),
           ui.menuitem("配方", goto=ctrl.recipe),
           ui.menuitem("切磋", validator=lambda x: False),
           ui.menuitem("离队", validator=lambda x: False)]
    return ret


def usage_menu(ctrl):
    ret = [ui.menuitem("使用", value=0, validator=ctrl.validator,  goto=ctrl.select),
           ui.menuitem("给与", value=1, validator=ctrl.validator, goto=ctrl.select),
           ui.menuitem("丢弃", value=2, goto=ctrl.select)]
    return ret


def transport_menu(targets):
    tmenu = []
    tmenu.append(ui.menuitem("留在原处", value=""))
    for target in targets:
        tmenu.append(ui.menuitem("前往%s" % target["name"], value=(target["scenario"], target["location"])))
    return tmenu


def handler_team_control(ctrl):
    title = ui.byellow("当前队伍：%s队" % ctrl.team.leader.name)
    ui.menu(team_menu(ctrl), title=title, columns=2, width=15, goback=True, backmethod=ctrl.close)


def handler_transport_control(ctrl):
    ret = ui.menu(transport_menu(ctrl.targets))
    return ret


def handler_item_usage_control(ctrl):
    ret = ui.menu(usage_menu(ctrl), goback=True, backmethod=ctrl.close)
    return ret
