# -- coding: utf-8 --

EVENT_START = \
  {"name": "开始脚本", "active": False,
   "actions": [{"type": "PersonConversationAction", "conversation": "DIALOG_INITIALIZE_1"},
               {"type": "WorldShowMapAction", "show_trace": False},
               {"type": "PersonConversationAction", "conversation": "DIALOG_INITIALIZE_2", "subject": "{PERSON_PLAYER}"},
               {"type": "WorldMoveAction", "subject": "{TEAM_PERSON_PLAYER}", "target": "(23, 16)"},
               {"type": "EventSwitchOnAction", "event": "EVENT_START_2"}]}
               
   
EVENT_START_2 = \
  {"name": "开始脚本3",
   "conditions": [{"type": "TeamPositionOnCondition", "team": "{TEAM_PERSON_PLAYER}", "scenario": "{MAP_SUZHOUCHENG}", "location": "(23, 16)"}],
   "actions": [{"type": "WorldShowMapAction", "show_trace": True},
               {"type": "PersonConversationAction", "conversation": "DIALOG_INITIALIZE_3", 
                "subject": "{PERSON_PLAYER}", "object": "{PERSON_DENG_MAFU_SUZHOU}"},
               {"type": "WorldTeamCleanPathAction", "team": "{TEAM_PERSON_PLAYER}"},
               {"type": "EventSwitchOnAction", "event": "EVENT_START_4"}]}
                
EVENT_START_4 = \
  {"name": "开始脚本4",
   "actions": [{"type": "PersonConversationAction", "conversation": "DIALOG_INITIALIZE_4", 
                "subject": "{PERSON_PLAYER}"}]}
