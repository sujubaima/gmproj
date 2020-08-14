# -- coding: utf-8 --


# 太乙玄门剑
SUPERSKILL_TAIYIXUANMENJIAN = \
    {"name": "太乙玄门剑", "rank": 0,
     "nodes": [{"name": "执掌权衡", "tags": "SKILL_TAIYIXUANMENJIAN_1", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIYIXUANMENJIAN_1"}],
                "description": "习得招式【执掌权衡】"},
               {"name": "利剑", "exp": 750, "next": [2],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "剑法+3"},
               {"name": "追星赶月", "tags": "SKILL_TAIYIXUANMENJIAN_2", "next": [3],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIYIXUANMENJIAN_2"}],
                "description": "习得招式【追星赶月】"},
               {"name": "利剑", "exp": 750, "next": [4, 5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "剑法+3"},
               {"name": "伏阴", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "yinyang", "delta": -5}]}],
                "description": "内力阳性-3%，阴性+3%"},
               {"name": "炽阳", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "yinyang", "delta": 5}]}],
                "description": "内力阳性+3%，阴性-3%"},]}
                
                
# 天音剑气
SUPERSKILL_TIANYINJIANQI = \
    {"name": "天音剑气", "rank": 2,
     "nodes": [{"name": "空谷传声", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANYINJIANQI_1"}]},
               {"name": "风送轻云", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANYINJIANQI_2"}]},
               {"name": "振索鸣铃",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TIANYINJIANQI_3"}]}]}


# 卧龙剑法
SUPERSKILL_WOLONGJIANFA = \
    {"name": "卧龙剑法", "rank": 2,
     "nodes": [{"name": "幽谷飞泉", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_WOLONGJIANFA_1"}]},
               {"name": "长沟冷月", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_WOLONGJIANFA_2"}]},
               {"name": "碧潭龙隐",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_WOLONGJIANFA_3"}]}]}


# 龙华剑术
SUPERSKILL_LONGHUAJIANSHU = \
    {"name": "龙华剑术", "rank": 1,
     "nodes": [{"name": "指点迷津", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LONGHUAJIANSHU_1"}]},
               {"name": "出幽入冥", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LONGHUAJIANSHU_2"}]},
               {"name": "一气冲霄",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LONGHUAJIANSHU_3"}]}]}
                
                
# 同归剑法
SUPERSKILL_TONGGUIJIANFA = \
    {"name": "同归剑法", "rank": 2,
     "nodes": [{"name": "一别两宽", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TONGGUIJIANFA_1"}]},
               {"name": "殊途同归",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TONGGUIJIANFA_2"}]}]}
                          

# 兰阳剑法
SUPERSKILL_LANYANGJIANFA = \
    {"name": "兰阳剑法", "rank": 0,
     "nodes": [{"name": "兰之猗猗", "exp": 500, "tags": "SKILL_LANYANGJIANFA_1", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_1"}],
                "description": "习得招式【兰之猗猗】"},
               {"name": "沉静", "exp": 500, "next": [2],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "dongjing", "delta": -5}]}],
                "description": "灵动-5%，沉静+5%"},
               {"name": "不采而佩", "exp": 750, "tags": "SKILL_LANYANGJIANFA_2", "next": [3, 4],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_2"}],
                "description": "习得招式【不采而佩】"},
               {"name": "利剑", "exp": 750, "next": [5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "剑法+3"},
               {"name": "利剑", "exp": 750, "next": [5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "剑法+3"},
               {"name": "君子之守", "exp": 1000, "tags": "SKILL_LANYANGJIANFA_3", 
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_3"}],
                "description": "习得招式【君子之守】"}]}


# 黄芦苦竹剑
SUPERSKILL_HUANGLUKUZHUJIAN = \
    {"name": "黄芦苦竹剑", "rank": 0,
     "nodes": [{"name": "黄芦颤叶", "exp": 750, "tags": "SKILL_HUANGLUKUZHUJIAN_1", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_HUANGLUKUZHUJIAN_1"}],
                "description": "习得招式【黄芦颤叶】"},
               {"name": "苦竹摇风", "exp": 750, "tags": "SKILL_HUANGLUKUZHUJIAN_2", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_HUANGLUKUZHUJIAN_2"}],
                "description": "习得招式【苦竹摇风】"},
               {"name": "利剑", "exp": 750, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "剑法+3"},               
               {"name": "利剑", "exp": 750, "next": [4, 5],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 3}]}],
                "description": "剑法+3"},
               {"name": "芦轻", "exp": 750, 
                "functions": [{"type": "PersonChangeAttribute", 
                               "attrs": [{"name": "dongjing", "delta": 4}]},
                              {"type": "PersonSkillChangeAttribute", "skill": "SKILL_HUANGLUKUZHUJIAN_1",
                               "attrs": [{"name": "shape", "value": "Line.Emit,1,3"}]}],
                "description": "灵动+4%，沉静-4%；【黄芦颤叶】一式增加1格溅射范围"},
               {"name": "竹劲", "exp": 750,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "gangrou", "delta": 4}]},
                              {"type": "PersonSkillChangeAttribute", "skill": "SKILL_HUANGLUKUZHUJIAN_2",
                               "attrs": [{"name": "cd", "value": 0}]}],
                "description": "刚猛+4%，柔易-4%；【苦竹摇风】一式冷却时间减少为0"}]}
                

# 细柳剑法
SUPERSKILL_XILIUJIANFA = \
    {"name": "细柳剑法", "rank": 0,
     "nodes": [{"name": "碧玉千条", "tags": "SKILL_XILIUJIANFA_1", "next": [1, 2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XILIUJIANFA_1"}],
                "description": "习得招式【碧玉千条】"},
               {"name": "剪春风", "exp": 500, 
                "functions": [{"type": "PersonSkillAddEffect", "skill": "SKILL_XILIUJIANFA_1", 
                               "effect": {"id": "EXERT.STATUS_QIANCHAN", "turns": 2}}],
                "description": "招式【碧玉千条】增加【牵缠】效果"},
               {"name": "满城风絮", "tags": "SKILL_XILIUJIANFA_2", "next": [3, 4, 5],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_XILIUJIANFA_2"}],
                "description": "习得招式【满城风絮】"},
               {"name": "利剑", "exp": 500,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 4}]}],
                "description": "剑法+5"},
               {"name": "灵慧", "exp": 500,
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "zhipu", "delta": 5}]}],
                "description": "颖悟+5%，朴拙-5%"},
               {"name": "袅晴丝", "exp": 750, 
                "functions": [{"type": "PersonSkillChangeAttribute", "skill": "SKILL_XILIUJIANFA_2",
                               "attrs": [{"name": "shape", "value": "SmallSector.Seep,1,3"}]}],
                "description": "招式【满城风絮】增加1格溅射范围"}]}
      

# 屯云飞烟剑
SUPERSKILL_TUNYUNFEIYANJIAN = \
    {"name": "屯云飞烟剑", "rank": 1,
     "nodes": [{"name": "荡胸生层云", "exp": 750, "next": [1, 2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_1"}],
                "description": "习得招式【荡胸生层云】"},
               {"name": "破绽", "exp": 500, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "critical_rate_", "delta": 0.02}]}],
                "description": "暴击+2"},
               {"name": "精准", "exp": 500, "next": [3],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "hit_rate_", "delta": 0.02}]}],
                "description": "命中+2"},
               {"name": "惊风涌飞流", "exp": 1000, "next": [4, 5],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_2"}],
                "description": "习得招式【惊风涌飞流】"},
               {"name": "利剑", "exp": 500, "next": [6],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 4}]}],
                "description": "剑法+4"},
               {"name": "利剑", "exp": 500, "next": [6],
                "functions": [{"type": "PersonChangeAttribute",
                               "attrs": [{"name": "jianfa", "delta": 4}]}],
                "description": "剑法+4"},
               {"name": "齐州九点烟", "exp": 1250,
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_3"}],
                "description": "习得招式【齐州九点烟】"}]}


