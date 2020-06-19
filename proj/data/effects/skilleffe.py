# -- coding: utf-8 --

EFFECT_EXERT = {"name": "", "module": "proj.entity.effect", "class": "ExcertEffect"}


# 拔狗牙
EFFECT_BAGOUYA = \
    {"name": "拔狗牙",
     "module": "proj.builtin.effects", "class": "BaGouYaEffect"}


# 打狗头
EFFECT_DAGOUTOU = \
    {"name": "打狗头",
     "module": "proj.builtin.effects", "class": "DaGouTouEffect"}

# 拔山劲    
EFFECT_BASHANJIN = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "attack_factor_", "ratio": 1.25}]}


# 病心
EFFECT_BINGXIN = \
    {"name": "病心", "style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "hp_recover_rate_", "value": 0, "locked": True}]}


# 尝胆
EFFECT_CHANGDAN = \
    {"name": "尝胆", "style": 1,
     "module": "proj.builtin.effects", "class": "ChangDanEffect"}

EFFECT_CHANGDAN_ANONYMOUS = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "critical_rate_", "delta": 0.03}]}


# 错骨
EFFECT_CUOGU = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "motion_", "delta": -1}]}


# 定身
EFFECT_DINGSHEN = \
    {"style": 1, "module": "proj.builtin.effects", "class": "JinYongEffect", "action": "Move"}


# 弃武
EFFECT_QIWU = \
    {"style": 1, "module": "proj.builtin.effects", "class": "JinYongEffect", "action": "Attack"}


# 断筋
EFFECT_DUANJIN = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "speed_factor_", "ratio": 0.6}]}


# 飞电
EFFECT_FEIDIAN = \
    {"name": "飞电", "style": 1, 
     "module": "proj.builtin.effects", "class": "FeiDianEffect"}


# 负心
EFFECT_FUXIN = \
    {"name": "负心", "style": 0,
     "module": "proj.builtin.effects", "class": "TongXinEffect",
     "text": "对{object}的伤害提升了",
     "description": "自身与目标共同拥有的状态数越多，伤害量越高"}


# 攻气
EFFECT_GONGQI = \
    {"name": "攻气", "style": 0,
     "module": "proj.builtin.effects", "class": "GongQiEffect", "level": 20,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "额外造成{mp_drain}点内力伤害",
     "description": "一定比例的伤害追加为内力伤害，颖悟值越高比例越大"}

EFFECT_GONGQI_XIAO = \
    {"name": "小攻气", "style": 0,
     "module": "proj.builtin.effects", "class": "GongQiEffect", "level": 10,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "额外造成{mp_drain}点内力伤害",
     "description": "较小比例的伤害追加为内力伤害，颖悟值越高比例越大"}

EFFECT_GONGQI_DA = \
    {"name": "大攻气", "style": 0,
     "module": "proj.builtin.effects", "class": "GongQiEffect", "level": 30,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "额外造成{mp_drain}点内力伤害",
     "description": "较高比例的伤害追加为内力伤害，颖悟值越高比例越大"}


# 豪气干云
EFFECT_HAOQIGANYUN = \
    {"name": "豪气干云", "style": 1,
     "module": "proj.builtin.effects", "class": "HaoQiGanYunEffect"}

EFFECT_HAOQIGANYUN_ANONYMOUS = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "speed_", "delta": 10}]}


# 含颦
EFFECT_HANPIN = \
    {"name": "含颦", "style": 1,
     "module": "proj.builtin.effects", "class": "HanPinEffect"}

EFFECT_HANPIN_ANONYMOUS = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "dodge_rate_", "delta": 0.03}]}

EFFECT_HANPIN_ANONYMOUS_DA = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "dodge_rate_", "delta": 0.05}]}


# 换骨
EFFECT_HUANGU = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "HuanGuEffect", "level": 20}

EFFECT_HUANGU_ANONYMOUS = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "counter_rate_", "delta": 0.01},
               {"name": "critical_rate_", "delta": 0.01},
               {"name": "dodge_rate_", "delta": 0.01},
               {"name": "anti_damage_rate_", "delta": 0.01}]}


