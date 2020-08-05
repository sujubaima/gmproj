# -- coding: utf-8 --

import importlib

from proj import data

from proj.engine import Action
from proj.engine import Message as MSG
from proj.engine import JsonScript

from proj.runtime import context


class ContextVariableAddAction(Action):

    def take(self):
        context.variables[self.key] = self.value


class ContextVariableRemoveAction(Action):

    def take(self):
        if self.key in context.variables:
            context.variables.pop(self.key)


class ContextPlayerChangeAction(Action):

    def take(self):
        if self.person.team.scenario is None:
            self.person.team.scenario = context.PLAYER.team.scenario
        self.person.dongjing = context.PLAYER.dongjing
        self.person.gangrou = context.PLAYER.gangrou
        self.person.zhipu = context.PLAYER.zhipu
        self.person.yinyang = context.PLAYER.yinyang
        self.person.neigong = context.PLAYER.neigong
        context.PLAYER = self.person


class PauseAction(Action):

    def initialize(self):
        super(PauseAction, self).initialize()
        self.timeflow = 1

    def take(self):
        context.timeflow(self.timeflow)
        MSG(style=MSG.Show, wait=True)


class ScriptAction(Action):

    def finish(self):
        super(ScriptAction, self).finish()
        self.script_id = self.script
        self.script = JsonScript(getattr(data.scripts, self.script))
        

class ScriptAddBranchAction(ScriptAction):
    """
    脚本增加分支选项
    """
    def take(self):
        if self.branch not in self.script.by_label(self.branch)["branches"]:
            if self.position is not None:
                self.script.by_label(self.branch)["branches"].insert(self.position, self.option)
            else:
                self.script.by_label(self.branch)["branches"].append(self.option)
        if self.script_id not in context.script_branches:
            context.script_branches[self.script_id] = {}
        context.script_branches[self.script_id][self.branch] = self.script.by_label(self.branch)["branches"]


class ScriptRemoveBranchAction(ScriptAction):
    """
    脚本删除分支选项
    """
    def take(self):
        for idx, b in enumerate(self.script.by_label(self.branch)["branches"]):
            if b["label"] == self.branch_label:
                remove_idx = idx
                break
        self.by_label(self.branch)["branches"].pop(remove_idx)
        if self.script_id not in context.script_branches:
            context.script_branches[self.script_id] = {}
        context.script_branches[self.script_id][self.branch] = self.script.by_label(self.branch)["branches"]


class ScriptChangeBranchAction(ScriptAction):
    """
    脚本修改分支选项
    """
    def take(self):
        self.script.by_label(self.branch)["branches"][self.position] = self.option
        if self.script_id not in context.script_branches:
            context.script_branches[self.script_id] = {}
        context.script_branches[self.script_id][self.branch] = self.script.by_label(self.branch)["branches"]
        
        
class GameFailAction(Action):

    def take(self):
        MSG(style=MSG.GameFail) 
