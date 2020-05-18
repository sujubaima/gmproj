# -- coding: utf-8 --
from proj.console import control as inter

from proj.runtime import context

menuitem = inter.MenuItem

dg = [("小李", "谁来了？"),
      ("小王（在门外）", "快开门！"),
      ("小李", "快去给人开门。"),
      ("你", [menuitem("开门"),
              menuitem("不开门")])]

borns = ["成都",
         "苏州",
         "杭州",
         "北京",
         "吉州",
         "泉州",
         "洛阳",
         "大同"]

born_menu = [menuitem(itm) for itm in borns]

def start():
    loc = inter.menu(born_menu, title="请选择你的出身地：")
    context.LOCACTION = loc
    inter.dialog(dg)