# 回春
EFFECT_HUICHUN = \
    {"name": "回春", "style": 1,
     "module": "proj.builtin.effects", "class": "HuiChunEffect", "level": 2000,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "为{object}回复了{recover}点气血",
     "description": "为目标回复气血，颖悟值越高回复效果越佳"}


# 刚劲
EFFECT_GANGJIN = \
    {"name": "刚劲", "style": 0,
     "module": "proj.builtin.effects", "class": "GangJinEffect", "level": 30,
     "influence": "Gang", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{injury}点外伤",
     "description": "一定比例的伤害追加为外伤，刚猛值越高效果越佳"}

EFFECT_GANGJIN_XIAO = \
    {"name": "小刚劲", "style": 0,
     "module": "proj.builtin.effects", "class": "GangJinEffect", "level": 15,
     "influence": "Gang", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{injury}点外伤",
     "description": "较小比例的伤害追加为外伤，刚猛值越高效果越佳"}

EFFECT_GANGJIN_DA = \
    {"name": "大刚劲", "style": 0, 
     "module": "proj.builtin.effects", "class": "GangJinEffect", "level": 45,
     "influence": "Gang", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{injury}点外伤",
     "description": "较大比例的伤害追加为外伤，刚猛值越高效果越佳"}


EFFECT_JITUI = \
    {"name": "击退", "style": 0,
     "module": "proj.builtin.effects", "class": "JiTuiEffect",
     "text": "{object}被击退1格",
     "description": "攻击命中时目标单位会后退一格"}


# 云剑
EFFECT_YUNJIAN = \
    {"name": "云剑", "style": 1,
     "module": "proj.builtin.effects", "class": "YunJianEffect",
     "text": "在{location}及其周边地块施放了剑气",
     "description": "在目标及其周边2格地块施放一团剑气，在该区域内停留的敌方单位均会遭受伤害"}

EFFECT_YUNJIAN_ANONYMOUS = \
    {"name": "云剑", "style": 1,
     "module": "proj.builtin.effects", "class": "YunJianAnonymousEffect",
     "text": "{object}在剑气中受到{hp_delta}点伤害"}


# 金关玉锁     
EFFECT_BIJINGUAN = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "hp_max_factor_", "ratio": 1.2}]}

EFFECT_KOUYUSUO = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "mp_max_factor_", "ratio": 1.2}]}
     
     
# 金钟罩
EFFECT_TONGPITIEGU = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "anti_injury_rate_", "value": 0, "locked": True}]}

EFFECT_JINGANGBUHUAI = \
    {"name": "金钟罩", "style": 1, "module": "proj.builtin.effects", "class": "JinGangBuHuaiEffect",
     "influence": "Gang", "factor_middle": 1, "factor_upper": 1.5,
     "text": "伤害减为1点"}


# 惧剑
EFFECT_JUJIAN = \
    {"style": 1, "module": "proj.builtin.effects", "class": "JuWuEffect", "level": 30, "skill_style": "Jianfa",
     "text": "{object}被剑法类武学攻击时会受到更多伤害",
     "description": "被剑法类武学攻击时受到更多伤害"}


# 涓流
EFFECT_JUANLIU = \
    {"style": 0, "module": "proj.builtin.effects", "class": "JuanLiuEffect"}


# 迷形
EFFECT_MIXING = \
    {"name": "迷形", "style": 1, 
     "module": "proj.builtin.effects", "class": "MiXingEffect",
     "text": "{attacker}背向了{subject}",
     "description": "对方攻击自身后会背向目标"}


# 美人如玉
EFFECT_MEIRENRUYU = \
    {"name": "美人如玉", "style": 0,
     "module": "proj.builtin.effects", "class": "MeiRenRuYuEffect",
     "description": "对男性角色伤害大幅增加"}


# 摩诃无量
EFFECT_MOHEWULIANG_XIAO = \
    {"name": "恒河沙数", "style": 0, "module": "proj.builtin.effects", "class": "MoHeWuLiangEffect", "level": 2,
     "description": "本次攻击伤害为当前战斗除本武学外，所有打出的伤害中排名第三高的数值，内力消耗视伤害与内功修为而定"}

EFFECT_MOHEWULIANG = \
    {"name": "阿僧祇数", "style": 0, "module": "proj.builtin.effects", "class": "MoHeWuLiangEffect", "level": 1,
     "description": "本次攻击伤害为当前战斗除本武学外，所有打出伤害里中排名第二高的数值，内力消耗视伤害与内功修为而定"}

