# -- coding: utf-8 --

from proj.engine import Condition

from proj.entity import Person


class PersonAttributeCondition(Condition):

    def check(self):
        attr = getattr(self.person, self.name)
        lower, upper = self.range[1:-1].split(",")
        lower = int(lower)
        upper = int(upper)
        if self.range.startswith("("):
            lowerfunc = lambda x: x > lower
        else:
            lowerfunc = lambda x: x >= lower
        if self.range.endswith(")"):
            upperfunc = lambda x: x < upper
        else:
            upperfunc = lambda x: x <= upper
        return lowerfunc(attr) and upperfunc(attr)