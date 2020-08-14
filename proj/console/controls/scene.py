# -- coding: utf-8 --

from proj import options

from proj import data

from proj.engine import Control
from proj.engine import Message as MSG
from proj.engine import script

from proj.entity import Map
from proj.entity import Person

from proj.builtin.actions import WorldMoveAction
from proj.builtin.actions import WorldRestAction
from proj.builtin.actions import WorldAttackAction
from proj.builtin.actions import WorldExploreAction
from proj.builtin.actions import PersonItemTransferAction
from proj.builtin.actions import WorldScenarioChangeAction

from proj.console.controls.common import PipeControl
from proj.console.controls.common import EnsureControl
from proj.console.controls.common import PersonSelectControl
from proj.console.controls.common import PersonSelectMultipleControl
from proj.console.controls.common import PositionSelectControl
from proj.console.controls.common import ItemSelectControl
from proj.console.controls.team import TeamControl
from proj.console.controls.system import SystemControl

from proj.runtime import context


class ScenarioControl(Control):

    def launch(self):
        if context.guide_dest is not None:
            context.guide = set(self.scenario.connect_dynamic(self.team.location,
                                   context.guide_dest.location, self.team.leader)[:-1])
        else:
            context.guide = None
        MSG(style=MSG.ScenarioControl, control=self)

    def macros(self):
        macs = {}
        descs = {}
        descs["#path.{person}"] = "显示到达特定人物的导航路径，需要该人物也处于当前场景中（例：#path.chen_tingzhi）"
        for entity in self.scenario.loc_entity.values():
            macs["#path.%s" % entity.leader.tpl_id[7:].lower()] = self.showpath
        macs["#path.clean"] = self.cleanpath
        descs["#path.clean"] = "清除导航路径"
        return macs, descs

    def showpath(self, tag):
        person = Person.one("PERSON_%s" % tag[6:].upper())
        if person.team.id not in self.scenario.entity_loc:
            return
        context.guide_dest = person.team
        self.launch()

    def cleanpath(self, tag):
        context.guide_dest = None
        self.launch()

    @Control.listener
    def move(self, arg):
        position_text = "请输入要移动的地块坐标"
        p = self.team
        p_loc = p.scenario.location(p)
        motion = options.MOTION_SCENARIO
        allinscope, connections = self.scenario.move_scope(p, motion=motion, enable_zoc=False)
        self.connections = connections
        validator = lambda x: PositionSelectControl.validator(self.scenario, x, allinscope, False)
        control = PositionSelectControl(positions=allinscope, scenario=self.scenario, 
                      validator=validator, text=position_text)
        control.run()
        if control.target is not None:
            loc = self.scenario.location(self.team)
            move_trace = self.scenario.move_trace(control.target, loc, self.connections)
            WorldMoveAction(subject=self.team, target=control.target, path=move_trace).do()
        self.close()

    @Control.listener
    def talk(self, arg):
        position_text = "请输入要交谈的角色坐标"
        person_title = "请选择要与之交谈的角色："
        loc = self.scenario.location(self.team)
        allinscope = self.scenario.circle(loc, 1, mr=0, allow_object=True)
        positions = []
        for pos in allinscope:
            if pos in self.scenario.loc_entity:
                positions.append(pos)
        validator = lambda x: PositionSelectControl.validator(self.scenario, x, allinscope, True)
        control = PipeControl()
        control.pipe(PositionSelectControl(positions=positions, scenario=self.scenario,
                         validator=validator, text=position_text), valves=["target"])\
               .pipe(ScenarioPersonSelectControl(scenario=self.scenario,
                         title=person_title), valves=["person"])
        control.run()
        if control.person is not None:
            if control.person.conversation is not None:
                conversation = control.person.conversation
            else:
                conversation = "SCRIPT_DEFAULT"
            script.run(getattr(data.scripts, conversation), name=conversation, 
                       subject=self.team.leader, object=control.person)
        self.close()

    @Control.listener
    def explore(self, arg):
        position_text = "请输入要探索的地块坐标"
        tool_title = "请选择探索使用的工具："
        loc = self.scenario.location(self.team)
        allinscope = self.scenario.circle(loc, 1, mr=0, allow_object=True)
        validator = lambda x: PositionSelectControl.validator(self.scenario, x, allinscope, True)
        control = PipeControl()
        control.pipe(PositionSelectControl(positions=allinscope, scenario=self.scenario,
                         validator=validator, text=position_text), valves=["target"])
        control.pipe(ExploreToolSelectControl(persons=self.team.members, team=self.team, 
                         scenario=self.scenario, title=tool_title), 
                     valves=["owneritem"], optionals=["owner", "item"])
        control.run()
        if control.owneritem is not None:
            WorldExploreAction(subject=control.owner, position=control.target, tool=control.item).do()
        self.close()

    @Control.listener
    def attack(self, arg):
        position_text = "请输入要攻击的对象坐标"
        ensure_text = ret = "动手之前要想清楚，是否进行攻击？（若插手NPC间的战斗，人物的初始位置将是随机的）"
        loc = self.scenario.location(self.team)
        allinscope = self.scenario.circle(loc, 1)
        positions = []
        for pos in allinscope:
            if pos in self.scenario.loc_entity:
                positions.append(pos)
        validator = lambda x: PositionSelectControl.validator(self.scenario, x, allinscope, True)
        control = PipeControl()
        control.pipe(PositionSelectControl(positions=positions,
                         scenario=self.scenario, validator=validator, 
                         ensure_text=ensure_text, ensure=True,
                         text=position_text), valves=["target"])
        control.pipe(PersonSelectMultipleControl(candidates=self.team.members,
                         number=min(options.BATTLE_MAX_PERSONS_MAIN, len(self.team.members))), 
                     valves=["persons"])
        control.run()
        if control.persons is not None:
            object = self.team.scenario.entity(control.target)
            WorldAttackAction(subject=self.team, subject_group=control.persons,
                object=object, death=True).do()
        self.close()

    @Control.listener
    def transfer(self, arg):
        position_text = "请输入要赠予的角色坐标"
        person_title = "请选择要赠予物品的角色："
        loc = self.scenario.location(self.team)
        allinscope = self.scenario.circle(loc, 1, mr=0)
        positions = []
        for pos in allinscope:
            if pos in self.scenario.loc_entity:
                positions.append(pos)
        validator = lambda x: PositionSelectControl.validator(self.scenario, x, allinscope, True)
        control = PipeControl()
        control.pipe(PositionSelectControl(positions=positions, scenario=self.scenario,
                         validator=validator, text=position_text), valves=["target"])\
               .pipe(ScenarioPersonSelectControl(scenario=self.scenario, 
                         title=person_title), valves=["person"])\
               .pipe(ItemSelectControl(scenario=self.scenario,
                         title=person_title), 
                     valves=["owneritem"], optionals=["owner", "item"])\
               .pipe(QuantitySelectControl(), valves=["quantity"])
        control.run()
        if control.quantity is not None:
            PersonItemTransferAction(subject=control.owner, object=control.person, 
                item=self.item, quantity=self.quantity).do() 
        self.close()

    @Control.listener
    def rest(self, arg):
        WorldRestAction(subject=self.team, duration=options.MOTION_SCENARIO).do()
        control = RestControl(team=self.team)
        control.run()
        self.close()

    @Control.listener
    def teaminfo(self, arg):
        control = TeamControl(team=self.team)
        control.run()
        self.close()

    @Control.listener
    def thumbnail(self, arg):
        control = ThumbnailControl(scenario=self.scenario)
        control.run()
        self.close()

    @Control.listener
    def system(self, arg):
        control = SystemControl()
        control.run()
        self.close()