EFFECT_MOHEWULIANG_DA = \
    {"name": "不思议数", "style": 0, "module": "proj.builtin.effects", "class": "MoHeWuLiangEffect", "level": 0,
     "description": "本次攻击伤害为当前战斗除本武学外，所有打出的伤害中排名第一高的数值，内力消耗视伤害与内功修为而定"}


# 目盲
EFFECT_MUMANG = \
    {"style": 0, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "influence": "Rou", "factor_lower": 1.2, "factor_middle": 1,
     "attrs": [{"name": "hit_rate_factor_", "ratio": 0.8}]}

EFFECT_MUMANG_DA = \
    {"style": 0, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "influence": "Rou", "factor_lower": 1.2, "factor_middle": 1,
     "attrs": [{"name": "hit_rate_factor_", "ratio": 0.6}]}


# 逆脉     
EFFECT_NIMAI_ATTACK = \
    {"name": "逆脉", "style": 1,
     "module": "proj.builtin.effects", "class": "NiMaiAttackEffect",
     "text": "攻击的内力消耗转换为气血消耗，同时自身受到一定程度内伤",
     "description": "攻击时有一定几率将耗气改为耗血，但自身会受到一定程度内伤"}

EFFECT_NIMAI_DEFENSE = \
    {"name": "逆脉", "style": 1,
     "module": "proj.builtin.effects", "class": "NiMaiDefenseEffect",
     "text": "防御的气血消耗转换为内力消耗，同时自身受到一定程度内伤",
     "description": "防御时有一定几率将耗血改为耗气，但自身会受到一定程度内伤"}


# 缥缈
EFFECT_PIAOMIAO = \
    {"name": "缥缈", "style": 2,
     "module": "proj.builtin.effects", "class": "PiaoMiaoEffect",
     "text": "{subject}后退了一格",
     "description": "攻击前后退一格"}


# 盘根
EFFECT_PANGEN = \
    {"name": "盘根", "style": 1,
     "module": "proj.builtin.effects", "class": "PanGenEffect",
     "text": "移除了{status}状态",
     "description": "若攻击前未发生移动，可随机移除自身一个负面状态"}


# 柔劲
EFFECT_ROUJIN = \
    {"name": "柔劲", "style": 0,
     "module": "proj.builtin.effects", "class": "RouJinEffect", "level": 30,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{wound}点内伤",
     "description": "一定比例的伤害追加为内伤，柔易值越高效果越佳"}

EFFECT_ROUJIN_XIAO = \
    {"name": "小柔劲", "style": 0,
     "module": "proj.builtin.effects", "class": "RouJinEffect", "level": 15,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{wound}点内伤",
     "description": "较小比例的伤害追加为内伤，柔易值越高效果越佳"}

EFFECT_ROUJIN_DA = \
    {"name": "大柔劲", "style": 0,
     "module": "proj.builtin.effects", "class": "RouJinEffect", "level": 45,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{wound}点内伤",
     "description": "较大比例的伤害追加为内伤，柔易值越高效果越佳"}


# 太极神功
EFFECT_TAIJIJIN = \
    {"name": "太极劲", "style": 1,
     "module": "proj.builtin.effects", "class": "TaiJiJinEffect"}

EFFECT_QINGFENGFUSHANGANG = \
    {"name": "清风拂山冈", "style": 1,
     "influlence": "Rou", "factor_middle": 1, "factor_upper": 2,
     "module": "proj.builtin.effects", "class": "QingFengFuShanGangEffect",
     "text": "对{object}施加了{wound}点内伤"}

EFFECT_MINGYUEZHAODAJIANG = \
    {"name": "明月照大江", "style": 1,
     "module": "proj.builtin.effects", "class": "MingYueZhaoDaJiangEffect"}

EFFECT_MINGYUEZHAODAJIANG_LEAVE = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "MingYueZhaoDaJiangLeaveEffect"}

EFFECT_MINGYUEZHAODAJIANG_ANONYMOUS = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "counter_rate_factor_", "ratio": 1}],
     "influence": "Jing", "factor_middle": 1, "factor_upper": 2}


