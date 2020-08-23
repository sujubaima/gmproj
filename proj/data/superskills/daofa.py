# -- coding: utf-8 --


# ------------------------------------- 分割线：C级刀法 -------------------------------------


# 鸾影刀法
SUPERSKILL_LUANYINGDAOFA = \
    {"name": "鸾影刀法", "rank": 0,
     "nodes": [{"name": "鸣鸾佩玉", "tags": "SKILL_LUANYINGDAOFA_1", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LUANYINGDAOFA_1"}],
                "description": "习得招式【鸣鸾佩玉】"},
               {"name": "快刀", "exp": 750, "next": [2],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "daofa", "delta": 2}]}],
                "description": "刀法+2"},
               {"name": "快刀", "exp": 750, "next": [3, 4, 5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "daofa", "delta": 2}]}],
                "description": "刀法+2"},
               {"name": "鸾光两破", "tags": "SKILL_LUANYINGDAOFA_2",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LUANYINGDAOFA_2"}],
                "description": "习得招式【鸾光两破】"},
               {"name": "快刀", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "daofa", "delta": 2}]}],
                "description": "刀法+2"},
                {"name": "灵动", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "dongjing", "delta": 5}]}],
                "description": "灵动+5%，沉静-5%"}]}
                
                
# 拦路刀法
SUPERSKILL_LANLUDAOFA = \
    {"name": "拦路刀法", "rank": 0,
     "nodes": [{"name": "一夫当关", "tags": "SKILL_LUANYINGDAOFA_1", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LUANYINGDAOFA_1"}],
                "description": "习得招式【一夫当关】"},
               {"name": "雷池勿越", "tags": "SKILL_LUANYINGDAOFA_1",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LUANYINGDAOFA_1"}],
                "description": "习得招式【雷池勿越】"}]}


# 青天刀法
SUPERSKILL_QINGTIANDAOFA = \
    {"name": "青天刀法", "rank": 0,
     "nodes": [{"name": "云归穴暝", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_QINGTIANDAOFA_1"}]},
               {"name": "拨云见日",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_QINGTIANDAOFA_2"}]}]}


# 分筋析骨刀
SUPERSKILL_FENJINXIGUDAO = \
    {"name": "分筋析骨刀", "rank": 0,
     "nodes": [{"name": "分筋刀", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_FENJINXIGUDAO_1"}]},
               {"name": "析骨刀",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_FENJINXIGUDAO_2"}]}]}


# ------------------------------------- 分割线：B级刀法 -------------------------------------


# 破锋八刀
SUPERSKILL_POFENGBADAO = \
    {"name": "破锋八刀", "rank": 1,
     "nodes": [{"name": "剑锋破尽", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_POFENGBADAO_1"}]},
               {"name": "枪锋破尽", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_POFENGBADAO_2"}]},
               {"name": "奇锋破尽",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_POFENGBADAO_3"}]}]}
                
                
# 黑风刀
SUPERSKILL_HEIFENGDAO = \
    {"name": "黑风刀", "rank": 0,
     "nodes": [{"name": "黑云压城", "exp": 10, "tags": "SKILL_HEIFENGDAO_1", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_HEIFENGDAO_1"}],
                "description": "习得技能【黑云压城】"},
               {"name": "快刀", "exp": 750, "next": [2],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "daofa", "delta": 1}]}],
                "description": "刀法+1"},
               {"name": "快刀", "exp": 750, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "daofa", "delta": 2}]}],
                "description": "刀法+2"},
               {"name": "快刀", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "daofa", "delta": 3}]}],
                "description": "刀法+3"},
               {"name": "阴风阵阵", "tags": "SKILL_HEIFENGDAO_1",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_HEIFENGDAO_2"}],
                "description": "习得技能【阴风阵阵】"}]}
                

# 飞廉刀法
SUPERSKILL_FEILIANDAOFA = \
    {"name": "飞廉刀法", "rank": 1,
     "nodes": [{"name": "迎风斩",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_FEILIANDAOFA_1"}]},
               {"name": "逆风斩",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_FEILIANDAOFA_2"}]}]}


# ------------------------------------- 分割线：A级刀法 -------------------------------------


# 刀剑攻
SUPERSKILL_DAOJIANJUE = \
    {"name": "刀剑攻", "rank": 2,
     "nodes": [{"name": "上刀下剑法", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DAOJIANJUE_1"}]},
               {"name": "上剑下刀法", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DAOJIANJUE_2"}]},
               {"name": "刀剑合一法",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DAOJIANJUE_3"}]}]}


# 猩红刀法
SUPERSKILL_XINGHONGDAOFA = \
    {"name": "猩红刀法", "rank": 2,
     "nodes": [{"name": "含血喷人", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XINGHONGDAOFA_1"}]},
               {"name": "磨牙吮血", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XINGHONGDAOFA_2"}]},
               {"name": "血雨腥风",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XINGHONGDAOFA_3"}]}]}


# ------------------------------------- 分割线：S级刀法 -------------------------------------
