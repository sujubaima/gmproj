# -- coding: utf-8 --
import os
import sys
import time
import importlib

import locale
locale.setlocale(locale.LC_ALL, '')

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../"))

from proj import options
from proj.entity import Person

from proj.console import message as msg
from proj.console import ui
from proj.console import format as fmt

from proj import runtime
from proj.runtime import context
from proj.runtime import saveload

from proj import modules


menuitem = ui.menuitem


def newstart(arg):
    ui.menu([menuitem("创建新人物", goto=create_role),
             menuitem("扮演已有的人物")], validator=lambda x: x.showword == "创建新人物")

def load_mod():
    runtime.MODULE = importlib.import_module("proj.modules.%s" % modules.CURRENT)


def change_mod(new_mod):
    f = modules.__file__
    if f.endswith(".pyc"):
        f = f[:-1]
    with open(f, "w") as fd:
        fd.write("CURRENT = \"%s\"" % new_mod)
    modules.CURRENT = new_mod
    load_mod()
    ui.menu(main_menu, title=main_title(), title_color="red")


def person_info(p):
    pf = []
    pf.append("  " + "姓名：" + p.name)
    pf.append("")
    pf.append("  " + ui.fixed(18, n="灵动：" + ui.colored("%s%%" % (50 + p.dongjing))) + \
                     ui.fixed(18, n="沉静：" + ui.colored("%s%%" % (50 - p.dongjing))))
    pf.append("  " + ui.fixed(18, n="刚猛：" + ui.colored("%s%%" % (50 + p.gangrou))) + \
                     ui.fixed(18, n="柔易：" + ui.colored("%s%%" % (50 - p.gangrou))))
    pf.append("  " + ui.fixed(18, n="颖悟：" + ui.colored("%s%%" % (50 + p.zhipu))) + \
                     ui.fixed(18, n="朴拙：" + ui.colored("%s%%" % (50 - p.zhipu))))
    pf.append("")
    pf.append("  " + ui.fixed(18, n="内功阴性：" + ui.colored("%s%%" % (50 - p.yinyang), color="cyan")) + \
                     ui.fixed(18, n="内功阳性：" + ui.colored("%s%%" % (50 + p.yinyang), color="yellow")))
    pf.append("")
    pf.append("  " + ui.fixed(18, n="内功：%s" % p.neigong))
    pf.append("  " + ui.fixed(18, n="搏击：%s" % p.boji) + ui.fixed(15, n="剑法：%s" % p.jianfa))
    pf.append("  " + ui.fixed(18, n="刀法：%s" % p.daofa) + ui.fixed(15, n="长兵：%s" % p.changbing))
    pf.append("  " + ui.fixed(18, n="暗器：%s" % p.anqi) + ui.fixed(15, n="奇门：%s" % p.qimen))
    return pf


def create_role(args):
    #xing = ui.read("请输入你的姓氏：", 
    #               handler=lambda x: x if len(x.strip()) > 0 else None)
    #ui.echo()
    #ming = ui.read("请输入你的名字：", 
    #               handler=lambda x: x if len(x.strip()) > 0 else None)
    #ui.echo()
    #sex = ui.menu(sex_menu, title="请选择你的性别：")
    lead = Person.one("PERSON_PLAYER")
    while True:
        #lead = person.create_player(xing, ming, sex)
        lead.random()
        ui.echo()
        ui.echo(ui.colored("你的初始属性如下", attrs=["bold"]))
        ui.echo()
        ui.echo(person_info(lead))
        ui.echo()
        if ui.sure(msg.ACCEPT):
            break
    context.PLAYER = lead
    ui.echo()
    runtime.MODULE.scripts.start()


def show_mods(arg):
    mod_menu = []
    moddir = "%s/modules" % os.path.dirname(os.path.abspath(__file__))
    for itm in os.listdir(moddir):
        apath = moddir + "/" + itm
        if not os.path.isdir(apath):
            continue
        infopath = apath + "/info.py"
        if not os.path.exists(infopath):
            continue
        tinfo = importlib.import_module("proj.modules.%s.info" % itm)
        showword = "%s：%s" % (tinfo.MOD_SHOW_NAME if itm != "origin" else "原版",
                               tinfo.MOD_VERSION)
        if itm == "origin":
            mod_menu.insert(0, menuitem(showword, value=itm, goto=lambda x: change_mod(x)))
        else:
            mod_menu.append(menuitem(showword, value=itm, goto=lambda x: change_mod(x)))
    ui.menu(mod_menu, title="当前可用模组：", goback=True)

def load_file(f):
    runtime.MODULE.scripts.start()
    saveload.load(f)

def show_files(arg):
    load_menu = []
    loaddir = options.SAVEFILE_PATH
    for itm in os.listdir(loaddir):
        apath = loaddir + "/" + itm
        if not apath.endswith(".savefile"):
            continue
        mtime = os.stat(apath).st_mtime
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        showword = "%s (%s)" % (itm, mtime)
        load_menu.append(menuitem(showword, value=itm, goto=lambda x: load_file(x)))
    ui.menu(load_menu, title="当前可用存档：", goback=True)

def show_wikis(arg):
    runtime.MODULE.wikis.run()


main_menu = [menuitem("重新开始", goto=create_role),
             menuitem("读取存档", goto=show_files),
             menuitem("加载模组", validator=lambda x: False, goto=show_mods),
             menuitem("游戏百科", goto=show_wikis),
             menuitem("算了，还是专心工作吧", goto=lambda x: sys.exit(0))]

sex_menu = [menuitem("男"),
            menuitem("女")]

load_menu = []


def main_title():
    if len(runtime.MODULE.info.MOD_SHOW_NAME) > 0:
        title_str = "《摸鱼群侠传：%s》" % runtime.MODULE.info.MOD_SHOW_NAME
    else:
        title_str = "《摸鱼群侠传》"
    return ui.colored(title_str, color="red", attrs=["bold"])

def main(stdscr=None):
    if stdscr is not None:
        scr.stdscr = stdscr
    load_mod()
    ui.echo()
    ui.echo("欢迎体验简易粗糙无界面的上班开会摸鱼专用游戏！")
    ui.echo()
    ui.menu(main_menu, title=main_title())


if __name__ == "__main__":
   main()
   