# 端狗窝
EFFECT_DUANGOUWO = \
    {"name": "端狗窝",
     "module": "proj.builtin.effects", "class": "DuanGouWoEffect",
     "description": "攻击范围内敌方单位越多，伤害越高"}


# 屠狗
EFFECT_TUGOU = \
    {"name": "屠狗", "style": 1,
     "module": "proj.builtin.effects", "class": "TuGouEffect"}


# 无畏
EFFECT_WUWEI = \
    {"name": "无畏",
     "module": "proj.builtin.effects", "class": "WuWeiEffect",
     "text": "受到的伤害降低了"}

# 吸髓
EFFECT_XISUI = \
    {"name": "吸髓", "style": 0,
     "module": "proj.builtin.effects", "class": "XiSuiEffect", "level": 20,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "从施加的伤害中吸取了{mp_drain}点内力",
     "description": "施加的伤害一部分转为内力伤害，并将这部分内力吸收，颖悟值越高吸髓效果越佳"}

EFFECT_XISUI_XIAO = \
    {"name": "小吸髓", "style": 0,
     "module": "proj.builtin.effects", "class": "XiSuiEffect", "level": 10,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "从施加的伤害中吸取了{mp_drain}点内力",
     "description": "施加的伤害一部分转为少量内力伤害，并将这部分内力吸收，颖悟值越高吸髓效果越佳"}

EFFECT_XISUI_DA = \
    {"name": "大吸髓", "style": 0,
     "module": "proj.builtin.effects", "class": "XiSuiEffect", "level": 30,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "从施加的伤害中吸取了{mp_drain}点内力",
     "description": "施加的伤害一部分转为大量内力伤害，并将这部分内力吸收，颖悟值越高吸髓效果越佳"}


# 吸血
EFFECT_XIXUE = \
    {"name": "吸血", "style": 0,
     "module": "proj.builtin.effects", "class": "XiXueEffect", "level": 20,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "从施加的伤害中吸取了{hp_drain}点气血",
     "description": "从施加的伤害中吸取气血，颖悟值越高吸血效果越佳"}

EFFECT_XIXUE_XIAO = \
    {"name": "小吸血", "style": 0,
     "module": "proj.builtin.effects", "class": "XiXueEffect", "level": 10,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "从施加的伤害中吸取了{hp_drain}点气血",
     "description": "从施加的伤害中吸取少量气血，颖悟值越高吸血效果越佳"}

EFFECT_XIXUE_DA = \
    {"name": "大吸血", "style": 0,
     "module": "proj.builtin.effects", "class": "XiXueEffect", "level": 30,
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "从施加的伤害中吸取了{hp_drain}点气血",
     "description": "从施加的伤害中吸取大量气血，颖悟值越高吸血效果越佳"}


# 卸甲
EFFECT_XIEJIA = \
    {"name": "卸甲", "style": 0,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "defense_factor_", "ratio": 0.5}],
     "description": "基础防御降低"}


# 虚耗
EFFECT_XUHAO = \
    {"name": "虚耗", "style": 0,
     "module": "proj.builtin.effects", "class": "XuHaoEffect",
     "text": "{object}的内力消耗增多了",
     "description": "攻击时消耗更多内力"}


# 虚晃
EFFECT_XUHUANG = \
    {"name": "虚晃", "style": 0,
     "module": "proj.builtin.effects", "class": "XuHuangEffect",
     "text": "{object}随机转向了一个方位",
     "description": "被攻击的目标不会转向攻击者，而是转向随机方位"}


# 虚弱
EFFECT_XURUO = \
    {"name": "虚弱", "style": 0,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "attack_factor_", "ratio": 0.7}]}


# 迅疾
EFFECT_XUNJI = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "speed_factor_", "ratio": 2}]}


# 易筋
EFFECT_YIJIN = \
    {"name": "易筋", "style": 1,
     "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "hp_max_factor_", "ratio": 1.2},
               {"name": "mp_max_factor_", "ratio": 1.2},
               {"name": "attack_factor_", "ratio": 1.2},
               {"name": "defense_factor_", "ratio": 1.2},]}


