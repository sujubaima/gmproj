# -- coding: utf-8 --

import importlib
import random

from proj import options

from proj.engine import Action
from proj.engine import Message as MSG

from proj.entity import Map
from proj.entity import Item

from proj.builtin.actions.battle import BattleStartAction
from proj.builtin.actions.battle import BattleJoinAction
from proj.builtin.actions.team import TeamTransportAction

from proj.runtime import context

from proj.utils import ratio


class WorldProcessAction(Action):
    """
    非战斗地图即时制核心action
    控制时间流逝
    """
    refresh_path = False

    def initialize(self):
        self.battles = set()
        
    def update_scenario(self, team):       
        if team.location not in team.scenario.transport_locs:
            return
        orders = importlib.import_module("proj.console.orders")  
        if team.leader == context.PLAYER:
            orders.WorldScenarioChangeOrder(team=team)
        else:
            pass

    def update_target(self, team):
        if team.scenario is None:
            return
        circle_pts = team.scenario.circle(team.location, options.MOTION_SCENARIO)
        for pt in circle_pts:
            if pt not in team.scenario.loc_entity:
                continue
            ent = team.scenario.loc_entity[pt]
            if context.relationship(ent, team) < 30:
                WorldTeamActiveAction(subject=ent).do()
            if context.relationship(team, ent) >= 30:
                continue
            elif team.scenario.distance(team.location, pt) > 1:
                team.targets.append((1, ent))
            else:
                WorldAttackAction(subject=team, object=ent).do()

    def pick(self):
        min_time = context.timestamp
        min_team = []
        for team in context.teams.values():
            if len(team.targets) == 0 and team.battle is None:
                continue
            if team.process < min_time:
                min_time = team.process 
                min_team = [team]
            elif team.process == min_time:
                min_team.append(team)
        return min_team

    def process_target(self, team):
        orders = importlib.import_module("proj.console.orders")
        if team.leader == context.PLAYER:
            team.go()
            team.last_move = context.timestamp_
            if team.next in team.scenario.loc_entity:
                team.cut_path()
                MSG(style=MSG.WorldClash, subject=team, map=team.scenario)
                return
            else:
                team.scenario.locate(team, team.next)
            if team.next == team.path[0]:
                team.targets.pop()
                self.update_scenario(team)
                #self.recenter(team)
            else:
                team.process += team.step
        else:
            self.update_target(team)
            if team.battle is not None:
                return
            path = team.scenario.connect_dynamic(team.location, team.target, team, steps=1)
            if team.process <= context.timestamp - context.duration() + team.step:
                team.path = [team.scenario.location(team)]
            team.path.append(path[0])
            team.scenario.locate(team, path[0])
            if path[0] == team.target:
                team.targets.pop()
                self.update_scenario(team)
            else:
                team.process += team.step
            team.last_move = context.timestamp_
            self.update_target(team)

    def process_battle(self, team):    
        orders = importlib.import_module("proj.console.orders")      
        if team.battle.finished():
            if team.battle.id not in self.battles:
                #if team.battle in context.battles:
                #    context.battles.remove(team.battle)
                self.battles.add(team.battle.id)
                orders.BattleFinishOrder(battle=team.battle)
        else: 
            if team.battle.id not in self.battles:
                self.battles.add(team.battle.id)
                orders.BattleNewTurnOrder(battle=team.battle)               
                if not team.battle.silent:
                    #orders.BattleNewTurnOrder(battle=team.battle) 
                    context.timeflow(6)
                #else:
                #    if "turncount" not in team.battle.extensions:
                #        team.battle.extensions["turncount"] = 1
                #    else:
                #        team.battle.extensions["turncount"] += 1
                #    if team.battle not in context.battles:
                #        context.battles.append(team.battle)
            team.process += 6
            
    def _process_battle(self, team):    
        orders = importlib.import_module("proj.console.orders")    
        if team.battle.finished():
            team.result = team.battle.result(team)
            team.battle = None
        elif team.battle.id not in self.battles:
            self.battles.add(team.battle.id)
            if not team.battle.silent:
                orders.BattleNewTurnOrder(battle=team.battle)                       
                context.timeflow(6)
            else:
                context.battles.append(team.battle)
            team.process += 1
        else:
            team.process += 1
        
    def do(self):
        self.battles = set()
        teams = self.pick()
        if len(teams) == 0:
            context.timestamp_ = context.timestamp
            return
        for team in teams:
            if context.timestamp_ < team.process:
                context.timestamp_ = team.process
            if team.battle is not None:
                self.process_battle(team)
            elif len(team.targets) != 0 and team.scenario is not None:
                self.process_target(team)
            if team.leader != context.PLAYER and \
               len(team.targets) == 0 and team.battle is None:
                context.teams.pop(team.id)


class WorldTimeFlowAction(Action):
    """
    开始时间流逝
    """
    def do(self):
        context.timeflow(self.period)


class WorldTimePauseAction(Action):
    """
    中断时间流逝
    """
    def do(self):
        context.timestamp = context.timestamp_


class WorldMoveAction(Action):

    def do(self):
        self.subject.targets.append((0, self.target))
        if self.subject.scenario.tpl_id == "MAP_WORLD":
            self.subject.step = 30
        else:
            self.subject.step = 1
        self.subject.process = context.timestamp + self.subject.step
        if self.subject.leader == context.PLAYER:
            if self.path is None:
                self.path = self.subject.scenario.connect_dynamic(self.subject.location, self.target, self.subject)
            self.subject.reset_path(self.path)
            context.timeflow((len(self.path) - 1) * self.subject.step)
        else:
            context.teams[self.subject.id] = self.subject
            self.subject.path = [self.subject.scenario.location(self.subject)]
            
            
