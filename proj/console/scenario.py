from proj.engine import Order

class TalkOrder(Order):

    def initialize(self):
        pass

    def carry(self):
        pass


class SearchOrder(Order):

    def initialize(self):
        self.subject = None
        self.scene = None

    def carry(self):
        action.SearchAction(subject=self.subject, scene=self.scene).do()
