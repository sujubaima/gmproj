# -- coding: utf-8 --

DIALOG_ZHAOQIER_1 = \
    [{"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "（看戏中）哎呀，这个西施怎么跟吴王好上了！"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "历史上西施就是跟吴王好上了，你这都不知道？"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "可是我哥跟我说，西施最后跟范大夫在一起了啊？"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "这不是还没演完吗，吴王得到西施之后便沉迷酒色，致使国力不振。再然后范蠡和越王勾践卧薪尝胆……"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "停停停，你别说了。这本戏我第一次看，你不要跟我剧透好伐？"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "你哥不是已经告诉你结局了吗？"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "我哥只跟我说了西施和范大夫，没有什么吴王越王的。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "……行吧，那你继续欣赏，我不打扰你了。"},
     {"type": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_ZHAO_LING}", "conversation": "DIALOG_ZHAOQIER_2"}]


DIALOG_ZHAOQIER_2 = \
    [{"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "我跟你讲，我大哥就是丐帮的八袋长老路不平。他本来是我师父，有一次和我打赌打输了，就变成我大哥了。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "所以呢？"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "所以你能不能冲着我大哥的名号，施舍我一点银钱啊。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "……"}]
