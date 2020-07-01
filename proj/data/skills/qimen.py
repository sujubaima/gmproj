# -- coding: utf-8 --

# 天罡刺-虹铃暗法
SKILL_TIANGANGCI_1 = \
    {"name": "虹铃暗法", "style": "Duanbing",
     "mp": 80, "power": 400, "cd": 0, "yinyang": 1, "shape": "Point.Emit,1,0"}
     
# 天罡刺-燕雀穿枝
SKILL_TIANGANGCI_2 = \
    {"name": "燕雀穿枝", "style": "Duanbing",
     "mp": 80, "power": 400, "cd": 0, "yinyang": 1, "shape": "Point.Emit,1,0"}
     
     
# 越人歌-今夕何夕
SKILL_YUERENGE_1 = \
    {"name": "今夕何夕", "style": "Yueqi,Duanbing", "targets": "Friends",
     "mp": 150, "power": 0, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_HUICHUN", "level": 800},
                 {"id": "EFFECT_TONGXIN", "level": 20}]}
     
# 越人歌-搴舟中流
SKILL_YUERENGE_2 = \
    {"name": "搴舟中流", "style": "Yueqi,Duanbing",
     "mp": 150, "power": 725, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_FUXIN", "level": 20}]}

# 越人歌-山木有枝
SKILL_YUERENGE_3 = \
    {"name": "山木有枝", "style": "Yueqi", "targets": "All",
     "mp": 150, "power": 0, "cd": 2, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_LIANZHI"}]}
     

# 天雷地火引-起萍生浪
SKILL_TIANLEIDIHUOYIN_1 = \
    {"name": "起萍生浪", "style": "Yueqi",
     "mp": 175, "power": 850, "cd": 0, "yinyang": -1, "shape": "Point.Seep,99,0",
     "effects": [{"id": "EFFECT_GUHUO_EXERT"}]}

## 天雷地火引-野火春风
#SKILL_TIANLEIDIHUOYIN_2 = \
#    {"name": "野火春风", "style": "Yueqi",
#     "mp": 720, "power": 825, "cd": 1, "yinyang": 1, "shape": "SmallSector.Seep,1,3"}

# 天雷地火引-火泻雷嗔
SKILL_TIANLEIDIHUOYIN_3 = \
    {"name": "火泻雷嗔", "style": "Yueqi",
     "mp": 577, "power": 875, "cd": 3, "yinyang": 0, "shape": "Point.Seep,99,2"}


# 日月双轮-偷天换日
SKILL_RIYUESHUANGLUN_1 = \
    {"name": "偷天换日", "style": "Duanbing",
     "mp": 480, "power": 650, "cd": 0, "yinyang": 1, "shape": "BigSector.Swap,1,2",
     "effects": [{"id": "EFFECT_RIRU"}]}

# 日月双轮-月落参横
SKILL_RIYUESHUANGLUN_2 = \
    {"name": "月落参横", "style": "Duanbing",
     "mp": 480, "power": 650, "cd": 0, "yinyang": -1, "shape": "BigSector.Swap,1,2",
     "effects": [{"id": "EFFECT_PINGDAN"}]}

# 日月双轮-日月争辉
SKILL_RIYUESHUANGLUN_3 = \
    {"name": "日月争辉", "style": "Duanbing", "double_weapon": ["Duanbing", "Duanbing"],
     "mp": 840, "power": 750, "cd": 0, "yinyang": 0, "shape": "Around.Swap,1,2",
     "effects": [{"id": "EFFECT_RIYUEZHENGHUI"}]}