# 太岳三青峰
SUPERSKILL_TAIYUESANQINGFENG = \
    {"name": "太岳三青峰", "rank": 2,
     "nodes": [{"name": "素手托莲", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIYUESANQINGFENG_1"}]},
               {"name": "横眉观日", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIYUESANQINGFENG_2"}]},
               {"name": "高天落雁",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIYUESANQINGFENG_3"}]}]}
                
                
# 越女剑法
SUPERSKILL_YUENVJIANFA = \
    {"name": "越女剑法", "rank": 3,
     "nodes": [{"name": "移花接木", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUENVJIANFA_1"}]},
               {"name": "决云断地", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUENVJIANFA_2"}]},
               {"name": "逐影追形",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUENVJIANFA_3"}]}]}
                
                
# 碧城剑法
SUPERSKILL_BICHENGJIANFA = \
    {"name": "碧城剑法", "rank": 1,
     "nodes": [{"name": "栖鸾附鹤", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BICHENGJIANFA_1"}]},
               {"name": "紫凤放娇", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BICHENGJIANFA_2"}]},
               {"name": "玉轮生魄", "next": [3],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BICHENGJIANFA_3"}]},
               {"name": "黛蛾长敛", 
                "functions": [{"type": "PersonSkillRemoveEffect",
                               "skill": "SKILL_BICHENGJIANFA_3", "effect": {"id": "EFFECT_GONGQI"}},
                              {"type": "PersonSkillAddEffect",
                               "skill": "SKILL_BICHENGJIANFA_3", "effect": {"id": "EFFECT_GONGQI_DA"}}],
                "description": "增强【玉轮生魄】的攻气效果"}]}


# 玉女素心剑
SUPERSKILL_YUNVSUXINJIAN = \
    {"name": "玉女素心剑", "rank": 2,
     "nodes": [{"name": "神女投壶", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUNVSUXINJIAN_1"}]},
               {"name": "窥窗扫月", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUNVSUXINJIAN_2"}]},
               {"name": "如虹似玉",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YUNVSUXINJIAN_3"}]}]}
                
                
# 裴将军剑
SUPERSKILL_PEIJIANGJUNJIAN = \
    {"name": "裴将军剑", "rank": 2,
     "nodes": [{"name": "左右交光", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_PEIJIANGJUNJIAN_1"}]},
               {"name": "随风游电", 
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_PEIJIANGJUNJIAN_2"}]}]}


# 太极剑意
SUPERSKILL_TAIJIJIANYI = \
    {"name": "太极剑意", "rank": 3,
     "nodes": [{"name": "古树盘根", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIJIJIANYI_1"}]},
               {"name": "顺水推舟", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIJIJIANYI_2"}]},
               {"name": "云摩三舞",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_TAIJIJIANYI_3"}]}]}
