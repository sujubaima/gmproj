# -- coding: utf-8 --

from proj.engine import Condition

from proj.entity import Person


class TeamCondition(Condition):

    def finish(self):
        if self.leader is None:
            self.leader = self.team.leader
        if self.team is None:
            self.team = self.leader.team


class PersonInTeamCondition(TeamCondition):

    def check(self):
        return self.person in self.team.members
        
        
class TeamPositionOnCondition(TeamCondition):

    def check(self):
        return self.team.scenario == self.scenario and self.team.location == self.location


class TeamBattleWinCondition(TeamCondition):

    def check(self):
        return self.team.result
