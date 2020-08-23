# -- coding: utf-8 --

# 卧龙剑法-幽谷飞泉
SKILL_5_1 = {"name": "幽谷飞泉", "style": "Jianfa",
             "mp": 110, "power": 550, "cd": 1, "yinyang": 1, "shape": "Line,1,2"}

# 卧龙剑法-长沟冷月
SKILL_5_2 = {"name": "长沟冷月", "style": "Jianfa",
             "mp": 188, "power": 625, "cd": 2, "yinyang": 0, "shape": "Line,1,3"}

# 卧龙剑法-碧潭龙隐
SKILL_5_3 = {"name": "碧潭龙隐", "style": "Jianfa",
             "mp": 560, "power": 700, "cd": 3, "yinyang": 0, "shape": "BigSector,1,2"}


# 天音剑气-空谷传声
SKILL_4_1 = {"name": "空谷传声", "style": "Qimen",
             "mp": 120, "power": 600, "cd": 1, "yinyang": -1, "shape": "Point,4,1"}

# 天音剑气-风送轻云
SKILL_4_2 = {"name": "风送轻云", "style": "Qimen",
             "mp": 270, "power": 675, "cd": 2, "yinyang": 0, "shape": "Line,1,4"}

# 天音剑气-振索鸣铃
SKILL_4_3 = {"name": "振索鸣铃", "style": "Qimen",
             "mp": 900, "power": 750, "cd": 3, "yinyang": 0, "shape": "Around,0,99"}


# 猩红刀法-含血喷人
SKILL_7_1 = {"name": "含血喷人", "style": "Daofa",
             "mp": 300, "power": 600, "cd": 1, "yinyang": -1, "shape": "SmallSector,1,2"}

# 猩红刀法-磨牙吮血：附带【吸血（大）】效果
SKILL_7_2 = {"name": "磨牙吮血", "style": "Daofa",
             "mp": 150, "power": 750, "cd": 2, "yinyang": -1, "shape": "Point,2,0",
             "effects": [{"id": "EFFECT_XIXUE_DA"}]}

# 猩红刀法-血雨腥风：附带【吸血（中）】效果
SKILL_7_3 = {"name": "血雨腥风", "style": "Daofa",
             "mp": 960 , "power": 800, "cd": 3, "yinyang": -1, "shape": "Around,0,2",
             "effects": [{"id": "EFFECT_XIXUE"}]}


# 幽闭三击-金屋夜寒
SKILL_YOUBISANJI_1 = \
    {"name": "金屋夜寒", "style": "Boji",
     "mp": 130, "power": 650, "cd": 0, "yinyang": -1, "shape": "Point,2,0",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 幽闭三击-昭阳歌断
SKILL_YOUBISANJI_2 = \
    {"name": "昭阳歌断", "style": "Boji",
     "mp": 140, "power": 700, "cd": 1, "yinyang": -1, "shape": "Point,2,0",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 幽闭三击-长门深闭
SKILL_YOUBISANJI_3 = \
    {"name": "长门深闭", "style": "Boji",
     "mp": 150, "power": 750, "cd": 2, "yinyang": -1, "shape": "Point,2,0",
     "effects": [{"id": "EFFECT_ROUJIN"}]}


# 龙华剑术-指点迷津：附带【神准】效果
SKILL_8_1 = {"name": "指点迷津", "style": "Jianfa",
             "mp": 90, "power": 450, "cd": 1, "yinyang": 0, "shape": "Point,2,0",
             "effects": [{"id": "EFFECT_SHENZHUN"}]}

# 龙华剑术-出幽入冥
SKILL_8_2 = {"name": "出幽入冥", "style": "Jianfa",
             "mp": 165, "power": 550, "cd": 1, "yinyang": -1, "shape": "Line,1,3",
             "effects": [{"id": "EFFECT_ROUJIN"}]}

# 龙华剑术-一气冲霄
SKILL_8_3 = {"name": "一气冲霄", "style": "Jianfa",
             "mp": 130, "power": 650, "cd": 3, "yinyang": 0, "shape": "Point,2,1",
             "effects": [{"id": "EFFECT_ROUJIN"}]}


# 破锋八刀-剑锋破尽：附带【除剑】效果
SKILL_9_1 = {"name": "剑锋破尽", "style": "Daofa",
             "mp": 90, "power": 450, "cd": 2, "yinyang": 0, "shape": "BigSector,1,1"}

# 破锋八刀-枪锋破尽：附带【除枪】效果
SKILL_9_2 = {"name": "枪锋破尽", "style": "Daofa",
             "mp": 90, "power": 450, "cd": 2, "yinyang": 0, "shape": "BigSector,1,1"}

# 破锋八刀-奇锋破尽：附带【除奇】效果
SKILL_9_3 = {"name": "奇锋破尽", "style": "Daofa",
             "mp": 90, "power": 450, "cd": 2, "yinyang": 0, "shape": "BigSector,1,1"}


# 西楚霸王枪-以一当十
SKILL_10_1 = {"name": "以一当十", "style": "Changbing",
             "mp": 320, "power": 400, "cd": 1, "yinyang": 0, "shape": "BigSector,1,2"}

# 西楚霸王枪-破釜沉舟
SKILL_10_2 = {"name": "破釜沉舟", "style": "Changbing",
             "mp": 165, "power": 550, "cd": 3, "yinyang": 0, "shape": "Line,1,3"}

# 西楚霸王枪-霸王别姬
SKILL_10_3 = {"name": "霸王别姬", "style": "Changbing",
             "mp": 140, "power": 700, "cd": 2, "yinyang": 0, "shape": "Point,1,0"}


# 兰阳剑法-秋兰可喻
SKILL_LANYANGJIANFA_1 = \
    {"name": "秋兰可喻", "style": "Jianfa",
     "mp": 70, "power": 350, "cd": 0, "yinyang": 1, "shape": "Point,1,0"}

# 兰阳剑法-幽兰自赏
SKILL_LANYANGJIANFA_2 = \
    {"name": "幽兰自赏", "style": "Jianfa",
     "mp": 90, "power": 450, "cd": 0, "yinyang": -1, "shape": "Point,2,0"}

# 兰阳剑法-芝兰满砌
SKILL_LANYANGJIANFA_3 = \
    {"name": "芝兰满砌", "style": "Jianfa",
     "mp": 275, "power": 550, "cd": 1, "yinyang": 0, "shape": "SmallSector,1,2"}


#TaoLu(name="天机掌法")
#ZhaoShi(name="藏巧", power=660, cd=1, shape=Shape(Shape.Point, 3, 0), haoqi=132, yinyang=1, style=skill.Boji, belongs=Skill.search("天机掌法"))
#ZhaoShi(name="藏拙", power=660, cd=1, shape=Shape(Shape.Point, 3, 0), haoqi=132, style=skill.Boji, belongs=Skill.search("天机掌法"))
#ZhaoShi(name="藏意", power=720, cd=2, shape=Shape(Shape.SmallSector, 1, 2), haoqi=144, style=skill.Boji, belongs=Skill.search("天机掌法"))
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
