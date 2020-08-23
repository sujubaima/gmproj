# -- coding: utf-8 --

# 冰肌玉骨术
STATUS_ZHUYAN = \
    {"name": "驻颜", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_ZHUYAN"}],
     "description": "所有武学不消耗内力"}
     
STATUS_LIUGUANG = \
    {"name": "流光", "phase": "FinishTurn", "style": 2,
     "functions": [{"id": "EFFECT_LIUGUANG"}],
     "description": "每回合结束时流失一定内力，补充给周身2格内友方单位"}
     
# 太极神功
STATUS_MINGYUEZHAODAJIANG = \
    {"name": "明月照大江", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_MINGYUEZHAODAJIANG"}],
     "description": "遭受攻击时，对方基础攻击越高，自身反击率越高"}

STATUS_MINGYUEZHAODAJIANG_LEAVE = \
    {"phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_MINGYUEZHAODAJIANG_LEAVE"}]}

STATUS_MINGYUEZHAODAJIANG_ANONYMOUS = \
    {"phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_MINGYUEZHAODAJIANG_ANONYMOUS"}]}

STATUS_QINGFENGFUSHANGANG = \
    {"name": "清风拂山冈", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_QINGFENGFUSHANGANG"}],
     "description": "攻击敌人时施加内伤，敌方基础防御越高，施加的内伤越多"}

STATUS_TAIJIJIN = \
    {"name": "太极劲", "phase": "Start", "style": 1,
     "functions": [{"id": "EFFECT_TAIJIJIN"}],
     "description": "武学『太极拳』、『太极剑意』所有招式威力提升"}


# 定身
STATUS_DINGSHEN = \
    {"name": "定身", "phase": "StartTurn", "accepttype": "Overlap",
     "functions": [{"id": "EFFECT_DINGSHEN"}],
     "description": "无法主动移动"}


# 日月
STATUS_PINGDAN = \
    {"phase": "Instant", "accepttype": "Overlap", "overtype": "Exert", "style": 2,
     "functions": [{"id": "EFFECT_PINGDAN_INCREASE"},
                   {"id": "EFFECT_PINGDAN_DECREASE"}]}

STATUS_RIRU = \
    {"phase": "Instant", "accepttype": "Overlap", "overtype": "Exert", "style": 2,
     "functions": [{"id": "EFFECT_RIRU_INCREASE"},
                   {"id": "EFFECT_RIRU_DECREASE"}]}

STATUS_RIYUEZHENGHUI = \
    {"phase": "Instant", "accepttype": "Overlap", "overtype": "Exert", "style": 2,
     "functions": [{"id": "EFFECT_RI_ANONYMOUS"},
                   {"id": "EFFECT_YUE_ANONYMOUS"},
                   {"id": "EFFECT_RIYUE_ANONYMOUS"}]}

STATUS_YURI = \
    {"name": "日轮观", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_RI_ANONYMOUS"},
                   {"id": "EFFECT_RIYUE_ANONYMOUS"}],
     "description": "武学『日月双轮』中『偷天换日』、『日月争辉』二式威力提升"}

STATUS_ZHIYUE = \
    {"name": "月轮观", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_YUE_ANONYMOUS"},
                   {"id": "EFFECT_RIYUE_ANONYMOUS"}],
     "description": "武学『日月双轮』中『月落参横』、『日月争辉』二式威力提升"}


# 弃武
STATUS_QIWU = \
    {"name": "弃武", "phase": "StartTurn", "accepttype": "Overlap",
     "functions": [{"id": "EFFECT_QIWU"}],
     "description": "无法主动攻击"}


# 豪气干云
STATUS_HAOQIGANYUN = \
    {"name": "豪气干云", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_HAOQIGANYUN"}],
     "description": "每次攻击只要命中目标，自身时序速度便会提升"}