class WorldShowMapAction(Action):

    def initialize(self):
        if context.PLAYER is not None and context.PLAYER.team is not None:
            self.map = context.PLAYER.team.scenario

    def do(self):
        MSG(style=MSG.WorldMap, map=self.map, show_trace=self.show_trace)
        
        
class WorldTeamCleanPathAction(Action):

    def do(self):
        MSG.sync()
        self.team.path = []


class WorldExploreAction(Action):

    def do(self):
        s_id = self.subject.team.scenario.tpl_id
        terran = self.subject.team.scenario.grid(self.position).terran.tpl_id
        if s_id not in context.explorations:
            context.explorations[s_id] = {}
        s_exp = context.explorations[s_id]
        found = False
        for dis in context.discoveries.get(s_id, []) + context.discoveries.get("ALL", []):
            dis_id = dis["id"]
            if dis_id not in s_exp:
                s_exp[dis_id] = {}
            if self.position not in s_exp[dis_id]: 
                if "terrans" in dis and terran not in dis["terrans"]:
                    continue
                if "locations" in dis and self.position not in dis["locations"]:
                    continue
                if "tools" in dis and (self.tool is None or len(self.tool.tags & dis["tools"]) == 0):
                    continue
            if "rate" in dis:
                rate = dis["rate"]
            else:
                rate = 1
            if not ratio.if_rate(rate):
                continue
            if "quantity" in dis:
                if self.position not in s_exp[dis_id] or \
                   ("refresh" in dis and s_exp[dis_id][self.position]["timestamp"] + \
                                         dis["refresh"] <= context.timestamp):
                    s_exp[dis_id][self.position] = {"quantity": dis["quantity"], 
                                                    "timestamp": context.timestamp}
            if "range" in dis:
                quantity = min(random.randint(*dis["range"]), s_exp[dis_id][self.position]["quantity"])
            else:
                quantity = min(1, s_exp[dis_id][self.position]["quantity"])
            if quantity == 0:
                continue
            s_exp[dis_id][self.position]["quantity"] -= quantity
            found = True
            item = Item.one(dis["item"])
            self.subject.add_item(item, quantity=quantity)
            MSG(style=MSG.PersonItemAcquire, subject=self.subject, item=item, quantity=quantity)
        if not found:
            MSG(style=MSG.PersonItemAcquire, subject=self.subject, item=None, quantity=0)
        context.timeflow(1)
        
        
class WorldAttackAction(Action):

    def do(self):
        # 获取战斗地图，暂时只支持一个场景关联一张战斗地图
        # TODO: 支持一个场景可关联多张战斗地图，根据实际坐标进行获取
        if self.battle_map is None:
            map = Map.template("%s_BTL" % self.subject.scenario.tpl_id)
        else:
            map = self.battle_map
        context.teams[self.object.id] = self.object
        context.teams[self.subject.id] = self.subject
        subject_group = self.subject_group if self.subject_group is not None else self.subject.members
        if self.object.battle is None:
            silent = self.subject != context.PLAYER.team and self.object != context.PLAYER.team
            BattleStartAction(map=map, groups=[subject_group, self.object.members], 
                              death=self.death, silent=silent).do()
        else:
            allies = self.object.battle.allies
            new_group_index = len(self.object.battle.groups)
            enemy_group = self.object.battle.groups.index(self.object.leader.group)
            for al in allies:
                if enemy_group in al:
                    continue
                al.append(new_group_index)
            BattleJoinAction(battle=self.object.battle, group=subject_group, 
                             death=self.death, allies=allies).do()
        
        
class WorldRestAction(Action):
    
    def do(self):
        context.timeflow(self.duration)
        WorldProcessAction().do()
        
        
class WorldTeamActiveAction(Action):

    def do(self):
        context.teams[self.subject.id] = self.subject
        
        
class WorldScenarioChangeAction(Action):

    def do(self):
        old_scene = self.team.scenario
        new_scene = Map.one(old_scene.transport_locs[self.team.location])
        tmp_locs = []
        # 确定角色转换场景后的位置与方向
        if new_scene.tpl_id == "MAP_WORLD":
            for loc, tpl in new_scene.transport_locs.items():
                if tpl == old_scene.tpl_id:
                    tmp_loc = loc
                    break
            old_dire = old_scene.direction(self.team.location, (old_scene.x // 2, old_scene.y // 2))
            for pt in new_scene.circle(tmp_loc, 1):
                if not new_scene.can_stay(self.team.leader, pt):
                    continue
                new_dire = new_scene.direction(pt, tmp_loc)
                dire_diff = abs(new_dire - old_dire)
                tmp_locs.append((pt, 1 if dire_diff == 5 else dire_diff))        
        else:
            old_dire = old_scene.direction(self.team.path[1], self.team.path[0])
            for loc, tpl in new_scene.transport_locs.items():
                if tpl == old_scene.tpl_id:
                    new_dire = new_scene.direction(loc, (new_scene.x // 2, new_scene.y // 2))
                    dire_diff = abs(new_dire - old_dire)
                    tmp_locs.append((loc, 1 if dire_diff == 5 else dire_diff))
        tmp_locs.sort(key=lambda x: x[1])
        location = tmp_locs[0][0]
        TeamTransportAction(team=self.team, scenario=new_scene, location=location).do()
            
