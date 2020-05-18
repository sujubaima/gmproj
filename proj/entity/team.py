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
        self.target = None
        self.path = []
        self.step = 1
       
        self.last_move = 0
 
        self.follow = None

        self.process = 0

        self.move_style = "move"
        
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
