# -- coding: utf-8 --

from proj import engine
from proj.engine import Control
from proj.engine import Message as MSG

from proj.runtime import saveload
from proj.runtime import context


class SystemControl(Control):

    def launch(self):
        MSG(style=MSG.SystemControl, control=self)

    @Control.listener
    def showevents(self, arg):
        control = PipeControl()
        control.pipe(EventSelectControl(), valves=["task"])\
               .pipe(EventDetailControl())
        control.run()
        self.launch()

    @Control.listener
    def savefile(self, arg):
        control = FileSelectControl(allow_new=True)
        control.run()
        if control.file is not None:
            saveload.save(control.file)
            self.close()
        else:
            self.launch()

    @Control.listener
    def loadfile(self, arg):
        control = FileSelectControl()
        control.run()
        if control.file is not None:
            saveload.load(control.file)
            self.close()
        else:
            self.launch()

    @Control.listener
    def exit(self, arg):
        engine.stop()


class EventSelectControl(Control):

    def launch(self):
        self.tasks = []
        for idx in context.tasks_index:
            self.tasks.append((idx, context.tasks_status[idx])) 
        MSG(style=MSG.EventSelectControl, control=self)

    @Control.listener
    def select(self, task):
        self.task =  task
        self.close()


class EventDetailControl(Control):
   
    def launch(self):
        self.tasktxt = context.tasks[self.task]
        MSG(style=MSG.EventDetailControl, control=self)


class FileSelectControl(Control):

    def launch(self):
         MSG(style=MSG.FileSelectControl, control=self)

    @Control.listener
    def select(self, file):
        self.file = file
        self.close()
