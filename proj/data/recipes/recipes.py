# -- coding: utf-8 --

RECIPE_QINGZHENGLUYU = \
    {"name": "清蒸鲈鱼", "tags": "Food",
     "materials": [{"id": "ITEM_LUYU"},
                   {"id": "ITEM_YAN"},
                   {"tag": "Wine"}],
     "effects": [{"id": "EFFECT_QINGZHENGLUYU_RECIPE"}]}
     
     
RECIPE_CHANGJIAN = \
    {"name": "长剑", "tags": "Equip,Weapon",
     "materials": [{"id": "ITEM_SHENGTIE", "quantity": 4},
                   {"id": "ITEM_TONGMU", "quantity": 1}],
     "effects": [{"id": "EFFECT_ITEM_MAKE", "item": "ITEM_CHANGJIAN", "rate": 1}]}
     
     
RECIPE_PODAO = \
    {"name": "朴刀", "tags": "Equip,Weapon",
     "materials": [{"id": "ITEM_SHENGTIE", "quantity": 4},
                   {"id": "ITEM_TONGMU", "quantity": 2}],
     "effects": [{"id": "EFFECT_ITEM_MAKE", "item": "ITEM_PODAO", "rate": 1}]}
 
 
RECIPE_HOUSE_SMALL = \
    {"name": "民居（小）", "tags": "Building",
     "materials": [{"id": "ITEM_LUYU"},
                   {"id": "ITEM_YAN"},
                   {"tag": "Wine"}],
     "effects": []}
