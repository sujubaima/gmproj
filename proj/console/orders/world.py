# -- coding: utf-8 --

from proj import options

from proj.engine import Order
from proj.engine import Message as MSG

from proj.entity import Map
from proj.entity import Team

from proj.builtin.actions import WorldProcessAction
from proj.builtin.actions import WorldMoveAction
from proj.builtin.actions import WorldRestAction
from proj.builtin.actions import WorldAttackAction
from proj.builtin.actions import WorldExploreAction
from proj.builtin.actions import PersonConversationAction
from proj.builtin.actions import PersonItemTransferAction
from proj.builtin.actions import BattleNewTurnAction
from proj.builtin.actions import WorldScenarioChangeAction

from proj.console import ui

from proj.console.orders.person import PersonItemObjectOrder
from proj.console.orders.person import PersonItemTransferOrder

from proj.console.orders.battle import BattleNewTurnOrder

from proj.runtime import context


class WorldOrder(Order):

    def initialize(self):
        if context.PLAYER is not None and context.PLAYER.team is not None:
            self.map = context.PLAYER.team.scenario
            self.subject = context.PLAYER.team


class WorldProcessOrder(Order):

    hub = True

    def carry(self):
        if context.timestamp_ < context.timestamp:
            WorldProcessAction().do()
        else:
            WorldPlayerOrder()
        WorldProcessOrder()

class WorldPlayerOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldPlayer, subject=self.subject, map=self.map)
        #for btl in context.battles:
        #    BattleNewTurnOrder(battle=btl, turncount=btl.extensions["turncount"])
        #    btl.extensions["turncount"] = 0
        #context.battles = []


class WorldMovePositionOrder(WorldOrder):

    def carry(self):
        p = context.PLAYER.team
        p_loc = p.scenario.location(p)
        allinscope, connections = self.map.move_scope(p, style=p.move_style, motion=options.MOTION_SCENARIO, enable_zoc=False)
        self.scope = allinscope
        self.connections = connections
        MSG(style=MSG.WorldMovePosition,
            map=self.map,
            positions=allinscope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            WorldMoveOrder(subject=self.subject, map=self.map, target=pos, connections=self.connections)
        #else:
        #    WorldPlayerOrder()


class WorldMoveOrder(WorldOrder):


    def carry(self):
        loc = self.map.location(self.subject)
        move_trace = self.map.move_trace(self.target, loc, self.connections)
        WorldMoveAction(subject=self.subject, target=self.target, path=move_trace).do()
        #WorldProcessOrder()


class WorldTalkPositionOrder(WorldOrder):

    def carry(self):
        loc = self.map.location(self.subject)
        allinscope = self.map.circle(loc, 1, mr=0, allow_object=True)
        self.scope = allinscope
        MSG(style=MSG.WorldTalkPosition,
            map=self.map,
            positions=allinscope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            WorldTalkObjectOrder(subject=self.subject, pos=pos)
        #else:
        #    WorldPlayerOrder()


class WorldTalkObjectOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldTalkObject, pos=self.pos, map=self.map).callback=self.callback
                                                          
    def callback(self, obj):                              
        if obj is not None:                               
            WorldTalkOrder(subject=self.subject, object=obj)                              
        #else:                                             
        #    WorldPlayerOrder()     


class WorldTalkOrder(WorldOrder):   


    def initialize(self):
        self.idx = 0    
    
    def carry(self):
        if self.conversation is not None:
            conversation = self.conversation
        elif self.object.conversation is not None:
            conversation = self.object.conversation
        else:
            conversation = "DIALOG_DEFAULT"
        PersonConversationAction(conversation=conversation, subject=self.subject, object=self.object, idx=self.idx).do()
        #WorldProcessOrder()                                                                                                                                                                                                                                                  
 

class WorldGivePositionOrder(WorldOrder):

    def carry(self):
        loc = self.map.location(self.subject)
        allinscope = self.map.circle(loc, 1, mr=0)
        self.scope = allinscope
        MSG(style=MSG.WorldGivePosition,
            map=self.map,
            positions=allinscope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            persons = []
            for p in self.map.loc_entity[pos].members:
                if p == self.subject.leader:
                    continue
                persons.append(p)
            PersonItemObjectOrder(subject=self.subject.leader, persons=self.subject.members,  
                                  candidates=persons, order=PersonItemTransferOrder)
            #WorldProcessOrder()
        #else:
        #    WorldPlayerOrder()
        

class WorldAttackPositionOrder(WorldOrder):               
                                                          
    def carry(self):
        loc = self.map.location(self.subject)
        allinscope = self.map.circle(loc, 1)
        self.scope = allinscope
        MSG(style=MSG.WorldAttackPosition,
            map=self.map,
            positions=allinscope).callback = self.callback
            
    def callback(self, pos):
        if pos is not None:
            WorldAttackEnsureOrder(subject=self.subject, position=pos)
        #else:
        #    WorldPlayerOrder()
            
            
class WorldAttackEnsureOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldAttackEnsure).callback = self.callback
        
    def callback(self, sure):
        if sure:
            #WorldAttackOrder(subject=self.subject, position=self.position)
            WorldAttackSelectOrder(subject=self.subject, position=self.position)
        #else:
        #    WorldPlayerOrder()


class WorldAttackSelectOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldAttackSelect, subject=self.subject, 
            number=min(6, len(self.subject.members))).callback = self.callback

    def callback(self, subject_group):
        if self.object is None:
            self.object = self.subject.scenario.loc_entity[self.position]
        if subject_group is not None:
            WorldAttackOrder(subject=self.subject, subject_group=subject_group, 
                             object=self.object, position=self.position)


