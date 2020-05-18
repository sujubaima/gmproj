# -- coding: utf-8 --

from proj.console.interaction import Colored

a = "是" + Colored("我", color="red") + "是"
print type(a)
