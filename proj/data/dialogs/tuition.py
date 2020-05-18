# -- coding: utf-8 --

DIALOG_BATTLE_TUITION_1 = \
    [{"style": "Script", "breaking": True,
      "scripts": [{"type": "Action.ContextPlayerChangeAction", "person": "{PERSON_PLAYER_TUITION}"},
                  {"type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_RESET_PLAYER"},
                  {"type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_1"},
                  {"type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_FORBID_ATTACK"},
                  {"type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_FINISH"},
                  {"type": "Action.WorldAttackAction", 
                   "subject": "{TEAM_PERSON_PLAYER_TUITION}", "object": "{TEAM_PERSON_MURENZHUANG}",
                   "battle_map": "{MAP_TUITION_BTL}"}]}]


DIALOG_BATTLE_TUITION_2 = \
    [{"style": "Speak", "talker": "object",
      "content": ["比武切磋，均以回合为关节。一般来说，你只能在自己的回合内行动。",
                  "回合的顺序取决于人物的速度，速度越快，回合到来得也越快。",
                  "自己出手一回的时间里，敌人已经数番出手，这在实战中也不是什么罕见的情况。"]},
     {"style": "Speak", "talker": "object",
      "content": ["在一个回合内，你可以执行【移动】、【攻击】、【物品】与【休息】四种行动。",
                  "【移动】可以改变人物的位置。",
                  "【攻击】可以对目标使用招式，对其造成伤害或施加各类效果与状态。",
                  "【物品】可以从自己的背包中使用可使用的物品，效果视物品种类而定。",
                  "【休息】可以恢复一定的气血与内力，如果你休息之前进行了移动，则回复量会有所下降。",
                  "需要记住的是，移动必须在后三类指令之前执行；后三类指令一旦执行，正常情况下，你的回合便结束了。"]},
     {"style": "Speak", "talker": "object",
      "content": ["现在是你的回合，你可以尝试使用【移动】指令，移动到坐标(2, 2)的位置。"]},
     {"style": "Script", 
      "scripts": [{"type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_2"},
                  {"type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_MOVE_WRONG"}]}]


DIALOG_BATTLE_TUITION_2_1 = \
    [{"style": "Speak", "talker": "object",
      "content": "不对，你需要移动到坐标(2, 2)的位置。"}]
     

DIALOG_BATTLE_TUITION_3 = \
    [{"style": "Speak", "talker": "object",
      "content": ["很好，你已经知道了如何在战场上移动。",
                  "在真实的战场上，地形往往十分多变，有很多地方一时之间难以到达。所以行动前你必须要做好计算，确定合适的行进方案。",
                  "此外，当你接近敌方人物的身边时，移动力也会下降。想要暗度陈仓的话，也不是那么容易。"]},
     {"style": "Speak", "talker": "object",
      "content": ["现在你离敌人还有一段距离，这回合就先到此为止吧。请使用【休息】指令来结束回合。"]},
     {"style": "Script", "type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_3"}]


DIALOG_BATTLE_TUITION_4 = \
    [{"style": "Speak", "talker": "object",
      "content": "现在又轮到你行动了，请你再次使用移动指令，行进到木人桩的身边吧。"},
     {"style": "Script", "type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_4"}]


DIALOG_BATTLE_TUITION_5 = \
    [{"style": "Speak", "talker": "object",
      "content": ["敌人已经在你的攻击范围内了，你可以使用【攻击】指令来攻击木人桩。",
                  "使用【攻击】指令时，需要先选择使用的技能，然后选择你要攻击的坐标，最后进行确认。",
                  "现在请对木人桩进行攻击吧。"]},
     {"style": "Script", "type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_5"}]


DIALOG_BATTLE_TUITION_6 = \
    [{"style": "Speak", "talker": "object",
      "content": "看来你已经学会如何给敌人造成伤害了。"},
     {"style": "Speak", "talker": "subject",
      "content": "等等，我打它只掉一点血唉！怎么样才能造成更多伤害？"},
     {"style": "Speak", "talker": "object",
      "content": ["影响攻击伤害的因素那就太多了……人物特质、内力的阴阳相性、装备和技能自身的威力、以及攻击的位置都有影响。",
                  "前几项不是一朝一夕可以改变的，但这最后一项，少侠实战的时候可以稍加注意。",
                  "在人物的姓名后边有一个箭头标识，代表人物的朝向。你若从敌人的正后方或侧后方进行攻击，就会造成更多伤害。"]},
     {"style": "Speak", "talker": "object",
      "content": ["还有，你可能已经注意到了，在你的技能列表里，有几项剑法是无法使用的，因为你没有装备剑类武器。",
                  "这里有一把长剑，你待会可以使用【物品】指令，将其装备于自己身上。"]},
     {"style": "Script", 
      "type": "Action.PersonItemAcquireAction",
      "subject": "{PERSON_PLAYER_TUITION}", "item": "{ITEM_CHANGJIAN}", "quantity": 1},
     {"style": "Script", "type": "Action.EventSwitchOnAction", "event": "EVENT_BATTLE_TUITION_ATTACK_SCOPE"}]
                  
                  
DIALOG_BATTLE_TUITION_8 = \
    [{"style": "Speak", "talker": "object",
      "content": ["很好，你已经装备了长剑，下一回合便可以用它进行攻击了。但是在使用之前，你需要了解一下招式的攻击范围。",
                  "攻击范围得表达式为攻击形状加施展方式加作用半径，比如直线冲击3、大扇形横扫1。",
                  "其中的直线、大扇形指的是攻击形状，冲击、横扫指的施展类型，3和1表明其作用半径。"]},
     {"style": "Speak", "talker": "object",             
      "content": ["攻击形状分为【单体】、【直线】、【小扇形】、【大扇形】以及【周身】五种。",
                  "【单体】顾名思义，其攻击范围为一个地块。有一些单体攻击的武学带有溅射范围，在攻击地块周边的格子也会被纳入攻击范围。",
                  "【直线】是攻击一条直线上的单位，攻击方向是你所在格子与你选择的地块所连成的向量。",
                  "【小扇形】、【大扇形】与【周身】分别是六十度、一百二十度以及三百六十度范围攻击，攻击时你需要选择一个初始向量。", 
                  "真正的攻击范围则是从该向量起，顺时针旋转对应角度后覆盖的格子。"]},
     {"style": "Speak", "talker": "object",             
      "content": ["接下来说施展方式。施展方式主要影响存在障碍物情况下攻击范围的修正，共有【横扫】、【冲击】与【无视】三类。",
                  "【横扫】类型的技能，在扫过障碍物后，其作用半径会变小。",
                  "【冲击】类型的技能，仅仅无法击中障碍物正后方的地块。",
                  "【无视】类型的技能，障碍物对攻击范围没有任何影响。"]},
     {"style": "Speak", "talker": "object",             
      "content": ["最后说一下作用半径，它表示该技能最远能影响到的位置。比如直线3，则意味着在选定方向上，最多只能攻击到3格以外。"]},
     {"style": "Speak", "talker": "subject",
      "content": "停，这听上去太复杂了,我记不住啊。"},
     {"style": "Speak", "talker": "object",
      "content": ["没有关系，下一回合开始你可以自由行动，目标就是击倒对面的木人桩。",
                  "你可以利用这个机会把各类招式逐一试验，细细揣摩。"]}]
