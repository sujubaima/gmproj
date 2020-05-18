# -- coding: utf-8 --

# 万鹏飞
PERSON_WAN_PENGFEI = \
    {"firstname": "万", "lastname": "鹏飞", "title": "无名小卒",
     "dongjing": 10, "gangrou": 7, "zhipu": 19,
     "neigong": 24, "boji": 31, "jianfa": 16, "daofa": 34, "changbing": 29, "anqi": 8, "qimen": 13, "yinyang": 24,
     "superskills": [{"id": "SUPERSKILL_BOYUNJIANRIDAO", "learn": [0]}],
     "equipment": [{"id": "ITEM_PODAO", "position": "MainHand"}],
     "items": [{"id": "ITEM_MONEY", "quantity": 72}],
     "criticaltxt": "这一刀不敢说后无来者，至少也是前无古人了。",
     "conversation": "DIALOG_WANPENGFEI_1"}

     
# 赵乞儿
PERSON_ZHAO_LING = \
    {"firstname": "赵", "lastname": "零", "showname": "赵乞儿", "title": "丐帮弟子",
     "dongjing": 20, "gangrou": 6, "zhipu": -18,
     "neigong": 20, "boji": 30, "jianfa": 2, "daofa": 5, "changbing": 32, "anqi": 12, "qimen": 18, "yinyang": 4,
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": [0, 1, 2]},
                     {"id": "SUPERSKILL_BOYUNJIANRIDAO", "learn": [0, 1]}],
     "items": [],
     "conversation": "DIALOG_ZHAOQIER_1"}

     
# 黄金颊
PERSON_HUANG_JINJIA = \
    {"firstname": "黄", "lastname": "金颊", "title": "无名小卒",
     "dongjing": 17, "gangrou": 27, "zhipu": 8,
     "neigong": 20, "boji": 49, "jianfa": 20, "daofa": 28, "changbing": 30, "anqi": 17, "qimen": 21, "yinyang": 35,
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": [0, 1, 2]},
                     {"id": "SUPERSKILL_BOYUNJIANRIDAO", "learn": [0, 1]}],
     "items": [],
     "criticaltxt": "人生何所为，当求无上道。",
     "conversation": "DIALOG_HUANGJINJIA_1"}


# 薛四彭
PERSON_XUE_SIPENG = \
    {"firstname": "薛", "lastname": "四彭", "title": "江湖宵小",
     "dongjing": 18, "gangrou": 8, "zhipu": -9,
     "neigong": 27, "boji": 31, "jianfa": 20, "daofa": 30, "changbing": 22, "anqi": 27, "qimen": 17, "yinyang": 3,
     "superskills": [{"id": "SUPERSKILL_JIANGHUXINFA", "learn": "All"},
                     {"id": "SUPERSKILL_TIESHAZHANG", "learn": "All"}],
     "equipment": [],
     "items": [],
     "criticaltxt": "苏州城里我最大！我！最！大！"}
     
     
# 邓老二
PERSON_DENG_LAOER = \
    {"firstname": "邓", "lastname": "老二", "title": "江湖宵小",
     "dongjing": 18, "gangrou": 8, "zhipu": -9,
     "neigong": 27, "boji": 31, "jianfa": 20, "daofa": 30, "changbing": 22, "anqi": 27, "qimen": 17, "yinyang": 3,
     "superskills": [{"id": "SUPERSKILL_LANLUDAOFA", "learn": "All"}],
     "equipment": [],
     "items": [],
     "criticaltxt": "此路是我开，此树是我栽。要想从此过，把钱交出来！"}
     
     
# 王小虎
PERSON_WANG_XIAOHU = \
    {"firstname": "王", "lastname": "小虎", "title": "江湖宵小",
     "dongjing": 18, "gangrou": 8, "zhipu": -9,
     "neigong": 27, "boji": 31, "jianfa": 20, "daofa": 30, "changbing": 22, "anqi": 27, "qimen": 17, "yinyang": 3,
     "superskills": [{"id": "SUPERSKILL_BAICHANSHOU", "learn": "All"}],
     "equipment": [],
     "items": [],
     "criticaltxt": "敢惹老子，命都不要了？"}
     
     
