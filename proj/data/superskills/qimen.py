# -- coding: utf-8 --

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
                
                
# 越人歌
SUPERSKILL_YUERENGE = \
    {"name": "越人歌", "rank": 2,
     "nodes": [{"name": "今夕何夕", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUERENGE_1"}]},
               {"name": "搴舟中流", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUERENGE_2"}]},
               {"name": "山木有枝",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUERENGE_3"}]}]}
                

# 天雷地火引
SUPERSKILL_TIANLEIDIHUOYIN = \
    {"name": "天雷地火引", "rank": 3,
     "nodes": [{"name": "起萍生浪", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANLEIDIHUOYIN_1"}]},
               {"name": "野火春风", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANLEIDIHUOYIN_2"}]},
               {"name": "火泻雷嗔",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANLEIDIHUOYIN_3"}]}]}
