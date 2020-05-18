# -- coding: utf-8 --

from proj.runtime import context

from proj.console.scenario import SearchOrder
from proj.console import control as inter

menuitem = inter.MenuItem

def interact(arg):
    obj_menu = [menuitem("a")]
    inter.menu(obj_menu, title="请选择你要交互的对象：", pagesize=6, rollpages=True, goback=True)

bar_menu = [menuitem("队伍"),
            menuitem("背包", goto=lambda x: inter.menu(item_menu, title="请选择你要查看的物品种类", goback=True)),
            menuitem("武学"),
            menuitem("日志"),
            menuitem("百科"),
            menuitem("系统")]

caiji_menu = [menuitem("采药"),
              menuitem("挖矿"),
              menuitem("狩猎")]

scene_menu = [menuitem("互动", goto=interact),
              menuitem("事务", goto=lambda x: inter.menu(action_menu, title="请选择你要进行的事物：", goback=True)),
              menuitem("探索", goto=lambda x: SearchOrder(subject=context.PLAYER, scene=context.SCENARIO)),
              menuitem("移动")]

action_menu = [menuitem("采集", goto=lambda x: inter.menu(caiji_menu, title="请选择你要采集的类型：", goback=True)),
               menuitem("制造"),
               menuitem("建设"),
               menuitem("鉴赏"),
               menuitem("修炼")]

com_menu = [menuitem("交谈"),
            menuitem("出示"),
            menuitem("盗窃"),
            menuitem("攻击")]

item_menu = [menuitem("全部"),
             menuitem("装备"),
             menuitem("补给"),
             menuitem("秘籍"),
             menuitem("材料"),
             menuitem("其他")]


def scene(s=None):
    inter.menu(scene_menu, 
               title="当前场景：%s\n\n请选择你的行动：" % context.SCENARIO.name, 
               pagesize=10, rollpages=False, bars=bar_menu) 

