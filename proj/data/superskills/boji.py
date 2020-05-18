# -- coding: utf-8 --


# 百缠手
SUPERSKILL_BAICHANSHOU = \
    {"name": "百缠手", "rank": 0,
     "nodes": [{"name": "软磨硬泡", "tags": "SKILL_BAICHANSHOU_1", "next": [1, 2, 3],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BAICHANSHOU_1"}],
                "description": "习得招式【软磨硬泡】"},
               {"name": "劲拳", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "boji", "delta": 3}]}],
                "description": "搏击+3"},
               {"name": "柔易", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "gangrou", "delta": -3}]}],
                "description": "刚猛-3%，柔易+3%"},
               {"name": "劲拳", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "boji", "delta": 3}]}],
                "description": "搏击+3"},
               {"name": "柔易", "exp": 750, "next": [5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "gangrou", "delta": -3}]}],
                "description": "刚猛-3%，柔易+3%"},
               {"name": "死缠烂打", "tags": "SKILL_BAICHANSHOU_2",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BAICHANSHOU_2"}],
                "description": "习得招式【死缠烂打】"}]}
                
                
# 幽闭三击 
SUPERSKILL_YOUBISANJI = \
    {"name": "幽闭三击", "rank": 2,
     "nodes": [{"name": "金屋藏春色", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_1"}]},
               {"name": "寒鸦带日影", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_2"}]},
               {"name": "长门悬孤月",          
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_3"}]}]}


# 铁砂掌 
SUPERSKILL_TIESHAZHANG = \
    {"name": "铁砂掌", "rank": 0,
     "nodes": [{"name": "崩山碎石",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIESHAZHANG_1"}]}]}


# 窃钩术
SUPERSKILL_QIEGOUSHU = \
    {"name": "窃钩术", "rank": 0,
     "nodes": [{"name": "妙手空空",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_QIEGOUSHU_1"}]}]}
