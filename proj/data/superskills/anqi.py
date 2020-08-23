# -- coding: utf-8 --


# ------------------------------------- 分割线：C级暗器 -------------------------------------


# 弹弓术
SUPERSKILL_DANGONGSHU = \
    {"name": "弹弓术", "rank": 0,
     "nodes": [{"name": "射弹丸",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_DANGONGSHU_1"}]}]}
                
# 蜻蜓点水式
SUPERSKILL_QINGTINGDIANSHUISHI = \
    {"name": "蜻蜓点水式", "rank": 0,
     "nodes": [{"name": "露荷", "tags": "SKILL_QINGTINGDIANSHUISHI_1", "next": [1, 2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_QINGTINGDIANSHUISHI_1"}],
                "description": "习得招式【露荷】"},
               {"name": "准星", "exp": 750, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "暗器+3"},
               {"name": "准星", "exp": 750, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "暗器+3"},               
               {"name": "避燕", "tags": "SKILL_QINGTINGDIANSHUISHI_2", "next": [4, 5],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_QINGTINGDIANSHUISHI_1"}],
                "description": "习得招式【避燕】"},
               {"name": "疾步", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "motion_", "delta": 0.5}]}],
                "description": "基础移动力+0.5"},
               {"name": "轻身", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "speed_", "delta": 50}]}],
                "description": "基础速度+50"}]}


# ------------------------------------- 分割线：B级暗器 -------------------------------------


# 璇玑图
SUPERSKILL_XUANJITU = \
    {"name": "璇玑图", "rank": 1,
     "nodes": [{"name": "三星照人", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XUANJITU_1"}]},
               {"name": "芙蓉印月",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XUANJITU_2"}]}]}
                

# 春风九归
SUPERSKILL_CHUNFENGJIUGUI = \
    {"name": "春风九归", "rank": 1,
     "nodes": [{"name": "淡烟笼柳", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_CHUNFENGJIUGUI_1"}]},
               {"name": "回风摇蕙",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_CHUNFENGJIUGUI_2"}]}]}


# ------------------------------------- 分割线：A级暗器 -------------------------------------



# ------------------------------------- 分割线：S级暗器 -------------------------------------