STATUS_HAOQIGANYUN_ANONYMOUS = \
    {"phase": "Instant", "style": 1, "countable": True, "accepttype": "Overlap", "overtype": "Exert",
     "functions": [{"id": "EFFECT_HAOQIGANYUN_ANONYMOUS"}]}

# 金钟罩
STATUS_TONGPITIEGU = \
    {"name": "铜皮铁骨", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_TONGPITIEGU"}],
     "description": "免疫外伤"}
     
STATUS_JINGANGBUHUAI = \
    {"name": "金刚不坏", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_JINGANGBUHUAI"}],
     "description": "受到攻击时有一定几率将伤害减为1点"}  
     

# 云剑
STATUS_YUNJIAN_ANONYMOUS = \
    {"phase": "FinishTurn", "style": 1, "accepttype": "Overlap", "overtype": "Exert",
     "functions": [{"id": "EFFECT_YUNJIAN_ANONYMOUS"}]}


# 无畏
STATUS_WUWEI = \
    {"name": "无畏", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_WUWEI"}],
     "description": "在回合外受到多次攻击时，伤害都不会高于第一次"}
     

# 卸甲
STATUS_XIEJIA = \
    {"name": "卸甲", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_XIEJIA"}],
     "description": "基础防御下降"}


# 卸劲
STATUS_XIEJIN = \
    {"name": "卸劲", "phase": "AfterAttack", "accepttype": "Overlap", "style": 1,
     "functions": [{"id": "EFFECT_XIEJIN"}],
     "description": "可以用内力抵消一部分伤害"}


# 吸血
STATUS_XIXUE = \
    {"name": "吸血", "phase": "AfterAttack",
     "functions": [{"id": "EFFECT_XIXUE"}]}


# 虚耗
STATUS_XUHAO = \
    {"name": "虚耗", "phase": "AfterDamage",
     "functions": [{"id": "EFFECT_XUHAO"}],
     "description": "攻击时消耗更多内力"}


# 虚弱
STATUS_XURUO = \
    {"name": "虚弱", "phase": "Instant",
     "functions": [{"id": "EFFECT_XURUO"}],
     "description": "基础攻击下降"}


# 易筋
STATUS_YIJIN = \
    {"name": "易筋", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_YIJIN"}],
     "description": "气血上限、内力上限、基础攻击与基础防御得到大幅提升"}

STATUS_HUANGU = \
    {"name": "换骨", "phase": "FinishTurn", "style": 1,
     "functions": [{"id": "EFFECT_HUANGU"}],
     "description": "前20回合（包括其他角色回合）中，每回合结束时自身基础暴击率、基础闪避率、基础反击率与基础拆招率+1"}

STATUS_HUANGU_ANONYMOUS = \
    {"phase": "Instant", "countable": True, "style": 1,
     "functions": [{"id": "EFFECT_HUANGU_ANONYMOUS"}]}


# 浴血
STATUS_YUXUE = \
    {"name": "浴血", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_YUXUE"}],
     "description": "受到攻击时，部分伤害会溅射给周身二格内所有敌方单位"}


# 神准
STATUS_SHENZHUN = \
    {"name": "神准", "phase": "BeforeDamage",
     "functions": [{"id": "EFFECT_SHENZHUN"}]}


STATUS_FENDUAN = \
    {"name": "分断", "phase": "BeforeDamage", "style": 2,
     "functions": [{"id": "EFFECT_FENDUAN"}],
     "description": "一定回合内，施放者与目标相互攻击无效"}

 
STATUS_TONGGUI = \
    {"name": "同归", "phase": "AfterDamage", "style": 2,
     "functions": [{"id": "EFFECT_TONGGUI"}],
     "description": "一定回合内，施放者与目标相互攻击伤害翻倍"} 

     
STATUS_GANGJIN = \
    {"name": "刚劲", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_GANGJIN"}],
     "description": "攻击时有几率给目标施加外伤，刚猛值越高几率越大"}