class WorldAttackOrder(WorldOrder):

    def carry(self):
        if self.object is None:
            self.object = self.subject.scenario.loc_entity[self.position]           
        WorldAttackAction(subject=self.subject, subject_group=self.subject_group, 
                          object=self.object, map=self.battle_map, death=True).do()


class WorldExplorePositionOrder(WorldOrder):

    def carry(self):
        loc = self.map.location(self.subject)
        allinscope = self.map.circle(loc, 1, mr=0, allow_object=True)
        self.scope = allinscope
        MSG(style=MSG.WorldExplorePosition,
            map=self.map,
            positions=allinscope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            terran = self.subject.scenario.grid(pos).terran.tpl_id.split("_")[-1].capitalize()
            filter = lambda p, q, itm: "Tool" in itm.tags and terran in itm.tags
            WorldExploreToolOrder(subject=self.subject, position=pos, filter=filter) 


class WorldExploreToolOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldExploreTool, subject=self.subject, filter=self.filter).callback = self.callback

    def callback(self, ptool):
        if ptool != "":
            tool, person = ptool
        else:
            tool = None
            person = self.subject.leader
        WorldExploreOrder(subject=person, position=self.position, tool=tool)


class WorldExploreOrder(WorldOrder):

    def carry(self):
        WorldExploreAction(subject=self.subject, position=self.position, tool=self.tool).do()


class WorldBuildPositionOrder(WorldOrder):

    def carry(self):
        loc = self.map.location(self.subject)
        allinscope = self.map.circle(loc, 1, mr=0, allow_object=True)
        self.scope = allinscope
        MSG(style=MSG.WorldBuildPosition,
            map=self.map,
            positions=allinscope).callback = self.callback

    def callback(self, pos):
        if pos is not None:
            WorldBuildPlanOrder()


class WorldBuildPlanOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldBuildPlan)


class WorldBuildOrder(WorldOrder):
    pass


class WorldTerranOrder(WorldOrder):
    pass


class WorldRestOrder(WorldOrder):

    def carry(self):
        self.duration = options.MOTION_SCENARIO
        WorldRestAction(subject=self.subject, duration=self.duration).do()
        MSG(style=MSG.WorldRest, subject=self.subject, map=self.subject.scenario).callback = self.callback
        
    def callback(self, ret):
        if ret:
            WorldRestOrder(subject=self.subject, duration=self.duration)
        #else:
        #    WorldPlayerOrder()
        
        
class WorldScenarioChangeOrder(WorldOrder):

    def carry(self):
        MSG(style=MSG.WorldScenarioChangeEnsure, team=self.team).callback = self.callback
        
    def callback(self, sure):
        if sure:
            WorldScenarioChangeAction(team=self.team).do()
