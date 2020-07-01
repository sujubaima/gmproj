# -- coding: utf-8 --


# 拳套
ITEM_QUANTAO = \
    {"name": "拳套", "rank": 0, "tags": "Equip,Weapon,Boji", "shape": "Around,0,0,0",
     "weight": 1.0, "volume": 1.0, "durability": 40, "money": 200,
     "inlays": [{"name": "表皮", "accept": "Fur"}],
     "inlays_prefix": "Fur",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_CHANGJIAN_ATTR"}],
     "description": "拳师们戴在手上的装备，主要用于保护双手，对于提升伤害作用有限"}


# 护手
ITEM_HUSHOU = \
    {"name": "护手", "rank": 0, "tags": "Equip,Weapon,Boji", "shape": "Around,0,0,0",
     "weight": 0.8, "volume": 0.8, "durability": 40, "money": 200,
     "inlays": [{"name": "表皮", "accept": "Fur"}],
     "inlays_prefix": "Fur",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_CHANGJIAN_ATTR"}],
     "description": "拳师们戴在手上的装备，主要用于保护手掌，对于提升伤害作用有限"}
     

# 长剑     
ITEM_CHANGJIAN = \
    {"name": "长剑", "rank": 0, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0",
     "weight": 1.2, "volume": 1.2, "durability": 45, "money": 250,
     "inlays": [{"name": "剑柄", "accept": "Wood|Jade|Metal"},
                {"name": "剑身", "accept": "Jade|Metal"}],
     "inlays_prefix": "Jade|Metal",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_CHANGJIAN_ATTR"}],
     "description": "最常见的剑类武器，即使不练武的人也会买一把来配在身上"}


# 万字剑
ITEM_WANZIJIAN = \
    {"name": "万字剑", "rank": 1, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0",
     "weight": 1.2, "volume": 1.2, "durability": 45, "money": 250,
     "inlays": [{"name": "剑柄", "accept": "Wood|Jade|Metal"},
                {"name": "剑身", "accept": "Jade|Metal"}],
     "inlays_prefix": "Jade|Metal",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_WANZIJIAN_ATTR"}],
     "description": ""}


# 单刀
ITEM_DANDAO = \
    {"name": "单刀", "rank": 0, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0",
     "weight": 1.2, "volume": 1.2, "durability": 45, "money": 250,
     "inlays": [{"name": "刀柄", "accept": "Wood|Jade|Metal"},
                {"name": "刀刃", "accept": "Jade|Metal"}],
     "inlays_prefix": "Jade|Metal",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_DANDAO_ATTR"}],
     "description": "最常见的刀类武器，形制轻巧，单手即很容易使用"}


# 朴刀
ITEM_PODAO = \
    {"name": "朴刀", "rank": 0, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "double_hand": True,
     "weight": 1.5, "volume": 1.5, "durability": 50, "money": 280,
     "inlays": [{"name": "刀柄", "accept": "Wood"},
                {"name": "刀刃", "accept": "Jade|Metal", "prefix": True}],
     "inlays_prefix": "Jade|Metal",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_PODAO_ATTR"}],
     "description": "流水线量产刀型，绿林好汉人手一把，需要双手持握"}


# 工部刀
ITEM_GONGBUDAO = \
    {"name": "工部刀", "rank": 1, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0",
     "weight": 1.2, "volume": 1.2, "durability": 45, "money": 250,
     "inlays": [{"name": "刀柄", "accept": "Wood|Jade|Metal"},
                {"name": "刀刃", "accept": "Jade|Metal"}],
     "inlays_prefix": "Jade|Metal",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_GONGBUDAO_ATTR"}],
     "description": ""}


# 内弧刀
ITEM_NEIHUDAO = \
    {"name": "内弧刀", "rank": 1, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0",
     "weight": 1.0, "volume": 0.8, "durability": 60, "money": 280,
     "inlays": [{"name": "刀刃", "accept": "Jade|Metal", "prefix": True}],
     "inlays_prefix": "Metal",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_NEIHUDAO_ATTR"}],
     "description": "西域民族的战刀，刀刃向内弯曲，在中土并不常见"}


# 长棍
ITEM_CHANGGUN = \
    {"name": "长棍", "rank": 0, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "double_hand": True,
     "weight": 2.0, "volume": 2.0, "durability": 50, "money": 350,
     "inlays": [{"name": "棍身", "accept": "Wood|Metal|Jade"}],
     "inlays_prefix": "Jade|Metal|Wood",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_CHANGGUN_ATTR"}],
     "description": "初级长兵武器，需要双手持握"}     


