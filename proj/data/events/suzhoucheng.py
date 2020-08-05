# -- coding: utf-8 --

EVENT_BATTLE_LUANTAN_WIN = \
    {"name": "教训栾檀（胜）", "action": "BattleFinishAction",
     "conditions": [{"type": "TeamBattleWinCondition", "team": "{TEAM_PERSON_PLAYER}"}],
     "scripts": [{"type": "Include", "script": "SCRIPT_LUANTAN_2", 
                  "subject": "{PERSON_PLAYER}", "object": "{PERSON_LUAN_TAN}"}]}


EVENT_BATTLE_LUANTAN_LOSE = \
    {"name": "教训栾檀（负）", "ordername": "BattleFinishAction",
     "conditions": [{"type": "TeamBattleWinCondition", "team": "{TEAM_PERSON_PLAYER}", "expect": False}],
     "scripts": [{"type": "Include", "script": "SCRIPT_LUANTAN_3", 
                  "subject": "{PERSON_PLAYER}", "object": "{PERSON_LUAN_TAN}"}]}
