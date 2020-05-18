# -- coding: utf-8 --

from proj.entity.common import Entity

class Conversation(Entity):

    def initialize(self):
        self.talks = []