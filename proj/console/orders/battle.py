# -- coding: utf-8 --
import math

from proj.engine import Message as MSG
from proj.engine import Order
from proj.engine import Action

from proj.entity.map import Shape
from proj.entity import BattlePhase
from proj.entity import Person

from proj.builtin.actions import BattleStartAction
from proj.builtin.actions import BattleFinishAction
from proj.builtin.actions import BattleNewTurnAction
from proj.builtin.actions import BattleMoveAction
from proj.builtin.actions import BattleSkillAction
from proj.builtin.actions import BattleItemAction
from proj.builtin.actions import BattleRestAction 
from proj.builtin.actions import BattleAdditionalAction
from proj.builtin.actions import GameFailAction

#from proj.console.orders.world import WorldProcessOrder

from proj.runtime import context


class BattleOrder(Order):

    def initialize(self):
        if context.PLAYER is not None:
            self.battle = context.PLAYER.battle


class BattleStartOrder(BattleOrder):

    def carry(self):
        self.battle = BattleStartAction(map=self.map, groups=self.groups, allies=self.allies, silent=self.silent, death=self.death).do()
        BattleNewTurnOrder(battle=self.battle)

        
class BattleFinishOrder(BattleOrder):

    def carry(self):
        BattleFinishAction(battle=self.battle).do()
        if not self.battle.silent:
            if not context.PLAYER.team.result and self.battle.death:
                GameFailAction().do()


class BattlePlayerOrder(BattleOrder):

    def carry(self):
        if not self.battle.moved[self.battle.current.id] or \
           not self.battle.attacked[self.battle.current.id] or \
           not self.battle.itemed[self.battle.current.id]:
            MSG(style=MSG.BattlePlayer, battle=self.battle, subject=self.battle.current, back=self.back, persons=self.battle.snapshot(False))
        else:
            MSG(style=MSG.Halt)


class BattleNewTurnOrder(BattleOrder):

    def carry(self):
        if self.turncount is None:
            self.turncount = 1
        BattleNewTurnAction(battle=self.battle).do()
        if self.battle.controllable():
            self.battle.current.stash["original_position"] = self.battle.map.location(self.battle.current)
            self.battle.current.stash["original_direction"] = self.battle.current.direction
            BattlePlayerOrder(battle=self.battle)
        else:
            # 非可控制人员，转入AI模块生成action并执行
            self.ai_actions = self.battle.action(self.battle.current)
            #self.handle_next()
            BattleAIActionOrder(battle=self.battle, ai_actions=self.ai_actions, turncount=self.turncount)


class BattleAIActionOrder(BattleOrder):

    def carry(self):
        self.handle_next()

    def handle_next(self):
        try:
            self.next_action = next(self.ai_actions)
        except StopIteration as e:
            self.next_action = None
        if self.next_action is not None:
            self.next_action.do()
            MSG(style=MSG.Null).callback = self.callback
            #self.handle_next()
        else:
            #WorldProcessOrder()
            self.turncount -= 1
            BattleFinishTurnOrder()
            if self.turncount > 0:
                BattleNewTurnOrder(battle=self.battle, turncount=self.turncount)

    def callback(self, arg):
        self.handle_next()
        
        
class BattleFinishTurnOrder(BattleOrder):
    pass


