# -- coding: utf-8 --

TERRAN_BLANK = \
    {"name": "空地", "motivation": 1,
     "vision_half": {"character": " "},
     "vision_full": {"character": " "}}


TERRAN_ROAD = \
    {"name": "道路", "motivation": 1,
     "vision_half": {"character": "十"},
     "vision_full": {"character": "十"}}


TERRAN_WATER = \
    {"name": "水域", "motivation": -1,
     "vision_half": {"character": "~", "effects": {"color": "cyan", "attrs": ["bold"]}},
     "vision_full": {"character": "~", "effects": {"color": "cyan", "attrs": ["bold"]}}}


TERRAN_HILL = \
    {"name": "丘陵", "motivation": 2,
     "vision_half": {"character": "⌒ ", "effects": {"color": "yellow", "attrs": ["dark"]}},
     "vision_full": {"character": "⌒", "effects": {"color": "yellow", "attrs": ["dark"]}}}
     

TERRAN_MARSH = \
    {"name": "洼地", "motivation": 2,
     "vision_half": {"character": "︶", "effects": {"color": "yellow", "attrs": ["dark"]}},
     "vision_full": {"character": "︶", "effects": {"color": "yellow", "attrs": ["dark"]}}}


TERRAN_MOUNTAIN = \
    {"name": "山岳", "motivation": -1,
     "vision_half": {"character": "Λ ", "effects": {"color": "yellow", "attrs": ["dark"]}},
     "vision_full": {"character": "Λ", "effects": {"color": "yellow", "attrs": ["dark"]}}}


TERRAN_GRASS = \
    {"name": "草地", "motivation": 1,
     "vision_half": {"character": "ｖ", "effects": {"color": "green"}},
     "vision_full": {"character": "ｖ", "effects": {"color": "green"}}}


TERRAN_FLOWER_RED = \
    {"name": "红花", "motivation": 1,
     "vision_half": {"character": "＊", "effects": {"color": "red", "attrs": ["dark"]}},
     "vision_full": {"character": "＊", "effects": {"color": "red", "attrs": ["dark"]}}}
     
     
TERRAN_FLOWER_YELLOW = \
    {"name": "黄花", "motivation": 1,
     "vision_half": {"character": "＊", "effects": {"color": "yellow", "attrs": ["dark"]}},
     "vision_full": {"character": "＊", "effects": {"color": "yellow", "attrs": ["dark"]}}}
     

#丯龵
TERRAN_FOREST = \
    {"name": "树林", "motivation": 1,
     "vision_half": {"character": "礻", "effects": {"color": "green"}},
     "vision_full": {"character": "礻", "effects": {"color": "green"}}}
     
     
TERRAN_CLIFF = \
    {"name": "悬崖", "motivation": 1,
     "vision_half": {"character": "/", "effects": {"color": "yellow", "attrs": ["dark"]}},
     "vision_full": {"character": "/", "effects": {"color": "yellow", "attrs": ["dark"]}}}


TERRAN_JUNGLE = \
    {"name": "密林", "motivation": 1,
     "vision_half": {"character": "林", "effects": {"color": "green"}},
     "vision_full": {"character": "林", "effects": {"color": "green"}}}


TERRAN_DESERT = \
    {"name": "沙漠", "motivation": 2,
     "vision_half": {"character": ". ", "effects": {"color": "yellow"}},
     "vision_full": {"character": ". ", "effects": {"color": "yellow"}}}


TERRAN_SNOW = \
    {"name": "雪地", "motivation": 2,
     "vision_half": {"character": "* ", "effects": {"attrs": ["bold"]}},
     "vision_full": {"character": "* ", "effects": {"attrs": ["bold"]}}}


TERRAN_CLOUD = \
    {"name": "云雾", "motivation": 2,
     "vision_half": {"character": "~ ", "effects": {"color": "grey", "attrs": ["bold"]}},
     "vision_full": {"character": "~ ", "effects": {"color": "grey", "attrs": ["bold"]}}}
