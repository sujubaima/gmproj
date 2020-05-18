# -- coding: utf-8 --

STATUS_XIEJIN = \
    {"name": "卸劲", "phase": "AfterAttack",
     "functions": [{"id": "EFFECT_XIEJIN"}]}


STATUS_XIXUE = \
    {"name": "吸血", "phase": "AfterAttack",
     "functions": [{"id": "EFFECT_XIXUE"}]}


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


# 惧剑     
STATUS_JUJIAN = \
    {"name": "惧剑", "phase": "AfterDamage", "style": 0,
     "functions": [{"id": "EFFECT_JUJIAN"}],
     "description": "受到剑法类武学攻击时伤害+30%"}


# 精剑     
STATUS_JINGJIAN = \
    {"name": "精剑", "phase": "AfterDamage", "style": 1,
     "functions": [{"id": "EFFECT_JINGJIAN"}],
     "description": "剑法类武学伤害+30%"}

     
STATUS_JIANQIRUXIA = \
    {"name": "剑气如霞", "phase": "Start", "style": 1,
     "functions": [{"id": "EFFECT_JIANQIRUXIA"}],
     "description": "剑法类武学溅射范围+1"}

     
STATUS_LIHUNBUJI = \
    {"name": "离魂不系", "phase": "StartTurn", "style": 1,
     "functions": [{"id": "EFFECT_LIHUNBUJI"}],
     "description": "战斗中无法主动移动，但每回合开始会随机投放至地图一点"}

     
STATUS_GUHUO = \
    {"name": "蛊惑", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_GUHUO"}],
     "description": "阵营暂时发生变化"}


STATUS_MUMANG = \
    {"name": "目盲", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_MUMANG"}],
     "description": "命中率暂时下降"}
     

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
     "functions": [{"id": "EFFECT_FUYUAN", "level": 500}],
     "description": "自身回合结束时，恢复一定气血"}


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

     
STATUS_CHOUSUI = \
    {"name": "抽髓", "phase": "AfterAttack", "style": 1,
     "functions": [{"id": "EFFECT_XISUI_DA"}],
     "description": "攻击同时造成内力伤害，内力伤害将被自身吸收，颖悟值越高吸髓效果越佳"}

     
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


STATUS_DUANJIN = \
    {"name": "断筋", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_DUANJIN"}],
     "description": "时序速度暂时减少"}


STATUS_CUOGU = \
    {"name": "错骨", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_CUOGU"}],
     "description": "移动力暂时减少"}


STATUS_QIANCHAN = \
    {"name": "牵缠", "phase": "Instant", "style": 0,
     "functions": [{"id": "EFFECT_QIANCHAN"}],
     "description": "闪避率暂时减少"}


STATUS_LONGXING = \
    {"name": "龙行", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_LONGXING"}],
     "description": "时序速度暂时提升"}


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
     "description": "拆招暂时提升"}


STATUS_BAIZHONG = \
    {"name": "百中", "phase": "Instant", "style": 1,
     "functions": [{"id": "EFFECT_BAIZHONG"}],
     "description": "命中暂时提升"}


STATUS_XIANJI = \
    {"name": "先机", "phase": "AfterMove", "style": 1,
     "functions": [{"id": "EFFECT_XIANJI"}],
     "description": "敌人进入攻击范围时可先行攻击一次"}


STATUS_WUQIANG = \
    {"phase": "Finish", "style": 1,
     "functions": [{"id": "EFFECT_WUQIANG"}]}