# 长枪
ITEM_CHANGQIANG = \
    {"name": "长枪", "rank": 0, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "double_hand": True,
     "weight": 2.4, "volume": 2.4, "durability": 50, "money": 350,
     "inlays": [{"name": "枪杆", "accept": "Wood|Metal|Jade"},
                {"name": "枪头", "accept": "Metal"}],
     "inlays_prefix": "Metal|Wood",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_CHANGGUN_ATTR"}],
     "description": "初级长兵武器，需要双手持握"}


# 齐眉棍
ITEM_QIMEIGUN = \
    {"name": "齐眉棍", "rank": 1, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "double_hand": True,
     "weight": 2.0, "volume": 2.0, "durability": 50, "money": 350,
     "inlays": [{"name": "棍身", "accept": "Wood|Metal|Jade"}],
     "inlays_prefix": "Jade|Metal|Wood",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_QIMEIGUN_ATTR"}],
     "description": ""}
     

# 匕首     
ITEM_BISHOU = \
    {"name": "匕首", "rank": 0, "tags": "Equip,Weapon,Qimen,Duanbing", "shape": "Around,0,0,0",
     "weight": 0.5, "volume": 0.5, "durability": 55, "money": 160,
     "inlays": [{"name": "锋刃", "accept": "Metal"}],
     "inlays_prefix": "Jade",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_BISHOU_ATTR"}],
     "description": "初级短兵武器，一般用于暗杀"} 
     

# 飞刀     
ITEM_FEIDAO = \
    {"name": "飞刀", "rank": 0, "tags": "Equip,Weapon,Anqi", "shape": "Around,0,0,0",
     "weight": 2, "volume": 1.0, "durability": 100, "money": 100,
     "inlays": [{"name": "刀刃", "accept": "Metal"}],
     "inlays_prefix": "Jade",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_FEIDAO_ATTR"}],
     "description": "和匕首形似的暗器，但比匕首更小，因此可以随身携带多把"} 
     
     
ITEM_HENGDI = \
    {"name": "横笛", "rank": 0, "tags": "Equip,Weapon,Duanbing,Yueqi,Guanyue", "shape": "Around,0,0,0", 
     "weight": 0.4, "volume": 0.5, "durability": 30, "money": 180,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_HENGDI_ATTR"}],
     "description": "寻常可见的吹奏乐器，也可以当做短兵来使用"}
     

ITEM_DONGXIAO = \
    {"name": "洞箫", "rank": 0, "tags": "Equip,Weapon,Duanbing,Yueqi,Guanyue", "shape": "Around,0,0,0", 
     "weight": 0.5, "volume": 0.6, "durability": 30, "money": 200,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_DONGXIAO_ATTR"}],
     "description": "寻常可见的吹奏乐器，也可以当做短兵来使用"}

ITEM_PIPA = \
    {"name": "琵琶", "rank": 0, "tags": "Equip,Weapon,Yueqi,Xianyue", "shape": "Around,0,0,0", 
     "weight": 3, "volume": 1.8, "durability": 50, "money": 550,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_PIPA_ATTR"}],
     "description": "由西域传来的弹拨乐器，在勾栏瓦肆中十分流行"}     

     
ITEM_QIXIANQIN = \
    {"name": "七弦琴", "rank": 1, "tags": "Equip,Weapon,Yueqi,Xianyue", "shape": "Around,0,0,0", 
     "weight": 3, "volume": 2.0, "durability": 50, "money": 800,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_QIXIANQIN_ATTR"}],
     "description": "相传为上古神农氏发明，深受文人雅士喜爱"}
     
     
ITEM_SANLENGQIANG = \
    {"name": "三棱枪", "rank": 1, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "double_hand": True,
     "weight": 5, "volume": 2.5, "durability": 60,
     "inlays": [{"name": "枪杆", "accept": "Wood|Metal"},
                {"name": "枪头", "accept": "Metal"}],
     "inlays_prefix": "Metal|Wood",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_SANLENGQIANG_ATTR"}]}
     

ITEM_TAIJIHUSHOU = \
    {"name": "太极护手", "rank": 3, "tags": "Equip,Weapon,Boji", "shape": "Around,0,0,0",
     "weight": 0.2, "volume": 0.2, "durability": 50,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_TAIJIHUSHOU_ATTR"},
                 {"id": "EXERT.STATUS_JUANLIU"}]}


