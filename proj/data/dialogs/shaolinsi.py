# -- coding: utf-8 --

DIALOG_SHAOLINLUNWU = \
    [{"style": "Speak", "talker": "subject", 
      "content": "奇怪，刚才比武，明明觉因方丈暂居上风，怎么突然就不打了？"},
     {"style": "Speak", "talker": "{PERSON_YUAN_LONG}", 
      "content": "这……小僧也有此疑惑……"},
     {"style": "Conditions", 
      "conditions": [{"type": "PersonInTeamCondition", "person": "{PERSON_LAN_ZIWEI}", "leader": "{PERSON_PLAYER}"}],
      "result": {"true": 3, "false": 7}},
     {"style": "Speak", "talker": "{PERSON_LAN_ZIWEI}", 
      "content": "他们表面上是在比武，实际上是在讨论佛理。觉因方丈使的是『摩诃无量掌』中的『如恒河沙』一式，" + 
                 "是想以此劝说班觉喇嘛，世间八万四千法门，如恒河沙一般数不胜数，何必执着于《那洛六法》。" + 
                 "而班觉喇嘛则用『菩提刀法』中的『万法一如』进行回应，意为法门虽多，但佛理都是如一的。" + 
                 "只要能致人通明，即是不二法门，所以觉因方丈也不必执着于禅修之法。" +
                 "二人所论，实为一事，他们都发觉了这一情况，所以就点到为止了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "原来如此。没想到兰姑娘还知晓佛法，而且能一眼辨认出各家武学。"},
     {"style": "Speak", "talker": "{PERSON_LAN_ZIWEI}", 
      "content": "白老师见笑了。家母在世之时笃好佛学，我自小耳濡目染，只能说略知一二。家母送我学医，也是出于慈悲心。" + 
                 "至于武学的甄别，其实是因为天下武艺施展方法不同，造成的损伤也不一样。想要对症医治，不得不有所涉猎。"},
     {"style": "Speak", "talker": "{PERSON_YUAN_LONG}", 
      "content": "兰姑娘一席指点，令小僧醍醐灌顶。看来以后小僧要多向兰姑娘请教佛法。"},
     {"style": "Speak", "talker": "{PERSON_SUONAN_RAODAN}", 
      "content": "他们表面上是在比武，实际上是在讨论佛理。觉因方丈使的是『摩诃无量掌』中的『如恒河沙』一式，" + 
                 "是想以此劝说班觉上师，世间八万四千法门，如恒河沙一般数不胜数，何必执着于《那洛六法》。" + 
                 "而班觉上师则用『菩提刀法』中的『万法一如』进行回应，意为法门虽多，但佛理都是如一的。" + 
                 "只要能致人通明，即是不二法门，所以觉因方丈也不必执着于禅修。" +
                 "二人所论，实为一事，他们都发觉了这一情况，所以就点到为止了。"},
     {"style": "Speak", "talker": "subject", 
      "content": "咦，小喇嘛你懂得还挺多嘛。"},
     {"style": "Speak", "talker": "{PERSON_SUONAN_RAODAN}", 
      "content": "我叫索南饶丹，不叫小喇嘛。话说回来，这次在少林寺总算见识倒了，中原武学真是博大精深。"},     
     {"style": "Speak", "talker": "{PERSON_SUONAN_RAODAN}", 
      "content": "哈哈哈，中原武学果然是博大精深，民间的佛学修为也同样令人佩服赞叹。"},
     {"style": "Speak", "talker": "subject", 
      "content": "嗯？小师傅你是……？"},
     {"style": "Speak", "talker": "{PERSON_SUONAN_RAODAN}", 
      "content": "我叫索南饶丹，是跟着班觉上师前来少林交流武学的僧人。"},
     {"style": "Speak", "talker": "{PERSON_SUONAN_RAODAN}", 
      "content": "看起来索南师傅对武学比佛法更有兴趣？"},
     {"style": "Speak", "talker": "{PERSON_SUONAN_RAODAN}", 
      "content": "没有强艺傍身如何弘法？护法除魔，可不是嘴上说说而已。" + 
                 "你们汉地承平百年，少林寺香火旺盛，所以才能专注于禅修之法。" + 
                 "而我所在的喜足尊胜州，诸部林立，乱象犹存，纵是转世活佛，也不能日夜安寝。" +
                 "故而班觉上师这次前来，就是希望能求得少林寺的上乘武功，回去助我教派渡过难关。"},
     {"style": "Speak", "talker": "{PERSON_YUAN_LONG}", 
      "content": "出家人不打诳语。敝寺的武功，从来无有外流之理，恐怕……"}]