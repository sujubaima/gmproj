# -- coding: utf-8 --

# 夜叉棍法-飞天堕地
SKILL_YECHAGUNFA_1 = \
    {"name": "飞天堕地", "style": "Changbing",
     "mp": 280, "power": 400, "cd": 0, "yinyang": 1, "shape": "Point.Emit,3,1"}

# 夜叉棍法-大力如风
SKILL_YECHAGUNFA_2 = \
    {"name": "大力如风", "style": "Changbing",
     "mp": 108, "power": 540, "cd": 0, "yinyang": 1, "shape": "Point.Emit,3,0"}
     
     
# 西楚霸王枪-以一当十
SKILL_XICHUBAWANGQIANG_1 = \
    {"name": "以一当十", "style": "Changbing",
     "mp": 400, "power": 500, "cd": 2, "yinyang": 0, "shape": "BigSector.Swap,1,2"}

# 西楚霸王枪-破釜沉舟
SKILL_XICHUBAWANGQIANG_2 = \
    {"name": "破釜沉舟", "style": "Changbing",
     "mp": 180, "power": 600, "cd": 2, "yinyang": 0, "shape": "Line.Emit,1,3"}

# 西楚霸王枪-霸王别姬
SKILL_XICHUBAWANGQIANG_3 = \
    {"name": "霸王别姬", "style": "Changbing",
     "mp": 140, "power": 700, "cd": 1, "yinyang": 0, "shape": "Point.Emit,3,0"}
     
     
# 十力降魔棍-十力具备
SKILL_SHILIXIANGMOGUN_1 = \
    {"name": "十力具备", "style": "Changbing",
     "mp": 142, "power": 710, "cd": 0, "yinyang": 1, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_GANGJIN_DA"}]}

# 十力降魔棍-泰然无惧
SKILL_SHILIXIANGMOGUN_2 = \
    {"name": "泰然无惧", "style": "Changbing",
     "mp": 240, "power": 800, "cd": 2, "yinyang": 1, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EXERT.STATUS_WUWEI", "targets": "Subject", "turns": 2}]}


# 打狗棒法-棒打狗头
SKILL_DAGOUBANGFA_1 = \
    {"name": "棒打狗头", "style": "Changbing",
     "mp": 183, "power": 865, "cd": 1, "yinyang": 0, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_DAGOUTOU", "turns": 1}]}

# 打狗棒法-獒口夺杖
SKILL_DAGOUBANGFA_2 = \
    {"name": "獒口夺杖", "style": "Changbing",
     "mp": 150, "power": 750, "cd": 0, "yinyang": 0, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_BAGOUYA", "turns": 1}]}

# 打狗棒法-天下无狗
SKILL_DAGOUBANGFA_3 = \
    {"name": "天下无狗", "style": "Changbing",
     "mp": 1006, "power": 838, "cd": 2, "yinyang": 0, "shape": "Around.Seep,1,3",
     "effects": [{"id": "EFFECT_DUANGOUWO"}]}
