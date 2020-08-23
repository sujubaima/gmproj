# -- coding: utf-8 --


# ------------------------------------- 分割线：C级长兵 -------------------------------------


# 夜叉棍法
SUPERSKILL_YECHAGUNFA = \
    {"name": "夜叉棍法", "rank": 0,
     "nodes": [{"name": "飞空堕地", "tags": "SKILL_YECHAGUNFA_1", "next": [1, 2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YECHAGUNFA_1"}],
                "description": "习得招式【飞空堕地】"},
               {"name": "刚猛", "exp": 750, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "gangrou", "delta": 3}]}],
                "description": "刚猛+3%，柔易-3%"},
               {"name": "灵动", "exp": 750, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "dongjing", "delta": 3}]}],
                "description": "灵动+3%，沉静-3%"},
               {"name": "丈威", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "changbing", "delta": 3}]}],
                "description": "长兵+3"},
               {"name": "大力如风", "tags": "SKILL_YECHAGUNFA_2", "next": [5],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YECHAGUNFA_2"}],
                "description": "习得招式【大力如风】"},
               {"name": "丈威", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "changbing", "delta": 3}]}],
                "description": "长兵+3"}]}


# 五郎棍
SUPERSKILL_WULANGGUN = \
    {"name": "五郎棍", "rank": 0,
     "nodes": [{"name": "横冲直撞", "tags": "SKILL_YECHAGUNFA_1", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YECHAGUNFA_1"}],
                "description": "习得招式【横冲直撞】"},
               {"name": "下马提拦", "tags": "SKILL_YECHAGUNFA_1",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YECHAGUNFA_1"}],
                "description": "习得招式【下马提拦】"}]}


# ------------------------------------- 分割线：B级长兵 -------------------------------------


# 西楚霸王枪
SUPERSKILL_XICHUBAWANGQIANG = \
    {"name": "西楚霸王枪", "rank": 1,
     "nodes": [{"name": "以一当十", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XICHUBAWANGQIANG_1"}]},
               {"name": "破釜沉舟", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XICHUBAWANGQIANG_2"}]},
               {"name": "霸王别姬",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XICHUBAWANGQIANG_3"}]}]}
                

# ------------------------------------- 分割线：A级长兵 -------------------------------------

                
# 十力降魔棍
SUPERSKILL_SHILIXIANGMOGUN = \
    {"name": "十力降魔棍", "rank": 2,
     "nodes": [{"name": "十力具备", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_SHILIXIANGMOGUN_1"}]},
               {"name": "泰然无惧", 
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_SHILIXIANGMOGUN_2"}]}]}


# ------------------------------------- 分割线：S级长兵 -------------------------------------


# 打狗棒法
SUPERSKILL_DAGOUBANGFA = \
    {"name": "打狗棒法", "rank": 3,
     "nodes": [{"name": "棒打狗头", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DAGOUBANGFA_1"}]},
               {"name": "獒口夺杖", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DAGOUBANGFA_2"}]},
               {"name": "天下无狗",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DAGOUBANGFA_3"}]}]}
