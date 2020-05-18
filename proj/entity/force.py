# -- coding: utf-8 --

from proj.entity.common import Entity

class Force(Entity):

    def initialize(self):
        self.name = None
        self.titles = []
        self.description = None
        self.members = []
        self.buildings = []

    def include(self, p):
        self.members.append(p) 
        p.force = self
