# -- coding: utf-8 --
    
     
# 太乙玄门剑-执掌权衡
SKILL_TAIYIXUANMENJIAN_1 = \
    {"name": "执掌权衡", "style": "Jianfa",
     "mp": 80, "power": 400, "cd": 0, "yinyang": 0, "shape": "SmallSector.Emit,1,1"}
     
# 太乙玄门剑-追星赶月
SKILL_TAIYIXUANMENJIAN_2 = \
    {"name": "追星赶月", "style": "Jianfa",
     "mp": 100, "power": 450, "cd": 0, "yinyang": 0, "shape": "Line.Emit,1,3"}
     
     
# 卧龙剑法-幽谷飞泉
SKILL_WOLONGJIANFA_1 = \
    {"name": "幽谷飞泉", "style": "Jianfa",
     "mp": 110, "power": 550, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,2"}

# 卧龙剑法-长沟冷月
SKILL_WOLONGJIANFA_2 = \
    {"name": "长沟冷月", "style": "Jianfa",
     "mp": 188, "power": 625, "cd": 2, "yinyang": 0, "shape": "Line.Emit,1,3"}

# 卧龙剑法-碧潭龙隐
SKILL_WOLONGJIANFA_3 = \
    {"name": "碧潭龙隐", "style": "Jianfa",
     "mp": 560, "power": 700, "cd": 3, "yinyang": 0, "shape": "BigSector.Swap,1,2"}


# 天音剑气-空谷传声
SKILL_TIANYINJIANQI_1 = \
    {"name": "空谷传声", "style": "Qimen",
     "mp": 120, "power": 600, "cd": 1, "yinyang": -1, "shape": "Point.Seep,4,1"}

# 天音剑气-风送轻云
SKILL_TIANYINJIANQI_2 = \
    {"name": "风送轻云", "style": "Qimen",
     "mp": 270, "power": 675, "cd": 2, "yinyang": 0, "shape": "Line.Seep,1,4"}

# 天音剑气-振索鸣铃
SKILL_TIANYINJIANQI_3 = \
    {"name": "振索鸣铃", "style": "Qimen",
     "mp": 900, "power": 750, "cd": 3, "yinyang": 0, "shape": "Around.Seep,1,99"}


# 龙华剑术-指点迷津
SKILL_LONGHUAJIANSHU_1 = \
    {"name": "指点迷津", "style": "Jianfa",
     "mp": 90, "power": 550, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_SHENZHUN"}]}

# 龙华剑术-出幽入冥
SKILL_LONGHUAJIANSHU_2 = \
    {"name": "出幽入冥", "style": "Jianfa",
     "mp": 165, "power": 550, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 龙华剑术-一气冲霄
SKILL_LONGHUAJIANSHU_3 = \
    {"name": "一气冲霄", "style": "Jianfa",
     "mp": 455, "power": 650, "cd": 3, "yinyang": 0, "shape": "Point.Seep,2,1",
     "effects": [{"id": "EFFECT_ROUJIN"}]}
 
 
# 同归剑法-一别两宽
SKILL_TONGGUIJIANFA_1 = \
    {"name": "一别两宽", "style": "Jianfa",
     "mp": 140, "power": 700, "cd": 2, "yinyang": 0, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_FENDUAN_EXERT", "turns": 2}]}
     
# 同归剑法-殊途同归
SKILL_TONGGUIJIANFA_2 = \
    {"name": "殊途同归", "style": "Jianfa",
     "mp": 170, "power": 825, "cd": 2, "yinyang": 0, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_TONGGUI_EXERT", "turns": 2}]}


# 兰阳剑法-兰之猗猗
SKILL_LANYANGJIANFA_1 = \
    {"name": "兰之猗猗", "style": "Jianfa",
     "mp": 70, "power": 350, "cd": 0, "yinyang": -1, "shape": "Point.Emit,1,0"}

# 兰阳剑法-不采而佩
SKILL_LANYANGJIANFA_2 = \
    {"name": "不采而佩", "style": "Jianfa",
     "mp": 85, "power": 425, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0"}

# 兰阳剑法-君子之守
SKILL_LANYANGJIANFA_3 = \
    {"name": "君子之守", "style": "Jianfa",
     "mp": 250, "power": 500, "cd": 1, "yinyang": -1, "shape": "SmallSector.Emit,1,2"}
     
     
# 黄芦苦竹剑-黄芦颤叶
SKILL_HUANGLUKUZHUJIAN_1 = \
    {"name": "黄芦颤叶", "style": "Jianfa",
     "mp": 70, "power": 400, "cd": 0, "yinyang": 0, "shape": "Line.Emit,1,2"}

# 黄芦苦竹剑-苦竹摇风
SKILL_HUANGLUKUZHUJIAN_2 = \
    {"name": "苦竹摇风", "style": "Jianfa",
     "mp": 90, "power": 450, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0"}


# 细柳剑法-碧玉千条
SKILL_XILIUJIANFA_1 = \
    {"name": "碧玉千条", "style": "Jianfa",
     "mp": 126, "power": 420, "cd": 0, "yinyang": -1, "shape": "Line.Emit,1,3"}

# 细柳剑法-满城风絮
SKILL_XILIUJIANFA_2 = \
    {"name": "满城风絮", "style": "Jianfa",
     "mp": 450, "power": 500, "cd": 2, "yinyang": -1, "shape": "SmallSector.Seep,1,2",
     "effects": [{"id": "EXERT.STATUS_MUMANG", "turns": 2}]}
 
 
# 碧城剑法-栖鸾附鹤
SKILL_BICHENGJIANFA_1 = \
    {"name": "栖鸾附鹤", "style": "Jianfa",
     "mp": 91, "power": 455, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_XUHUANG"}]}
 
# 碧城剑法-紫凤放娇
SKILL_BICHENGJIANFA_2 = \
    {"name": "紫凤放娇", "style": "Jianfa",
     "mp": 157, "power": 505, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EXERT.STATUS_MIXING", "targets": "Subject", "turns": 2}]}
     
# 碧城剑法-玉轮生魄
SKILL_BICHENGJIANFA_3 = \
    {"name": "玉轮生魄", "style": "Jianfa",
     "mp": 333, "power": 555, "cd": 1, "yinyang": -1, "shape": "Around.Seep,1,1",
     "effects": [{"id": "EFFECT_GONGQI"}]}
     

# 裴将军剑-左右交光
SKILL_PEIJIANGJUNJIAN_1 = \
    {"name": "左右交光", "style": "Jianfa",
     "mp": 227, "power": 755, "cd": 1, "yinyang": 1, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_SHENZHUN"}]}
 
# 裴将军剑-随风游电
SKILL_PEIJIANGJUNJIAN_2 = \
    {"name": "随风游电", "style": "Jianfa",
     "mp": 249, "power": 830, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EXERT.STATUS_JUJIAN", "phase": "BeforeDamage", "turns": 2}]}
     
  
# 玉女素心剑-神女投壶
SKILL_YUNVSUXINJIAN_1 = \
    {"name": "神女投壶", "style": "Jianfa",
     "mp": 227, "power": 755, "cd": 1, "yinyang": 1, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_SHENZHUN"}]}
  
# 玉女素心剑-虚风扫月
SKILL_YUNVSUXINJIAN_2 = \
    {"name": "虚风扫月", "style": "Jianfa",
     "mp": 227, "power": 755, "cd": 1, "yinyang": 1, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_SHENZHUN"}]}
 
# 玉女素心剑-如虹似玉
SKILL_YUNVSUXINJIAN_3 = \
    {"name": "如虹似玉", "style": "Jianfa",
     "mp": 249, "power": 830, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EXERT.STATUS_JUJIAN", "phase": "BeforeDamage", "turns": 2}]}
     
                 
                 
# 太岳三青峰-素手托莲
SKILL_TAIYUESANQINGFENG_1 = \
    {"name": "素手托莲", "style": "Jianfa",
     "mp": 126, "power": 630, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0"}

# 太岳三青峰-横眉观日
SKILL_TAIYUESANQINGFENG_2 = \
    {"name": "横眉观日", "style": "Jianfa",
     "mp": 147, "power": 735, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,3"}

# 太岳三青峰-高天落雁
SKILL_TAIYUESANQINGFENG_3 = \
    {"name": "高天落雁", "style": "Jianfa",
     "mp": 577, "power": 825, "cd": 3, "yinyang": 0, "shape": "Point.Seep,2,1"}


# 越女剑法-移花接木
SKILL_YUENVJIANFA_1 = \
    {"name": "移花接木", "style": "Jianfa", "targets": "Friends",
     "mp": 180, "power": 0, "cd": 2, "yinyang": -1, "shape": "Point.Emit,3,0,1",
     "effects": [{"id": "EFFECT_YIHUA"},
                 {"id": "EFFECT_HUICHUN"}]}

# 越女剑法-决云断地
SKILL_YUENVJIANFA_2 = \
    {"name": "决云断地", "style": "Jianfa",
     "mp": 270, "power": 900, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EFFECT_QUEBU", "level": 250}]}

# 越女剑法-逐影追形
SKILL_YUENVJIANFA_3 = \
    {"name": "逐影追形", "style": "Jianfa",
     "mp": 200, "power": 999, "cd": 1, "yinyang": -1, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_JUEYING"},
                 {"id": "EFFECT_LIANJI"}]}


# 太极剑意-古树盘根
SKILL_TAIJIJIANYI_1 = \
    {"name": "古树盘根", "style": "Jianfa",
     "mp": 180, "power": 720, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0,1",
     "effects": [{"id": "EFFECT_PANGEN"}]}

# 太极剑意-顺水推舟
SKILL_TAIJIJIANYI_2 = \
    {"name": "顺水推舟", "style": "Jianfa",
     "mp": 270, "power": 800, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EXERT.STATUS_XUHAO", "turns": 2}]}

# 太极剑意-云摩三舞
SKILL_TAIJIJIANYI_3 = \
    {"name": "云摩三舞", "style": "Jianfa", "targets": "Grids",
     "mp": 960, "power": 0, "cd": 1, "yinyang": 0, "shape": "Point.Emit,2,2",
     "effects": [{"id": "EFFECT_JIANYUN", "targets": "Subject", "turns": 3}]}


# 西河剑法-一剑动四方
SKILL_XIHEJIANFA_1 = \
    {"name": "一剑动四方", "style": "Jianfa", "targets": "Friends",
     "mp": 180, "power": 0, "cd": 2, "yinyang": 0, "shape": "Point.Emit,3,0,1",
     "effects": [{"id": "EFFECT_YIHUA"},
                 {"id": "EFFECT_HUICHUN"}]}

# 西河剑法-羿射九日落
SKILL_XIHEJIANFA_2 = \
    {"name": "羿射九日落", "style": "Jianfa",
     "mp": 270, "power": 900, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EFFECT_QUEBU", "level": 250}]}

# 西河剑法-群帝骖龙翔
SKILL_XIHEJIANFA_3 = \
    {"name": "群帝骖龙翔", "style": "Jianfa",
     "mp": 200, "power": 999, "cd": 1, "yinyang": 0, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_JUEYING"},
                 {"id": "EFFECT_LIANJI"}]}


# 长空神剑-劈剑势
SKILL_CHANGKONGSHENJIAN_1 = \
    {"name": "劈剑势", "style": "Jianfa",
     "mp": 270, "power": 850, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,3"}

# 长空神剑-悬剑势
SKILL_CHANGKONGSHENJIAN_2 = \
    {"name": "悬剑势", "style": "Jianfa",
     "mp": 270, "power": 875, "cd": 2, "yinyang": 0, "shape": "Point.Emit,2,1"}

# 长空神剑-挂剑势
SKILL_CHANGKONGSHENJIAN_3 = \
    {"name": "挂剑势", "style": "Jianfa",
     "mp": 270, "power": 0, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,1"}
