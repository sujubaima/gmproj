# -- coding: utf-8 --

EVENT_BATTLE_TUITION_FORBID_ATTACK = \
    {"name": "教程1", "ordername": "BattleNewTurnAction",
     "conditions": [{"type": "BattlePersonTurnCondition", 
                     "person": "{PERSON_PLAYER_TUITION}"}],
     "scripts": [{"type": "Action.BattleOrderStatusAction", 
                  "subject": "{PERSON_PLAYER_TUITION}", "order": "attack", "status": True},
                 {"type": "Action.BattleOrderStatusAction", 
                  "subject": "{PERSON_PLAYER_TUITION}", "order": "item", "status": True},
                 {"type": "Action.EventSwitchOnAction", 
                  "event": "EVENT_BATTLE_TUITION_FORBID_ATTACK"}]}
                  

EVENT_BATTLE_TUITION_1 = \
    {"name": "教程1", "ordername": "BattleNewTurnAction",
     "conditions": [{"type": "BattlePersonTurnCondition", 
                     "person": "{PERSON_PLAYER_TUITION}"}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_2"}]}
                  
                  
EVENT_BATTLE_TUITION_2 = \
    {"name": "教程2", "ordername": "BattleMoveEnsureAction",
     "conditions": [{"type": "BattlePersonPositionOnCondition", 
                     "person": "{PERSON_PLAYER_TUITION}", "location": "(2, 2)"}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_3"},
                 {"type": "Action.EventSwitchOffAction", 
                  "event": "EVENT_BATTLE_TUITION_MOVE_WRONG"}]}
                  

EVENT_BATTLE_TUITION_MOVE_WRONG = \
    {"name": "教程2", "ordername": "BattleMoveEnsureAction", "phase": 0,
     "conditions": [{"type": "ActionCurrentAttributeCondition", 
                     "attribute": "position", "value": "(2, 2)", "expect": False}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_2_1"},
                 {"type": "Action.CancelAction"},
                 {"type": "Action.EventSwitchOnAction", 
                  "event": "EVENT_BATTLE_TUITION_MOVE_WRONG"},
                 {"type": "Control.BattleControl"}]}                
                  
                  
EVENT_BATTLE_TUITION_3 = \
    {"name": "教程3", "ordername": "BattleNewTurnAction",
     "conditions": [{"type": "BattlePersonTurnCondition", 
                     "person": "{PERSON_PLAYER_TUITION}"}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_4"}]}
                  
                  
EVENT_BATTLE_TUITION_4 = \
    {"name": "教程4", "ordername": "BattleMoveEnsureAction",
     "conditions": [{"type": "BattlePersonsDistanceCondition", 
                     "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_MURENZHUANG}", "range": "[1, 1]"}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_5"},
                 {"type": "Action.EventSwitchOffAction", 
                  "event": "EVENT_BATTLE_TUITION_FORBID_ATTACK"},
                 {"type": "Action.BattleOrderStatusAction", 
                  "subject": "{PERSON_PLAYER_TUITION}", "order": "attack", "status": False}]}
                  
                  
EVENT_BATTLE_TUITION_5 = \
    {"name": "教程5", "ordername": "BattleSkillAction",
     "conditions": [{"type": "BattlePersonTurnCondition", 
                     "person": "{PERSON_PLAYER_TUITION}"}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_6"}]}
                  

EVENT_BATTLE_TUITION_ATTACK_SCOPE = \
    {"name": "教程-讲解攻击范围", "ordername": "BattleSkillAction",
     "conditions": [{"type": "ActionCurrentAttributeCondition", 
                     "attribute": "skill", "value": "{ITEM_CHANGJIAN}"}],
     "scripts": [{"type": "Include", 
                  "subject": "{PERSON_PLAYER_TUITION}", "object": "{PERSON_GENG_ZHUQIAO}", 
                  "script": "SCRIPT_BATTLE_TUITION_8"}]}
                  
                  
EVENT_BATTLE_TUITION_FINISH = \
    {"name": "教程结束", "ordername": "BattleFinishAction",
     "scripts": [{"type": "Include", 
                  "script": "SCRIPT_GENGZHUQIAO_1", 
                  "subject": "{PERSON_PLAYER}", "object": "{PERSON_GENG_ZHUQIAO}", "from": "LABEL_J"}]}