ITEM_DAGOUBANG = \
    {"name": "打狗棒", "rank": 4, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0",
     "weight": 1.4, "volume": 1.2, "durability": 50,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_DAGOUBANG_ATTR"},
                 {"id": "EXERT.STATUS_TUGOU"}]}

     
ITEM_ZHITAO = \
    {"name": "玳瑁指套", "rank": 2, "tags": "Equip,Weapon,Boji", "shape": "Around,0,0,0",
     "weight": 0.5, "volume": 0.2, "durability": 40,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_ZHITAO_ATTR"}]}


# 指虎
ITEM_ZHIHU = \
    {"name": "指虎", "rank": 1, "tags": "Equip,Weapon,Boji", "shape": "Around,0,0,0",
     "weight": 0.8, "volume": 0.5, "durability": 45,
     "inlays": [{"name": "指尖", "accept": "Jade|Metal"}],
     "inlays_prefix": "Metal|Jade",
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_ZHIHU_ATTR"}]}


# 合璧
ITEM_HEBI = \
    {"name": "合璧", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_XIE_HUI",
     "weight": 1.5, "volume": 1, "durability": 48, 
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_HEBI_ATTR"}],
     "description": "百兵堂玉剑舵舵主谢蕙的佩剑，原剑已断，后用另一把断剑与熔融之合铸，方才修复，因此改名合璧"}
     

# 太岳
ITEM_TAIYUE = \
    {"name": "太岳", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_YANG_LEI",
     "weight": 1.6, "volume": 1.1, "durability": 50,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_TAIYUE_ATTR"}],
     "description": "华山派掌门杨磊的佩剑，用华山赤铜精炼而成，乃是华山派镇派之宝"}
     

# 紫郢     
ITEM_ZIYING = \
    {"name": "紫郢", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_RAN_WUHUA",
     "weight": 1.5, "volume": 1, "durability": 60,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_ZIYING_ATTR"},
                 {"id": "EXERT.STATUS_CHOUSUI_XIAO_RATIO"}],
     "description": "峨眉派创派祖师所用的名剑，剑体通身发紫，故得名紫郢"}
     
     
# 青萍     
ITEM_QINGPING = \
    {"name": "青萍", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_MU_SHUANGQING",
     "weight": 1.3, "volume": 1, "durability": 45,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_QINGPING_ATTR"}],
     "description": "九溪派掌门穆怀珠的佩剑，即著名的鱼肠剑；因穆怀珠不喜其名，故改名青萍"}


# 真武
ITEM_ZHENWU = \
    {"name": "真武", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_ZHANG_YINSONG",
     "weight": 1.5, "volume": 1.2, "durability": 60,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_ZHENWU_ATTR"},
                 {"id": "EXERT.STATUS_GONGQI_XIAO_RATIO"}],
     "description": "相传为真武大帝的佩剑，为武当山镇派之宝，历来只有掌门可以使用"}
  
  
# 湛卢
ITEM_ZHANLU = \
    {"name": "湛卢", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_CHEN_TINGZHI",
     "weight": 1.3, "volume": 1, "durability": 45,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_ZHANLU_ATTR"}],
     "description": "北辰派首徒陈挺之的佩剑，为北辰派前任掌门商河洛所传；商河洛在华山击败众多高手，所用正是此剑"}
  

# 巨阙   
ITEM_JUQUE = \
    {"name": "巨阙", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "double_hand": True, "bind": "PERSON_YU_JIANQI",
     "weight": 1.3, "volume": 1, "durability": 45,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_TAIYUE_ATTR"}],
     "description": "渔阳老人俞剑奇的佩剑，乃是少见的双手重剑，一旦出鞘则气势非凡"}
     

# 攻玉     
ITEM_GONGYU = \
    {"name": "攻玉", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_YANG_LEI",
     "weight": 1.3, "volume": 1, "durability": 45,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_TAIYUE_ATTR"}],
     "description": "昆仑弟子公孙惊鸿的佩剑，原为掌门公孙衡所有；因公孙衡厚爱惊鸿，特赠与之"}
     

# 道生一     
ITEM_DAOSHENGYI = \
    {"name": "道生一", "rank": 4, "tags": "Equip,Weapon,Jianfa", "shape": "Around,0,0,0", "bind": "PERSON_YANG_LEI",
     "weight": 1.3, "volume": 1, "durability": 45,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_TAIYUE_ATTR"}],
     "description": "武当掌门张隐松的佩剑，看上去与普通长剑无异，只是刻有三字铭文道生一"}
     
     
