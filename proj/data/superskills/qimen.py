# -- coding: utf-8 --


# ------------------------------------- 分割线：C级奇门 -------------------------------------


# 天罡刺
SUPERSKILL_TIANGANGCI = \
    {"name": "天罡刺", "rank": 0,
     "nodes": [{"name": "虹铃暗法", "tags": "SKILL_TIANGANGCI_1", "next": [2, 3],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANGANGCI_1"}],
                "description": "习得招式【虹铃暗法】"},
               {"name": "燕雀穿枝", "tags": "SKILL_TIANGANGCI_2", "next": [2, 3],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANGANGCI_2"}],
                "description": "习得招式【燕雀穿枝】"},
               {"name": "奇变", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "qimen", "delta": 2}]}],
                "description": "奇门+2"}, 
               {"name": "奇变", "exp": 750, "next": [4],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "qimen", "delta": 2}]}],
                "description": "奇门+2"}, 
               {"name": "奇变", "exp": 750, "next": [5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "qimen", "delta": 2}]}],
                "description": "奇门+2"},
               {"name": "看破", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "hit_rate", "ratio": 1.05}]}],
                "description": "基础命中+5%"}]}


# ------------------------------------- 分割线：B级奇门 -------------------------------------


# ------------------------------------- 分割线：A级奇门 -------------------------------------


# 天音剑气
SUPERSKILL_TIANYINJIANQI = \
    {"name": "天音剑气", "rank": 2,
     "nodes": [{"name": "空谷传声", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANYINJIANQI_1"}]},
               {"name": "风送轻云", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANYINJIANQI_2"}]},
               {"name": "振索鸣铃",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANYINJIANQI_3"}]}]}
                
                
# 越人歌
SUPERSKILL_YUERENGE = \
    {"name": "越人歌", "rank": 2,
     "nodes": [{"name": "今夕何夕", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUERENGE_1"}]},
               {"name": "搴舟中流", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUERENGE_2"}]},
               {"name": "山木有枝",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUERENGE_3"}]}]}


# 日月双轮
SUPERSKILL_RIYUESHUANGLUN = \
    {"name": "日月双轮", "rank": 2,
     "nodes": [{"name": "偷天换日", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_RIYUESHUANGLUN_1"}]},
               {"name": "月落参横", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_RIYUESHUANGLUN_2"}]},
               {"name": "日月同辉",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_RIYUESHUANGLUN_3"}]}]}
                

# ------------------------------------- 分割线：S级奇门 -------------------------------------


# 天雷地火引
SUPERSKILL_TIANLEIDIHUOYIN = \
    {"name": "天雷地火引", "rank": 3,
     "nodes": [{"name": "起萍生浪", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANLEIDIHUOYIN_1"}]},
               {"name": "火泻雷嗔",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANLEIDIHUOYIN_3"}]}]}