class BattleMovePositionOrder(BattleOrder):
    """
    移动指令：选择移动位置
    """
    def carry(self):
        p = self.battle.current
        allinscope, connections = self.battle.map.move_scope(p, style=p.move_style)
        #if self.battle.attacked[p.id] or self.battle.itemed[p.id]:
        #    self.scope = allinscope + [self.battle.map.location(p)]
        #else:
        #    self.scope = allinscope
        self.scope = allinscope
        self.connections = connections
        MSG(style=MSG.BattleMovePosition, 
            battle=self.battle,
            persons=self.battle.snapshot(False),
            positions=self.scope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            BattleMoveEnsureOrder(battle=self.battle, position=pos, scope=self.scope, connections=self.connections)
        elif not self.hooked:
            BattlePlayerOrder(battle=self.battle)


class BattleMoveEnsureOrder(BattleOrder):
    """
    移动指令：确认移动位置
    """
    def carry(self):
        map = self.battle.map
        p = self.battle.current
        self.direction = p.direction
        self.location = map.location(p)
        move_trace = map.move_trace(self.position, self.location, self.connections)
        BattleMoveAction(subject=p, battle=self.battle, target=self.position, scope=self.scope, path=move_trace).do()
        #MSG(style=MSG.BattleMoveEnsure, 
        #    battle=self.battle, 
        #    persons=self.battle.snapshot(), 
        #    trace=move_trace).callback = self.callback
        self.battle.reset = True
        MSG(style=MSG.BattleMap, battle=self.battle, persons=self.battle.snapshot())
        BattlePlayerOrder(battle=self.battle)

    def callback(self, sure):
        if sure:
            MSG(style=MSG.BattleMap, battle=self.battle, persons=self.battle.snapshot(False))
            BattlePlayerOrder(battle=self.battle)
        else:
            map = self.battle.map
            p = self.battle.current
            map.locate(p, self.location)
            p.direction = self.direction
            self.battle.sequence.pop()
            BattleMovePositionOrder(battle=self.battle)


class BattleSkillChooseOrder(BattleOrder):
    """
    攻击指令：选择招式
    """
    def carry(self):
        MSG(style=MSG.BattleSkillChoose, battle=self.battle, back=self.back).callback = self.callback

    def callback(self, skill):
        if skill is not None:
            BattleSkillPositionOrder(battle=self.battle, skill=skill)


class BattleSkillPositionOrder(BattleOrder):
    """
    攻击指令：选择攻击位置
    """
    def carry(self):
        map = self.battle.map
        p = self.battle.current
        loc = map.location(p)
        if self.skill.shape.style == Shape.Around and self.skill.shape.block != 1:
            BattleSkillEnsureOrder(battle=self.battle, position=(-1, -1), skill=self.skill, isitem=self.isitem)
        elif self.back and self.isitem:
            BattleItemChooseOrder(battle=self.battle, back=self.back)
        elif self.back:
            BattleSkillChooseOrder(battle=self.battle, back=self.back)
        else:
            #allinscope = map.circle(loc, self.skill.shape.scope)
            allinscope = map.shape_scope(loc, self.skill.shape)
            MSG(style=MSG.BattleSkillPosition, battle=self.battle,
                persons=self.battle.snapshot(False),
                skill=self.skill, positions=allinscope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            BattleSkillEnsureOrder(battle=self.battle, position=pos, skill=self.skill, isitem=self.isitem)
        elif self.isitem:
            BattleItemChooseOrder(battle=self.battle, back=True)
        else:
            BattleSkillChooseOrder(battle=self.battle, back=True)


class BattleSkillEnsureOrder(BattleOrder):
    """
    攻击指令：确认攻击位置
    """
    def carry(self):
        map = self.battle.map
        p = self.battle.current
        self.scope = map.shape(map.location(p), self.position, self.skill.shape)
        MSG(style=MSG.BattleSkillEnsure, 
            battle=self.battle, 
            persons=self.battle.snapshot(False), 
            scope=self.scope).callback = self.callback

    def callback(self, sure):
        if sure:
            BattleSkillOrder(battle=self.battle, skill=self.skill, position=self.position, scope=self.scope, isitem=self.isitem)
        else:
            #BattleSkillPositionOrder(battle=self.battle, skill=self.skill, back=True, isitem=self.isitem)
            MSG(style=MSG.BattleMap, battle=self.battle, persons=self.battle.snapshot(False))
            BattlePlayerOrder(battle=self.battle)


class BattleSkillOrder(BattleOrder):
    """
    攻击指令，流程包括：选择招式->选择攻击位置->确认攻击位置->完成
    """
    
    def carry(self):
        if self.isitem:
            BattleItemAction(item=self.skill, battle=self.battle, subject=self.battle.current,
                             target=self.position, scope=self.scope).do()
        else:
            BattleSkillAction(skill=self.skill, battle=self.battle, subject=self.battle.current,
                              target=self.position, scope=self.scope, counter=False).do()
        if self.battle.moved[self.battle.current.id] and \
           self.battle.attacked[self.battle.current.id] and \
           self.battle.itemed[self.battle.current.id]:
            #BattleNewTurnOrder(battle=self.battle)
            #WorldProcessOrder()
            BattleFinishTurnOrder(battle=self.battle)
        else:
            BattlePlayerOrder(battle=self.battle)


class BattleItemChooseOrder(BattleOrder):

    def carry(self):
        MSG(style=MSG.BattleItemChoose, battle=self.battle, back=self.back).callback = self.callback

    def callback(self, item):
        if item is not None:
            BattleSkillPositionOrder(battle=self.battle, skill=item, isitem=True)
            
            
class BattlePersonChooseOrder(BattleOrder):

    def carry(self):
        MSG(style=MSG.BattlePersonChoose, battle=self.battle, back=self.back)


class BattleRestOrder(BattleOrder):
    """
    休息指令
    """
    def carry(self):
        BattleRestAction(subject=self.battle.current, battle=self.battle).do()
        BattleFinishTurnOrder(battle=self.battle)
        #BattleNewTurnOrder(battle=self.battle)
        #WorldProcessOrder()


class BattleResetOrder(BattleOrder):

    def carry(self):
        self.battle.map.locate(self.battle.current, self.battle.current.stash["original_position"])
        self.battle.current.direction = self.battle.current.stash["original_direction"]
        self.battle.moved[self.battle.current.id] = False
        self.battle.reset = False
        MSG(style=MSG.BattleMap, battle=self.battle, persons=self.battle.snapshot(False))
        BattlePlayerOrder(battle=self.battle)