# 李不通
PERSON_LI_BUTONG = \
    {"firstname": "李", "lastname": "不通", "title": "江湖宵小",
     "dongjing": 18, "gangrou": 8, "zhipu": -9,
     "neigong": 27, "boji": 31, "jianfa": 20, "daofa": 30, "changbing": 22, "anqi": 27, "qimen": 17, "yinyang": 3,
     "superskills": [{"id": "SUPERSKILL_WULANGGUN", "learn": "All"}],
     "equipment": [],
     "items": [],
     "criticaltxt": "金盆洗手的前提是，你得有个金盆哪！"}   
     
     
# 赵衙役
PERSON_ZHAO_YAYI_SUZHOU = \
    {"firstname": "赵", "lastname": "衙役", "title": "普通百姓",
     "conversation": "DIALOG_ZHAOYAYI_1"}
  
  
# 丁铁匠
PERSON_DING_TIEJIANG_SUZHOU = \
    {"firstname": "丁", "lastname": "铁匠", "title": "普通百姓", "tags": "Businessman,Equip",
     "items": [{"id": "ITEM_MONEY", "quantity": 5000},
               {"id": "ITEM_PODAO", "quantity": 3},
               {"id": "ITEM_CHANGGUN", "quantity": 3},
               {"id": "ITEM_CHANGJIAN", "quantity": 3},
               {"id": "ITEM_CHANGJIAN,0-ITEM_YUNMU", "quantity": 1}],
     "recipes": [{"id": "RECIPE_PODAO"}],
     "conversation": "DIALOG_DINGTIEJIANG_1"}
    
    
# 王阿娇
PERSON_WANG_AJIAO_SUZHOU = \
    {"firstname": "王", "lastname": "阿娇", "sex": 1, "title": "普通百姓",
     "conversation": "DIALOG_WANGAJIAO_1"}
    
    
# 蔡婆子
PERSON_CAI_POZI_SUZHOU = \
    {"firstname": "蔡", "lastname": "婆子", "sex": 1, "title": "普通百姓"}
    
    
# 李大娘
PERSON_LI_DANIANG_SUZHOU = \
    {"firstname": "李", "lastname": "大娘", "sex": 1, "title": "普通百姓"}


# 张屠户
PERSON_ZHANG_TUHU_SUZHOU = \
    {"firstname": "张", "lastname": "屠户", "title": "普通百姓"}
    
    
# 孙小二
PERSON_SUN_XIAOER_SUZHOU = \
    {"firstname": "孙", "lastname": "小二", "title": "普通百姓"}
    
    
# 戴郎中
PERSON_DAI_LANGZHONG_SUZHOU = \
    {"firstname": "戴", "lastname": "郎中", "title": "普通百姓"}
    
    
# 马琴师
PERSON_MA_YUESHI_SUZHOU = \
    {"firstname": "马", "lastname": "琴师", "title": "普通百姓",
     "items": [{"id": "ITEM_MONEY", "quantity": 5000},
               {"id": "ITEM_HENGDI", "quantity": 10},
               {"id": "ITEM_DONGXIAO", "quantity": 10},
               {"id": "ITEM_PIPA", "quantity": 4},
               {"id": "ITEM_QIXIANQIN", "quantity": 2}],
     "conversation": "DIALOG_MAYUESHI_1"}
    
    
# 朱裁缝
PERSON_ZHU_CAIFENG_SUZHOU = \
    {"firstname": "朱", "lastname": "裁缝", "sex": 1, "title": "普通百姓"}
    
    
# 钱阿姐
PERSON_QIAN_AJIE_SUZHOU = \
    {"firstname": "钱", "lastname": "阿姐", "sex": 1, "title": "普通百姓"}
    
    
# 谢掌柜
PERSON_XIE_ZHANGGUI_SUZHOU = \
    {"firstname": "谢", "lastname": "掌柜", "title": "普通百姓"}
    
    
# 萧姨妈
PERSON_XIAO_YIMA_SUZHOU = \
    {"firstname": "萧", "lastname": "姨妈", "sex": 1, "title": "普通百姓",
     "conversation": "DIALOG_XIAOYIMA_1"}
    
    
