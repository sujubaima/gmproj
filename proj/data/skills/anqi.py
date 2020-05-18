# -- coding: utf-8 --

# 弹弓术-射弹丸
SKILL_DANGONGSHU_1 = \
    {"name": "射弹丸", "style": "Anqi",
     "mp": 60, "power": 250, "cd": 0, "yinyang": 0, "shape": "Point.Emit,4,0,2"}
     

# 蜻蜓点水式-露荷
SKILL_QINGTINGDIANSHUISHI_1 = \
    {"name": "露荷", "style": "Anqi",
     "mp": 75, "power": 375, "cd": 0, "yinyang": -1, "shape": "Point.Emit,4,0,2"}
     
# 蜻蜓点水式-避燕
SKILL_QINGTINGDIANSHUISHI_2 = \
    {"name": "避燕", "style": "Anqi", "targets": "Friends",
     "mp": 50, "power": 0, "cd": 0, "yinyang": -1, "shape": "Around.Seep,0,0,0"}


# 璇玑图-三星照人
SKILL_XUANJITU_1 = \
    {"name": "三星照人", "style": "Anqi",
     "mp": 190, "power": 475, "cd": 0, "yinyang": -1, "shape": "Line.Seep,2,4,2"}

# 璇玑图-芙蓉印月
SKILL_XUANJITU_2 = \
    {"name": "芙蓉印月", "style": "Anqi",
     "mp": 560, "power": 560, "cd": 1, "yinyang": -1, "shape": "BigSector.Seep,3,3,3"}
     
     
# 春风九归-淡烟笼柳
SKILL_CHUNFENGJIUGUI_1 = \
    {"name": "淡烟笼柳", "style": "Anqi",
     "mp": 175, "power": 500, "cd": 0, "yinyang": -1, "shape": "Point.Seep,3,1,2",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 春风九归-回风摇蕙
SKILL_CHUNFENGJIUGUI_2 = \
    {"name": "回风摇蕙", "style": "Anqi",
     "mp": 550, "power": 550, "cd": 2, "yinyang": -1, "shape": "SmallSector.Swap,2,3,2",
     "effects": [{"id": "EFFECT_ROUJIN_DA"}]}
