# -- coding: utf-8 --

SCRIPT_INITIALIZE_1 = \
    [{"type": "Action.PersonSpeakAction", 
      "content": "（明万历三十五年某月某日，苏州城。马夫邓大叔将一个年轻人送出驿站。）"}]

SCRIPT_INITIALIZE_2 = \
    [{"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "少侠，苏州城到了，你感觉怎么样啊？"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "赵先生说得果然不错，上有天堂，下有苏杭。可以考虑把这里当做我闯荡江湖的第一站！"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "别考虑了，少侠就你那点盘缠，也只够老夫送你到苏州了，别的地方去不了。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "啊？我还想把少林武当都见识完一圈再决定从哪儿出道呢。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "咱们驿站可还是要做生意的。要么您出钱，要么您还是自己走过去吧。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "大叔，能不能通融通融，再带我去几个地方。万一我以后成了大侠，必定来报答大叔。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "你这种想做大侠的臭小子，我见得多了，哪里通融得过来！"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "好吧，那大叔能不能再指点一下，从哪可以赚点路费？"}, 
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "你……你这什么都不懂还出来混！也罢也罢，你去街上打听打听，总有人托付事情，多多少少能挣些报酬，够你在这落脚了。"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "谢谢大叔！"},
     {"type": "Action.PersonSpeakAction",
      "content": "这时有一队官吏从旁敲锣经过。"},
     {"type": "Action.PersonSpeakAction", "talker": "{PERSON_ZHAO_YAYI_SUZHOU}",
      "content": "近日苏州城北有盗匪剪径伤人，望居民出城多加防范，切忌远离官道！"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.object)",
      "content": "唉，盗贼蜂起，这世道不太平哪！"},
     {"type": "Action.PersonSpeakAction", "talker": "(plot.subject)",
      "content": "……"},
     {"type": "Action.PersonTaskUpdateAction", 
      "task": "TASK_SHENGCUNZHIDAO", "contents": ["TASK_SHENGCUNZHIDAO_1"]}]


