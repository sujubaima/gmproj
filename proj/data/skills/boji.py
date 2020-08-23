# -- coding: utf-8 --


# ------------------------------------- 分割线：C级搏击 -------------------------------------


# 无名拳法-单体式
SKILL_WUMINGQUANFA_1 = \
    {"name": "单体式", "style": "Boji",
     "mp": 0, "power": 1, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0"}
     
# 王八拳-乱打一通
SKILL_WANGBAQUAN_1 = \
    {"name": "乱打一通", "style": "Boji",
     "mp": 0, "power": 1, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0"}
     
     
# 百缠手-软磨硬泡
SKILL_BAICHANSHOU_1 = \
    {"name": "软磨硬泡", "style": "Boji",
     "mp": 72, "power": 360, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0"}
          
# 百缠手-死缠烂打
SKILL_BAICHANSHOU_2 = \
    {"name": "死缠烂打", "style": "Boji",
     "mp": 80, "power": 400, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0"}


# 铁砂掌-崩山碎石
SKILL_TIESHAZHANG_1 = \
    {"name": "崩山碎石", "style": "Boji",
     "mp": 110, "power": 550, "cd": 0, "yinyang": 1, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EFFECT_GANGJIN_DA"}]}


# 窃钩术-妙手空空
SKILL_QIEGOUSHU_1 = \
    {"name": "妙手空空", "style": "Boji",
     "mp": 0, "power": 0, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EFFECT_TOUDAO"}]}


# ------------------------------------- 分割线：B级搏击 -------------------------------------


# 长风拳法-大风扬旗
SKILL_CHANGFENGQUANFA_1 = \
    {"name": "大风扬旗", "style": "Boji",
     "mp": 130, "power": 650, "cd": 0, "yinyang": 1, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EFFECT_GANGJIN"}]}

# 长风拳法-乘风破浪
SKILL_CHANGFENGQUANFA_2 = \
    {"name": "乘风破浪", "style": "Boji",
     "mp": 120, "power": 600, "cd": 0, "yinyang": 1, "shape": "Point.Emit,3,0",
     "effects": [{"id": "EFFECT_TENGYUE"}]}


# ------------------------------------- 分割线：A级搏击 -------------------------------------


# 幽闭三击-金屋藏春色
SKILL_YOUBISANJI_1 = \
    {"name": "金屋藏春色", "style": "Boji",
     "mp": 130, "power": 650, "cd": 0, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 幽闭三击-寒鸦带日影
SKILL_YOUBISANJI_2 = \
    {"name": "寒鸦带日影", "style": "Boji",
     "mp": 140, "power": 700, "cd": 1, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_ROUJIN"}]}

# 幽闭三击-长门悬孤月
SKILL_YOUBISANJI_3 = \
    {"name": "长门悬孤月", "style": "Boji",
     "mp": 150, "power": 750, "cd": 2, "yinyang": -1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_ROUJIN"}]}
     
     
# 混元掌-混元一气
SKILL_HUNYUANZHANG_1 = \
    {"name": "混元一气", "style": "Boji",
     "mp": 200, "power": 0, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0"}


# 醉拳-铁拐李旋踵膝撞
SKILL_ZUIQUAN_1 = \
    {"name": "铁拐李旋踵膝撞", "style": "Boji",
     "mp": 140, "power": 700, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EFFECT_ZUIYI"},
                 {"id": "EFFECT_LIANJI"}]}

# 醉拳-汉钟离跌步抱酲
SKILL_ZUIQUAN_2 = \
    {"name": "汉钟离跌步抱酲", "style": "Boji",
     "mp": 140, "power": 700, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0,2",
     "effects": [{"id": "EFFECT_ZUIYI"},
                 {"id": "EFFECT_TENGYUE"}]}

# 醉拳-张果老醉酒抛杯
SKILL_ZUIQUAN_3 = \
    {"name": "张果老醉酒抛杯", "style": "Boji",
     "mp": 140, "power": 700, "cd": 1, "yinyang": 0, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EFFECT_ZUIYI"},
                 {"id": "EFFECT_ROUJIN"}]}

# 醉拳-何仙姑弹腰献酒
SKILL_ZUIQUAN_4 = \
    {"name": "何仙姑弹腰献酒", "style": "Boji",
     "mp": 140, "power": 700, "cd": 1, "yinyang": 0, "shape": "SmallSector,1,1",
     "effects": [{"id": "EFFECT_ZUIYI"},
                 {"id": "EFFECT_PIAOMIAO"}]}
     
     
# 天机拳法-藏巧
SKILL_TIANJIQUANFA_1 = \
    {"name": "藏巧", "style": "Boji",
     "mp": 200, "power": 0, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0"}    
     
# 天机拳法-藏拙
SKILL_TIANJIQUANFA_2 = \
    {"name": "藏拙", "style": "Boji",
     "mp": 200, "power": 0, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0"}  
     
     
# 清秋指法-半山飞急雨
SKILL_QINGQIUZHIFA_1 = \
    {"name": "半山飞急雨", "style": "Boji",
     "mp": 200, "power": 0, "cd": 0, "yinyang": 1, "shape": "Point.Emit,1,0"}    
     
# 清秋指法-万木送秋声
SKILL_QINGQIUZHIFA_2 = \
    {"name": "万木送秋声", "style": "Boji",
     "mp": 200, "power": 0, "cd": 0, "yinyang": 1, "shape": "Point.Emit,1,0"} 
     
# 清秋指法-剑气倚清商
SKILL_QINGQIUZHIFA_3 = \
    {"name": "剑气倚清商", "style": "Boji",
     "mp": 200, "power": 0, "cd": 0, "yinyang": 1, "shape": "Point.Seep,1,0"}


# 大日如来掌-如来胎藏式
SKILL_DARIRULAIZHANG_1 = \
    {"name": "如来胎藏式", "style": "Boji",
     "mp": 576, "power": 720, "cd": 1, "yinyang": 0, "shape": "Point.Emit,2,1",
     "effects": [{"id":"EXERT.STATUS_JINGQUAN", "phase": "BeforeDamage", "targets": "Subject", "turns": 2},
                {"id": "EFFECT_ROUJIN"}]}

# 大日如来掌-如来金刚式
SKILL_DARIRULAIZHANG_2 = \
    {"name": "如来金刚式", "style": "Boji",
     "mp": 576, "power": 720, "cd": 1, "yinyang": 0, "shape": "Point.Emit,2,1",
     "effects": [{"id": "EXERT.STATUS_JUQUAN", "phase": "BeforeDamage", "turns": 2},
                 {"id": "EFFECT_GANGJIN"}]}


# ------------------------------------- 分割线：S级搏击 -------------------------------------


# 摩诃无量指-如恒河沙
SKILL_MOHEWULIANGZHI_1 = \
    {"name": "如恒河沙", "style": "Boji",
     "mp": 0, "power": 0, "cd": 0, "yinyang": 1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_MOHEWULIANG_XIAO"}]}

# 摩诃无量指-如阿僧祇
SKILL_MOHEWULIANGZHI_2 = \
    {"name": "如阿僧祇", "style": "Boji",
     "mp": 0, "power": 0, "cd": 1, "yinyang": 1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_MOHEWULIANG"}]}

# 摩诃无量指-如不思议
SKILL_MOHEWULIANGZHI_3 = \
    {"name": "如不思议", "style": "Boji",
     "mp": 0, "power": 0, "cd": 2, "yinyang": 1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EFFECT_MOHEWULIANG_DA"}]}


# 太极拳-野马分鬃
SKILL_TAIJIQUAN_1 = \
    {"name": "野马分鬃", "style": "Boji",
     "mp": 141, "power": 705, "cd": 0, "yinyang": 0, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EXERT.STATUS_DINGSHEN", "name": "沾连", "turns": 1}]}

# 太极拳-白鹤亮翅
SKILL_TAIJIQUAN_2 = \
    {"name": "白鹤亮翅", "style": "Boji",
     "mp": 234, "power": 780, "cd": 1, "yinyang": 0, "shape": "BigSector.Swap,1,1",
     "effects": [{"id": "EXERT.STATUS_XIEJIN", "targets": "Subject", "turns": 1}]}

# 太极拳-如封似闭
SKILL_TAIJIQUAN_3 = \
    {"name": "如封似闭", "style": "Boji",
     "mp": 1026, "power": 855, "cd": 2, "yinyang": 0, "shape": "Around.Swap,1,2",
     "effects": [{"id": "EFFECT_YUANZHUAN"},
                 {"id": "EXERT.STATUS_DINGSHEN", "name": "沾连", "turns": 1},
                 {"id": "EXERT.STATUS_XIEJIN", "targets": "Subject", "turns": 1}]}


# 降龙手-亢龙有悔
SKILL_XIANGLONGSHOU_1 = \
    {"name": "亢龙有悔", "style": "Boji",
     "mp": 165, "power": 825, "cd": 1, "yinyang": 1, "shape": "Point.Emit,2,0",
     "effects": [{"id": "EXERT.STATUS_XURUO", "name": "破攻", "turns": 2},
                 {"id": "EFFECT_GANGJIN"}]}

# 降龙手-见龙卸甲
SKILL_XIANGLONGSHOU_2 = \
    {"name": "见龙卸甲", "style": "Boji",
     "mp": 180, "power": 900, "cd": 1, "yinyang": 1, "shape": "Line.Emit,1,2",
     "effects": [{"id": "EXERT.STATUS_XIEJIA", "name": "破防", "turns": 2},
                 {"id": "EFFECT_GANGJIN"}]}

# 降龙手-龙战于野
SKILL_XIANGLONGSHOU_3 = \
    {"name": "龙战于野", "style": "Boji",
     "mp": 682, "power": 975, "cd": 2, "yinyang": 1, "shape": "Point.Emit,1,1",
     "effects": [{"id": "EXERT.STATUS_YUXUE", "name": "其血玄黄", "targets": "Subject", "turns": 2},
                 {"id": "EFFECT_GANGJIN_DA"}]}


# 五雷天音掌-天音震
SKILL_WULEITIANYINZHANG_1 = \
    {"name": "天音震", "style": "Boji",
     "mp": 141, "power": 725, "cd": 0, "yinyang": 0, "shape": "Point.Emit,2,0",
     "effects": []}

# 五雷天音掌-六神怒
SKILL_WULEITIANYINZHANG_2 = \
    {"name": "六神怒", "style": "Boji",
     "mp": 234, "power": 800, "cd": 1, "yinyang": 0, "shape": "Around.Emit,1,1",
     "effects": []}

# 五雷天音掌-五雷轰
SKILL_WULEITIANYINZHANG_3 = \
    {"name": "五雷轰", "style": "Boji",
     "mp": 1200, "power": 999, "cd": 2, "yinyang": 0, "shape": "Around.Seep,0,20",
     "effects": []}


# 大灭绝掌-成败枯荣
SKILL_DAMIEJUEZHANG_1 = \
    {"name": "成败枯荣", "style": "Boji",
     "mp": 0, "power": 0, "cd": 2, "yinyang": 0, "shape": "Point.Emit,1,0",
     "effects": [{"id": "EFFECT_KURONG"}]}