# 苏花魁
PERSON_SU_HUAKUI_SUZHOU = \
    {"firstname": "苏", "lastname": "彩云", "sex": 1, "title": "普通百姓"}
    

# 周花魁
PERSON_ZHOU_HUAKUI_SUZHOU = \
    {"firstname": "周", "lastname": "青霞", "sex": 1, "title": "普通百姓",
     "conversation": "DIALOG_ZHOUHUAKUI_1"}

    
# 刘秀才
PERSON_LIU_XIUCAI_SUZHOU = \
    {"firstname": "刘", "lastname": "秀才", "title": "普通百姓"}
    
    
# 黄道士
PERSON_HUANG_DAOSHI_SUZHOU = \
    {"firstname": "黄", "lastname": "道士", "title": "普通百姓"}
    
    
# 梁子伶
PERSON_LIANG_ZIYOU = \
    {"firstname": "梁", "lastname": "子伶", "sex": 1, "title": "普通百姓",
     "conversation": "DIALOG_LIANGZIYOU_1"}
    
    
# 魏公生
PERSON_WEI_GONGSHENG = \
    {"firstname": "魏", "lastname": "公生", "title": "普通百姓",
     "conversation": "DIALOG_LIANGZIYOU_1"}
   
   
# 冯梦龙
PERSON_FENG_MENGLONG = \
    {"firstname": "冯", "lastname": "梦龙", "title": "普通百姓",
     "conversation": "DIALOG_FENGMENGLONG_1"}
    
    
# 袁无涯
PERSON_YUAN_WUYA = \
    {"firstname": "袁", "lastname": "无涯", "title": "普通百姓",
     "items": [{"id": "ITEM_WUYINGJIAO", "quantity": 1},
               {"id": "ITEM_FENJINXIGUDAO", "quantity": 1}],
     "conversation": "DIALOG_YUANWUYA_1"}
    
    
# 邓马夫
PERSON_DENG_MAFU_SUZHOU = \
    {"firstname": "邓", "lastname": "马夫", "title": "普通百姓",
     "conversation": "DIALOG_DENGMAFU_1"}
    
    
# 宋公子
PERSON_SONG_GONGZI_SUZHOU = \
    {"firstname": "宋", "lastname": "公子", "title": "纨绔子弟",
     "conversation": "DIALOG_SONGGONGZI_1"}
     
     
# 张新
PERSON_ZHANG_XIN = \
    {"firstname": "张", "lastname": "新", "title": "普通百姓",
     "conversation": "DIALOG_ZHANGXIN_1"}
     
     
# 罗公子
PERSON_LUO_GONGZI_SUZHOU = \
    {"firstname": "罗", "lastname": "公子", "title": "纨绔子弟",
     "conversation": "DIALOG_LUOGONGZI_1"}
     
     
# 赵举人
PERSON_ZHAO_JUREN_SUZHOU = \
    {"firstname": "赵", "lastname": "举人", "title": "普通百姓",
     "conversation": "DIALOG_LUOGONGZI_1"}
     
     
# 叶忠
PERSON_YE_ZHONG = \
    {"firstname": "叶", "lastname": "忠", "title": "营造匠人",
     "dongjing": -10, "gangrou": 30, "zhipu": -5, "yinyang": 14,
     "neigong": 9, "boji": 15, "jianfa": 1, "daofa": 4, "changbing": 7, "anqi": 1, "qimen": 11,
     "conversation": "DIALOG_YEZHONG_1"}
     
     
# 李艄公
PERSON_LI_SHAOGONG_SUZHOU = \
    {"firstname": "李", "lastname": "艄公", "title": "普通百姓",
     "conversation": "DIALOG_LISHAOGONG_1"}


# 王老汉
PERSON_WANG_LAOHAN_SUZHOU = \
    {"firstname": "王", "lastname": "老汉", "title": "普通百姓",
     "conversation": "DIALOG_WANGLAOHAN_1"}
    
    
# 诰墙
PERSON_GAO_QIANG_SUZHOU = \
    {"firstname": "", "lastname": "", "tags": "Unlive", "showname": "公告栏"}