SCRIPT_WANPENGFEI_1 = \
    [{"type": "PersonSpeakAcction", 
      "content": "（客栈南窗最显眼的位置上，坐着一个瘦长汉子，背上挂着一柄单刀，自顾自地饮酒吃菜。）"},
     {"style": "Speak", "talker": "object", 
      "content": "十年磨一刀，霜刃未曾试。"},
     {"type": "Branch",
      "branches": [{"label": "SCRIPT_WANPENGFEI_BRANCH_A1"},
                   {"label": "SCRIPT_WANPENGFEI_BRANCH_A2"}]},
     {"style": "Speak", "talker": "object", "label": "SCRIPT_WANPENGFEI_BRANCH_A1",
      "content": "你念错了吧，明明是十年磨一剑。"},
     {"style": "Speak", "talker": "subject", "next": "SCRIPT_WANPENGFEI_HUB_A",
      "content": "哈哈哈，他人用剑，鄙人万鹏飞喜欢用刀。这么念又有何不可？"},
     {"style": "Speak", "talker": "subject", 
      "content": "今日把示君，谁有不平事！", "label": "SCRIPT_WANPENGFEI_BRANCH_A2"},
     {"style": "Speak", "talker": "object", 
      "content": "好！兄台这两句接得正是时候！要不是看在客栈人多，鄙人都想要舞刀助兴了。"},
     {"style": "Speak", "talker": "object", "label": "SCRIPT_WANPENGFEI_HUB_A",
      "content": "看来兄台是位刀法高手！"},
     {"style": "Speak", "talker": "subject", 
      "content": "高手说不上，只是小时候跟乡间武师们学过一点皮毛。但是成为一代刀法宗师，确实是鄙人的夙愿。"},
     {"style": "Speak", "talker": "object", 
      "content": "那兄台可曾去遍寻名师，学几门绝世刀法？"},
     {"style": "Speak", "talker": "subject", 
      "content": "说来见笑，这苏州城里并没有什么用刀的好手。我原本想去百兵堂、风云盟，还有南少林等地求访高人，只是路途遥远，迟迟没有成行。"},
     {"style": "Speak", "talker": "object", 
      "content": "这就是问题，听说有一个出口可以返回人间，但不知道具体在哪。可能要成为武林盟主什么的才能解锁吧。"},
     {"style": "Speak", "talker": "subject", 
      "content": "草，好不容易意识穿越一把，怎么遇到的是这么土的设定。"},
     {"style": "Speak", "talker": "object", 
      "content": "你想要什么设定？你是想做天际省法师张三，还是洛圣都悍匪李四？你的名字放进去不觉得很出戏吗？"},
     {"style": "Speak", "talker": "subject", 
      "content": "难道武林盟主白老师听上去就很响亮吗？"},
     {"style": "Speak", "talker": "object", 
      "content": "够了，不要抬杠。再说了，做武林盟主的搞不好是我不是你哦，不信咱俩试试。"},
     {"style": "Speak", "talker": "", 
      "content": "（万鹏飞话音刚落，便操起手中的弯刀往你脸上抹过来。你情急之下只好架起双拳，一顿乱挥。" + 
                 "没想到万鹏飞只是虚晃一招，你正准备还击的时候，他已经笑嘻嘻地收刀入鞘。）"},
     {"style": "Speak", "talker": "subject", 
      "content": "卧槽，你怎么还会武功？"},
     {"style": "Speak", "talker": "object", 
      "content": "我刚来的时候一个NPC教给我的，刚才那些关于这个世界的事情也是他说的，说完人就消失了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "有主线任务和武功凭什么只告诉你不告诉我？"},
     {"style": "Speak", "talker": "object", 
      "content": "可能是觉得我比较像主角吧。"},
     # 20
     {"style": "Speak", "talker": "subject", 
      "content": "行行行，你是主角，你带着我混吧。"},
     {"style": "Speak", "talker": "object", 
      "content": "好，那大哥要启程了，小弟你赶紧跟上。"},
     {"style": "Branch", "branches": ["SCRIPT_WANPENGFEI_A", "SCRIPT_WANPENGFEI_B"]},
     {"style": "Speak", "talker": "subject", "label": "SCRIPT_WANPENGFEI_A",
      "content": "等下，我先去上个厕所，待会再回来找你。"},
     {"style": "Speak", "talker": "object",
      "content": "……"},
     {"style": "Script", "next": 999,
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_WAN_PENGFEI}", "conversation": "DIALOG_WANPENGFEI_2"},
     {"style": "Speak", "talker": "subject", "label": "SCRIPT_WANPENGFEI_B",
      "content": "走，我们出发！"},
     {"style": "Script", 
      "scripts": [{"type": "Action.TeamIncludePersonAction", 
                   "person": "{PERSON_WAN_PENGFEI}", "leader": "{PERSON_PLAYER}"},
                  {"type": "Action.PersonTaskUpdateAction", 
                   "task": "TASK_HUIGUIXIANSHI", "contents": ["TASK_HUIGUIXIANSHI_1"]}]}]
                   

DIALOG_WANPENGFEI_1 = \
    [{"style": "Speak", "talker": "", 
      "content": "（客栈南窗最显眼的位置上，坐着一个瘦长汉子。你仔细辨别，发现竟然是自己的同事万鹏飞。）"},
     {"style": "Speak", "talker": "subject", 
      "content": "鹏飞！你怎么在这！"},
     {"style": "Speak", "talker": "object", 
      "content": "白老师，我已经在此等你数日了。关于你现在的处境，我有重要的事情告诉你。"},
     {"style": "Speak", "talker": "subject", 
      "content": "那你快说，这个奇怪的世界到底是怎么回事？"},
     {"style": "Speak", "talker": "object", 
      "content": "这是一个幻觉构成的世界，你濒死状态下的意识漂流到了这里。你的身体其实还在ICU里抢救，想要活下去就必须找到离开这个世界的办法。"},
     # 5
     {"style": "Speak", "talker": "subject", 
      "content": "原来我还没被救活……可既然这是濒死状态产生的幻觉世界，莫非你也……？"},
     {"style": "Speak", "talker": "object", 
      "content": "害，最近加班的人又不止你一个，大家都扛不住了。你再晚两天倒的话，进ICU都要摇号了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "那你刚提到的离开这个世界的办法是什么？"},
     {"style": "Speak", "talker": "object", 
      "content": "这就是问题，听说有一个出口可以返回人间，但不知道具体在哪。可能要成为武林盟主什么的才能解锁吧。"},
     {"style": "Speak", "talker": "subject", 
      "content": "武林盟主？"},
     # 10
     {"style": "Speak", "talker": "object", 
      "content": "对呀这是个武侠背景的世界。你来多久了，怎么还懵懵懂懂的。"},
     {"style": "Speak", "talker": "subject", 
      "content": "草，好不容易意识穿越一把，怎么遇到的是这么土的设定。"},
     {"style": "Speak", "talker": "object", 
      "content": "你想要什么设定？你是想做天际省法师张三，还是洛圣都悍匪李四？你的名字放进去不觉得很出戏吗？"},
     {"style": "Speak", "talker": "subject", 
      "content": "难道武林盟主白老师听上去就很响亮吗？"},
     {"style": "Speak", "talker": "object", 
      "content": "够了，不要抬杠。再说了，做武林盟主的搞不好是我不是你哦，不信咱俩试试。"},
     # 15
     {"style": "Speak", "talker": "", 
      "content": "（万鹏飞话音刚落，便操起手中的弯刀往你脸上抹过来。你情急之下只好架起双拳，一顿乱挥。" + 
                 "没想到万鹏飞只是虚晃一招，你正准备还击的时候，他已经笑嘻嘻地收刀入鞘。）"},
     {"style": "Speak", "talker": "subject", 
      "content": "卧槽，你怎么还会武功？"},
     {"style": "Speak", "talker": "object", 
      "content": "我刚来的时候一个NPC教给我的，刚才那些关于这个世界的事情也是他说的，说完人就消失了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "有主线任务和武功凭什么只告诉你不告诉我？"},
     {"style": "Speak", "talker": "object", 
      "content": "可能是觉得我比较像主角吧。"},
     # 20
     {"style": "Speak", "talker": "subject", 
      "content": "行行行，你是主角，你带着我混吧。"},
     {"style": "Speak", "talker": "object", 
      "content": "好，那大哥要启程了，小弟你赶紧跟上。"},
     {"style": "Branch", "branches": [23, 26]},
     {"style": "Speak", "talker": "subject", 
      "content": "等下，我先去上个厕所，待会再回来找你。"},
     {"style": "Speak", "talker": "object",
      "content": "……"},
     # 25
     {"style": "Script", "next": 999,
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_WAN_PENGFEI}", "conversation": "DIALOG_WANPENGFEI_2"},
     {"style": "Speak", "talker": "subject", 
      "content": "走，我们出发！"},
     {"style": "Script", 
      "scripts": [{"type": "Action.TeamIncludePersonAction", 
                   "person": "{PERSON_WAN_PENGFEI}", "leader": "{PERSON_PLAYER}"},
                  {"type": "Action.PersonTaskUpdateAction", 
                   "task": "TASK_HUIGUIXIANSHI", "contents": ["TASK_HUIGUIXIANSHI_1"]}]}]
     
     
DIALOG_WANPENGFEI_2 = \
    [{"style": "Speak", "talker": "object", 
      "content": "你厕所上完了没有啊？"},
     # 20
     {"style": "Branch", "branches": [2, 4]},
     {"style": "Speak", "talker": "subject", 
      "content": "还没有，待会再回来找你。"},
     {"style": "Speak", "talker": "object", "next": 999,
      "content": "……"},
     {"style": "Speak", "talker": "subject", 
      "content": "完事了，我们出发！"},
     {"style": "Script", 
      "scripts": [{"type": "Action.TeamIncludePersonAction", 
                   "person": "{PERSON_WAN_PENGFEI}", "leader": "{PERSON_PLAYER}"},
                  {"type": "Action.PersonTaskUpdateAction", 
                   "task": "TASK_HUIGUIXIANSHI", "contents": ["TASK_HUIGUIXIANSHI_1"]}]}]
  

DIALOG_HUANGJINJIA_1 = \
    [{"style": "Speak", "talker": "", 
      "content": "（一个身形矫健的汉子靠在北辰派外面的墙壁上，他脸上似乎有几道刀疤，走近一看才发现那是犯人才有的黥面。）"},
     {"style": "Speak", "talker": "object", 
      "content": "小兄弟想不想知道些江湖传闻？"},
     {"style": "Speak", "talker": "subject", 
      "content": "有什么江湖传闻？"}, 
     {"style": "Speak", "talker": "object", 
      "content": "江湖传闻那可太多了，就说这近的。北辰派的剑法与学问历来为人称道，但依我看来，不过是徒有虚名。" + 
                 "他们的大当家陈挺之脸皮还挺厚，动不动就把其他门派的武学贬得一文不值。"
                 "其实北辰派要是真有什么厉害东西，就凭陈挺之那点能耐，早就像巨阙门一样被人盯上了，怎么可能还在这苏州城里偏安一隅？"},
     {"style": "Speak", "talker": "subject", 
      "content": "嗯？你刚说的巨阙门又是什么事件？"},
     {"style": "Speak", "talker": "object", 
      "content": "哦，没、没什么，你别打岔。"},
     {"style": "Speak", "talker": "subject", 
      "content": "明明是你先拿巨阙门举例子的。"},
     {"style": "Speak", "talker": "object", 
      "content": "例子是可以瞎编的，难道你做文章的时候就没有编造过子曰诗云之类的吗？"},
     {"style": "Speak", "talker": "subject", 
      "content": "好吧，确实编过……不过我们一般编的是鲁迅。"},
     {"style": "Speak", "talker": "object", 
      "content": "编谁都一样。总之陈挺之要是在你面前把自家武功吹得天花乱坠，你别信以为真就行了。"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_2"}]


DIALOG_HUANGJINJIA_2 = \
    [{"style": "Speak", "talker": "object", 
      "content": "偌大个苏州城，称得上高手的恐怕没几个。小兄弟要是想在武学上有所进步，恐怕还得去其他地方碰碰运气。"},
     {"style": "Speak", "talker": "subject", 
      "content": "比如哪些地方？"},
     {"style": "Speak", "talker": "object", 
      "content": "远一点的少林武当，近一点的杭州城里，风云盟的功夫也是不赖的。"},
     {"style": "Speak", "talker": "subject", 
      "content": "风云盟是什么组织？"},
     {"style": "Speak", "talker": "object", 
      "content": "这风云盟的创始人归海平，原本是戚家军的一个校尉，后来戚将军调任北地，归海平留下来作为义军继续对抗倭寇。" +
                 "久而久之，这支义军就发展成了风云盟。风云盟内部大多是军旅子弟，所以武学简洁凌厉，配合戚将军留下的鸳鸯阵，攻防一体。" +
                 "戚将军去世之前，把自己的武学著作《纪效新书》传给了风云盟。从此之后，风云盟在江湖中地位就更高一筹了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "那有时间我一定要去拜访一下风云盟。"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_3"}]
      
      
DIALOG_HUANGJINJIA_3 = \
    [{"style": "Speak", "talker": "object", 
      "content": "除了风云盟，武林中还有个响当当的组织叫百兵堂。" + 
                 "创始人武十全原本是个铁匠，有一身家传功夫，但最出名的还是他铸造的各种精良兵器。" +
                 "他建立百兵堂，原本也只是给自己的兵器提供一个演武的场所而已。" +
                 "可没想到被这些神兵利器吸引前来的人越来越多，大家都想跟在武十全身边，最后竟然一下子就生出来四大分舵。" +
                 "不过这些人里除了几个分舵主外，大部分都是些乌合之众。"}, 
     {"style": "Speak", "talker": "subject", 
      "content": "百兵堂这四大分舵分别是哪四大？"},    
     {"style": "Speak", "talker": "object", 
      "content": "铁枪舵、钢刀舵、金鞭舵以及玉剑舵，分别擅长枪法、刀法、剑法以及奇门类武学。" +
                 "这四大分舵主都是带艺入门，因此整个百兵堂的武学十分混杂，毫无系统可言。"},
     {"style": "Speak", "talker": "subject", 
      "content": "天下攘攘，皆为利往。为了顶级装备，大家凑到一起工作也是可以理解的嘛。"},                 
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_4"}]
     
     
DIALOG_HUANGJINJIA_4 = \
    [{"style": "Speak", "talker": "object", 
      "content": "少林、武当、丐帮、峨眉作为四大门派，武学都有高明之处，但近年来人才也相当匮乏。" +
                 "少林的觉因方丈重佛法而轻武学，连般若堂堂主月空和尚都因此赌气出走泉州。" +
                 "武当掌门张隐松威望虽高，颇有些武林盟主的气势，可他不懂教人，门下能领悟太极功法的寥寥无几。" + 
                 "丐帮帮主邢飞龙常年行踪不定，传功长老厉苍鹰代为处理帮内事务，也无暇教习帮众武艺。" +
                 "而峨眉派早些年间分裂成释门道门，高深武学互不相传，以致日益衰败。" + 
                 "不过也正因为如此，才使得其他小门派迅猛发展，有了今日武林的繁荣之相。"}, 
     {"style": "Speak", "talker": "subject", 
      "content": "释门道门是怎么回事？"},    
     {"style": "Speak", "talker": "object", 
      "content": "峨眉山最早为道士所据，后来渐渐有了僧众上山。原本两派倒也相安无事，各自的武学也能互相分享。" +
                 "但如今佛学兴旺，峨眉释门有一家独大的趋势。那道门自觉峨眉功夫由他初创，而如今风头都被释门夺去，便耿耿于怀。" +
                 "而释门又觉得道门武功，常有不合佛理之处，由是龃龉频生，最后不再往来了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "看来内讧真是武侠世界亘古不变的主题之一呢。"},                  
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_5"}]
     
     
DIALOG_HUANGJINJIA_5 = \
    [{"style": "Speak", "talker": "object", 
      "content": "青城、华山、崆峒、点苍乃是中原武林中后起之秀，不过规模上还是无法与四大高门相提并论。" +
                 "青城掌门玄谷子为人好义，以天师传人自诩，江湖上有斩邪除魔之事，往往第一个出面。" +
                 "华山掌门杨磊，年纪轻轻便精通了华山首屈一指的『太岳三青峰』剑法，不少武林后辈都以之为榜样。" +
                 "崆峒掌门严铭九、点苍掌门梅选冰名气不及前两位，但也算是一时之豪杰。"},    
     {"style": "Speak", "talker": "subject", 
      "content": "华山首屈一指的剑法怎么是『太岳三青峰』，不是『独孤九剑』啊？"},    
     {"style": "Speak", "talker": "object", 
      "content": "『独孤九剑』是什么东西？"},
     {"style": "Speak", "talker": "subject", 
      "content": "看来这个世界没有『独孤九剑』这门武功。"},                  
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_6"}]
     
     
DIALOG_HUANGJINJIA_6 = \
    [{"style": "Speak", "talker": "object", 
      "content": "中原之外，还有昆仑、天山、吐蕃密宗、幽冥宫诸派。" + 
                 "昆仑、天山的武学与中土渊源极深，都以奇诡著名，实际上都是故弄玄虚罢了。" + 
                 "吐蕃密宗不甚了解。但幽冥宫近年来强人倍出，颇有染指中原武林之意。"},
     {"style": "Speak", "talker": "subject", 
      "content": "这个幽冥宫又是什么来头？"},
     {"style": "Speak", "talker": "object", 
      "content": "怪就怪在，这幽冥宫宫主齐成败，谁也不知道他的身世，仿佛突然之间就冒了出来。" + 
                 "他在西域仿照《山海经》里所述的幽都建立了幽冥宫，下面设有玄鸟、玄蛇、玄豹、玄虎、玄狐五玄使。" + 
                 "只要有人前去投奔，他也不管是否作奸犯科、欺师灭祖之徒，都一并收留。" + 
                 "再加上幽冥宫行事确实诡异无常，因此惹怒了不少中原正派。" +
                 "数年前武当张掌门曾经牵头，想同中原各派剿灭幽冥宫，因为少林寺觉因方丈不同意而未成行。" +
                 "如今幽冥宫势力越来越大，怕是张掌门又要旧事重提了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "少林方丈为何不同意剿灭幽冥宫？"},
     {"style": "Speak", "talker": "object", 
      "content": "掌门人开峰会，我哪能在场？不过是道听途说，道听途说而已。"},
     {"style": "Speak", "talker": "subject", 
      "content": "……将来报道上出了偏差，你是要负责任地！"},       
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_7"}]
     
     
DIALOG_HUANGJINJIA_7 = \
    [{"style": "Speak", "talker": "subject", 
      "content": "听你讲了这么多江湖上的掌故，你都是从哪打听来的？"},
     {"style": "Speak", "talker": "object", 
      "content": "大部分都是尽人皆知的事，只不过看你刚上道，而且我在这里也无聊得紧，所以才讲给你听。"},
     {"style": "Speak", "talker": "subject", 
      "content": "江湖故事讲完了，你是不是该讲一讲你自己的故事了？"},
     {"style": "Speak", "talker": "object", 
      "content": "我区区一介游侠，哪有什么故事！"},
     {"style": "Branch", "branches": [5, 8]},
     {"style": "Speak", "talker": "subject", 
      "content": "那你脸上的黥印是怎么回事？"},
     {"style": "Speak", "talker": "object", 
      "content": "（脸色突然一沉）那我最后再告诉你一件尽人皆知的事情。行走江湖，不该问的就不要多问。"},
     {"style": "Script", "next": 999,
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_7,1"},
     {"style": "Speak", "talker": "subject", 
      "content": "好吧，那等我在江湖里遇到什么疑问，再回来找你聊天。"},      
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_HUANG_JINJIA}", "conversation": "DIALOG_HUANGJINJIA_7,0"}]
      

DIALOG_MAYUESHI_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "小伙子，要不要买件乐器啊？这会你买的话，老夫还可以送你一本乐谱。"},
     {"style": "Speak", "talker": "subject", 
      "content": "我一个行走江湖的，买乐器干嘛？找一群掌门去组乐队吗？"},
     {"style": "Speak", "talker": "object", 
      "content": "原来是位大侠，老夫失敬。大侠有所不知，你们比武之时，若有人在后方演奏适当的乐曲，对提振士气，增益战力可都有很好的作用哪。"},
     {"style": "Speak", "talker": "subject", 
      "content": "害，说白了就是当啦啦队呗！"},
     {"style": "Speak", "talker": "object", 
      "content": "啦……啦啦队？"},
     {"style": "Speak", "talker": "subject", 
      "content": "你就当是乐队好了。"},
     {"style": "Speak", "talker": "object", 
      "content": "老夫明白……大侠要是不满足于在后方奏乐，老夫听说有几门武功是将招式蕴藏于音律之中，大侠何不买件乐器回去，钻研一下这样的武学呢？"},
     {"style": "Conditions", 
      "conditions": [{"type": "PersonInTeamCondition", "person": "{PERSON_WAN_PENGFEI}", "leader": "{PERSON_PLAYER}"}],
      "result": {"true": 8, "false": 15}},
     {"style": "Speak", "talker": "{PERSON_WAN_PENGFEI}", 
      "content": "白老师，要不咱还是买点吧，等日后队里有女队员了，真的可以组个啦啦队。"},
     {"style": "Branch", "branches": [10, 13]},
     {"style": "Speak", "talker": "subject", 
      "content": "算了吧，那么重的东西，万一以后招不到女队员怎么办？"},
     {"style": "Speak", "talker": "{PERSON_WAN_PENGFEI}", 
      "content": "白老师，你要相信自己。实在不行，你相信我也可以。"},
     {"style": "Speak", "talker": "subject", "next": 16, 
      "content": "那行吧，老板我看看这里都有什么。"},
     {"style": "Speak", "talker": "subject", "next": 14,
      "content": "你说得对，咱们多买几件，以后多招几个女队员！"},
     {"style": "Speak", "talker": "object", "next": 16,
      "content": "大侠看看都要买什么？"},
     {"style": "Speak", "talker": "subject", "next": 16,
      "content": "那就看看都有什么吧。不过我可不是要练什么武学，我就是为了陶冶情操！"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_MA_YUESHI_SUZHOU}"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_MA_YUESHI_SUZHOU}", "conversation": "DIALOG_MAYUESHI_2"}]


DIALOG_MAYUESHI_2 = \
    [{"style": "Speak", "talker": "object",
      "content": "少侠，要不要买件乐器啊？"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_MA_YUESHI_SUZHOU}"}]
     
     
DIALOG_GAOQIANG_1 = \
    [{"style": "Speak", "talker": "subject", 
      "content": "『有初来乍到之人识我名者，可至吴中客栈，有要事相商。万鹏飞。』"},
     {"style": "Conditions", 
      "conditions": [{"type": "PersonInTeamCondition", "person": "{PERSON_WAN_PENGFEI}", "leader": "{PERSON_PLAYER}"}],
      "result": {"true": 2, "false": 11}},
     {"style": "Speak", "talker": "subject", 
      "content": "鹏飞，这是你贴的？"},
     {"style": "Speak", "talker": "object", 
      "content": "对，这是公告墙，我们要是想要求些东西，也可以在这里发布悬赏帖，看会不会有人来帮我们。"},
     {"style": "Speak", "talker": "{PERSON_WAN_PENGFEI}", 
      "content": "那我们能在这张个榜，让大家帮我们找到回家的办法吗？"},
     {"style": "Speak", "talker": "subject",
      "content": "理论上是可以的，不过应该没有人能办得到……而且还有个问题，咱们的毛笔字写得太差了，写出来的东西也狗屁不通，人家不让我们贴。"},
     {"style": "Speak", "talker": "subject", 
      "content": "那你这个寻人启事怎么贴上去的？"},
     {"style": "Speak", "talker": "object", 
      "content": "找城东平江路书院的那个秀才帮我写的，润笔费贵得一比。要不想找人代笔，那只能老老实实去买几本字帖学了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "没想到还挺麻烦的。"},
     {"style": "Speak", "talker": "subject", 
      "content": "麻是麻烦点，不过白老师，我们不能成天只帮别人完成任务对不对，总有一天也要尝一回当甲方的感觉。"},
     {"style": "Speak", "talker": "subject", "next": 99,
      "content": "那等什么时候我想做甲方了再去学吧。"},
     {"style": "Speak", "talker": "subject", 
      "content": "万鹏飞？这不是我前同事的名字吗？难道他也到这里来了……看来我应该去这个吴中客栈会一会他。"}]
                 
                 
DIALOG_YEZHONG_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "台上演戏的魏公生小时候就住我家隔壁，我们还一起掏过鸟窝。没想到他现在成了名角，而我还是一事无成。" +
                 "待会演完这本，我得提前走开。要不然被他认出来，真是脸上无光。"}]
      
      
DIALOG_YEZHONG_2 = \
    [{"style": "Speak", "talker": "object", 
      "content": "戏演完了，我得回去干活了。"}]
      
      
DIALOG_YEZHONG_3 = \
    [{"style": "Speak", "talker": "object", 
      "content": "又是你啊，你老找我说话，莫非是最近家里要盖房子？"},
     {"style": "Speak", "talker": "subject", 
      "content": "为什么盖房子要来找你？"},
     {"style": "Speak", "talker": "object", 
      "content": "我是苏州城的工匠，一般来找我的，都是要盖房子的。"},
     {"style": "Branch", "branches": [4, 18]},
     {"style": "Speak", "talker": "subject", 
      "content": "那和我说说盖房子的事情吧。"},
     #5
     {"style": "Speak", "talker": "object", 
      "content": "你如果有了一块土地的所有权，就可以在上面进行建造。建造不同的建筑有不同的效果，比如田圃可以进行种植、" +
                 "营房可以进行训练等等。不同的地块可以建造的建筑也不一样，矿山只能在山地或者丘陵建造、港口只能靠近水域等等。" +
                 "别以为江湖人士不需要这些，建个根据地总比没有好，更何况还有可能发展成门派呢。"},
     {"style": "Speak", "talker": "subject", 
      "content": "我可从来没想过我有一天能开宗立派。"},
     {"style": "Speak", "talker": "object", 
      "content": "嗯，我也没想过。我觉得把手艺磨练好才是最重要的。"},
     {"style": "Script", "next": 3,
      "type": "Action.PersonConversationAddBranchAction", 
      "conversation": "DIALOG_YEZHONG_3", "master": 3, "branch": 9, "position": 1}, 
     {"style": "Speak", "talker": "subject", 
      "content": "我怎么才能获得土地的所有权？"},
     #10
     {"style": "Speak", "talker": "object", 
      "content": "一般来说有三种方式，第一种是从别人手里买下来，有时候有人会出售自己的地契，只要你有足够的钱，就能获得它；" + 
                 "第二种是强行驱赶它的所有人，举个例子，你要是能把北辰派想办法赶走，那他们的大宅子就归你了；" +
                 "第三种是找一块没人的地方占山为王，但是这种地方附近一般也很难招募到工匠，所以建造的成本与耗时都会相当高；"},
     {"style": "Speak", "talker": "subject", 
      "content": "那看来还是在有人的地方建造比较好。"},
     {"style": "Speak", "talker": "object", 
      "content": "有利也有弊吧。城镇的地块价格不菲，而且数量有限，建不了太多建筑的。"}, 
     {"style": "Script", "next": 3,
      "type": "Action.PersonConversationAddBranchAction", 
      "conversation": "DIALOG_YEZHONG_3", "master": 3, "branch": 14, "position": 2}, 
     {"style": "Speak", "talker": "subject", 
      "content": "除了拥有土地之外，建造还需要什么条件？"},
     #15
     {"style": "Speak", "talker": "object", 
      "content": "还需要建筑图纸。没有图纸的话，没人知道该建成什么样。建筑图纸可以通过学习获得。" + 
                 "有了土地和图纸，在对应地块上进行建造就行了。" + 
                 "最开始会需要消耗一些材料，但之后的事情就不用亲自操心了，直接等待建筑完成就行。"},
     {"style": "Speak", "talker": "subject", 
      "content": "那你肯定有很多建筑图纸咯？"},
     {"style": "Speak", "talker": "object", "next": 3,
      "content": "基础的建筑，当然是有的，太复杂的我也需要学习。我师傅以前说过，做这行就要活到老，学到老。"},
     {"style": "Speak", "talker": "subject", 
      "content": "打扰了，其实我没有什么房子要盖的。"},
     {"style": "Speak", "talker": "object", 
      "content": "没事，我一个人住这也挺无聊的，有人来看我，我还真是挺高兴的。" + 
                 "我这有一份民居的图纸就送给你了，说不定你以后有建造的机会。"},
     #20
     {"style": "Script",  
      "type": "Action.PersonLearnRecipeAction", 
      "subject": "{PERSON_PLAYER}", "recipe": "{RECIPE_HOUSE_SMALL}"},
     {"style": "Branch", "branches": [22, 34]},
     {"style": "Speak", "talker": "subject", 
      "content": "多谢老哥，不过我觉得你有点儿孤独。"},
     {"style": "Speak", "talker": "object", 
      "content": "唔……我有我的木工箱陪着我，实在无聊了我就会想，怎么样才能用它建造出更新奇的建筑来。"},
     {"style": "Speak", "talker": "subject", 
      "content": "新奇的建筑？"},
     #25
     {"style": "Speak", "talker": "object", 
      "content": "就是形状不一样的，比如北辰派的两座书阁，中间那些复道就是修缮的时候我给加上的。" + 
                 "我还想过把房子做成三角形的、星型的、网状的，可是都没有机会实现。"},
     {"style": "Branch", "branches": [27, 32]},
     {"style": "Speak", "talker": "subject", 
      "content": "要不老哥你跟着我一起闯荡吧，保证让你实现人生理想。"},
     {"style": "Speak", "talker": "object", 
      "content": "闯江湖么？可我除了营造，什么都不懂，恐怕要拖累你了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "没事的，我们武功高强，不怕拖累。"},
     #30
     {"style": "Speak", "talker": "object", 
      "content": "那……那好，我跟你们走！"},
     {"style": "Script", "next": 999, 
      "type": "Action.TeamIncludePersonAction", 
      "person": "{PERSON_YE_ZHONG}", "leader": "{PERSON_PLAYER}"},
     {"style": "Speak", "talker": "subject", 
      "content": "加油，你要是成功了，现代派建筑就提前几百年诞生了。"},
     {"style": "Speak", "talker": "object", "next": 999,
      "content": "多谢，我会努力的。"},
     {"style": "Speak", "talker": "subject", 
      "content": "多谢老哥，那我先告辞了。"}]
      
      
DIALOG_SONGGONGZI_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "这戏动不动就讲范蠡那边的事情，可我只想看西施。"},
     {"style": "Speak", "talker": "subject", 
      "content": "演西施的姑娘叫什么名字啊？"},
     {"style": "Speak", "talker": "object", 
      "content": "你连梁子伶的大名都不知道，这可是江南赫赫有名的旦角。"},
     {"style": "Speak", "talker": "subject", 
      "content": "我平时可不怎么看戏。"},
     {"style": "Speak", "talker": "object", 
      "content": "那你可真得看一看，尤其是她演的玉簪记，那个美呀……比现在这个戏要好。"},
     {"style": "Speak", "talker": "subject", 
      "content": "这个记那个记我分不清，你直接告诉我它好在哪吧。"},
     {"style": "Speak", "talker": "object", 
      "content": "玉簪记里子伶的戏份比较多，我可以看她一整天。"},
     {"style": "Speak", "talker": "subject", 
      "content": "今天的戏，我看你还不是看了一整天。"},
     {"style": "Speak", "talker": "object", 
      "content": "嗯，戏份比较少的话，我也可以等她一整天。"},
     {"style": "Speak", "talker": "subject", 
      "content": "好吧，你不嫌累就行。"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_SONG_GONGZI_SUZHOU}", "conversation": "DIALOG_SONGGONGZI_2"}]
      
      
DIALOG_SONGGONGZI_2 = \
    [{"style": "Speak", "talker": "object", 
      "content": "（哼唱）月明云淡露华浓，欹枕愁听四壁蛩……"}]
      
      
DIALOG_LISHAOGONG_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "客官要不要乘船去寒山寺游览啊？"},
     {"style": "Speak", "talker": "subject", 
      "content": "寒山寺有什么值得一看之处？"},
     {"style": "Speak", "talker": "object", 
      "content": "说实话，好像没有的。"},
     {"style": "Speak", "talker": "subject", 
      "content": "那我还去干嘛？"},
     {"style": "Speak", "talker": "object", 
      "content": "去进个香也是好的呀。客官有没有什么牵挂的人，可以求佛祖保佑保佑他们。"},
     {"style": "Speak", "talker": "subject", 
      "content": "有倒是有，只是都不在这里。也不知道以后还见不见得到了。"},
     {"style": "Speak", "talker": "object", 
      "content": "如此这般，更应该去拜拜佛祖了。"},
     {"style": "Script", "interrupting": True,
      "type": "Order.TeamTransportOrder", 
      "leader": "{PERSON_PLAYER}", 
      "targets": [{"scenario": "{MAP_SUZHOUCHENG}", "location": "(2, 22)", "name": "寒山寺"}]},
     {"style": "Conditions", 
      "conditions": [{"type": "TeamPositionOnCondition", 
                      "team": "{TEAM_PERSON_PLAYER}", "scenario": "{MAP_SUZHOUCHENG}", "location": "(2, 22)"}],
      "result": {"true": 9, "false": 11}},
     {"style": "Script", 
      "type": "Action.TeamTransportAction", 
      "leader": "{PERSON_LI_SHAOGONG_SUZHOU}", 
      "scenario": "{MAP_SUZHOUCHENG}", "location": "(1, 22)"},
     {"style": "Script", "next": 999,
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_LI_SHAOGONG_SUZHOU}", "conversation": "DIALOG_LISHAOGONG_2"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_LI_SHAOGONG_SUZHOU}", "conversation": "DIALOG_LISHAOGONG_3"}]


DIALOG_LISHAOGONG_2 = \
    [{"style": "Speak", "talker": "object", 
      "content": "客官要回城里吗？"},
     {"style": "Script", "interrupting": True,
      "type": "Order.TeamTransportOrder", 
      "leader": "{PERSON_PLAYER}", 
      "targets": [{"scenario": "{MAP_SUZHOUCHENG}", "location": "(6, 21)", "name": "苏州城"}]},
     {"style": "Conditions", 
      "conditions": [{"type": "TeamPositionOnCondition", 
                      "team": "{TEAM_PERSON_PLAYER}", "scenario": "{MAP_SUZHOUCHENG}", "location": "(6, 21)"}],
      "result": {"true": 3, "false": 999}},
     {"style": "Script", 
      "type": "Action.TeamTransportAction", 
      "leader": "{PERSON_LI_SHAOGONG_SUZHOU}", 
      "scenario": "{MAP_SUZHOUCHENG}", "location": "(6, 22)"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_LI_SHAOGONG_SUZHOU}", "conversation": "DIALOG_LISHAOGONG_3"}]
      
      
DIALOG_LISHAOGONG_3 = \
    [{"style": "Speak", "talker": "object", 
      "content": "客官要去寒山寺吗？"},
     {"style": "Script", "interrupting": True,
      "type": "Order.TeamTransportOrder", 
      "leader": "{PERSON_PLAYER}", 
      "targets": [{"scenario": "{MAP_SUZHOUCHENG}", "location": "(2, 22)", "name": "寒山寺"}]},
     {"style": "Conditions", 
      "conditions": [{"type": "TeamPositionOnCondition", 
                      "team": "{TEAM_PERSON_PLAYER}", "scenario": "{MAP_SUZHOUCHENG}", "location": "(2, 22)"}],
      "result": {"true": 3, "false": 999}},
     {"style": "Script", 
      "type": "Action.TeamTransportAction", 
      "leader": "{PERSON_LI_SHAOGONG_SUZHOU}", 
      "scenario": "{MAP_SUZHOUCHENG}", "location": "(1, 22)"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_LI_SHAOGONG_SUZHOU}", "conversation": "DIALOG_LISHAOGONG_2"}]
 

DIALOG_ZHANGXIN_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "客官，新采摘的虎丘茶，要不要来点呢？除了芽茶，饼茶也是有的。"},
     {"style": "Speak", "talker": "subject", 
      "content": "芽茶和饼茶有什么区别？"},
     {"style": "Speak", "talker": "object", 
      "content": "客官看来不常吃茶。这芽茶呢，就是直接将茶树的嫩叶泡水。至于饼茶，乃是前人的吃法。" + 
                 "是把茶叶做成团饼，吃的时候碾成碎末，用沸水冲调食用。"},
     {"style": "Speak", "talker": "subject", 
      "content": "有意思，这饼茶我倒未曾吃过，就尝试一下吧。"},
     {"style": "Speak", "talker": "object", 
      "content": "好嘞，客官尝尝这福建龙团，我怕你吃不惯，少放了一些，就不收客官你银钱了。"},
     #5
     {"style": "Speak", "talker": "", 
      "content": "（茶博士拿出一个小纸包，里面是黑黢黢的茶团。茶博士磨下两勺碎末，便从锡壶里倒出开水，" + 
                 "用竹刷把茶叶沫调成糊状，直到整盅茶汤都变成绿色，才让顾客开饮。）"},
     {"style": "Speak", "talker": "subject", 
      "content": "这和东瀛的抹茶真像。"},
     {"style": "Speak", "talker": "object", 
      "content": "嗯？客官从东瀛倭国来？"},
     {"style": "Speak", "talker": "subject", 
      "content": "不是，听说他们也这么个吃法。"},
     {"style": "Speak", "talker": "object", 
      "content": "那就好……最近杭州那边又有了倭寇，连协防海事的风云盟都被损失惨重，不少人都谈倭色变。"},
     #10
     {"style": "Branch", "branches": [11, 19]},
     {"style": "Speak", "talker": "subject", 
      "content": "能否详细讲一讲倭寇的事情？"},
     {"style": "Speak", "talker": "object", 
      "content": ["这倭寇在沿海作乱，其实已有百年之久。后来戚继光、俞大猷两位总兵前来荡寇，海事便清平了一阵子。",
                  "可自打前年开始，又有日本船频繁骚扰海上，渔民们苦不堪言。而这风云盟呐，原本就是戚总兵旧部结成的帮会，所以自告奋勇来协助官兵抗倭。",
                  "年初时候，风云盟在舟山海上跟倭寇打了一场大仗，原本风云盟占据上风，谁知道对面突然加入几艘艨艟快艇，船上还有不少西洋枪炮。",
                  "这一下风云盟措手不及，被毁坏了许多船只，只好退回杭州，整顿不出了。"]},
     {"style": "Script", "next": 10,
      "type": "Action.PersonConversationAddBranchAction", 
      "conversation": "DIALOG_ZHANGXIN_1", "master": 10, "branch": 14, "position": 1}, 
     {"style": "Speak", "talker": "subject", 
      "content": "西洋枪炮……这么说来，倭寇与洋人还勾结起来了？"},
     #15
     {"style": "Speak", "talker": "object", 
      "content": ["也难说呢。南洋一带确实有很多红毛番子活动，不过也有不少汉人也跑去做海盗。",
                  "这些人从红毛那儿买了不少武器，风云盟早就怀疑他们和倭寇勾结，可是又找不到证据。",
                  "风云盟这回吃了亏，帮主归海平气得四处找人调查那几艘快艇的底细，到时候咱们就等着看是谁在后面捣鬼吧。",
                  "你说是红毛番子也就罢了，要是那伙海盗的话，又成了咱们自家人欺负自家人，真令人心寒哪！"]},
     {"style": "Script", "next": 10,
      "type": "Action.PersonConversationAddBranchAction", 
      "conversation": "DIALOG_ZHANGXIN_1", "master": 10, "branch": 17, "position": 2}, 
     {"style": "Speak", "talker": "subject", 
      "content": "那杭州城近日岂不是很危险？"},
     {"style": "Speak", "talker": "object", "next": 10,
      "content": ["嗐，城内依然是歌舞升平，只是不太敢出海罢了。不过容小弟说句老实话，这年头，哪个地方还没个山贼乱兵的？", 
                  "就说咱们这苏州城，现下外头不也有土匪吗？所以大家早就认命了，只要客官您不去提它，那我们这些小民还不是今朝有酒今朝醉呗！"]},
     {"style": "Speak", "talker": "subject", 
      "content": "既然如此，那就不提它了。"},
     #20
     {"style": "Speak", "talker": "object", 
      "content": ["嗯，客官吃茶。您要是觉得味道不错，可以买一些带在身上。", 
                  "假如路上疲惫了，又找不到地方投宿，就地泡一壶茶，还是可以暂时解乏的。"]},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_ZHANG_XIN}", "conversation": "DIALOG_ZHANGXIN_2"}]
      
      
DIALOG_ZHANGXIN_2 = \
    [{"style": "Speak", "talker": "object", 
      "content": "客官，买点茶叶吗？之前你吃的龙团也还有货。"}]
     
     
DIALOG_LUOGONGZI_1 = \
    [{"style": "Speak", "talker": "{PERSON_LUO_GONGZI_SUZHOU}", 
      "content": "最近苏州城外匪盗作乱，耿知府天天在南园招募豪杰说要剿匪，也没几个去投奔的。" +
                 "上次我路过那边，好像只有两个人在里头练武。"},
     {"style": "Speak", "talker": "{PERSON_ZHAO_JUREN_SUZHOU}", 
      "content": "匪盗这么猖獗，就光看见耿知府在应对，北辰派怎么不出面帮个忙？"},
     {"style": "Speak", "talker": "{PERSON_LUO_GONGZI_SUZHOU}", 
      "content": "你想真多！除非那帮土匪杀进苏州城，把北极阁给烧了，否则北辰派愿意管这种俗事？"},
     {"style": "Speak", "talker": "{PERSON_ZHAO_JUREN_SUZHOU}", 
      "content": "说到北辰派，最近似乎只见到他们家大徒弟，二徒弟跑哪去啦？"},
     {"style": "Speak", "talker": "{PERSON_LUO_GONGZI_SUZHOU}", 
      "content": "就那个喜欢寻花问柳的家伙？怕是成天待在天香楼里没出来吧。"},
     {"style": "Speak", "talker": "{PERSON_ZHAO_JUREN_SUZHOU}", 
      "content": "没这回事。我前几天去天香楼，萧姨妈还抱怨说好久没看见他呢！"},
     {"style": "Speak", "talker": "{PERSON_LUO_GONGZI_SUZHOU}", 
      "content": "什么？你背着我跑去天香楼啦！咱们不是说好了花酒要一起喝，姑娘要一起看吗？"},
     {"style": "Speak", "talker": "{PERSON_ZHAO_JUREN_SUZHOU}", 
      "content": "呃……"}]
     
      
DIALOG_WANGAJIAO_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "天香楼花魁同款胭脂水粉，先到先得。客官要不要来点？"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_WANG_AJIAO_SUZHOU}"}]
     
     
DIALOG_DENGMAFU_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "客官是要寄存物品，还是搭乘驿马？"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_WANG_AJIAO_SUZHOU}"}]
     
     
DIALOG_DINGTIEJIANG_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "兄弟，要打造些铁器不要？"},
     {"style": "Speak", "talker": "subject", 
      "content": "铁匠铺！一般这种地方都可以买到兵器和护甲对吧！"},
     {"style": "Speak", "talker": "object", 
      "content": "呃……兄弟，你问这些装备，是要参军还是收藏啊？"},
     {"style": "Speak", "talker": "subject", 
      "content": "都不是，我要用它们称霸江湖！"},
     {"style": "Speak", "talker": "object", 
      "content": "称、称霸江湖？你简直要笑煞我了，我看你连武器的品级都搞不清楚，还说什么称霸江湖？"},
     #5
     {"style": "Branch", "branches": [6, 16]},
     {"style": "Speak", "talker": "subject", 
      "content": "那你给我讲讲武器品级的知识呗。"},
     {"style": "Speak", "talker": "object", 
      "content": ["武器、包括所有的物品，都有四个品级，从低到高依次用白色、绿色、蓝色和紫色标识。",
                  "除此之外还有一些黄色标识的物品，表示世上仅此一件。不过黄色只能代表其珍贵程度，与品质是没有直接关系。",
                  "武器的品级可以通过锻造强化来进行提升，前提是这件武器有可以强化的部分。不同武器可强化的位置、需要的材料都不一样。",
                  "比如长剑可以强化的地方有剑柄和剑身两处，剑柄可以接受木质或石质材料，剑身则只能接受金铁材料。",
                  "而飞刀可以强化的地方则只有刀刃，且只能使用金铁材料。",
                  "不同的材料会给武器带来不同的提升，有的可以提高武器的威力，有的则可以附加效果。但是在强化中有两点需要注意。",
                  "第一，已经强化过的地方无法恢复原样，也无法再次进行强化；",
                  "第二，强化用的材料品级不能低于原件。",
                  "也就是说，绿色装备只能使用绿色或绿色以上的材料进行强化。不过黄色装备由于不在品级标准内，所以没有这一条限制。"]},
     {"style": "Script", "next": 5,
      "scripts": [{"type": "Action.PersonConversationAddBranchAction", 
                   "conversation": "DIALOG_DINGTIEJIANG_1", "master": 5, "branch": 9, "position": 1},
                  {"type": "Action.PersonConversationChangeContentAction", 
                   "conversation": "DIALOG_DINGTIEJIANG_1", "index": 16,
                   "content": "我搞清楚了，后续我要是称霸武林了，也有你的一份功劳！"}]},                
     {"style": "Speak", "talker": "subject", 
      "content": "强化武器用的材料我该去那找？"},
     #10
     {"style": "Speak", "talker": "object", 
      "content": ["木质材料可以在各种林地砍伐获得，石质材料和金铁材料则是在丘陵、山地挖掘。",
                  "另外有些装备可能还需要毛皮或者丝线，这就只能通过四处游猎，或者去商店购买了。",
                  "当你获得了这些材料，除了可以拿来强化旧装备之外，还能修理旧装备，或者打造新装备。"]},
     {"style": "Script", "next": 5,
      "scripts": [{"type": "Action.PersonConversationAddBranchAction", 
                   "conversation": "DIALOG_DINGTIEJIANG_1", "master": 5, "branch": 12, "position": 2}, 
                  {"type": "Action.PersonConversationAddBranchAction", 
                   "conversation": "DIALOG_DINGTIEJIANG_1", "master": 5, "branch": 14, "position": 3}]}, 
     {"style": "Speak", "talker": "subject", 
      "content": "给我讲讲修理装备的事吧。"},
     {"style": "Speak", "talker": "object", "next": 5,
      "content": ["武器与护甲在战斗中被人刀劈斧凿的，经常会伤痕累累，时间一久耐久度就会下降。",
                  "当一件武器或护甲的耐久度降到了0，那么它就会永远损坏。想要让一件装备长期可用，就不能不定期对其进行保养修护。",
                  "修理一件装备可以使用背包里的材料，也可以直接付钱进行修理。"]},
     {"style": "Speak", "talker": "subject", 
      "content": "给我讲讲打造装备的事吧。"},
     #15
     {"style": "Speak", "talker": "object", "next": 5,
      "content": ["除了直接购买武器，你也可以委托我为你打造趁手的装备。",
                  "不过打造的前提是，装备的配方要么你会，要么我会。另外，打造兵器的材料必须由你来出，我可是不管的。"]},
     {"style": "Speak", "talker": "subject", 
      "content": "我清楚得很，不用你管。"},
     {"style": "Speak", "talker": "object", 
      "content": "呵呵，那你看看这里有没有你要的东西。"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_DING_TIEJIANG_SUZHOU}"},
     {"style": "Script", 
      "type": "Action.PersonChangeConversationAction", 
      "person": "{PERSON_DING_TIEJIANG_SUZHOU}", "conversation": "DIALOG_DINGTIEJIANG_2"}]


DIALOG_DINGTIEJIANG_2 = \
    [{"style": "Speak", "talker": "object",
      "content": "小兄弟，看看这里有没有你要的东西！"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder",
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_DING_TIEJIANG_SUZHOU}"}]
     
     
DIALOG_XIAOYIMA_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": "这位大人，要不要来天香阁小坐一会？"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_WANG_AJIAO_SUZHOU}"}]
 

DIALOG_LIQINGXIA_1 = \
    [{"style": "Speak", "talker": "object", 
      "content": ["苏州城寸土寸金，即使是我们天香楼这种名流雅集之所，也只能占得临水的一二间小楼而已。",
                  "不过也正因为地方小，容不下那么多人，我才能和彩云姐姐交替坐班，一旬五休哦~"]},
     {"style": "Branch", "branches": [2, 12]},
     {"style": "Speak", "talker": "subject",
      "content": "看来普天之下就没有房价低的地方……"},
     {"style": "Speak", "talker": "object",
      "content": "唉，别的地方我不知道，但听说杭州城最近因为又有倭寇骚扰，有很多人抛售地皮，你有意愿的话，可以去碰碰运气"},
     # 10
     {"style": "Speak", "talker": "subject",
      "content": "话说……彩云姐姐是谁？"},
     {"style": "Speak", "talker": "object",
      "content": "彩云姐姐就是天香楼的花魁苏彩云呀。你作为一个男人，竟然没有听过她的名字？"},
     {"style": "Speak", "talker": "subject",
      "content": "那又怎么了？"},
     # 15
     {"style": "Speak", "talker": "object",
      "content": "那也是正常的。毕竟她年纪也不小了。而我李青霞，才是天香楼的未来。有朝一日，我也会名动江南。"},
     {"style": "Speak", "talker": "subject",
      "content": "……"}]
     
      
DIALOG_LIANGZIYOU_1 = \
    [{"style": "Speak", "talker": "",
      "content": "（戏台上一男一女正在唱戏，女子扮演的乃是越国美女西施，男子扮演的是吴王夫差。）"},
     {"style": "Speak", "talker": "{PERSON_LIANG_ZIYOU}",
      "content": "（唱）秋江岸边莲子多，采莲女儿棹船歌。花房莲实齐戢戢，争前兢折歌绿波。" + 
                 "恨逢长茎不得藕，断处丝多刺伤手。何时寻伴归去来？水远山长莫回首。"},
     {"style": "Speak", "talker": "{PERSON_WEI_GONGSHENG}",
      "content": "（白）绝妙！拿酒来，我饮一大觥！"},
     {"style": "Speak", "talker": "{PERSON_LIANG_ZIYOU}",
      "content": "（唱）采莲采莲芙蓉衣，秋风起浪凫雁飞。桂棹兰桡下极浦，罗裙玉腕轻摇橹。" + 
                 "叶屿花潭一望平，吴歌越吹相思苦。相思苦，不可攀。江南采莲今已暮，海上征夫犹未还。"},
     {"style": "Speak", "talker": "{PERSON_WEI_GONGSHENG}",
      "content": "（白）更妙更妙！我再饮一大觥！"},
     {"style": "Speak", "talker": "",
      "content": "……"},
     {"style": "Speak", "talker": "subject",
      "content": "这戏暂时先听到这里吧。"}]



DIALOG_WANGLAOHAN_1 = \
    [{"style": "Speak", "talker": "object",
      "content": ["北辰派的大少爷经常在楼顶练剑，总让老夫想起他们前任掌门商大侠的英姿。",
                  "有一年元宵节，商大侠在北寺塔下表演了一段『西河剑法』，大伙儿闻讯都前去围观，老夫当时就在人群的最前面。",
                  "商大侠使出最后一招『群帝骖龙翔』的时候，突然腾身而起，剑指五云。那身法真个如仙帝御龙，潇洒之极，老夫登时便惊为天人了。",
                  "唉，只可惜呀，商大侠他英年早逝……接班的两个小子虽然剑法也练得有模有样，但比起商大侠还是要略逊一筹。",
                  "但愿他们俩的武艺能早日进步，好让老夫有生之年能再次见到『西河剑法』的神采。"]}]
                  
                  
DIALOG_XUESIPENG_1 = \
    [{"style": "Speak", "talker": "object",
      "content": "你小子是耿朱桥派来对付爷的，还是吃饱了闲出鸟来找爷聊天的？"},
     {"style": "Speak", "talker": "subject",
      "content": "薛四彭，耿知府让我将你们一网打尽！"},
     {"style": "Speak", "talker": "object",
      "content": "耿朱桥不亲自出马，倒派些杂碎过来！爷就让你们死个痛快！"},
     {"style": "Speak", "talker": "subject",
      "content": "我就是来陪你聊聊天的。"},
     {"style": "Speak", "talker": "object",
      "content": "哈哈哈哈，陪爷聊天？你可知道爷是谁么？爷就是最近苏州人嘴里经常提到的大盗薛四彭！"},
     {"style": "Speak", "talker": "subject",
      "content": "那算了，我不聊了，告辞……"},
     {"style": "Speak", "talker": "object",
      "content": "妈的，你以为这是你家，你想来就来想走就走？你既然知道了爷干的营生，就老老实实把买路钱留下，否则就让你见识一下爷的手段！"},
     {"style": "Speak", "talker": "subject",
      "content": "唉，只好破财消灾了。"},
     {"style": "Speak", "talker": "object",
      "content": "哼，见识就见识。我凭本事来，也凭本事走"},
     {"style": "Speak", "talker": "subject",
      "content": "盗贼里也有侠义之士，我不会因为你是盗贼就心存偏见。"},
     {"style": "Speak", "talker": "object",
      "content": ["哈？爷在长江边上这么些年，还第一次听见有人这么说话。既然你如此坦诚，爷就不为难你了。",
                  "不过你可得记住，爷可不是什么侠义之士，爷就是个彻头彻尾的强徒，只是看这世道不惯，带了几个兄弟啸聚山林。",
                  "原本想的倒是干些劫富济贫，替天行道的举动，只可惜入了这行就身不由己了。管你们是贫是富，又与爷何干？",
                  "你回去告诉你的亲戚朋友，下次见了爷，可别自己撞上来！"]},
     {"style": "Speak", "talker": "subject",
      "content": "好，我回去就告诉他们。"},
     {"style": "Speak", "talker": "subject",
      "content": "劫富济贫、替天行道，如果有这等想法，大哥也算侠义之心未泯了。"},
     {"style": "Speak", "talker": "object",
      "content": "嗨，你这人废话真多！还不快滚！"}]
                  
                  
DIALOG_XUESIPENG_2 = \
    [{"style": "Speak", "talker": "object",
      "content": "又是你？你小子怎么还在这？"},
     {"style": "Speak", "talker": "subject",
      "content": "薛四彭，耿知府让我将你们一网打尽！"},
     {"style": "Speak", "talker": "object",
      "content": "好家伙，原来到头来还是耿朱桥一伙儿的！"},
     {"style": "Speak", "talker": "subject",
      "content": "薛大哥，耿朱桥最近招揽了不少武林中人想要围剿你。"},
     {"style": "Speak", "talker": "object",
      "content": "那又怎么了？"},
     {"style": "Speak", "talker": "subject",
      "content": "就我之前与薛大哥的一面之交，我觉得薛大哥并非奸恶之人，耿朱桥的做法未免太过草率，所以特地前来通知大哥。"},
     {"style": "Speak", "talker": "object",
      "content": "去他娘的，耿朱桥能招到什么人？苏州城只要他和陈挺之不亲自出马，那还有能打的吗？"},
     {"style": "Speak", "talker": "subject",
      "content": ["不管怎么样，薛大哥还是要小心为妙。以耿朱桥在江湖的名气，请到其他门派的高手并不是什么难事。",
                  "先不说远的，就这南京丐帮、杭州风云盟，只要把你说成无恶不作的恶匪，他们八成是要仗义驰援的。",
                  "况且，就算武林同道不来，耿朱桥也不会一直稳居府衙，避而不出。他现在不出手，无非是因为身居公职，不便以江湖规矩行事。",
                  "倘若后面苏州民众闹腾起来，非要他亲自剿匪，他一顺水推舟，可就没有顾虑了。等到彼时再应对，可就是后发制于人咯。"]},
     {"style": "Speak", "talker": "object",
      "content": "嗯，你说的也是！也罢！反正这苏州城老子也呆腻了，若是真逼得耿朱桥过来，我们恐怕也不是对手。不如咱兄弟几个另投他处好了？"},
     {"style": "Speak", "talker": "{PERSON_WANG_XIAOHU}",
      "content": "大哥，就咱们这绿林出身，什么地方敢收留咱啊？"},
     {"style": "Speak", "talker": "object",
      "content": "就去西北幽冥宫！"},
     {"style": "Speak", "talker": "{PERSON_WANG_XIAOHU}",
      "content": "好！听大哥的！"},
     {"style": "Speak", "talker": "object",
      "content": ["这位兄弟，虽然咱们素昧平生，但是你能不把我们兄弟当外人，也算是条汉子，薛某感激不尽。",
                  "薛某这些时日在此劫道，也攒了不少好物，除去前往西域的盘缠，其余都赠予兄弟了。后续要是有缘再见，我薛某人再好生报答！"]},
     {"style": "Speak", "talker": "subject",
      "content": "多谢，幽冥宫此去路途遥远，望薛大哥多加保重！"},
     {"style": "Speak", "talker": "subject",
      "content": "打扰了，我这就走……"}]
                  
                  
DIALOG_YUANWUYA_1 = \
    [{"style": "Speak", "talker": "object",
      "content": "小兄弟要不要买点书看？经史子集、百工技艺、武林秘籍我这里都有。"},
     {"style": "Speak", "talker": "subject",
      "content": "你是卖书的？为什么会在寺庙里兜售？"},
     {"style": "Speak", "talker": "object",
      "content": ["还不是因为生意不景气，破产了呗。以前房子的地契都被我给典当了，我还上哪卖书去啊？", 
                  "好在寒山寺住持看在我以前给庙里捐了不少佛经和香火钱，让我在这长期挂单，顺便清空一下存货。只是卖书的钱，不得不与寺庙平分了。"]},
     {"style": "Speak", "talker": "subject",
      "content": "那看看你都有什么书卖吧。"},
     {"style": "Speak", "talker": "object",
      "content": "这就对喽。你要是有空来多买几本书，让我把地契赎回来，说不准我还能东山再起呢！"},
     {"style": "Script", "interrupting": True,
      "type": "Order.PersonTradeOrder", 
      "subject": "{PERSON_PLAYER}", "object": "{PERSON_YUAN_WUYA}"}]
      
      
DIALOG_FENGMENGLONG_1 = \
    [{"style": "Speak", "talker": "object",
      "content": "这位兄台，我看你在戏台驻足观看良久，不知你觉得这本戏的编排得如何？"},
     {"style": "Branch", "branches": [2, 4]},
     {"style": "Speak", "talker": "subject",
      "content": "我不太懂戏，听不出什么妙处。"},
     {"style": "Speak", "talker": "object", "next": 20,
      "content": "唉，也罢也罢，知音难觅。不过冯某最近在搜罗新作的传奇戏文，兄台要是见着了，可以告知冯某一声。"},
     {"style": "Speak", "talker": "subject",
      "content": "我不太懂戏，但文词曲调确实令人耳目一新。"},
     #5
     {"style": "Speak", "talker": "object",
      "content": "耳目一新！好！好！这正是冯某重新订正过词曲的浣纱记，今日首次搬演，就碰上了兄台这样的妙耳。"},
     {"style": "Speak", "talker": "subject",
      "content": "（自言自语）我就是随便夸一下，怎么还跟我尬聊起来了……"},
     {"style": "Branch", "branches": [8, 11, 16]}, 
     {"style": "Speak", "talker": "subject",     
      "content": "浣纱记是什么？"},
     {"style": "Speak", "talker": "object",
      "content": "这浣纱记乃是苏州名士梁伯龙为了推广昆山腔所写的传奇，以范蠡、西施二人为线索，讲述整个吴越争霸的故事。"},  
     #10
     {"style": "Script", "next": 7,
      "type": "Action.PersonConversationAddBranchAction", 
      "conversation": "DIALOG_FENGMENGLONG_1", "master": 7, "branch": 14, "position": 1},                 
     {"style": "Speak", "talker": "subject",     
      "content": "先生为何要重新订正曲谱？"},
     {"style": "Speak", "talker": "object",
      "content": ["昆山腔成型较晚，可用来演唱的戏本不多，所以我只好将一些旧有的戏本加以修改，让它符合昆腔的格律。", 
                  "这浣纱记原本虽是按昆腔所作。只是我嫌它的旧谱还不够动听，所以班门弄斧，重订了一版。"]},
     {"style": "Script", "next": 7,
      "type": "Action.PersonConversationAddBranchAction", 
      "conversation": "DIALOG_FENGMENGLONG_1", "master": 7, "branch": 14, "position": 2}, 
     {"style": "Speak", "talker": "subject",     
      "content": "昆山腔又是什么？"},
     #15
     {"style": "Speak", "talker": "object", "next": 7,
      "content": ["天下声腔，不出弋阳、海盐、余姚、昆山四类。这其中的昆山腔原是苏州本地小调，经过魏良辅等人改良，变得悠扬婉转，甚是动听。",
                  "正因如此，它颇受文士青睐，渐渐有压倒其他三腔的势头。"]},       
     {"style": "Speak", "talker": "subject",
      "content": "真、真是了不起的工作呢……"},
     {"style": "Speak", "talker": "object",
      "content": ["兄台过奖了。其实这些旧戏文，虽然也有佳品，大部分还是俚俗之作。", 
                  "要是能有一部文辞雅致的传奇新作交由我来打谱，肯定能让这昆山腔争相传唱。不知兄台平日里是否能帮我留意一下此事？"]},
     {"style": "Speak", "talker": "subject",
      "content": "啊？要我帮忙？我恐怕也分不出他们是好是坏。"},
     {"style": "Speak", "talker": "object",
      "content": "哪里的话，冯某相信兄台的眼光。"},
     #20
     {"style": "Speak", "talker": "subject",
      "content": "好吧……"},
     {"style": "Speak", "talker": "object",
      "content": "冯梦龙在此谢过兄台了。"},
     {"style": "Conditions", 
      "conditions": [{"type": "ConversationSpokenCondition", "conversation": "DIALOG_FENGMENGLONG_1", "index": 4},],
      "result": {"false": 24}},
     {"style": "Script", 
      "type": "Action.PersonAttitudeChangeAction", 
      "subject": "{PERSON_FENG_MENGLONG}", "object": "{PERSON_PLAYER}", "delta": 5},
     {"style": "Script", 
     "type": "Action.PersonTaskUpdateAction", 
     "task": "TASK_SHUIMOXINQIANG", "contents": ["TASK_SHUIMOXINQIANG_1"]}]