# 惧拳     
STATUS_JUQUAN = \
    {"name": "惧拳", "phase": "AfterDamage", "style": 0,
     "functions": [{"id": "EFFECT_JUQUAN"}],
     "description": "受到搏击类武学攻击时伤害增加"}


# 惧剑     
STATUS_JUJIAN = \
    {"name": "惧剑", "phase": "AfterDamage", "style": 0,
     "functions": [{"id": "EFFECT_JUJIAN"}],
     "description": "受到剑法类武学攻击时伤害增加"}


# 精拳
STATUS_JINGQUAN = \
    {"name": "精拳", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_JINGQUAN"}],
     "description": "运用拳法类武学时伤害大幅增加"}


# 精剑     
STATUS_JINGJIAN = \
    {"name": "精剑", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_JINGJIAN"}],
     "description": "运用剑法类武学时伤害大幅增加"}


# 精刀     
STATUS_JINGDAO = \
    {"name": "精刀", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_JINGDAO"}],
     "description": "运用刀法类武学时伤害大幅增加"}


# 剑气如霞     
STATUS_JIANQIRUXIA = \
    {"name": "剑气如霞", "phase": "Start", "style": 1,
     "functions": [{"id": "EFFECT_JIANQIRUXIA"}],
     "description": "剑法类武学增加一格溅射范围"}


# 离魂不系     
STATUS_LIHUNBUJI = \
    {"name": "离魂不系", "phase": "StartTurn", "style": 2,
     "functions": [{"id": "EFFECT_LIHUNBUJI"}],
     "description": "战斗中无法主动移动，但每回合开始会随机投放至地图一点"}


# 六龙回日
STATUS_LIULONGHUIRI = \
    {"name": "六龙回日", "phase": "AfterAttack,AfterItem", "style": 1,
     "functions": [{"id": "EFFECT_LIULONGHUIRI"}],
     "description": "回合内攻击或使用物品后获得额外的移动机会"}


# 日薄虞渊
STATUS_RIBOYUYUAN = \
    {"name": "日薄虞渊", "phase": "FinishTurn", "style": 1,
     "functions": [{"id": "EFFECT_RIBOYUYUAN", "turns": 1}],
     "description": "回合结束时对周身1格内的敌方单位施加大目盲状态，持续1回合"}


# 迷形
STATUS_MIXING = \
    {"name": "迷形", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_MIXING"}],
     "description": "受到攻击时，对方的朝向逆转"}     


# 震慑
STATUS_ZHENSHE = \
    {"name": "震慑", "phase": "AfterDamage",
     "functions": [{"id": "EFFECT_ZHENSHE"}],
     "description": "对状态施加者的攻击伤害减低"}


# 蛊惑
STATUS_GUHUO = \
    {"name": "蛊惑", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_GUHUO"}],
     "description": "阵营暂时发生变化"}


# 击退
STATUS_JITUI_RATIO = \
    {"name": "威震", "phase": "BeforeDamage", "style": 1,
     "ratio": 0.5, "influence": "Gang", "factor_middle": 1, "factor_upper": 2,
     "functions": [{"id": "EFFECT_JITUI"}],
     "description": "攻击时有一定几率将目标击退1格"}


# 攻气
STATUS_GONGQI_XIAO = \
    {"name": "小攻气", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_GONGQI_XIAO"}],
     "description": "攻击时较小比例的伤害转化为内力伤害"}


STATUS_GONGQI_XIAO_RATIO = \
    {"name": "荡气", "phase": "AfterAttack", "style": 1,
     "ratio": 0.5, "influence": "Zhi", "factor_middle": 1, "factor_upper": 2,
     "functions": [{"id": "EFFECT_GONGQI"}],
     "description": "攻击时有一定几率追加内力伤害"}


STATUS_MUMANG = \
    {"name": "目盲", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_MUMANG"}],
     "description": "命中率暂时下降"}