# 浴血
EFFECT_YUXUE = \
    {"name": "浴血", "style": 1,
     "module": "proj.builtin.effects", "class": "YuXueEffect", "level": 30,
     "influence": "Gang", "factor_middle": 1, "factor_upper": 1.5,
     "text": "{object}受到{hp_delta}点溅射伤害",
     "description": "受到伤害的一部分会溅射给周身2格内所有敌方单位"}


# 圆转
EFFECT_YUANZHUAN = \
    {"name": "圆转", "style": 2,
     "module": "proj.builtin.effects", "class": "BuFengEffect",
     "text": "{object}被拉至身边了",
     "description": "将攻击范围内的敌方单位拉至近身"}


# 瘴气
EFFECT_ZHANGQI = \
    {"name": "瘴气", "style": 0,
     "module": "proj.builtin.effects", "class": "FengDuEffect", "level": 30,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{poison_hp}点风毒",
     "description": "一定比例的伤害追加为风毒，颖悟值越高效果越佳"}

EFFECT_ZHANGQI_XIAO = \
    {"name": "小瘴气", "style": 0,
     "module": "proj.builtin.effects", "class": "FengDuEffect", "level": 15,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{poison_hp}点风毒",
     "description": "较小比例的伤害追加为风毒，颖悟值越高效果越佳"}

EFFECT_ZHANGQI_DA = \
    {"name": "大瘴气", "style": 0,
     "module": "proj.builtin.effects", "class": "FengDuEffect", "level": 45,
     "influence": "Zhi", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对{object}施加了{poison_hp}点风毒",
     "description": "较大比例的伤害追加为风毒，颖悟值越高效果越佳"}


# 鸩蛊
EFFECT_ZHENGU = \
    {"name": "鸩蛊", "style": 0,
     "module": "proj.builtin.effects", "class": "YuDuEffect", "level": 30,
     "text": "对{object}施加了{poison_mp}点瘀毒",
     "description": "有一定几率对目标施加瘀毒，柔易值越高几率越大"}

EFFECT_ZHENGU_XIAO = \
    {"name": "小鸩蛊", "style": 0,
     "module": "proj.builtin.effects", "class": "YuDuEffect", "level": 15,
     "text": "对{object}施加了{poison_mp}点瘀毒",
     "description": "有一定几率对目标施加少量瘀毒，柔易值越高几率越大"}

EFFECT_ZHENGU_DA = \
    {"name": "大鸩蛊", "style": 0,
     "module": "proj.builtin.effects", "class": "YuDuEffect", "level": 45,
     "text": "对{object}施加了{poison_mp}点瘀毒",
     "description": "有一定几率对目标施加大量瘀毒，柔易值越高几率越大"}


# 吞吴
EFFECT_TUNWU = \
    {"name": "吞吴", "style": 1,
     "module": "proj.builtin.effects", "class": "TunWuEffect",
     "text": "自身的外伤、内伤、风毒以及瘀毒全部恢复",
     "description": "自身的外伤、内伤、风毒以及瘀毒全部恢复"}



# 复元
EFFECT_FUYUAN = \
    {"name": "复元", "style": 1,
     "module": "proj.builtin.effects", "class": "FuYuanEffect",
     "text": "自身气血恢复了",
     "description": "自身恢复一定量气血"}


# 薰风
EFFECT_XUNFENG = \
    {"name": "薰风", "style": 1,
     "module": "proj.builtin.effects", "class": "XunFengEffect",
     "text": "周围2格内友方单位的中毒症状减轻了",
     "description": "为周围2格内友方单位减少风毒值以及瘀毒值"}


# 驱风
EFFECT_QUFENG = \
    {"name": "驱风", "style": 1,
     "module": "proj.builtin.effects", "class": "QuFengEffect",
     "text": "{object}的风毒值减少了{poison_recover}点",
     "description": "为目标减少风毒值，颖悟值越高效果越佳"}


# 化瘀
EFFECT_HUAYU = \
    {"name": "化瘀", "style": 1,
     "module": "proj.builtin.effects", "class": "HuaYuEffect",
     "text": "{object}的瘀毒值减少了{poison_recover}点",
     "description": "为目标减少瘀毒值，颖悟值越高效果越佳"}


