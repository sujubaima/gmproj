# -- coding: utf-8 --

SCRIPT_WANPENGFEI_TEST = \
    [#{"Set": {"subject": "{PERSON_PLAYER}", "object": "{PERSON_WANPENGFEI}"}},
     #{"Include": "SCRIPT_WANPENGFEI_ANIMATION_1"},
     {"Action.PersonSpeakAction": {"content": "（客栈南窗最显眼的位置上，坐着一个瘦长汉子，背上挂着一柄单刀，自顾自地饮酒吃菜。）"}},
     {"Action.PersonSpeakAction": {"talker": "(plot.object)",
                                   "content": "十年磨一刀，霜刃未曾试。"}},
     {"label": "LABEL_SCRIPT_WANPENGFEI_B1",
      "Branch": [{"label": "LABEL_SCRIPT_WANPENGFEI_1A"},
                 {"label": "LABEL_SCRIPT_WANPENGFEI_1B"}]},
     {"label": "LABEL_SCRIPT_WANPENGFEI_1A",
      "Action.PersonSpeakAction": {"talker": "(plot.subject)",
                                   "content": "你念错了吧，明明是十年磨一剑。"}},
     {"next": "LABEL_SCRIPT_WANPENGFEI_1C",
      "Action.PersonSpeakAction": {"talker": "(plot.object)",
                                   "content": "哈哈哈，他人用剑，鄙人万鹏飞喜欢用刀。这么念又有何不可？"}},
     {"label": "LABEL_SCRIPT_WANPENGFEI_1B",
      "Action.PersonSpeakAction": {"talker": "(plot.subject)",
                                   "content": "今日把示君，谁有不平事！"}},
     {"next": "LABEL_SCRIPT_WANPENGFEI_1C",
      "Action.PersonSpeakAction": {"talker": "(plot.object)",
                                   "content": "好！兄台这两句接得正是时候！要不是看在客栈人多，鄙人都想要舞刀助兴了。"}},
     {"label": "LABEL_SCRIPT_WANPENGFEI_TEST",
      "Action.PersonSpeakAction": {"talker": "(plot.subject)",
                                   "content": "别念了好烦啊！"}},
     {"next": "LABEL_SCRIPT_WANPENGFEI_1C",
      "Action.PersonSpeakAction": {"talker": "(plot.object)",
                                   "content": "你想要的吃我的刀子吗？"}},
     {"label": "LABEL_SCRIPT_WANPENGFEI_1C",
      "Action.PersonSpeakAction": {"talker": "(plot.subject)",
                                   "content": "看来兄台是位刀法高手！"}},
     {"Action.PersonSpeakAction": {"talker": "(plot.object)",
                                   "content": "高手说不上，只是小时候跟乡间武师们学过一点皮毛。但是成为一代刀法宗师，确实是鄙人的夙愿。"}},
     {"Action.PersonSpeakAction": {"talker": "(plot.subject)",
                                   "content": "那兄台可曾去遍寻名师，学几门绝世刀法？"}},
     {"Action.PersonSpeakAction": {"talker": "(plot.object)",
                                   "content": ["说来见笑，这苏州城里并没有什么用刀的好手。",
                                               "我原本想去百兵堂、风云盟，还有南少林等地求访高人，只是路途遥远，迟迟没有成行。"]}},
     {"Action.PersonSpeakAction": {"talker": "(plot.subject)",
                                   "content": "走，我们出发！"}},
     {"Action.TeamIncludePersonAction": {"person": "{PERSON_WAN_PENGFEI}", "leader": "{PERSON_PLAYER}"}},
     {"Action.PersonTaskUpdateAction": {"task": "TASK_HUIGUIXIANSHI", "contents": ["TASK_HUIGUIXIANSHI_1"]}},
     {"Action.SessionChangeBranchAction": {"script": "SCRIPT_WANPENGFEI_TEST", "branch": "LABEL_SCRIPT_WANPENGFEI_B1",
                                           "position": 1, "label": "LABEL_SCRIPT_WANPENGFEI_TEST"}}]