STATUS_MUMANG_DA = \
    {"name": "大目盲", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_MUMANG_DA"}],
     "description": "命中率大幅下降"}
     

STATUS_XUNFENG = \
    {"name": "薰风", "phase": "FinishTurn", "style": 1,
     "functions": [{"id": "EFFECT_XUNFENG", "level": 150}],
     "description": "自身回合结束时给周围2格内友方单位减少风毒、瘀毒值"}

     
STATUS_BINGXIN = \
    {"name": "病心", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_BINGXIN"}],
     "description": "无法通过休息的方式来恢复气血"}
          
STATUS_HANPIN = \
    {"name": "含颦", "phase": "Instant,AfterMove,AfterSettlement,AfterItem", "style": 1,
     "functions": [{"id": "EFFECT_HANPIN", "level": 1}],
     "description": "自身每获得一个负面状态，闪避率都会提升"}
     
STATUS_HANPIN_DA = \
    {"name": "含颦", "phase": "Instant,AfterMove,AfterAttack,AfterItem", "style": 1,
     "functions": [{"id": "EFFECT_HANPIN", "level": 2}],
     "description": "自身每获得一个负面状态，闪避率都会提升"}
     
STATUS_HANPIN_ANONYMOUS = \
    {"phase": "Instant", "style": 1, "countable": True, "accepttype": "Overlap", "overtype": "Exert",
     "functions": [{"id": "EFFECT_HANPIN_ANONYMOUS"}]}
     
STATUS_HANPIN_ANONYMOUS_DA = \
    {"phase": "Instant", "style": 1, "countable": True, "accepttype": "Overlap", "overtype": "Exert",
     "functions": [{"id": "EFFECT_HANPIN_ANONYMOUS_DA"}]}


STATUS_CHANGDAN = \
    {"name": "尝胆", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_CHANGDAN"}],
     "description": "自身每受到一次攻击，暴击率都会提升"}


STATUS_FUYUAN = \
    {"name": "复元", "phase": "FinishTurn", "style": 1,
     "functions": [{"id": "EFFECT_FUYUAN", "level": 5}],
     "description": "自身回合结束时，恢复一定气血与内力"}


STATUS_MIAOYUAN = \
    {"name": "妙圆", "phase": "FinishTurn", "style": 1,
     "functions": [{"id": "EFFECT_FUYUAN", "level": 5}],
     "description": "自身回合结束时，恢复一定气血与内力"}


STATUS_TONGXIN = \
    {"name": "同心", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_TONGXIN", "level": 20}],
     "description": "目标与自身拥有的共同状态种数越多，回复效果越佳"}


STATUS_CHANGDAN_ANONYMOUS = \
    {"phase": "Instant", "style": 1, "countable": True, "accepttype": "Overlap", "overtype": "Exert",
     "functions": [{"id": "EFFECT_CHANGDAN_ANONYMOUS"}]}


STATUS_TUNWU = \
    {"name": "吞吴", "phase": "AfterSettlement", "style": 1,
     "functions": [{"id": "EFFECT_TUNWU", "level": 99999}],
     "description": "攻击造成敌人退场时，自身外伤值、内伤值、风毒值、瘀毒值全部清零"}


STATUS_TUGOU = \
    {"name": "屠狗", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_TUGOU"}],
     "description": "武学『打狗棒法』所有招式威力提升"}

     
STATUS_CHOUSUI = \
    {"name": "大抽髓", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_XISUI_DA"}],
     "description": "攻击同时造成内力伤害，内力伤害将被自身吸收，颖悟值越高吸髓效果越佳"}


STATUS_CHOUSUI_XIAO = \
    {"name": "小抽髓", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_XISUI_XIAO"}],
     "description": "攻击同时造成内力伤害，内力伤害将被自身吸收，颖悟值越高吸髓效果越佳"}