# 却步
EFFECT_QUEBU = \
    {"name": "却步", "style": 0, 
     "module": "proj.builtin.effects", "class": "QueBuEffect",
     "influence": "Rou", "factor_middle": 1, "factor_upper": 1.5,
     "text": "{object}的时序倒退了{process}点",
     "description": "使目标时序倒退，柔易值越高时序倒退越多"}


# 连枝
EFFECT_LIANZHI = \
    {"name": "连枝", "style": 1,
     "module": "proj.builtin.effects", "class": "LianZhiEffect",
     "description": "随机将对方的一个增益状态施加给自身，自身的一个减益状态施加给对方"}


EFFECT_LIANZHI_BUFF = \
    {"name": "连枝", "style": 1,
     "module": "proj.builtin.effects", "class": "LianZhiBuffEffect",
     "text": "从{object}身上获取了状态{status}",
     "description": "随机将对方的一个增益状态施加给自身"}

EFFECT_LIANZHI_DEBUFF = \
    {"name": "连枝", "style": 1,
     "module": "proj.builtin.effects", "class": "LianZhiDebuffEffect",
     "text": "将{status}状态施加给了{object}",
     "description": "随机将自身的一个负面状态施加给对方"}
     
     
# 连击
EFFECT_LIANJI = \
    {"name": "连击", "style": 1, "level": 30,
     "module": "proj.builtin.effects", "class": "LianJiEffect",
     "influence": "Dong", "factor_middle": 1, "factor_upper": 1.5,
     "text": "对目标再次发动攻击",
     "description": "有一定几率再次使用相同技能对目标发动攻击，灵动值越高发动几率越大"}


# 流光
EFFECT_LIUGUANG = \
    {"name": "流光",
     "module": "proj.builtin.effects", "class": "LiuGuangEffect",
     "text": "{object}的内力得到了恢复"}


# 牵缠
EFFECT_QIANCHAN = \
    {"style": 0, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "dodge_rate_factor_", "ratio": 0.6}],
     "influence": "Rou", "factor_lower": 1.2, "factor_middle": 1}


# 日月
EFFECT_PINGDAN_DECREASE = \
    {"style": 0, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_2",
     "attrs": [{"name": "power", "delta": -100}]}

EFFECT_PINGDAN_INCREASE = \
    {"style": 1, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_1",
     "attrs": [{"name": "power", "delta": 100}]}

EFFECT_RIRU_DECREASE = \
    {"style": 0, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_1",
     "attrs": [{"name": "power", "delta": -100}]}

EFFECT_RIRU_INCREASE = \
    {"style": 1, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_2",
     "attrs": [{"name": "power", "delta": 100}]}

EFFECT_RI_ANONYMOUS = \
    {"style": 1, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_1",
     "attrs": [{"name": "power", "delta": 50}]}

EFFECT_YUE_ANONYMOUS = \
    {"style": 1, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_2",
     "attrs": [{"name": "power", "delta": 50}]}

EFFECT_RIYUE_ANONYMOUS = \
    {"style": 1, "module": "proj.entity.effect", "class": "PersonSkillChangeAttributeEffect",
     "skill": "SKILL_RIYUESHUANGLUN_3",
     "attrs": [{"name": "power", "delta": 50}]}

EFFECT_RIRU = \
    {"name": "日入", "style": 2,
     "module": "proj.builtin.effects", "class": "RiYueEffect",
     "exertion": "STATUS_RIRU", "status_leave": "STATUS_PINGDAN", "skill": "SKILL_RIYUESHUANGLUN_1", "limit": 100,
     "description": "使用后本次战斗中『偷天换日』威力降低100点，『月落参横』威力提高100点"}

EFFECT_PINGDAN = \
    {"name": "平旦", "style": 2,
     "module": "proj.builtin.effects", "class": "RiYueEffect",
     "exertion": "STATUS_PINGDAN", "status_leave": "STATUS_RIRU", "skill": "SKILL_RIYUESHUANGLUN_2", "limit": 100,
     "description": "使用后本次战斗中『月落参横』威力降低100点，『偷天换日』威力提高100点"}

EFFECT_RIYUEZHENGHUI = \
    {"name": "日月争辉", "style": 1,
     "module": "proj.builtin.effects", "class": "ExertEffect",
     "targets": "Subject", "exertion": "STATUS_RIYUEZHENGHUI",
     "description": "使用后本次战斗中『日月双轮』全部招式威力提高50点"}


