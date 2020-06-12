# -- coding: utf-8
from proj.engine import Condition
from proj.engine import Order

class BattlePersonPositionOnCondition(Condition):

    def check(self):
        battle = self.person.team.battle
        if battle != Order.Current.battle:
            return False
        scenario = self.person.team.battle.map
        return self.person.id in scenario.entity_loc and scenario.entity_loc[self.person.id] == self.location
        
        
class BattlePersonTurnCondition(Condition):

    def check(self):
        battle = self.person.team.battle
        if battle != Order.Current.battle:
            return False
        return self.person == battle.current
        
        
class BattlePersonsDistanceCondition(Condition):

    def check(self):
        battle = self.subject.team.battle
        if battle != Order.Current.battle:
            return False
        map = self.subject.team.battle.map
        distance = map.distance(map.location(self.subject), map.location(self.object))
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
        return lowerfunc(distance) and upperfunc(distance)
