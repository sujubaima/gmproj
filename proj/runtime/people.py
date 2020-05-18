# -- coding: utf-8 --
from proj.core.person import Person

LEAD = None

def create_player(xing, ming, sex):
    LEAD = Person(xing=xing, ming=ming, sex=sex)
    LEAD.random(total=90, attrs=["gengu", "lidao", "shenfa",
                                 "neigong", "dongcha", "wuxing"])
    LEAD.random(total=90, attrs=["boji", "jianfa", "daofa",
                                 "changbing", "anqi", "qimen"])
    return LEAD
