# -- coding: utf-8 --

from proj.console import ui

from proj.console.handlers.common import equipment


def equip_menu(ctrl):
    emenu = [ui.menuitem("主手卸下", value=0, goto=ctrl.equip_off),
             ui.menuitem("主手装上", value=(0, set(["Weapon"])), goto=ctrl.equip_on),
             ui.menuitem("副手卸下", value=1, goto=ctrl.equip_off),
             ui.menuitem("副手装上", value=(1, set(["Weapon"])), goto=ctrl.equip_on),
             ui.menuitem("身体卸下", value=2, goto=ctrl.equip_off),
             ui.menuitem("身体装上", value=(2, set(["Armor"])), goto=ctrl.equip_on),
             ui.menuitem("饰品卸下", value=3, goto=ctrl.equip_off),
             ui.menuitem("饰品装上", value=(3, set(["Ornament"])), goto=ctrl.equip_on)]
    return emenu


def handler_equip_control(ctrl):
    panel = ["",
             ui.byellow("装备一览：%s" % ctrl.person.name),
             ""]
    panel.extend(equipment(ctrl.person))
    ui.menu(equip_menu(ctrl), title="请选择你要进行的操作：",
            uppanel=panel, columns=2, width=19, goback=True, backmethod=ctrl.close)
