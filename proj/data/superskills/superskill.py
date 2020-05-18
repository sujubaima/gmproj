# -- coding: utf-8 --

# 天音剑气
SUPERSKILL_4 = {"name": "天音剑气", "rank": 2,
                "nodes": [{"name": "空谷传声", "next": [1],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_4_1"}]},
                          {"name": "风送轻云", "next": [2],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_4_2"}]},
                          {"name": "振索鸣铃",
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_4_3"}]}]}


# 卧龙剑法
SUPERSKILL_5 = {"name": "卧龙剑法", "rank": 2,
                "nodes": [{"name": "幽谷飞泉", "next": [1],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_5_1"}]},
                          {"name": "长沟冷月", "next": [2],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_5_2"}]},
                          {"name": "碧潭龙隐",
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_5_3"}]}]}


# 猩红刀法
SUPERSKILL_7 = {"name": "猩红刀法", "rank": 2,
                "nodes": [{"name": "含血喷人", "next": [1],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_7_1"}]},
                          {"name": "磨牙吮血", "next": [2],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_7_2"}]},
                          {"name": "血雨腥风", 
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_7_3"}]}]}


# 龙华剑术
SUPERSKILL_8 = {"name": "龙华剑术", "rank": 1,
                "nodes": [{"name": "指点迷津", "next": [1],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_8_1"}]},
                          {"name": "出幽入冥", "next": [2],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_8_2"}]},
                          {"name": "一气冲霄",
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_8_3"}]}]}
                          

# 破锋八刀
SUPERSKILL_9 = {"name": "破锋八刀", "rank": 1,
                "nodes": [{"name": "剑锋破尽", "next": [1],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_9_1"}]},
                          {"name": "枪锋破尽", "next": [2],
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_9_2"}]},
                          {"name": "奇锋破尽",
                           "functions": [{"type": "PersonAddSkill", "skill": "SKILL_9_3"}]}]}


# 西楚霸王枪
SUPERSKILL_XICHUBAWANGQIANG = \
    {"name": "西楚霸王枪", "rank": 1,
     "nodes": [{"name": "以一当十", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_10_1"}]},
               {"name": "破釜沉舟", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_10_2"}]},
               {"name": "霸王别姬",
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_10_3"}]}]}


# 幽闭三击 
SUPERSKILL_YOUBISANJI = \
    {"name": "幽闭三击", "rank": 2,
     "nodes": [{"name": "金屋夜寒", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_1"}]},
               {"name": "昭阳歌断", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_2"}]},
               {"name": "长门深闭",          
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_YOUBISANJI_3"}]}]}


# 拨云见日刀
SUPERSKILL_BOYUNJIANRIDAO = \
    {"name": "拨云见日刀", "rank": 0,
     "nodes": [{"name": "云归穴暝", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BOYUNJIANRIDAO_1"}]},
               {"name": "日出林开", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_BOYUNJIANRIDAO_2"}]}]}


# 兰阳剑法
SUPERSKILL_LANYANGJIANFA = \
    {"name": "兰阳剑法", "rank": 0,
     "nodes": [{"name": "秋兰可喻", "next": [1],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_1"}]},
               {"name": "幽兰自赏：", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_2"}]},
               {"name": "芝兰满砌：", "next": [2],
                "functions": [{"type": "PersonAddSkill", "skill": "SKILL_LANYANGJIANFA_2"}]}]}


#TaoLu(name="天机掌法")
#ZhaoShi(name="藏巧", power=660, cd=1, shape=Shape(Shape.Point, 3, 0), haoqi=132, yinyang=1, style=skill.Boji, belongs=Skill.search("天机掌法"))
#ZhaoShi(name="藏拙", power=660, cd=1, shape=Shape(Shape.Point, 3, 0), haoqi=132, style=skill.Boji, belongs=Skill.search("天机掌法"))
#ZhaoShi(name="藏意", power=720, cd=2, shape=Shape(Shape.SmallSector, 1, 2), haoqi=144, style=skill.Boji, belongs=Skill.search("天机掌法"))
#
#TaoLu(name="太岳三青峰")
#ZhaoShi(name="素手托莲", power=630, cd=1, shape=Shape(Shape.Point, 2, 0), haoqi=126, yinyang=-1, style=skill.Jianfa, belongs=Skill.search("太岳三青峰"))
#ZhaoShi(name="横眉观日", power=735, cd=2, Shape=Shape(Shape.Line, 1, 2), haoqi=147, style=skill.Jianfa, belongs=Skill.search("太岳三青峰"))
#ZhaoShi(name="高天落雁", power=825, cd=3, shape=Shape(Shape.Point, 2, 1), haoqi=167, style=skill.Jianfa, belongs=Skill.search("太岳三青峰"))
#
#TaoLu(name="清秋指法")
#ZhaoShi(name="半山飞急雨", power=540, cd=1, shape=Shape(Shape.Line, 1, 2), haoqi=108, yinyang=-2, style=skill.Boji, belongs=Skill.search("清秋指法"))
#ZhaoShi(name="万木送秋声", power=600, cd=2, shape=Shape(Shape.Line, 1, 3), haoqi=120, style=skill.Boji, belongs=Skill.search("清秋指法"))
#ZhaoShi(name="剑气倚清商", power=690, cd=3, shape=Shape(Shape.Line, 1, 4), haoqi=138, style=skill.Boji, belongs=Skill.search("清秋指法"))
#
#TaoLu(name="太极拳")
#ZhaoShi(name="野马分鬃", power=540, cd=0, haoqi=108, yinyang=0, style=skill.Boji, belongs=Skill.search("太极拳"))
#ZhaoShi(name="白鹤亮翅", power=600, cd=0, haoqi=120, yinyang=0, style=skill.Boji, belongs=Skill.search("太极拳"))
#ZhaoShi(name="如封似闭", power=690, cd=2, shape=Shape(Shape.Around, 1, 1), haoqi=138, yinyang=0, style=skill.Boji, belongs=Skill.search("太极拳")).exerteffect(exertion=EffectStatus(effect=Effect.search("卸劲")), target=effect.INITIATOR, exertturn=3)
#
#TaoLu(name="九宫八卦剑")
#ZhaoShi(name="坎离分", power=540, cd=0, shape=Shape(Shape.Point, 2, 0), haoqi=108, yinyang=0, style=skill.Boji, belongs=Skill.search("九宫八卦剑"))
#ZhaoShi(name="艮兑通", power=600, cd=1, shape=Shape(Shape.Line, 1, 3), haoqi=120, yinyang=0, style=skill.Boji, belongs=Skill.search("九宫八卦剑"))
#ZhaoShi(name="乾坤定", power=690, cd=2, shape=Shape(Shape.SmallSector, 1, 2), haoqi=138, yinyang=0, style=skill.Boji, belongs=Skill.search("九宫八卦剑"))
#
#TaoLu(name="流云飞袖")
#ZhaoShi(name="捧玉钟", power=540, cd=1, shape=Shape(Shape.Point, 3, 1), haoqi=108, yinyang=-2, style=skill.Qimen, belongs=Skill.search("流云飞袖"))
#ZhaoShi(name="盈暗香", power=620, cd=2, shape=Shape(Shape.BigSector, 1, 1), haoqi=120, style=skill.Qimen, belongs=Skill.search("流云飞袖"))
#ZhaoShi(name="弄西风", power=690, cd=3, shape=Shape(Shape.SmallSector, 1, 3), haoqi=138, style=skill.Qimen, belongs=Skill.search("流云飞袖"))