# 同心
EFFECT_TONGXIN = \
    {"name": "同心", "style": 1,
     "module": "proj.builtin.effects", "class": "TongXinEffect",
     "text": "对{object}的回复量提升了",
     "description": "自身与目标共同拥有的状态数越多，回复量越高"}

     
# 移花
EFFECT_YIHUA = \
    {"name": "移花", "style": 2, 
     "module": "proj.builtin.effects", "class": "YiHuaEffect",
     "text": "{subject}与{object}位置互换",
     "description": "与目标交换位置"}
     
     
# 绝影
EFFECT_JUEYING = \
    {"name": "绝影", "style": 1, 
     "module": "proj.builtin.effects", "class": "JueYingEffect",
     "text": "移动至{object}身后",
     "description": "在进行攻击前，先移动至目标身后"}
     

# 虎步
EFFECT_HUBU = \
    {"style": 0, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "motion_", "delta": 1}]}


# 天眼
EFFECT_TIANYAN = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "critical_rate_factor_", "ratio": 1.3}]}
     
     
# 看破
EFFECT_KANPO = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "anti_damage_rate_factor_", "ratio": 1.3}]}
     
     
# 高远无极
EFFECT_GAOYUANWUJI = \
    {"style": 0, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "zoc_scope", "delta": 1}]}
     
     
# 俯仰俱陈
EFFECT_FUYANGJUCHEN = \
    {"style": 0, "module": "proj.builtin.effects", "class": "FeiXingEffect", "level": 10}


# 百中
EFFECT_BAIZHONG = \
    {"style": 1, "module": "proj.builtin.effects", "class": "BattlePersonChangeAttributeEffect",
     "attrs": [{"name": "hit_rate_factor_", "ratio": 1.15}]}


# 先机
EFFECT_XIANJI = \
    {"name": "先机", "style": 1, 
     "module": "proj.builtin.effects", "class": "XianJiEffect",
     "text": "先行对{object}进行一次攻击",
     "description": "当敌人进入自身辅助技能攻击范围内时，有一定几率抢先对其发动攻击，沉静值越高几率越大"}


# 卸劲
EFFECT_XIEJIN = \
    {"name": "卸劲", "style": 1,
     "module": "proj.builtin.effects", "class": "XieJinEffect", "level": 20,
     "text": "{mp_trans}点伤害用内力抵消了",
     "description": "可以使用内力抵消一部分伤害，柔易值越高低效比例越大"}


# 偷盗
EFFECT_TOUDAO = \
    {"name": "偷盗", "style": 0,
     "module": "proj.builtin.effects", "class": "TouDaoEffect",
     "influence": "Dong", "factor_middle": 1, "factor_upper": 1.5, 
     "text": "从{object}处偷到了{item}×{quantity}",
     "description": "有一定几率从目标身上偷到物品，灵动值越高几率越大"}


# 除剑
EFFECT_CHUJIAN = \
    {"name": "除剑", "style": 0,
     "module": "proj.builtin.effects", "class": "ChuXieEffect", "equip_style": "Jianfa",
     "text": "{object}的武器{equip}被击落",
     "description": "如目标的主手武器为剑类，可将其卸除"}


# 除刀
EFFECT_CHUDAO = \
    {"name": "除刀", "style": 0,
     "module": "proj.builtin.effects", "class": "ChuXieEffect", "equip_style": "Daofa",
     "text": "{object}的武器{equip}被击落",
     "description": "如目标的主手武器为刀类，可将其卸除"}


# 除枪
EFFECT_CHUQIANG = \
    {"name": "除枪", "style": 0,
     "module": "proj.builtin.effects", "class": "ChuXieEffect", "equip_style": "Changbing",
     "text": "{object}的武器{equip}被击落",
     "description": "如目标的主手武器为长兵类，可将其卸除"}


# 除奇
EFFECT_CHUQI = \
    {"name": "除奇", "style": 0,
     "module": "proj.builtin.effects", "class": "ChuXieEffect", "equip_style": "Qimen",
     "text": "{object}的武器{equip}被击落",
     "description": "如目标的主手武器为奇门类，可将其卸除"}


