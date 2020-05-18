# -- coding: utf-8 --

import importlib

from proj.engine import Action
from proj.engine import Message as MSG
from proj.engine import Order

from proj.runtime import context


class ContextVariableAddAction(Action):

    def do(self):
        context.variables[self.key] = self.value


class ContextVariableRemoveAction(Action):

    def do(self):
        if self.key in context.variables:
            context.variables.pop(self.key)


class ContextPlayerChangeAction(Action):

    def do(self):
        if self.person.team.scenario is None:
            self.person.team.scenario = context.PLAYER.team.scenario
        self.person.dongjing = context.PLAYER.dongjing
        self.person.gangrou = context.PLAYER.gangrou
        self.person.zhipu = context.PLAYER.zhipu
        self.person.yinyang = context.PLAYER.yinyang
        self.person.neigong = context.PLAYER.neigong
        context.PLAYER = self.person


class OrderCancelAction(Action):

    def do(self):
        Order.Current.canceled = True


class OrderAction(Action):

    def do(self):
        orders = importlib.import_module("proj.console.orders")
        eval("orders.%s" % self.order)()
        
        
class GameFailAction(Action):

    def do(self):
        MSG(style=MSG.GameFail) 
