# -- coding: utf-8 --

from proj.engine import Condition

from proj.runtime import context

from proj import data

        
class TaskUpdatedCondition(Condition):

    def check(self):
        self.task = getattr(data.task, self.task)
        if self.task_branch is not None:        
            self.task_branch = getattr(data.task, self.task_branch) 
        return self.task in context.tasks and (self.task_branch is None or self.task_branch in context.tasks[self.tasks])
        
