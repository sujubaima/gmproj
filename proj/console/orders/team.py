# -- coding: utf-8 --

from proj.engine import Order
from proj.engine import Message as MSG

from proj.builtin.actions import TeamTransportAction

class TeamTransportOrder(Order):

    def carry(self):
        MSG(style=MSG.TeamTransport, leader=self.leader, targets=self.targets).callback = self.callback
        
    def callback(self, target):
        if len(target) > 0:
            TeamTransportAction(leader=self.leader, scenario=target[0], location=target[1]).do()