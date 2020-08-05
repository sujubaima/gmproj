# -- coding: utf-8 --

from proj.engine import Control
from proj.engine import Message as MSG

class SuperskillSelectControl(Control):

    def initialize(self):
        super(SuperskillSelectControl, self).initialize()
        self.title = "请选择你要翻阅的书籍："

    def launch(self):
        MSG(style=MSG.SuperskillSelectControl, control=self)

    @Control.listener
    def select(self, superskill):
        control = SuperskillControl(superskill=superskill)
        control.run()
        self.close()


class SuperskillControl(Control):

    def initialize(self):
        super(SuperskillControl, self).initialize()
        self.title = "请选择你要进行的操作："

    def launch(self):
        MSG(style=MSG.SuperskillControl, control=self)
