# -- coding: utf-8 --

from proj.engine import Message as MSG
from proj.engine import Action
from proj.engine import Control

from proj.entity.map import Shape
from proj.entity import SkillType

from proj.builtin.actions import BattleFinishAction
from proj.builtin.actions import BattleNewTurnAction
from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction
from proj.builtin.actions import BattleItemAction
from proj.builtin.actions import BattleRestAction 
from proj.builtin.actions import GameFailAction

from proj.console.controls.common import PipeControl
from proj.console.controls.common import SkillSelectControl
from proj.console.controls.common import ItemSelectControl
from proj.console.controls.common import PositionSelectControl
from proj.console.controls.common import PersonSelectControl
from proj.console.controls.common import PersonStatusControl

from proj.runtime import context


class BattleMapControl(Control):

    def run(self):
        self.launch()

    def launch(self):
        MSG(style=MSG.BattleMapControl, control=self)


class BattleControl(Control):
    """
    战斗系统根控件
    """
    def macros(self):
        macs = {}
        descs = {}
        macs["#sequence"] = self.showseq
        descs["#sequence"] = "显示当前时刻各角色行动顺序"
        return macs, descs

    def showseq(self, tag):
        pset = set()
        pmap = {}
        for p in self.battle.alive:
            pmap[p.id] = p.process
            pset.add(p.id)
        self.acseq = []
        while len(pset) != 0:
            min = (None, 1000) 
            for p in self.battle.alive:
                ctime = (1000 - pmap[p.id]) / p.speed
                if ctime < min[1]:
                    min = (p, ctime)
            for p in self.battle.alive:
                if p == min[0]:
                    pmap[p.id] = -1 * max(0, p.fatigue - 500)
                    if p.id in pset:
                        pset.remove(p.id)
                    self.acseq.append(p)
                else:
                    pmap[p.id] += int(min[1] * p.speed)
        MSG(style=MSG.BattleSequence, control=self)

    def run(self):
        if not self.battle.active():
            return 
        super(BattleControl, self).run()

    def launch(self):
        self.snapshot = self.battle.snapshot(False)
        MSG(style=MSG.BattleControl, control=self)

    @Control.listener
    def move(self, arg):
        position_text = "请输入要移动的地块坐标"
        p = self.battle.current
        allinscope, connections = self.battle.map.move_scope(p)
        validator=lambda x: PositionSelectControl.validator(self.battle.map, x, allinscope, False)
        control = BattlePositionSelectControl(battle=self.battle, subject=self.battle.current,
                      validator=validator, positions=allinscope, text=position_text)
        control.run()
        if control.target is not None:
            map = self.battle.map
            self.location = map.location(p)
            move_trace = map.move_trace(self.position, self.location, connections)
            BattleMoveAction(subject=p, battle=self.battle, target=control.target, 
                scope=allinscope, path=move_trace).do()
            self.battle.reset = True
        if self.battle.active():
            self.launch()
        else:
            self.close()

    @Control.listener
    def useskill(self, arg):
        control = PipeControl()
        control.pipe(BattleSkillSelectControl(battle=self.battle, person=self.battle.current), 
                     valves=["skill"])
        control.pipe(BattleSkillControl(battle=self.battle), valves=["target", "scope"])
        control.run()
        if control.target is not None and control.skill is not None:
            BattleSkillAction(skill=control.skill, battle=self.battle, subject=self.battle.current,
                target=control.target, scope=control.scope, type=SkillType.Normal).do()
        if self.battle.active():
            self.launch()
        else:
            self.close()

    @Control.listener
    def useitem(self, arg):
        control = PipeControl()
        control.pipe(ItemSelectControl(battle=self.battle, persons=[self.battle.current]), 
                     valves=["item"])
        control.pipe(ItemTargetSelectControl(battle=self.battle, subject=self.battle.current), 
                     valves=["target", "scope"])
        control.run()
        if control.target is not None and control.skill is not None:
            BattleItemAction(skill=control.skill, battle=self.battle, subject=self.battle.current,
                target=control.target, scope=control.scope).do()
        if self.battle.active():
            self.launch()
        else:
            self.close()

    @Control.listener
    def status(self, arg):
        person_title = "请选择要查看状态的人物："
        control = PipeControl()
        control.pipe(PersonSelectControl(candidates=self.battle.alive, 
                         title=person_title, canskip=False), valves=["person"])\
               .pipe(PersonStatusControl(), valves=["notexist"])
        control.run()
        if self.battle.active():
            self.launch()
        else:
            self.close()

    @Control.listener
    def rest(self, arg):
        BattleRestAction(subject=self.battle.current, battle=self.battle).do()
        if self.battle.active():
            self.launch()
        else:
            self.close()

    @Control.listener
    def reset(self, arg):
        self.battle.map.locate(self.battle.current, self.battle.current.tmpdict["original_position"])
        self.battle.current.direction = self.battle.current.tmpdict["original_direction"]
        self.battle.moved[self.battle.current.id] = False
        self.battle.reset = False
        if self.battle.active():
            self.launch()
        else:
            self.close()