class ThumbnailControl(Control):

    def launch(self):
        MSG(style=MSG.ThumbnailControl, control=self)


class BattleStartControl(PersonSelectMultipleControl):

    def launch(self):
        self.candidates=self.subject.members
        self.number=min(options.BATTLE_MAX_PERSONS_MAIN, len(self.subject.members))
        super(BattleStartControl, self).launch()

    @Control.listener
    def select(self, persons):
        if persons is not None:
            WorldAttackAction(subject=self.subject, subject_group=persons,
                object=self.object, death=self.death).do()
        self.close()


class ScenarioPersonSelectControl(PersonSelectControl):

    def launch(self):
        if self.candidates is None:
            self.candidates = self.scenario.entity(self.target).members
        super(ScenarioPersonSelectControl, self).launch()        


class ExploreToolSelectControl(ItemSelectControl):

    def filter(self, item):
        if self.terran is None:
            self.terran = self.scenario.grid(self.target).terran.tpl_id\
                              .split("_")[-1].capitalize()
        if "Tool" in item.tags and self.terran in item.tags:
            return 0
        else:
            return 2

    def launch(self):
        self.prepare()
        MSG(style=MSG.ExploreToolSelectControl, control=self) 


class ScenarioChangeControl(Control):

    def launch(self):
        target = self.team.scenario.transport_locs[self.team.location]
        target = Map.one(target).name
        self.text = "当前地块可通往%s，是否前往？" % target
        MSG(style=MSG.ScenarioChangeControl, control=self)

    @Control.listener
    def input(self, sure):
        if sure:
            WorldScenarioChangeAction(team=self.team).do()
        self.close() 


class RestControl(Control):

    def launch(self):
        MSG(style=MSG.RestControl, control=self)
        
    def input(self, ret):
        if ret:
            WorldRestAction(subject=self.team, duration=options.MOTION_SCENARIO).do()
            self.launch()
        else:
            self.close()
