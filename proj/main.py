# -- coding: utf-8 --
import os
import sys
import time
import importlib

import locale
locale.setlocale(locale.LC_ALL, '')

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../"))

from proj import options
from proj.core import person

from proj.console import message as msg
from proj.console import control as inter
from proj.console import format as fmt
from proj.console import scr

from proj import runtime
from proj.runtime import context

from proj import modules


menuitem = inter.MenuItem


def newstart(arg):
    inter.menu([menuitem("创建新人物", goto=create_role),
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
    inter.menu(main_menu, title=main_title(), title_color="red")


def create_role(args):
    xing = inter.read("请输入你的姓氏：", 
                      handler=lambda x: x if len(x.strip()) > 0 else None)
    inter.echo()
    ming = inter.read("请输入你的名字：", 
                      handler=lambda x: x if len(x.strip()) > 0 else None)
    inter.echo()
    sex = inter.menu(sex_menu, title="请选择你的性别：")
    while True:
        lead = person.create_player(xing, ming, sex)
        inter.echo("你的初始属性如下")
        inter.echo()
        inter.echo(fmt.people(lead, about="attrs"))
        inter.echo()
        if inter.sure(msg.ACCEPT):
            break
    context.PLAYER = lead
    inter.echo()
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
    inter.menu(mod_menu, title="当前可用模组：", goback=True)

def load_file(f):
    pass

def show_files(arg):
    load_menu = []
    loaddir = "%s/../savefiles" % os.path.dirname(os.path.abspath(__file__))
    for itm in os.listdir(loaddir):
        apath = loaddir + "/" + itm
        if not apath.endswith(".savefile"):
            continue
        mtime = os.stat(apath).st_mtime
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        showword = "%s (%s)" % (itm, mtime)
        load_menu.append(menuitem(showword, value=itm, goto=lambda x: load_file(x)))
    inter.menu(load_menu, title="当前可用存档：", goback=True)

def show_wikis(arg):
    runtime.MODULE.wikis.run()


main_menu = [menuitem("重新开始", goto=newstart),
             menuitem("读取存档", goto=show_files),
             menuitem("加载模组", goto=show_mods),
             menuitem("游戏百科", goto=show_wikis),
             menuitem("算了，还是专心工作吧", goto=lambda x: sys.exit(0))]

sex_menu = [menuitem("男"),
            menuitem("女")]

load_menu = []


def main_title():
    if len(runtime.MODULE.info.MOD_SHOW_NAME) > 0:
        return "《摸鱼群侠传：%s》" % runtime.MODULE.info.MOD_SHOW_NAME
    else:
        return "《摸鱼群侠传》"

def main(stdscr=None):
    if stdscr is not None:
        scr.stdscr = stdscr
    load_mod()
    inter.echo()
    inter.echo("欢迎体验简易粗糙无界面的上班开会摸鱼专用游戏！")
    inter.echo()
    inter.menu(main_menu, title=main_title(), title_color="red")

if __name__ == "__main__":
   #if options.USE_CURSES:
   #    from proj.console import scr
   #    scr.wrapper(main)
   #else:
   main()
   