class BattleNewTurnControl(Control):

    def run(self):
        BattleNewTurnAction(battle=self.battle).do()
        if self.battle.controllable():
            self.battle.current.tmpdict["original_position"] = self.battle.map.location(self.battle.current)
            self.battle.current.tmpdict["original_direction"] = self.battle.current.direction
            control = BattleControl(battle=self.battle)
            control.run()
        else:
            # 非可控制人员，转入AI模块生成action并执行
            self.ai_actions = self.battle.action(self.battle.current)
            for next_action in self.ai_actions:
                next_action.do()
        if self.battle.finished():
            BattleFinishAction(battle=self.battle).do()
            if not self.battle.silent:
                if not context.PLAYER.team.result and self.battle.death:
                    GameFailAction().do()
        MSG.sync()


class BattlePositionSelectControl(PositionSelectControl):

    def launch(self):
        self.snapshot = self.battle.snapshot(False)
        MSG(style=MSG.BattlePositionSelectControl, control=self)


class BattleSkillSelectControl(SkillSelectControl):

    def errmsg(self, skill):
        if self.skill_ava is None:
            self.skill_ava = self.battle.skill_available(self.person)
        skill_cd = self.battle.skill_cd(self.person, skill)
        if skill_cd > 0:
            return "还需等待%s回合" % skill_cd
        elif skill not in self.skill_ava:
            return "你未装备合适的武器"
        else:
            return None


class BattleSkillControl(Control):

    def run(self):
        control = SkillTargetSelectControl(battle=self.battle, skill=self.skill)
        control.run()
        self.target = control.target
        self.scope = control.scope


class SkillTargetSelectControl(Control):

    def launch(self):
        map = self.battle.map
        p = self.battle.current
        loc = map.location(p)
        if self.target is not None:
            self.scope = map.shape(map.location(p), self.target, self.skill.shape)
            MSG(style=MSG.BattleScopeControl, control=self)
        elif self.skill.shape.style == Shape.Around and self.skill.shape.block != 1:
            self.position = (-1, -1)
            self.scope = map.shape(map.location(p), self.position, self.skill.shape)
            MSG(style=MSG.BattleScopeControl, control=self)
        else:
            self.positions = map.shape_scope(loc, self.skill.shape)
            self.validator = lambda x: PositionSelectControl.validator(self.battle.map, x, self.positions, True)
            self.snapshot = self.battle.snapshot(False)
            MSG(style=MSG.BattlePositionSelectControl, control=self)

    @Control.listener
    def select(self, pos):
        self.target = pos
        self.launch()

    @Control.listener
    def input(self, sure):
        if not sure:
            self.scope = None
        self.close()


ItemTargetSelectControl = SkillTargetSelectControl

BattleItemControl = BattleSkillControl
