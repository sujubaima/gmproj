# -- coding: utf-8 --

import os

from proj.console import ui

menuitem = ui.menuitem

DOC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/docs"

def show_wiki(filepath):
    with open("%s/%s" % (DOC_PATH, filepath)) as fd:
        ui.text(fd.read())

wiki_menu = [menuitem("人物属性", goto=lambda x: show_wiki("person_attrs.txt")),
             menuitem("战斗系统"),
             menuitem("物品系统"),
             menuitem("门派系统"),
             menuitem("侠客系统")]

battle_menu = [menuitem("武学种类"),
               menuitem("套路与招式"),
               menuitem("攻击范围"),
               menuitem("阴阳武学"),
               menuitem("状态与效果")]

menpai_menu = [menuitem("武林门派"),
               menuitem("加入门派"),
               menuitem("门派设施"),
               menuitem("发展门派"),
               menuitem("分舵与附庸"),
               menuitem("门派外交")]


def run():
    ui.menu(wiki_menu, title="游戏百科", goback=True) 
