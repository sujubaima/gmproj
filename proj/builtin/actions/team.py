# -- coding: utf-8 --

from proj.engine import Action
from proj.engine import Message as MSG

from proj.builtin.actions.person import PersonItemTransferAction


class TeamAction(Action):

    def finish(self):
        if self.leader is None:
            self.leader = self.team.leader
        if self.team is None:
            self.team = self.leader.team


class TeamTransportAction(TeamAction):

    def take(self):
        if self.team.scenario != self.scenario:
             self.team.scenario.remove(self.team)
             self.team.scenario = self.scenario
        self.scenario.locate(self.team, self.location) 


class TeamIncludePersonAction(TeamAction):

    def take(self):
        self.team.include(self.person)
        MSG(style=MSG.PersonJoinTeam, action=self)
