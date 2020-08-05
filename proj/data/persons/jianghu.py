# -- coding: utf-8 --


# 教程用人物
PERSON_PLAYER_TUITION = \
    {"firstname": "刘", "lastname": "旭", "showname": "白老师", "title": "无名小卒",
     "dongjing": 0, "gangrou": 0, "zhipu": 0, "yinyang": 0,
     "neigong": 15, "boji": 15, "jianfa": 15, "daofa": 15, "changbing": 15, "anqi": 15, "qimen": 15,
     "superskills": [{"id": "SUPERSKILL_WUMINGQUANFA", "learn": "All"},
                     {"id": "SUPERSKILL_WUMINGJIANFA", "learn": "All"}],
     "items": [],
     "criticaltxt": "当你看到这句话的时候，说明你暴击了！"}



# 木人桩
PERSON_MURENZHUANG = \
    {"firstname": "", "lastname": "", "showname": "木人桩", "title": "练武器材", "tags": "Unlive",
     "dongjing": -50, "gangrou": 0, "zhipu": -50, "yinyang": 0,
     "neigong": 0, "boji": 0, "jianfa": 0, "daofa": 0, "changbing": 0, "anqi": 0, "qimen": 0,
     "superskills": [{"id": "SUPERSKILL_WANGBAQUAN", "learn": "All"}],
     "items": [],
     "recipes": []}


# 刘旭
PERSON_PLAYER = \
    {"firstname": "刘", "lastname": "旭", "showname": "白老师", "title": "无名小卒", 
     "dongjing": 0, "gangrou": -17, "zhipu": 21, "yinyang": -33,
     "neigong": 30, "boji": 18, "jianfa": 37, "daofa": 17, "changbing": 19, "anqi": 31, "qimen": 29,
     "superskills": [{"id": "SUPERSKILL_WANGBAQUAN", "learn": "All"},
                     {"id": "SUPERSKILL_TIESHAZHANG", "learn": "All"}],
     "items": [{"id": "ITEM_DANGONG", "quantity": 1, "position": "MainHand", "durability": 10},
               {"id": "ITEM_MONEY", "quantity": 250},
               {"id": "ITEM_XIZIPENGXINJUE", "quantity": 1},
               {"id": "ITEM_TUNYUNFEIYANJIAN", "quantity": 1},
               {"id": "ITEM_XILIUJIANFA", "quantity": 1},
               {"id": "ITEM_LOLITA", "quantity": 1, "durability": 23},
               {"id": "ITEM_CHANGJIAN", "quantity": 1, "durability": 15},
               {"id": "ITEM_CHANGJIAN,1-ITEM_JINGTIE", "quantity": 1},
               {"id": "ITEM_YUNMU", "quantity": 2},
               {"id": "ITEM_SHENGTIE", "quantity": 10},
               {"id": "ITEM_TONGMU", "quantity": 9},
               {"id": "ITEM_LUYU", "quantity": 1},
               {"id": "ITEM_YAN", "quantity": 1},
               {"id": "ITEM_HUADIAO", "quantity": 1},
               {"id": "ITEM_FENGGANGJIU", "quantity": 1},
               {"id": "ITEM_SHOUFU", "quantity": 1}],
     "recipes": [{"id": "RECIPE_QINGZHENGLUYU"},
                 {"id": "RECIPE_CHANGJIAN"}],
     "criticaltxt": "我有主角光环，你们还能斗得过我？"}


# 赵神机
PERSON_ZHAO_SHENJI = \
    {"firstname": "赵", "lastname": "神机", "title": "长生坛教主",
     "hp_max": 7900, "mp_max": 3700, "attack": 400, "defense": 350,
     "hit_rate": 0.96, "counter_rate": 0.08, "dodge_rate": 0.1, "critical_rate": 0.12, "anti_damage_rate": 0.06,
     "dongjing": 23, "gangrou": 5, "zhipu": 21, "yinyang": 0,
     "neigong": 83, "boji": 67, "jianfa": 20, "daofa": 73, "changbing": 4, "anqi": 66, "qimen": 69,
     "superskills": [{"id": "SUPERSKILL_QIXINGNIMAI", "learn": "All"},
                     {"id": "SUPERSKILL_XINGHONGDAOFA", "learn": "All"}],
     "skill_counter": {"id": "SKILL_XINGHONGDAOFA_2"},
     "equipment": [{"id": "ITEM_XUEYUE", "position": "MainHand"}],
     "items": [],
     "running": {"id": "SUPERSKILL_QIXINGNIMAI"},
     "criticaltxt": "看见没有，这就是逆运经脉的威力！"}


# 田威
PERSON_TIAN_WEI = \
    {"firstname": "田", "lastname": "威", "showname": "田公公", "title": "东厂督主",
     "hp_max": 6400, "mp_max": 3500, "attack": 380, "defense": 280,
     "hit_rate": 1.05, "counter_rate": 0.06, "dodge_rate": 0.15, "critical_rate": 0.15, "anti_damage_rate": 0.1,
     "dongjing": 30, "gangrou": -34, "zhipu": 35, "yinyang": -37,
     "neigong": 29, "boji": 73, "jianfa": 43, "daofa": 31, "changbing": 10, "anqi": 74, "qimen": 61, 
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": [0, 1, 2]},
                     {"id": "SUPERSKILL_YOUXIAXINFA", "learn": [0, 1, 2]},
                     {"id": "SUPERSKILL_CHOUSUIGONG", "learn": [0, 1, 2, 3, 4, 5]},
                     {"id": "SUPERSKILL_YOUBISANJI", "learn": [0, 1, 2]}],
     "skill_counter": {"id": "SKILL_YOUBISANJI_1"},
     "equipment": [{"id": "ITEM_ZHITAO", "position": "MainHand"}],
     "items": [],
     "running": {"id": "SUPERSKILL_CHOUSUIGONG"},
     "criticaltxt": "咱家警告过你，不要敬酒不吃吃罚酒。"}


# 闻人徽
PERSON_WENREN_HUI = \
    {"firstname": "闻人", "lastname": "徽", "title": "流云阁阁主",
     "dongjing": 2, "gangrou": -6, "zhipu": 6, "yinyang": -10,
     "neigong": 60, "boji": 21, "jianfa": 50, "daofa": 1, "changbing": 17, "anqi": 40, "qimen": 55,
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": [0, 1, 2]},
                     {"id": "SUPERSKILL_TIANYINJIANQI", "learn": [0, 1, 2]}],
     "equipment": [],
     "items": []}
