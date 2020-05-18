# -- coding: utf-8 --

from proj.engine import Order
from proj.engine import Message as MSG

from proj.entity import SuperSkill

class BeijigeOrder(Order):

    def carry(self):
        superskills = [SuperSkill.one("SUPERSKILL_BAICHANSHOU"),
                       SuperSkill.one("SUPERSKILL_TAIYIXUANMENJIAN"),
                       SuperSkill.one("SUPERSKILL_LUANYINGDAOFA"),
                       SuperSkill.one("SUPERSKILL_YECHAGUNFA"),
                       SuperSkill.one("SUPERSKILL_TIANGANGCI"),
                       SuperSkill.one("SUPERSKILL_QINGTINGDIANSHUISHI")]
        MSG(style=MSG.SuperSkillChoose, superskills=superskills)
 
class SuperSkillReadOrder(Order):

    def carry(self):
        MSG(style=MSG.SuperSkillRead, superskill=self.superskill)