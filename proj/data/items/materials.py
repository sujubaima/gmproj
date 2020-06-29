# -- coding: utf-8 --

ITEM_LUYU = \
    {"name": "鲈鱼", "tags": "Material,Food,Fish",
     "rank": 1, "weight": 1, "volume": 0.5,
     "description": "一种淡水鱼类"}
     
ITEM_YAN = \
    {"name": "盐", "tags": "Material,Condiment",
     "rank": 0, "weight": 0.1, "volume": 0.1,
     "description": "主要成分为氯化钠"}
     

ITEM_MUTAN = \
    {"name": "木炭", "tags": "Material,Catalyzer",
     "rank": 0, "weight": 0.1, "volume": 0.2,
     "description": "木材烧制后的碳化物，制作物品的材料"}


ITEM_SHENGTIE = \
    {"name": "生铁", "rank": 0, "tags": "Material,Metal",
     "weight": 0.4, "volume": 0.2,
     "effects": [{"id": "EFFECT_ITEM_ADD_FUNCTION", 
                  "effect": {"id": "EXERT.LAMBDA.EFFECT_SHENGTIE_ATTR"}}],
     "description": "深山里常见的金属矿物，打造武器的基本材料之一"}


ITEM_CUTONG = \
    {"name": "粗铜", "rank": 0, "tags": "Material,Metal",
     "weight": 0.4, "volume": 0.2,
     "description": "深山里常见的金属矿物，打造武器的基本材料之一"}


ITEM_JINGTIE = \
    {"name": "精铁", "rank": 1, "tags": "Material,Metal",
     "weight": 0.4, "volume": 0.2,
     "effects": [{"id": "EFFECT_ITEM_ADD_FUNCTION",
                  "effect": {"id": "EXERT.LAMBDA.EFFECT_JINGTIE_ATTR"}}],
     "description": "质量上佳的铁矿，打造武器的常用材料之一"}


ITEM_BINTIE = \
    {"name": "镔铁", "rank": 2, "tags": "Material,Metal",
     "weight": 0.4, "volume": 0.2,
     "effects": [{"id": "EFFECT_ITEM_ADD_FUNCTION",
                  "effect": {"id": "EXERT.STATUS_GANGJIN"}}],
     "description": "从西域传来的钢铁，打造上品武器的常用材料之一"}


ITEM_YUNMU = \
    {"name": "云母", "rank": 1, "tags": "Material,Jade",
     "weight": 0.4, "volume": 0.2, "money": 150,
     "description": "玉石类矿物的一种，呈透明片状，可用于物品的装饰与点缀"}


ITEM_TONGMU = \
    {"name": "桐木", "rank": 1, "tags": "Material,Wood",
     "weight": 0.2, "volume": 0.2,
     "description": "梧桐或泡桐树干制成的木材，柔软但富有韧性"}


ITEM_WUMU = \
    {"name": "乌木", "rank": 2, "tags": "Material,Wood",
     "weight": 0.2, "volume": 0.3,
     "effects": [{"id": "EFFECT_ITEM_ADD_FUNCTION",
                  "effect": {"id": "EXERT.STATUS_JITUI_RATIO"}}],
     "description": "铁力木等树干埋藏碳化后形成的木材，质地极其坚硬"}


ITEM_TANMU = \
    {"name": "檀木", "rank": 3, "tags": "Material,Wood",
     "weight": 0.3, "volume": 0.3,
     "effects": [{"id": "EFFECT_ITEM_ADD_FUNCTION",
                  "effect": {"id": "EXERT.STATUS_ZHENJI"}}],
     "description": "紫檀树的树干加工成的木材，质地极其坚硬"}
