# -- coding: utf-8 --


# ------------------------------------- 分割线：C级剑法 -------------------------------------
    
     
# 太乙玄门剑-执掌权衡
SKILL_TAIYIXUANMENJIAN_1 = \
    {"name": "执掌权衡", "style": "Jianfa",
     "mp": 120, "power": 400, "cd": 0, "yinyang": 0, "shape": "SmallSector.Emit,1,1"}
     
# 太乙玄门剑-追星赶月
SKILL_TAIYIXUANMENJIAN_2 = \
    {"name": "追星赶月", "style": "Jianfa",
     "mp": 135, "power": 450, "cd": 0, "yinyang": 0, "shape": "Line.Emit,1,2"}


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
     "mp": 300, "power": 500, "cd": 1, "yinyang": -1, "shape": "SmallSector.Emit,1,2"}


# 黄芦苦竹剑-黄芦颤叶
SKILL_HUANGLUKUZHUJIAN_1 = \
    {"name": "黄芦颤叶", "style": "Jianfa",
     "mp": 80, "power": 400, "cd": 0, "yinyang": 0, "shape": "Line.Emit,1,2"}

# 黄芦苦竹剑-苦竹摇风
SKILL_HUANGLUKUZHUJIAN_2 = \
    {"name": "苦竹摇风", "style": "Jianfa",
     "mp": 135, "power": 450, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0"}


# 细柳剑法-碧玉千条
SKILL_XILIUJIANFA_1 = \
    {"name": "碧玉千条", "style": "Jianfa",
     "mp": 126, "power": 420, "cd": 0, "yinyang": -1, "shape": "Line.Emit,1,2"}

# 细柳剑法-满城风絮
SKILL_XILIUJIANFA_2 = \
    {"name": "满城风絮", "style": "Jianfa",
     "mp": 300, "power": 500, "cd": 2, "yinyang": -1, "shape": "SmallSector.Seep,1,2",
     "effects": [{"id": "EXERT.STATUS_MUMANG", "turns": 2}]}


# ------------------------------------- 分割线：B级剑法 -------------------------------------
     
     
# 卧龙剑法-幽谷飞泉
SKILL_WOLONGJIANFA_1 = \
    {"name": "幽谷飞泉", "style": "Jianfa",
     "mp": 165, "power": 550, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,2"}

# 卧龙剑法-长沟冷月
SKILL_WOLONGJIANFA_2 = \
    {"name": "长沟冷月", "style": "Jianfa",
     "mp": 188, "power": 625, "cd": 2, "yinyang": 0, "shape": "Line.Emit,1,2"}

# 卧龙剑法-碧潭龙隐
SKILL_WOLONGJIANFA_3 = \
    {"name": "碧潭龙隐", "style": "Jianfa",
     "mp": 280, "power": 700, "cd": 3, "yinyang": 0, "shape": "BigSector.Swap,1,2"}


# 龙华剑术-指点迷津
SKILL_LONGHUAJIANSHU_1 = \
    {"name": "指点迷津", "style": "Jianfa",
     "mp": 90, "power": 550, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_SHENZHUN"}]}

# 龙华剑术-出幽入冥
SKILL_LONGHUAJIANSHU_2 = \
    {"name": "出幽入冥", "style": "Jianfa",
     "mp": 165, "power": 550, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 龙华剑术-一气冲霄
SKILL_LONGHUAJIANSHU_3 = \
    {"name": "一气冲霄", "style": "Jianfa",
     "mp": 520, "power": 650, "cd": 3, "yinyang": 0, "shape": "Point.Seep,2,1",
     "effects": [{"id": "EFFECT_ROUJIN"}]}
 
 
# 碧城剑法-栖鸾附鹤
SKILL_BICHENGJIANFA_1 = \
    {"name": "栖鸾附鹤", "style": "Jianfa",
     "mp": 91, "power": 455, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_XUHUANG"}]}
 
# 碧城剑法-紫凤放娇
SKILL_BICHENGJIANFA_2 = \
    {"name": "紫凤放娇", "style": "Jianfa",
     "mp": 151, "power": 505, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EXERT.STATUS_MIXING", "targets": "Subject", "turns": 2}]}
     
# 碧城剑法-玉轮生魄
SKILL_BICHENGJIANFA_3 = \
    {"name": "玉轮生魄", "style": "Jianfa",
     "mp": 388, "power": 555, "cd": 1, "yinyang": -1, "shape": "Around.Seep,1,1",
     "effects": [{"id": "EFFECT_GONGQI"}]}


# 霜月快剑-新月剑
SKILL_SHUANGYUEKUAIJIAN_1 = \
    {"name": "新月剑", "style": "Jianfa",
     "mp": 80, "power": 400, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_FENJIN", "targets": "Subject", "level": 100}]}

# 霜月快剑-弦月剑
SKILL_SHUANGYUEKUAIJIAN_2 = \
    {"name": "弦月剑", "style": "Jianfa",
     "mp": 80, "power": 400, "cd": 1, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_FENJIN", "targets": "Subject", "level": 100},
                 {"id": "EFFECT_ERDUANJI"}]}

# 霜月快剑-满月剑
SKILL_SHUANGYUEKUAIJIAN_3 = \
    {"name": "望月剑", "style": "Jianfa",
     "mp": 80, "power": 400, "cd": 2, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_FENJIN", "targets": "Subject", "level": 100},
                 {"id": "EFFECT_SANDUANJI"}]}


# 屯云飞烟剑-荡胸生层云
SKILL_TUNYUNFEIYANJIAN_1 = \
    {"name": "荡胸生层云", "style": "Jianfa",
     "mp": 165, "power": 550, "cd": 0, "yinyang": -1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EFFECT_GONGQI"}]}

# 屯云飞烟剑-惊风涌飞流
SKILL_TUNYUNFEIYANJIAN_2 = \
    {"name": "惊风涌飞流", "style": "Jianfa",
     "mp": 375, "power": 625, "cd": 1, "yinyang": -1, "shape": "SmallSector.Emit,1,2",
     "effects": [{"id": "EFFECT_LIANJI", "level": 30}]}

# 屯云飞烟剑-齐州九点烟
SKILL_TUNYUNFEIYANJIAN_3 = \
    {"name": "齐州九点烟", "style": "Jianfa",
     "mp": 840, "power": 700, "cd": 2, "yinyang": -1, "shape": "Around.Seep,1,2",
     "effects": [{"id": "EFFECT_CHAORAN", "targets": "Subject"}]}


# ------------------------------------- 分割线：A级剑法 -------------------------------------


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


# 渔阳剑诀-狡兔追风
SKILL_YUYANGJIANJUE_1 = \
    {"name": "狡兔追风", "style": "Jianfa",
     "mp": 140, "power": 700, "cd": 0, "yinyang": 0, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_TENGYUE"}]}

# 渔阳剑诀-醒狮顿地
SKILL_YUYANGJIANJUE_2 = \
    {"name": "醒狮顿地", "style": "Jianfa",
     "mp": 543, "power": 775, "cd": 1, "yinyang": 0, "shape": "Around.Emit,1,1",
     "effects": [{"id": "EXERT.STATUS_DUANJIN", "turns": 2}]}

# 渔阳剑诀-龙翻虎跃
SKILL_YUYANGJIANJUE_3 = \
    {"name": "龙翻虎跃", "style": "Jianfa",
     "mp": 340, "power": 850, "cd": 2, "yinyang": 0, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EXERT.STATUS_XUNJI_DA", "targets": "Subject", "turns": 2}]}


# 裴将军剑-左右交光
SKILL_PEIJIANGJUNJIAN_1 = \
    {"name": "左右交光", "style": "Jianfa",
     "mp": 302, "power": 755, "cd": 1, "yinyang": 1, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EFFECT_SHENZHUN"}]}
 
# 裴将军剑-随风游电
SKILL_PEIJIANGJUNJIAN_2 = \
    {"name": "随风游电", "style": "Jianfa",
     "mp": 252, "power": 840, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EXERT.STATUS_JUJIAN", "phase": "BeforeDamage", "turns": 2}]}
     
  
# 玉女素心剑-神女投壶
SKILL_YUNVSUXINJIAN_1 = \
    {"name": "神女投壶", "style": "Jianfa",
     "mp": 140, "power": 700, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_FEIDIAN", "turns": 2}]}
  
# 玉女素心剑-窥窗扫月
SKILL_YUNVSUXINJIAN_2 = \
    {"name": "窥窗扫月", "style": "Jianfa",
     "mp": 225, "power": 750, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EFFECT_PIAOMIAO"}]}
 
# 玉女素心剑-如虹似玉
SKILL_YUNVSUXINJIAN_3 = \
    {"name": "如虹似玉", "style": "Jianfa",
     "mp": 972, "power": 810, "cd": 2, "yinyang": -1, "shape": "BigSector.Swap,2,3,2",
     "effects": [{"id": "EFFECT_MEIRENRUYU"}]}
                 
                 
# 太岳三青峰-素手托莲
SKILL_TAIYUESANQINGFENG_1 = \
    {"name": "素手托莲", "style": "Jianfa",
     "mp": 126, "power": 630, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0"}

# 太岳三青峰-横眉观日
SKILL_TAIYUESANQINGFENG_2 = \
    {"name": "横眉观日", "style": "Jianfa",
     "mp": 220, "power": 735, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,2"}

# 太岳三青峰-高天落雁
SKILL_TAIYUESANQINGFENG_3 = \
    {"name": "高天落雁", "style": "Jianfa",
     "mp": 660, "power": 825, "cd": 3, "yinyang": 0, "shape": "Point.Seep,2,1"}


# ------------------------------------- 分割线：S级剑法 -------------------------------------


# 越女剑法-移花接木
SKILL_YUENVJIANFA_1 = \
    {"name": "移花接木", "style": "Jianfa", "targets": "Friends",
     "mp": 175, "power": 0, "cd": 2, "yinyang": -1, "shape": "Point.Emit,3,0,1",
     "effects": [{"id": "EFFECT_YIHUA"},
                 {"id": "EFFECT_HUICHUN"}]}

# 越女剑法-决云断地
SKILL_YUENVJIANFA_2 = \
    {"name": "决云断地", "style": "Jianfa",
     "mp": 270, "power": 900, "cd": 1, "yinyang": -1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EFFECT_QUEBU", "level": -400}]}

# 越女剑法-逐影追形
SKILL_YUENVJIANFA_3 = \
    {"name": "逐影追形", "style": "Jianfa",
     "mp": 200, "power": 999, "cd": 1, "yinyang": -1, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_JUEYING"},
                 {"id": "EFFECT_LIANJI"}]}


# 太极剑意-古树盘根
SKILL_TAIJIJIANYI_1 = \
    {"name": "古树盘根", "style": "Jianfa",
     "mp": 144, "power": 720, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0,1",
     "effects": [{"id": "EFFECT_PANGEN"}]}

# 太极剑意-顺水推舟
SKILL_TAIJIJIANYI_2 = \
    {"name": "顺水推舟", "style": "Jianfa",
     "mp": 240, "power": 800, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EXERT.STATUS_XUHAO", "turns": 2}]}

# 太极剑意-云摩三舞
SKILL_TAIJIJIANYI_3 = \
    {"name": "云摩三舞", "style": "Jianfa", "targets": "Grids",
     "mp": 960, "power": 0, "cd": 1, "yinyang": 0, "shape": "Point.Emit,2,2",
     "effects": [{"id": "EFFECT_YUNJIAN", "targets": "Subject", "turns": 3}]}


# 西河剑法-一剑动四方
SKILL_XIHEJIANFA_1 = \
    {"name": "一剑动四方", "style": "Jianfa",
     "mp": 595, "power": 850, "cd": 1, "yinyang": 0, "shape": "Around.Emit,1,1",
     "effects": [{"id": "EXERT.STATUS_JUJIAN", "phase": "BeforeDamage", "turns": 2}]}

# 西河剑法-羿射九日落
SKILL_XIHEJIANFA_2 = \
    {"name": "羿射九日落", "style": "Jianfa",
     "mp": 360, "power": 900, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,3",
     "effects": [{"id": "EFFECT_SHENZHUN"},
                 {"id": "EXERT.STATUS_MUMANG", "turns": 2}]}

# 西河剑法-群帝骖龙翔
SKILL_XIHEJIANFA_3 = \
    {"name": "群帝骖龙翔", "style": "Jianfa",
     "mp": 570, "power": 950, "cd": 3, "yinyang": 0, "shape": "SmallSector.Emit,1,3",
     "effects": [{"id": "EFFECT_YUWULONG"}]}


# 长空神剑-劈剑势
SKILL_CHANGKONGSHENJIAN_1 = \
    {"name": "劈剑势", "style": "Jianfa",
     "mp": 270, "power": 875, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,2"}

# 长空神剑-悬剑势
SKILL_CHANGKONGSHENJIAN_2 = \
    {"name": "悬剑势", "style": "Jianfa",
     "mp": 270, "power": 925, "cd": 2, "yinyang": 0, "shape": "Point.Emit,2,1"}

# 长空神剑-挂剑势
SKILL_CHANGKONGSHENJIAN_3 = \
    {"name": "挂剑势", "style": "Jianfa",
     "mp": 270, "power": 0, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,1"}
