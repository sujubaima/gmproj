# -- coding: utf-8 --

# 俞剑奇
PERSON_YU_JIANQI = \
    {"firstname": "俞", "lastname": "剑奇", "title": "渔阳老人",
     "dongjing": -7, "gangrou": -9, "zhipu": 17, "yinyang": -10,
     "neigong": 30, "boji": 33, "jianfa": 80, "daofa": 62, "changbing": 51, "anqi": 22, "qimen": 39,
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": [0, 1, 2]}],
     "equipment": [],
     "items": [],
     "criticaltxt": "没想到这江湖还有轮到老夫出手的一日！"}
     

# 耿朱桥
PERSON_GENG_ZHUQIAO = \
    {"firstname": "耿", "lastname": "朱桥", "title": "铁笛先生",
     "hp_max":5500, "mp_max": 1850, "attack": 396, "defense": 408, "motion": 0,
     "hit_rate": 1, "counter_rate": 0.1, "dodge_rate": 0.06, "critical_rate": 0.1, "anti_damage_rate": 0.1,
     "dongjing": -19, "gangrou": -4, "zhipu": 32, "yinyang": 0,
     "neigong": 62, "boji": 31, "jianfa": 69, "daofa": 64, "changbing": 53, "anqi": 10, "qimen": 61,
     "superskills": [{"id": "SUPERSKILL_MEIHUAXINYI", "learn": "All"},
                     {"id": "SUPERSKILL_DAOJIANJUE", "learn": "All"}],
     "running": {"id": "SUPERSKILL_MEIHUAXINYI"},
     "equipment": [{"id": "ITEM_GONGBUDAO,0-ITEM_JINGTIE", "position": "MainHand"},
                   {"id": "ITEM_WANZIJIAN,0-ITEM_JINGTIE", "position": "ViceHand"},
                   {"id": "ITEM_RUFU", "position": "Body"}],
     "items": [],
     "criticaltxt": "刀法外，剑法内，内外相辅，无往不利。",
     "conversation": "SCRIPT_GENGZHUQIAO_1"}


# 石敬岩
PERSON_SHI_JINGYAN = \
    {"firstname": "石", "lastname": "敬岩", "title": "江湖义士",
     "dongjing": 7, "gangrou": 4, "zhipu": -16,
     "neigong": 30, "boji": 27, "jianfa": 31, "daofa": 33, "changbing": 39, "anqi": 7, "qimen": 21, "yinyang": 0,
     "superskills": [{"id": "SUPERSKILL_LANYANGJIANFA", "learn": "All"}],
     "equipment": [{"id": "ITEM_CHANGJIAN", "position": "MainHand"}],
     "items": [],
     "status": [{"id": "STATUS_WUQIANG"}],
     "criticaltxt": "这等高深的武学，只能以心传心。",
     "conversation": "DIALOG_SHIJINGYAN_1"}
     
     
# 栾檀
PERSON_LUAN_TAN = \
    {"firstname": "栾", "lastname": "檀", "title": "江湖宵小",
     "dongjing": 10, "gangrou": -10, "zhipu": 10,
     "neigong": 15, "boji": 15, "jianfa": 15, "daofa": 15, "changbing": 15, "anqi": 15, "qimen": 15, "yinyang": 0,
     "superskills": [{"id": "SUPERSKILL_QIEGOUSHU", "learn": "All"},
                     #{"id": "SUPERSKILL_MEIHUAXINYI", "learn": "All"},
                     {"id": "SUPERSKILL_DANGONGSHU", "learn": "All"}],
     "running": {"id": "SUPERSKILL_MEIHUAXINYI"},
     "skill_counter": {"id": "SKILL_DANGONGSHU_1"},
     "equipment": [{"id": "ITEM_DANGONG", "position": "MainHand"}],
     "items": [{"id": "ITEM_MONEY", "quantity": 100}],
     "criticaltxt": "我什么都不会，刚刚只是不小心碰了你一下。",
     "conversation": "SCRIPT_LUANTAN_1"}
