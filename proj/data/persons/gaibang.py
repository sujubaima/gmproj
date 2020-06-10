# -- coding: utf-8 --


# 邢飞龙
PERSON_XING_FEILONG = \
    {"firstname": "邢", "lastname": "飞龙", "title": "丐帮帮主",
     "hp_max": 7800, "mp_max": 2900, "attack": 380, "defense": 340, "motion": 1,
     "hit_rate": 0.98, "counter_rate": 0.08, "dodge_rate": 0.09, "critical_rate": 0.1, "anti_damage_rate": 0.07,
     "dongjing": 14, "gangrou": 28, "zhipu": -16,
     "neigong": 72, "boji": 82, "jianfa": 21, "daofa": 32, "changbing": 87, "anqi": 35, "qimen": 49, "yinyang": 15,
     "superskills": [{"id": "SUPERSKILL_QIURANXINFA", "learn": "All"},
                     {"id": "SUPERSKILL_DAGOUBANGFA", "learn": "All"}],
     "skill_counter": {"id": "SKILL_DAGOUBANGFA_2"},
     "running": {"id": "SUPERSKILL_QIURANXINFA"},
     "items": [],
     "equipment": [{"id": "ITEM_DAGOUBANG", "position": "MainHand"}],
     "criticaltxt": "武林鼠辈，尚识得屠狗人否？！"}


# 厉苍鹰
PERSON_LI_CANGYING = \
    {"firstname": "厉", "lastname": "苍鹰", "title": "丐帮传功长老",
     "hp_max": 7200, "mp_max": 2800, "attack": 395, "defense": 350, "motion": 0,
     "hit_rate": 1, "counter_rate": 0.1, "dodge_rate": 0.06, "critical_rate": 0.15, "anti_damage_rate": 0.08,
     "dongjing": -12, "gangrou": 32, "zhipu": 20,
     "neigong": 70, "boji": 88, "jianfa": 17, "daofa": 36, "changbing": 71, "anqi": 43, "qimen": 44, "yinyang": 35,
     "superskills": [{"id": "SUPERSKILL_QIURANXINFA", "learn": "All"},
                     {"id": "SUPERSKILL_XIANGLONGSHIBAZHANG", "learn": "All"}],
     "running": {"id": "SUPERSKILL_QIURANXINFA"},
     "items": [],
     "equipment": [{"id": "ITEM_ZHITAO", "position": "MainHand"}],
     "criticaltxt": "人生在世，自当龙战三二十载，建功立业！"}


# 赵乞儿
PERSON_ZHAO_LING = \
    {"firstname": "赵", "lastname": "零", "showname": "赵乞儿", "title": "丐帮弟子",
     "dongjing": 20, "gangrou": 6, "zhipu": -18,
     "neigong": 20, "boji": 30, "jianfa": 2, "daofa": 5, "changbing": 32, "anqi": 12, "qimen": 18, "yinyang": 4,
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": [0, 1, 2]},
                     {"id": "SUPERSKILL_BOYUNJIANRIDAO", "learn": [0, 1]}],
     "items": [],
     "conversation": "DIALOG_ZHAOQIER_1"}