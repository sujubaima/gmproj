# -- coding: utf-8 --

from proj.engine import Control
from proj.engine import Message as MSG

from proj.console.controls.common import PipeControl
from proj.console.controls.common import PersonSelectControl
from proj.console.controls.common import ItemSelectControl
from proj.console.controls.common import ItemQuantitySelectControl
from proj.console.controls.common import SkillSelectControl
from proj.console.controls.common import RecipeSelectControl
from proj.console.controls.common import PersonStatusControl

from proj.builtin.actions import PersonItemTransferAction
from proj.builtin.actions import PersonItemLostAction
from proj.builtin.actions import PersonEquipOnAction
from proj.builtin.actions import PersonEquipOffAction
from proj.builtin.actions import PersonRecipeAction


class TeamControl(Control):

    def launch(self):
        MSG(style=MSG.TeamControl, control=self)

    @Control.listener
    def status(self, arg):
        person_title = "请选择要查看状态的角色："
        control = PipeControl()
        control.pipe(PersonSelectControl(candidates=self.team.members, canskip=False,
                         title=person_title), valves=["person"])\
               .pipe(PersonStatusControl(), valves=["notexist"])
        control.run()
        self.launch()

    @Control.listener
    def item(self, arg):
        item_title = "物品一览：%s队" % self.team.leader.name
        control = PipeControl()
        control.pipe(ItemSelectControl(persons=self.team.members, title=item_title), 
                         valves=["owner", "item"])\
               .pipe(ItemUsageControl(), valves=["usage"])
        control.run()
        item = control.item
        if control.usage == 0:
            person_title = "请选择需要使用此物品的角色："
            control = PersonSelectControl(candidates=self.person.team.members, title=person_title)
            control.run()
            if control.person is not None:
                PersonItemUseAction(subject=control.person, item=item, quantity=1).do()
        elif control.usage == 1:
            person_title = "请选择你想要给与的角色："
            quantity_text = "请输入你想要给与的数量"
            candidates = [m for m in self.person.team.members if m != self.person]
            control = PipeControl()
            control.pipe(PersonSelectControl(candidates=candidates, title=person_title),
                         valves=["person"])\
                   .pipe(ItemQuantitySelectControl(item=item, text=quantity_text), valves=["quantity"])
            control.run()
            if control.quantity is not None:
                PersonItemTransferAction(subject=self.person, object=control.person, 
                    item=item, quantity=control.quantity).do()
        elif control.usage == 2:
            quantity_text = "请输入你想要丢弃的数量"
            control = ItemQuantitySelectControl(person=self.person, item=item, text=quantity_text)
            control.run()
            if control.quantity is not None:
                PersonItemLostAction(subject=self.person, 
                    item=control.item, quantity=control.quantity).do()
        self.launch()

    @Control.listener
    def equip(self, arg):
        person_title = "请选择你要修改装备的队员："
        control = PipeControl()
        control.pipe(PersonSelectControl(candidates=self.team.members, canskip=False,
                         title=person_title), valves=["person"])\
               .pipe(EquipmentControl(), valves=["notexist"])
        control.run()
        self.launch()
 
    @Control.listener
    def skill(self, arg):
        person_title = "请选择你要配置技能的队员："
        control = PipeControl()
        control.pipe(PersonSelectControl(candidates=self.team.members, canskip=False,
                         title=person_title), valves=["person"])\
               .pipe(SkillControl(), valves=["notexist"])
        control.run()
        self.launch()

    @Control.listener
    def recipe(self, arg):
        recipe_title = "请选择要制作的配方："
        control = RecipeSelectControl(persons=self.team.members, title=recipe_title)
        control.run()
        products = PersonRecipeAction(subject=self.person, persons=self.persons,
                       recipe=recipe).do()
        self.launch()


class ItemUsageControl(Control):

    def launch(self):
        MSG(style=MSG.ItemUsageControl, control=self)

    def validator(self, usage):
        if usage == 0:
            return "Medicine" in self.item.tags or "Food" in self.item.tags
        if usage == 1:
            return len(self.owner.team.members) > 1

    @Control.listener
    def select(self, usage):
        self.usage = usage
        self.close()


class EquipmentControl(Control):

    def launch(self):
        MSG(style=MSG.EquipmentControl, control=self)

    @Control.listener
    def equip_on(self, arg):
        position, tags = arg
        control = EquipItemSelectControl(person=self.person, tags=tags)
        control.run()
        if control.item is not None:
            PersonEquipOnAction(subject=self.subject, position=position, equip=control.item).do()
        self.launch()

    @Control.listener
    def equip_off(self, position):
        PersonEquipOffAction(subject=self.person, position=position).do()
        self.launch()


class EquipItemSelectControl(ItemSelectControl):

    def filter(self, item):
        if len(item.tags & self.tags) > 0 and item not in self.person.equipment:
            return 0
        else:
            return 2


class SkillControl(Control):

    def launch(self):
        MSG(style=MSG.SkillControl, control=self)

    @Control.listener
    def skill_on(self, position):
        control = SkillSelectControl(person=self.person)
        control.run()
        if control.skill is not None:
            if self.position == -1:
                self.person.skill_counter = control.skill
            else:
                self.person.skills_equipped[position] = control.skill
        self.launch()

    @Control.listener
    def skill_off(self, position):
        if self.position == -1:
            self.person.skill_counter = None
        else:
            self.person.skills_equipped[position] = None
        self.launch()

    @Control.listener
    def skill_run(self, arg):
        control = SkillSelectControl(person=self.person, type=1)
        control.run()
        if control.skill is not None:
            self.person.running = control.skill
        self.launch()

    @Control.listener
    def skill_unrun(self,arg):
        self.person.running = None
        self.launch()

    @Control.listener
    def skill_study(self, arg):
        control = ItemSelectControl(person=self.person, tags=set(["Skillbook"]))
        control.run()
        if control.item is not None:
            control.item.work(self.person, objects=[self.person])
        self.launch()


class SkillNodeSelectControl(Control):

    def launch(self):
        MSG(style=MSG.SkillNodeSelectControl, control=self)

    @Control.listener
    def select(self, node):
        if node is not None:
            PersonStudySkillAction(subject=self.person, node=node).do()
        self.close()
