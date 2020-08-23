# -- coding: utf-8 --
import importlib

from proj.entity.common import Entity


class Team(Entity):

    @classmethod
    def one(cls, tpl_id):
        plib = importlib.import_module("proj.entity.person")
        return plib.Person.one(tpl_id[5:]).team

    def initialize(self):
        self.leader = None

        self.members = []
        
        self.battle = None

        self.direction = 1
        self.scenario = None
        self.path = []
        self.step = 1

        self.targets = []
       
        self.last_move = 0

        self.process = 0

        self.idx_ = 0

    def go(self):
        (self.path, self.idx_)
        self.idx_ -= 1 

    def include(self, *persons):
        for person in persons:
            if person.team is not None and person.team.scenario is not None:
                person.team.scenario.remove(person.team)
            self.members.append(person)
            person.team = self
            if self.leader is None:
                self.leader = person
                self.id = self.leader.id

    def reset_path(self, path):
        self.path = path
        self.idx_ = -1

    def cut_path(self):
        self.path = self.path[self.idx_:]

    @property
    def next(self):
        return self.path[self.idx_]
        
    @property
    def name(self):
        return self.leader.name
        
    @property
    def player(self):
        return self.leader.player
        
    @property
    def location(self):
        return self.scenario.location(self)

    @property
    def movitivity(self):
        return self.leader.movitivity

    @property
    def locativity(self):
        return self.leader.locativity

    @property
    def target(self):
        if len(self.targets) == 0:
            return None
        if self.targets[-1][0] == 1:
            if self.targets[-1][1].scenario == self.scenario:
                return self.scenario.location(self.targets[-1][1])
            else:
                self.targets.pop()
                return self.target
        else:
            return self.targets[-1][1]
