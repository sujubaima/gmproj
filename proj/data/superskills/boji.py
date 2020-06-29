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


# 长风拳法
SUPERSKILL_CHANGFENGQUANFA = \
    {"name": "长风拳法", "rank": 1,
     "nodes": [{"name": "大风扬旗", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_CHANGFENGQUANFA_1"}]},
               {"name": "乘风破浪",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_CHANGFENGQUANFA_2"}]}]}
                
                
# 幽闭三击 
SUPERSKILL_YOUBISANJI = \
    {"name": "幽闭三击", "rank": 2,
     "nodes": [{"name": "金屋藏春色", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_1"}]},
               {"name": "寒鸦带日影", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_2"}]},
               {"name": "长门悬孤月",          
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_3"}]}]}


# 醉拳
SUPERSKILL_ZUIQUAN = \
    {"name": "醉八仙拳", "rank": 2,
     "nodes": [{"name": "铁拐李", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_ZUIQUAN_1"}]},
               {"name": "汉钟离", "next": [2, 3],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_ZUIQUAN_2"}]},
               {"name": "张果老",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_ZUIQUAN_3"}]},
               {"name": "何仙姑",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_ZUIQUAN_4"}]}]}


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


# 摩诃无量掌
SUPERSKILL_MOHEWULIANGZHANG = \
    {"name": "摩诃无量掌", "rank": 3,
     "nodes": [{"name": "如恒河沙", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_MOHEWULIANGZHANG_1"}]},
               {"name": "如阿僧祇", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_MOHEWULIANGZHANG_2"}]},
               {"name": "如不思议",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_MOHEWULIANGZHANG_3"}]}]}


# 太极拳
SUPERSKILL_TAIJIQUAN = \
    {"name": "太极拳", "rank": 3,
     "nodes": [{"name": "野马分鬃", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIJIQUAN_1"}]},
               {"name": "白鹤亮翅", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIJIQUAN_2"}]},
               {"name": "如封似闭",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIJIQUAN_3"}]}]}


# 降龙十八掌
SUPERSKILL_XIANGLONGSHIBAZHANG = \
    {"name": "降龙十八掌", "rank": 3,
     "nodes": [{"name": "亢龙有悔", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XIANGLONGSHIBAZHANG_1"}]},
               {"name": "见龙卸甲", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XIANGLONGSHIBAZHANG_2"}]},
               {"name": "龙战于野",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XIANGLONGSHIBAZHANG_3"}]}]}