# 神准
EFFECT_SHENZHUN = \
    {"name": "神准", "style": 1,
     "module": "proj.builtin.effects", "class": "ShenZhunEffect",
     "text": "攻击必定命中",
     "description": "攻击必定命中，且不会被闪避"}
  
  
# 精剑
EFFECT_JINGJIAN = \
    {"name": "精剑", "style": 1,
     "module": "proj.builtin.effects", "class": "JingWuEffect", "skill_style": "Jianfa", "level": 30,
     "text": "剑法攻击伤害提升了{enhance}",
     "description": "剑法伤害大幅提高"}


# 枪神
EFFECT_WUQIANG = \
    {"name": "", "style": 1,
     "module": "proj.builtin.effects", "class": "WuShenEffect", "skill_style": "Changbing"} 
     
     
# 剑气如霞
EFFECT_JIANQIRUXIA = \
    {"name": "剑气如霞", "style": 1,
     "module": "proj.builtin.effects", "class": "GangFengEffect", "skill_style": "Jianfa",
     "text": "所有剑法溅射范围+1",
     "description": "所有剑法武学的溅射范围增加"}
     
     
# 六龙回日功
EFFECT_LIULONGHUIRI = \
    {"name": "六龙回日", "style": 1,
     "module": "proj.builtin.effects", "class": "QiYongEffect", "action": "Move,Rest",
     "text": "获得额外的行动机会"}

EFFECT_RIBOYUYUAN = \
    {"style": 1,
     "module": "proj.builtin.effects", "class": "RiBoYuYuanEffect"}


# 离魂不系
EFFECT_LIHUNBUJI = \
    {"name": "离魂不系", "style": 1,
     "module": "proj.builtin.effects", "class": "LiHunEffect",
     "text": "随机移动至战斗地图中一点",
     "description": "战斗中无法自由移动，但自己的回合开始前会随机投放至地图上某一点"}
     
     
# 蛊惑
EFFECT_GUHUO = \
    {"name": "蛊惑", "style": 1, 
     "module": "proj.builtin.effects", "class": "GuhuoEffect"}
     
     
EFFECT_GUHUO_EXERT = \
    {"name": "蛊惑", "style": 1,
     "module": "proj.entity.effect", "class": "ExertEffect", "exertion": "STATUS_GUHUO", "turns": 2, 
     "influence": "Rou", "factor_upper": 0.3, "factor_middle": 0.1,
     "text": "将{object}暂时拉拢至本方阵营",
     "description": "有一定概率将目标拉拢至本方阵营，柔易值越高几率越大"}
     

# 分断
EFFECT_FENDUAN_EXERT = \
    {"name": "分断", "style": 2,
     "module": "proj.builtin.effects", "class": "DoubleExertEffect", "status": "STATUS_FENDUAN",
     "description": "对自身与目标同时施加分断状态，一段时间内双方互相攻击无效"}

EFFECT_FENDUAN = \
    {"name": "分断", "style": 2,
     "module": "proj.builtin.effects", "class": "FenduanEffect",
     "text": "对{object}的攻击无效化",
     "description": "对目标的攻击无效化"}
     
# 同归
EFFECT_TONGGUI_EXERT = \
    {"name": "同归", "style": 2,
     "module": "proj.builtin.effects", "class": "DoubleExertEffect", "status": "STATUS_TONGGUI", "turns": 3,
     "description": "对自身与目标同时施加分断状态，一段时间内双方互相攻击伤害翻倍"}
     
EFFECT_TONGGUI = \
    {"name": "同归", "style": 2,
     "module": "proj.builtin.effects", "class": "TongGuiEffect",
     "text": "对{object}的攻击伤害翻倍",
     "description": "对目标的攻击伤害翻倍"}


# 震慑
EFFECT_ZHENSHE = \
    {"name": "震慑",
     "module": "proj.builtin.effects", "class": "ZhenSheEffect",
     "description": "对施加者的攻击伤害降低"}


# 驻颜
EFFECT_ZHUYAN = \
    {"name": "驻颜",
     "module": "proj.builtin.effects", "class": "ZhuYanEffect"}

     

EFFECT_4 = {"name": "退敌", "module": "proj.builtin.effect", "class": "TuiDiEffect"}
