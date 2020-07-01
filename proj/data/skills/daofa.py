# -- coding: utf-8 --

# 鸾影刀法-鸣鸾佩玉
SKILL_LUANYINGDAOFA_1 = \
    {"name": "鸣鸾佩玉", "style": "Daofa",
     "mp": 85, "power": 425, "cd": 0, "yinyang": -1, "shape": "BigSector.Swap,1,1"}
     
# 鸾影刀法-鸾光两破
SKILL_LUANYINGDAOFA_2 = \
    {"name": "鸾光两破", "style": "Daofa",
     "mp": 104, "power": 520, "cd": 0, "yinyang": -1, "shape": "SmallSector.Swap,1,2"}
     

# 拨云见日刀-云归穴暝 
SKILL_BOYUNJIANRIDAO_1 = \
    {"name": "云归穴暝", "style": "Daofa",
     "mp": 80, "power": 400, "cd": 0, "yinyang": 1, "shape": "Point.Emit,2,0"}

# 拨云见日刀-日出天开
SKILL_BOYUNJIANRIDAO_2 = \
    {"name": "日出天开", "style": "Daofa",
     "mp": 150, "power": 500, "cd": 0, "yinyang": 1, "shape": "BigSector.Swap,1,1"}
     
     
# 黑风刀-黑云压城
SKILL_HEIFENGDAO_1 = \
    {"name": "黑云压城", "style": "Daofa",
     "mp": 225, "power": 450, "cd": 1, "yinyang": -1, "shape": "SmallSector.Swap,1,2",
     "effects": [{"id": "EFFECT_ZHANGQI_XIAO", "from_damage": True}]}

# 黑风刀-阴风阵阵
SKILL_HEIFENGDAO_2 = \
    {"name": "阴风阵阵", "style": "Daofa",
     "mp": 360, "power": 450, "cd": 1, "yinyang": -1, "shape": "BigSector.Swap,1,2",
     "effects": [{"id": "EFFECT_ZHANGQI", "from_damage": True}]}


# 分筋析骨刀-分筋刀
SKILL_FENJINXIGUDAO_1 = \
    {"name": "分筋刀", "style": "Daofa",
     "mp": 100, "power": 500, "cd": 0, "yinyang": -1, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EXERT.STATUS_DUANJIN", "turns": 3}]}

# 分筋析骨刀-析骨刀
SKILL_FENJINXIGUDAO_2 = \
    {"name": "析骨刀", "style": "Daofa",
     "mp": 100, "power": 500, "cd": 0, "yinyang": -1, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EXERT.STATUS_CUOGU", "turns": 3}]}


# 飞廉刀法-迎风斩
SKILL_FEILIANDAOFA_1 = \
    {"name": "迎风斩", "style": "Daofa",
     "mp": 165, "power": 550, "cd": 1, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_YINGFENG"}]}

# 飞廉刀法-逆风斩
SKILL_FEILIANDAOFA_2 = \
    {"name": "逆风斩", "style": "Daofa",
     "mp": 165, "power": 550, "cd": 1, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_NIFENG"}]}


# 破锋八刀-剑锋破尽
SKILL_POFENGBADAO_1 = \
    {"name": "剑锋破尽", "style": "Daofa",
     "mp": 165, "power": 550, "cd": 2, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_CHUJIAN"}]}

# 破锋八刀-枪锋破尽
SKILL_POFENGBADAO_2 = \
    {"name": "枪锋破尽", "style": "Daofa",
     "mp": 165, "power": 550, "cd": 2, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_CHUQIANG"}]}

# 破锋八刀-奇锋破尽
SKILL_POFENGBADAO_3 = \
    {"name": "奇锋破尽", "style": "Daofa",
     "mp": 165, "power": 550, "cd": 2, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_CHUQI"}]}


# 刀剑攻-上刀下剑法
SKILL_DAOJIANGONG_1 = \
    {"name": "上刀下剑法", "style": "Jianfa,Daofa", "double_weapon": ["Daofa", "Jianfa"],
     "mp": 295, "power": 650, "cd": 0, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_POJIAN"}]}

# 刀剑攻-上剑下刀法
SKILL_DAOJIANGONG_2 = \
    {"name": "上剑下刀法", "style": "Jianfa,Daofa", "double_weapon": ["Daofa", "Jianfa"],
     "mp": 130, "power": 650, "cd": 0, "yinyang": 0, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EFFECT_PODAO"}]}

# 刀剑攻-刀剑合一法
SKILL_DAOJIANGONG_3 = \
    {"name": "刀剑合一法", "style": "Jianfa,Daofa", "double_weapon": ["Daofa", "Jianfa"],
     "mp": 375, "power": 750, "cd": 2, "yinyang": 0, "shape": "SmallSector,1,2",
     "effects": [{"id": "EXERT.STATUS_JINGJIAN", "targets": "Subject", "turns": 1},
                 {"id": "EXERT.STATUS_JINGDAO", "targets": "Subject", "turns": 1}]}
     
     
# 猩红刀法-含血喷人
SKILL_XINGHONGDAOFA_1 = \
    {"name": "含血喷人", "style": "Daofa",
     "mp": 300, "power": 600, "cd": 1, "yinyang": -1, "shape": "SmallSector.Emit,1,2"}

# 猩红刀法-磨牙吮血
SKILL_XINGHONGDAOFA_2 = \
    {"name": "磨牙吮血", "style": "Daofa",
     "mp": 150, "power": 750, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_XIXUE_DA"}]}

# 猩红刀法-血雨腥风
SKILL_XINGHONGDAOFA_3 = \
    {"name": "血雨腥风", "style": "Daofa",
     "mp": 960 , "power": 800, "cd": 3, "yinyang": -1, "shape": "Around.Seep,1,2",
     "effects": [{"id": "EFFECT_XIXUE"}]}