STATUS_CHOUSUI_XIAO_RATIO = \
    {"name": "紫电青霜", "phase": "AfterAttack", "style": 1,
     "ratio": 0.5, "influence": "Zhi", "factor_middle": 1, "factor_upper": 2,
     "functions": [{"id": "EFFECT_XISUI"}],
     "description": "攻击时有一定几率吸取目标内力"}


STATUS_JUANLIU = \
    {"name": "抱朴", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_JUANLIU"}],
     "description": "绝大部分武学内力消耗降低"}

     
STATUS_QIXINGNIMAI = \
    {"name": "逆脉", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_NIMAI_ATTACK"},
                   {"id": "EFFECT_NIMAI_DEFENSE"}],
     "description": "攻击时有几率用气血代替内力消耗；防御时有几率用内力代替气血消耗；触发时自身会受到一定内伤"}
                   
STATUS_BIJINGUAN = \
    {"name": "闭金关", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_BIJINGUAN"}],
     "description": "气血上限提升20%"}


STATUS_KOUYUSUO = \
    {"name": "扣玉锁", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_KOUYUSUO"}],
     "description": "内力上限提升20%"}


STATUS_BASHANJIN = \
    {"name": "力拔山兮", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_BASHANJIN"}],
     "description": "攻击提升25%"}


# 断筋
STATUS_DUANJIN = \
    {"name": "断筋", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_DUANJIN"}],
     "description": "时序速度遭到削减"}


STATUS_CUOGU = \
    {"name": "错骨", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_CUOGU"}],
     "description": "移动力减少"}


STATUS_QIANCHAN = \
    {"name": "牵缠", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_QIANCHAN"}],
     "description": "闪避率降低"}


STATUS_NIYUN = \
    {"name": "霓云", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_SUSHA"}],
     "description": "时序速度获得小幅提升"}


STATUS_HUBU = \
    {"name": "虎步", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_HUBU"}],
     "description": "移动力暂时提升"}


STATUS_TIANYAN = \
    {"name": "天眼", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_TIANYAN"}],
     "description": "暴击暂时提升"}
     
     
STATUS_GAOYUANWUJI = \
    {"name": "高远无极", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_GAOYUANWUJI"}],
     "description": "自身的ZOC范围增加"}
     
     
STATUS_KANPO = \
    {"name": "看破", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_KANPO"}],
     "description": "基础拆招获得提升"}


STATUS_BAIZHONG = \
    {"name": "百中", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_BAIZHONG"}],
     "description": "基础命中获得提升"}


STATUS_XIANJI = \
    {"name": "先机", "phase": "AfterMove", "style": 1,
     "functions": [{"id": "EFFECT_XIANJI"}],
     "description": "敌人进入攻击范围时可先行攻击一次"}


STATUS_WUQIANG = \
    {"phase": "Finish", "style": 1,
     "functions": [{"id": "EFFECT_WUQIANG"}]}


# 迅疾
STATUS_XUNJI = \
    {"name": "迅疾", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_XUNJI"}],
     "description": "时序速度获得提升"}

STATUS_XUNJI_DA = \
    {"name": "大迅疾", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_XUNJI_DA"}],
     "description": "时序速度获得大幅提升"}


# 一苇渡江
STATUS_YIWEIDUJIANG_MOVE = \
    {"name": "一苇渡江", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_YIWEIDUJIANG_MOVE"}],
     "description": "移动时可以经过水面，但无法停留"}

STATUS_YIWEIDUJIANG_STAY = \
    {"name": "一苇渡江", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_YIWEIDUJIANG_STAY"}],
     "description": "移动时可以经过并停留在水面"}


# 震击
STATUS_ZHENJI = \
    {"name": "震击", "phase": "AfterAttack", "style": 1,
     "ratio": 0.3, "influence": "Gang", "factor_middle": 1, "factor_upper": 2,
     "functions": [{"id": "EXERT.STATUS_DINGSHEN", "name": "震击"}],
     "description": "攻击时有一定几率给目标施加1回合定身状态"}
