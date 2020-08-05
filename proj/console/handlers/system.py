# -- coding: utf-8 --

import os
import sys

from proj import options

from proj.console import ui
from proj.console.handlers.common import team_info


def system_menu(ctrl):
    smenu = [ui.menuitem("事件", goto=ctrl.showevents),
             ui.menuitem("成就", validator=lambda x: False),
             ui.menuitem("存档", goto=ctrl.savefile),
             ui.menuitem("载入", goto=ctrl.loadfile),
             ui.menuitem("退出", goto=ctrl.exit)]
    return smenu


def task_menu(ctrl):
    tmenu = []
    for t, status in ctrl.tasks:
        tmenu.append(ui.menuitem(t, value=t, bold=status, goto=ctrl.select))
    return tmenu


def handler_system_control(ctrl):
    ui.menu(system_menu(ctrl), columns=2, width=15,
            goback=True, backmethod=ctrl.close)


def handler_event_select_control(ctrl):
    ui.menu(task_menu(), title="请选择查看的事件：", goback=True, backmethod=ctrl.close)


def handler_event_detail_control(ctrl):
    context.tasks_status[ctrl.task] = False
    ui.menu([], title="事件：%s" % ctrl.task, inpanel=ctrl.tasktxt, 
            shownone=False, goback=True, backmethod=ctrl.close)


def handler_file_select_control(ctrl):
    load_menu = []
    if ctrl.allow_new:
        load_menu.append(ui.menuitem("新建存档", value="/"))
    loaddir = options.SAVEFILE_PATH
    for itm in os.listdir(loaddir):
        apath = loaddir + "/" + itm
        if not apath.endswith(".savefile"):
            continue
        mtime = os.stat(apath).st_mtime
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        showword = "%s (%s)" % (itm, mtime)
        load_menu.append(ui.menuitem(showword, value=apath))
    ret = ui.menu(load_menu, title="当前可用存档：", goback=True, backmethod=ctrl.close)
    if ret == "/":
        ui.echo()
        ret = ui.read("请输入新建的存档名称：")
        loaddir = options.SAVEFILE_PATH
        ret = loaddir + "/" + ret + ".savefile"
    ctrl.select(ret)
