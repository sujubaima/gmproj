# -- coding: utf-8 --

EVENT_BATTLE_DEAD = \
    {"name": "战败死亡", "ordername": "BattleFinishOrder",
     "conditions": [{"type": "TeamBattleWinCondition", "team": "{TEAM_PERSON_PLAYER}", "expect": False}],
     "scripts": [{"type": "Action.GameFailAction"}]}


EVENT_BATTLE_RESET_PLAYER = \
    {"name": "还原玩家", "ordername": "BattleFinishOrder",
     "scripts": [{"type": "Action.ContextPlayerChangeAction", "person": "{PERSON_PLAYER}"}]}
