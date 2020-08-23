# -- coding: utf-8 --

from proj.console.ui import common as ui


def effectname(obj, txt=None, grey=False):
    if txt is None:
        txt = obj.name
    styles = ["red", "green", "magenta"]
    return ui.colored(txt, color=styles[obj.style])


def rankcolor(rank):
    ranks = [None, "green", "cyan", "magenta", "yellow"]
    return ranks[rank]


def rank(obj, txt=None, grey=False):
    if txt is None:
        txt = obj.name
    ranks = [None, "green", "cyan", "magenta", "yellow"]
    return ui.colored(txt, color=ranks[obj.rank], attrs=["dark"] if grey else ["bold"])


def tag(t):
    tagmap = {"Wine": "酒", "Fur": "毛皮", "Wood": "木材", "Jade": "玉石", "Metal": "金属", "Punk": "朋克"}
    return tagmap[t]
    

def nodecond(nd):
    sexmap = ["男", "女", "？"]
    symbolmap = {"(": ">", "[": ">=", ")": "<", "]": "<="}
    condlist = []
    for req in nd.required:
        name = req["attrname"]
        lower, upper = req["range"][1:-1].split(",")
        if name == "sex":
            condlist.append("性别为%s" % sexmap[int(lower)])
        else:
            if lower == upper:
                condlist.append("%s = %s" % (name, lower))
            elif len(lower) == 0:
                condlist.append("%s %s %s" % (name, symbolmap[req["range"][-1]], upper))
            elif len(upper) == 0:
                condlist.append("%s %s %s" % (name, symbolmap[req["range"][0]], lower))
    if len(condlist) == 0:
        condstr = ""
    else:
        condstr = "（要求%s）" % "、".join(condlist)
    return condstr


def inner_skill(obj, p):
    ret = []
    isks = []
    sts_names = []
    for sk in p.skills_inner:
        if sk.belongs.tpl_id != obj.tpl_id:
            continue
        isks.append(sk)
    ret.append("运行时获得状态：%s")
    for sk in isks:
        for effe in sk.effects:
            if effe.name is None:
                continue
            sts_names.append(effectname(effe.exertion))
            ret.append(effect(effe.exertion))
    ret[0] = ret[0] % "、".join(sts_names)
    return ret


def _inner_skill(obj, p):
    ret = []
    isks = []
    for sk in p.skills_inner:
        if sk.belongs.tpl_id != obj.tpl_id:
            continue
        showstr = "%s：%s，" % (rank(sk), sk.description)
        sts_names = []
        for effe in sk.effects:
            sts_names.append(effectname(effe.exertion))
        showstr += "、".join(sts_names)
        ret.append(showstr)
    return ret


def effect(obj, grey=False):
    ret = None
    if obj.name is not None and len(obj.name) > 0:
        ret = "%s" % effectname(obj)
        if grey:
            ret += ui.colored("：", color="grey", attrs=["bold"])
        else:
            ret += "："
        if obj.turns is not None and obj.turns > 0:
            desc_str = obj.description + "，持续%s回合" % obj.turns
        else:
            desc_str = obj.description
        if grey:
            ret += ui.colored(desc_str, color="grey", attrs=["bold"])
        else:
            ret += desc_str
    return ret


def status(obj, grey=False):
    ret = None
    if obj.name is not None and len(obj.name) > 0:
        ret = "%s" % effectname(obj)
        if grey:
            ret += ui.colored("：", color="grey", attrs=["bold"])
        else:
            ret += "："
        comment = ""
        if obj.source is not None:
            #comment += "来源："
            if obj.exertor is not None:
                comment += obj.exertor.name
            if "Neigong" in obj.source.tags:
                #comment += rank(obj.source.belongs, txt="【%s】" % obj.source.belongs.name)
                comment += "【%s】" % obj.source.belongs.name
            else:    
                #comment += rank(obj.source, txt="【%s】" % obj.source.name)
                comment += "【%s】" % obj.source.name
        if obj.leftturn > 0:
            comment += "，剩余%s回合" % obj.leftturn
        if obj.description is None:
            description = ""
        else:
            description = obj.description
        description += "（%s）" % comment
        if grey:
            ret += ui.colored(description, color="grey", attrs=["bold"])
        else:
            ret += description
    return ret


def skill(obj, grey=False):
    style_map = {"Boji": "搏击", "Jianfa": "剑法",
                 "Daofa": "刀法", "Changbing": "长兵",
                 "Duanbing": "短柄", "Ruansuo": "软索",
                 "Anqi": "暗器", "Yueqi": "乐曲"}
    effe_str = []
    for effe in obj.effects:
        effe_str.append(effectname(effe))
    if len(effe_str) == 0:
        effe_str = "无"
    else:
        effe_str = "、".join(effe_str)
    yinyang_str = ui.colored(["阴性", "调和", "阳性"][obj.yinyang + 1], color=["cyan", None, "yellow"][obj.yinyang + 1])
    style_str = []
    for style in style_map.keys():
        if style in obj.style:
            style_str.append(style_map[style])
    style_str = "兼".join(style_str)
    normal_str = "威力：%s，耗气：%s，范围：%s%s，冷却：%s回合，特效：" % \
             (obj.power, obj.mp, obj.shape.showword, 
             {"Friends": "友方", "Enemies": "敌方", "All": "不分敌友", "Grids": ""}[obj.targets], obj.cd)
    if grey:
        normal_str = ui.colored(normal_str, color="grey", attrs=["bold"])
    return "，".join([style_str, yinyang_str, normal_str + effe_str])


def item(obj, grey=False):
    comments = ["『%s』" % obj.description]
    for inlay in obj.inlays:
        if "filled" in inlay:
            comments.append("『在%s处使用一枚%s进行了强化』" % (inlay["name"], rank(inlay["filled"])))        
    for effe in obj.effects:
        effestr = effect(effe, grey=grey) 
        if effestr is not None:
            comments.append("『%s』" % effestr)
    return comments
