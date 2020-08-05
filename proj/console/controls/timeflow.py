# -- coding: utf-8 --

from proj import engine
from proj.engine import Message as MSG
from proj.engine import Control

from proj.console.controls import ScenarioControl
from proj.console.controls import ScenarioChangeControl
from proj.console.controls import BattleNewTurnControl

from proj.builtin.actions import WorldProcessAction

from proj.runtime import context

class TimeflowControl(Control):

    def run(self):
        while engine.running:
            if context.PLAYER is None:
                team = None
            else:
                team = context.PLAYER.team
            # 处理进行中的战斗
            for battle in list(context.battles.values()):
                BattleNewTurnControl(battle=battle).run()
            # 处理其他行动
            WorldProcessAction().do()
            if team is None:
                continue
            # 处理场景变换
            elif len(team.path) > 0 and team.next == team.path[0] and \
                 team.location in team.scenario.transport_locs:
                ScenarioChangeControl(team=team).run()
            # 处理路径阻断
            if team.clashed:
                team.clashed = False
                MSG(style=MSG.WorldClash, subject=team, map=team.scenario)
            if context.timestamp_ == context.timestamp and context.PLAYER is not None:
                ScenarioControl(team=team, scenario=team.scenario).run()
