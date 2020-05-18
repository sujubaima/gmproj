# -- coding: utf-8 --
from proj.console import control as inter
from proj.console import interscene

from proj.runtime import context

from proj.modules.lite import dialogs

menuitem = inter.MenuItem

def start():
    inter.dialog(dialogs.START)
    interscene.scene()