ITEM_XUEYUE = \
    {"name": "血月", "rank": 4, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": "赵神机以人血喂成的妖刀，长四尺，细如新月，故名血月"}
     

ITEM_BAOHUAN = \
    {"name": "宝环", "rank": 4, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": "赵神机以人血喂成的妖刀，长四尺，细如新月，故名血月"}
     
     
ITEM_LONGQUE = \
    {"name": "龙雀", "rank": 4, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": "赵神机以人血喂成的妖刀，长四尺，细如新月，故名血月"}
     
     
ITEM_MINGHONG = \
    {"name": "鸣鸿", "rank": 4, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": "赵神机以人血喂成的妖刀，长四尺，细如新月，故名血月"}
     
     
ITEM_GUNZHU = \
    {"name": "滚珠", "rank": 4, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": ""}
     
     
ITEM_TAIYI = \
    {"name": "太一", "rank": 4, "tags": "Equip,Weapon,Daofa", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": ""}
     
     
ITEM_LIANGYIN = \
    {"name": "亮银", "rank": 4, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": ""}
     
     
ITEM_DINGHAI = \
    {"name": "定海", "rank": 4, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": "南少林方智所持宝棍，由月空神僧亲自挑选海石打造，因此命名定海，又兼有怀念抗倭诸将之意"}
     
     
ITEM_DINGHAI = \
    {"name": "火尖", "rank": 4, "tags": "Equip,Weapon,Changbing", "shape": "Around,0,0,0", "bind": "PERSON_ZHAO_SHENJI",
     "weight": 2, "volume": 1.5, "durability": 57,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_XUEYUE_ATTR"}],
     "description": "南少林方智所持宝棍，由月空神僧亲自挑选海石打造，因此命名定海，又兼有怀念抗倭诸将之意"}
     
     
ITEM_FENGSHOU = \
    {"name": "凤首", "rank": 4, "tags": "Equip,Weapon,Yueqi", "shape": "Around,0,0,0", "bind": "PERSON_YING_QINGFENG",
     "weight": 4.5, "volume": 4, "durability": 50, 
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_FENGSHOU_ATTR"}],
     "description": "幽冥宫玄狐使婴青凤所用的曲项琵琶，因琴头雕成凤凰模样而得名"}


# 喻日法轮
ITEM_YURIFALUN = \
    {"name": "喻日法轮", "rank": 4, "tags": "Equip,Weapon,Duanbing", "shape": "Around,0,0,0", "bind": "PERSON_CI_GUANG",
     "weight": 1.4, "volume": 0.6, "durability": 50,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_FALUN_ATTR"},
                 {"id": "EXERT.STATUS_YURI", "vice_enable": True}],
     "description": "天台庵住持慈光使用的轮宝武器，与中原常见法器似有不同"}


# 指月法轮
ITEM_ZHIYUEFALUN = \
    {"name": "指月法轮", "rank": 4, "tags": "Equip,Weapon,Duanbing", "shape": "Around,0,0,0", "bind": "PERSON_CI_GUANG",
     "weight": 1.4, "volume": 0.6, "durability": 50,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_FALUN_ATTR"},
                 {"id": "EXERT.STATUS_ZHIYUE", "vice_enable": True}],
     "description": "天台庵住持慈光使用的轮宝武器，与中原常见法器似有不同"}


ITEM_BAZHANDAO = \
    {"name": "紫金八斩刀", "rank": 2, "shape": "Around,0,0,0", "tags": "Equip,Weapon,Daofa",
     "weight": 1.5, "volume": 1, "durability": 50,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_BAZHANDAO_ATTR"}]}
    

ITEM_DANGONG = \
    {"name": "弹弓", "rank": 0, "shape": "Around,0,0,0", "tags": "Equip,Weapon,Anqi", "double_hand": True,
     "weight": 1, "volume": 0.6, "durability": 100,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_DANGONG_ATTR"}],
     "description": "常见的弹射器，可以发射石子或弹珠，小孩们喜欢用它来打鸟"}
 
     
ITEM_YANWEIBIAO = \
    {"name": "燕尾镖", "rank": 1, "shape": "Around,0,0,0", "tags": "Equip,Weapon,Anqi",
     "weight": 1, "volume": 0.5, "durability": 100,
     "effects": [{"id": "EXERT.LAMBDA.EFFECT_YANWEIBIAO_ATTR"}]}
