# -- coding: utf-8 --

EVENT_START = \
  {"name": "开始脚本", "active": True,
   "scripts": [{"type": "Set", "subject": "{PERSON_PLAYER}", "object": "{PERSON_DENG_MAFU_SUZHOU}"},
               {"type": "Include", "script": "SCRIPT_INITIALIZE_1"},
               {"type": "Action.WorldShowMapAction", "show_trace": False},
               {"type": "Include", "script": "SCRIPT_INITIALIZE_2"}]}
