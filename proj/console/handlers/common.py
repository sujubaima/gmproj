# -- coding: utf-8 --

from proj.console import ui

from proj.runtime import context


def digitcolor(digit):
    #if digit == 0:
    #    return None
    #if digit > 0:
    #    return "green"
    #if digit < 0:
    #    return "red"
    return None


def attrsts(p, attrname):
    delta_base = attrname + "_"
    ratio_base = delta_base + "factor_"
    delta_stash = "delta_" + delta_base
    ratio_stash = "ratio_" + ratio_base
    d_x = p.stash.get(delta_stash, 0)
    r_x = p.stash.get(ratio_stash, 1)
    d_c = getattr(p, delta_base)
    r_c = getattr(p, ratio_base)
    attrd = d_c * r_c - (d_c - d_x) * (r_c / r_x)
    if attrd == 0:
        return 0
    else:
        return int(attrd / abs(attrd))


def attrcolor(p, attrname):
    colormap = [None, "green", "red"]
    return colormap[attrsts(p, attrname)]


def person_status(ctrl):
    p = ctrl.person
    pf = []
    pf.append("【基本情况】")
    pf.append("")
    pf.append("  " + ui.fixed(18, n="气血：%s/%s" % (p.hp, p.hp_limit)))
    pf.append("  " + ui.fixed(18, n="内力：%s/%s" % (p.mp, p.mp_limit)))
    pf.append("")
    pf.append("  " + ui.fixed(18, n="外伤：" + ui.colored(str(p.injury), color=None if p.injury == 0 else "red")) + \
                     ui.fixed(18, n="内伤：" + ui.colored(str(p.wound), color=None if p.wound == 0 else "red")))
    pf.append("  " + ui.fixed(18, n="风毒：%s" % p.poison_hp) + \
                     ui.fixed(18, n="瘀毒：%s" % p.poison_mp))
    pf.append("  " + ui.fixed(18, n="饥饿：%s" % p.hunger) + \
                     ui.fixed(18, n="疲劳：%s" % p.fatigue))
    pf.append("")
    pf.append("")
    pf.append("【人物特质】")
    pf.append("")
    pf.append("  " + ui.fixed(18, n="灵动：" + ui.colored("%s%%" % (50 + p.dongjing), color=digitcolor(p.dongjing))) + \
                     ui.fixed(18, n="沉静：" + ui.colored("%s%%" % (50 - p.dongjing), color=digitcolor(-1 * p.dongjing))))
    pf.append("  " + ui.fixed(18, n="刚猛：" + ui.colored("%s%%" % (50 + p.gangrou), color=digitcolor(p.gangrou))) + \
                     ui.fixed(18, n="柔易：" + ui.colored("%s%%" % (50 - p.gangrou), color=digitcolor(-1 * p.gangrou))))
    pf.append("  " + ui.fixed(18, n="颖悟：" + ui.colored("%s%%" % (50 + p.zhipu), color=digitcolor(p.zhipu))) + \
                     ui.fixed(18, n="朴拙：" + ui.colored("%s%%" % (50 - p.zhipu), color=digitcolor(-1 * p.zhipu))))
    pf.append("")
    pf.append("  " + ui.fixed(18, n="内功阴性：" + ui.colored("%s%%" % (50 - p.yinyang), color="cyan")) + \
                     ui.fixed(18, n="内功阳性：" + ui.colored("%s%%" % (50 + p.yinyang), color="yellow")))
    pf.append("")
    pf.append("【武学能力】")
    pf.append("")
    pf.append("  " + ui.fixed(18, n="内功：%s" % p.neigong))
    pf.append("")
    pf.append("  " + ui.fixed(18, n="内功：%s" % p.neigong))
    pf.append("  " + ui.fixed(18, n="搏击：%s" % p.boji) + ui.fixed(15, n="剑法：%s" % p.jianfa))
    pf.append("  " + ui.fixed(18, n="刀法：%s" % p.daofa) + ui.fixed(15, n="长兵：%s" % p.changbing))
    pf.append("  " + ui.fixed(18, n="暗器：%s" % p.anqi) + ui.fixed(15, n="奇门：%s" % p.qimen))
    pf.append("")
    pf.append("【战斗数据】")
    pf.append("")
    pf.append("  " + ui.fixed(18, n="攻击力：%s" % p.attack) + ui.fixed(15, n="防御力：%s" % p.defense))
    pf.append("  " + ui.fixed(18, n="移动力：%s" % p.motion) + ui.fixed(15, n="速度：%s" % p.speed))
    pf.append("  " + ui.fixed(18, n="时序值：%s" % p.process))
    pf.append("")
    pf.append("  " + ui.fixed(18, n="命中率：" + ui.colored("%s%%" % int(p.hit_rate * 100), color=attrcolor(p, "hit_rate"))) + \
                     ui.fixed(18, n="闪避率：" + ui.colored("%s%%" % int(p.dodge_rate * 100), color=attrcolor(p, "dodge_rate"))))
    pf.append("  " + ui.fixed(18, n="暴击率：" + ui.colored("%s%%" % int(p.critical_rate * 100), color=attrcolor(p, "critical_rate"))) + \
                     ui.fixed(18, n="暴伤率：" + ui.colored("%s%%" % int(p.critical_damage * 100), color=attrcolor(p, "critical_damage"))))
    pf.append("  " + ui.fixed(18, n="拆招率：" + ui.colored("%s%%" % int(p.anti_damage_rate * 100), color=attrcolor(p, "anti_damage_rate"))) + \
                     ui.fixed(18, n="减伤率：" + ui.colored("%s%%" % int((1 - p.anti_damage) * 100), color=attrcolor(p, "anti_damage"))))
    pf.append("  " + ui.fixed(18, n="反击率：" + ui.colored("%s%%" % int(p.counter_rate * 100), color=attrcolor(p, "counter_rate"))))
    pf.append("")

    af = []
    af.append("【当前装备】")
    af.append("")
    af.extend(equipment(p))
    af.append("")
    af.append("【当前状态】")
    af.append("")
    sts_count = 0
    for sts in p.status:
        if sts.name is not None:
            af.append("  " + ui.status(sts))
            sts_count += 1
    if sts_count == 0:
        af.append("  无")
    af.append("")
    af.extend(skills(p))
    af.append("")
    ui.pages([pf, af], title=ui.byellow("%s %s%s" % (p.title, p.firstname, p.lastname)), 
           goback=True, backmethod=ctrl.close)


def team_info(ctrl):

    retlist = []

    map = ctrl.scenario

    for loc, entity in map.loc_entity.items():
        ret = {"location": None,
               "contents": ["", "", ""],
               "trace": [],
               "player": False}
        ret["location"] = map.entity_loc[entity.id]

        if len(entity.members) == 1:
            title = entity.leader.name
        else:
            title = "%s队" % entity.leader.name
        # 处理标题文本
        if entity.leader.player:
            ret["player"] = True
            ret["contents"][0] = ui.colored(title,
                                            color="grey",
                                            on_color="on_cyan")
        else:
            ret["contents"][0] = ui.colored(title,
                                            color="cyan",
                                            attrs=["bold"])
        if entity.battle is not None:
            ret["contents"][1] += ui.colored("（战斗中）", color="yellow", attrs=["bold"])

        # 处理路径
        if entity.last_move + context.duration() > context.timestamp and len(entity.path) > 1:
            ret["trace"].extend(entity.path)
        retlist.append(ret)
    last_timestamp = context.timestamp
    return retlist


def equipment(p):
    ret = []
    ret.append("  主手：" + \
                (ui.rank(p.equipment[0]) if p.equipment[0] is not None else "无") + \
                ("（双手持握）" if p.equipment[0] is not None and p.equipment[0].double_hand else ""))
    ret.append("  副手：" + \
               (ui.rank(p.equipment[1]) if p.equipment[1] is not None else "无") + \
               ("（双手持握）" if p.equipment[0] is not None and p.equipment[0].double_hand else ""))
    ret.append("  身体：" + (ui.rank(p.equipment[2]) if p.equipment[2] is not None else "无"))
    ret.append("  饰品：" + (ui.rank(p.equipment[4]) if p.equipment[4] is not None else "无"))
    return ret


def skills(p):
    ret = []
    ret.append("【运行心法】")
    ret.append("")
    if p.running is None:
        ret.append("  无")
    else:
        ret.append("  " + ui.rank(p.running))
        #for isk_str in ui.inner_skill(p.running, p):
        #    ret.append("  %s" % isk_str)
        isk_str = ui.inner_skill(p.running, p)[0]
        ret.append("  %s" % isk_str)
    ret.append("")
    ret.append("【使用武学】")
    ret.append("")
    #str_list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", ]
    for idx, sk in enumerate(p.skills):
        ret.append("  " + "%s：%s" % (ui.rank(sk.belongs), ui.rank(sk)))
        ret.append("  " + ui.skill(sk))
        for effe in sk.effects:
            ret.append("  " + ui.effect(effe))
    return ret


def item_menu(ctrl):
    smenu = []
    for itm, person, valid in ctrl.items:
        suffix_list = []
        if len(ctrl.persons) > 1:
            suffix_list.append("持有人：%s" % ui.colored(person.name, attrs=["bold"]))
        if "Equip" in itm.tags:
            suffix_list.append("数量：1，耐久度：%s/%s" % (itm.durability_current, itm.durability))
        else:
            suffix_list.append("数量：%s" % person.quantities[itm.tpl_id])
        if ctrl.showmoney and itm.tpl_id != "ITEM_MONEY":
            if ctrl.moneystyle == 0:
                money_num = itm.money
            else:
                money_num = int(itm.money * 0.4)
            suffix_list.append("价值：%s" % ui.byellow(money_num))
        if itm in person.equipment:
            suffix_list.append(ui.colored("装备中", color="green"))
        suffix = "（%s）" % "，".join(suffix_list)
        if not valid:
            mitem = ui.menuitem(ui.rank(itm) + ui.bgrey(suffix), value=(itm, person), validator=lambda x: False)
        else:
            comments = ui.item(itm)
            mitem = ui.menuitem(ui.rank(itm) + suffix, comments=comments, value=(itm, person), goto=ctrl.select)
        smenu.append(mitem)
    return smenu



def recipe_menu(ctrl):
    str_list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", ]
    rmenu = []
    for idx, ownerrecipe in enumerate(ctrl.recipes):
        owner, recipe = ownerrecipe
        enabled = recipe.check(ctrl.persons)
        if len(recipe.materials) == 0:
            comments = ["无"]
        else:
            comments = ["，".join(["任意%s" % ui.tag(k) if isinstance(k, str) else ui.rank(k, grey=not enabled) +
                                   ui.colored("×%s" % v, color=None if enabled else "grey", attrs=None if enabled else ["bold"]) \
                                   for k, v in recipe.materials])]
        showword = ("方案%s" % str_list[idx]) if ctrl.sub else recipe.name
        suffix = []
        if enabled:
            if not ctrl.sub:
                suffix.append("持有人：%s" % owner.name)
            if owner not in ctrl.persons:
                suffix.append("费用：%s" % ui.byellow(str(25 + recipe.tmpdict.get("money", 0))))
            if len(suffix) > 0:
                showword += "（%s）" %"，".join(suffix)
            mitem = ui.menuitem(showword, value=(owner, recipe), comments=comments, goto=ctrl.select)
        else:
            mitem = ui.menuitem(showword + "（材料不足）", comments=comments, validator=lambda x: False)
        rmenu.append(mitem)
    return rmenu


def skill_menu(ctrl):
    smenu = []
    if ctrl.type == 0:
        skills = ctrl.person.skills
    else:
        tmp = set()
        skills = []
        for skill_inner in ctrl.person.skills_inner:
            if skill_inner.belongs.tpl_id in tmp:
                continue
            skills.append(skill_inner.belongs)
            tmp.add(skill_inner.belongs.tpl_id)
    for sk in skills:
        sk_str = "%s：%s" % (ui.rank(sk.belongs), ui.rank(sk))
        comments = [ui.skill(sk)]
        for effe in sk.effects:
            comments.append(ui.effect(effe))
        smenu.append(ui.menuitem(sk_str, comments=comments, value=sk, goto=ctrl.select))
    return smenu



def handler_show(ctx):
    if not ui.blankline():
        ui.echo()
    if ctx.text is not None:
        ui.echo(ctx.text)
        ui.echo()
    if ctx.wait:
        ui.read("（回车继续）")


def handler_show_macros(ctrl):
    ui.echo()
    ui.echo("当前可用宏指令：")
    ui.echo()
    ui.echo(ui.fixed(20, n="#macros") + ctrl.macs_desc["#macros"])
    for mac in sorted(list(ctrl.macs_desc.keys())):
        if mac == "#macros":
            continue
        ui.echo(ui.fixed(20, n=mac) + ctrl.macs_desc[mac])
    ui.echo()
    ui.read("（回车继续）")
    ctrl.launch()


def handler_control_test(ctx):
    if not ui.blankline():
        ui.echo()
    if ctx.text is not None:
        ui.echo(ctx.text)
        ui.echo()
    if ctx.wait:
        ui.read("（回车继续）")
    #th = threading.Thread(target=ctx.control.hook, daemon=True)
    #th.start()
    ctx.hook()


def handler_branch_control(ctrl):
    menulist = []
    ui.echo("%s：" % ctrl.subject.name)
    for b in ctrl.branches:
        label_idx = ctrl.labels[b["label"]]
        if "content" in b:
            content = b["content"]
        elif "content" in ctrl.script[label_idx]:
            content = ctrl.script[label_idx]["content"]
        elif "scripts" in ctrl.script[label_idx] and "content" in ctrl.script[label_idx]["script"][0]:
            content = ctrl.script[label_idx]["script"][0]["content"]
        bold = ctrl.name not in context.script_status or \
               b["label"] not in context.script_status[ctrl.name]
        menulist.append(ui.menuitem(content, value=(b["label"], label_idx), bold=bold, goto=ctrl.select))
        #context.executed(ctrl.name, b["label"])
    ret = ui.menu(menulist)
    ui.echo()


def handler_session_branch_v2(ctx):
    menulist = []
    ui.echo("%s：" % ctx.subject.name)
    for b in ctx.branches:
        label_idx = ctx.labels[b["label"]]
        if "content" in b:
            content = b["content"]
        elif "Action.PersonSpeakAction" in ctx.script[label_idx]:
            content = ctx.script[label_idx]["Action.PersonSpeakAction"]["content"]
        elif "Block" in ctx.script[label_idx] and "Action.PersonSpeakAction" in ctx.script[label_idx]["Block"][0]:
            content = ctx.script[label_idx]["Block"][0]["Action.PersonSpeakAction"]["content"]
        menulist.append(ui.menuitem(content, value=label_idx))
    ret = ui.menu(menulist)
    ui.echo()
    return ret


def handler_session_branch(ctx):
    menulist = []
    ui.echo("%s：" % ctx.subject.name)
    for b in ctx.branches:
        label_idx = ctx.labels[b["label"]]
        if "content" in b:
            content = b["content"]
        elif "content" in ctx.script[label_idx]:
            content = ctx.script[label_idx]["content"]
        elif "scripts" in ctx.script[label_idx] and "content" in ctx.script[label_idx]["script"][0]:
            content = ctx.script[label_idx]["script"][0]["content"]
        bold = ctx.name not in context.script_status or \
               b["label"] not in context.script_status[ctx.name]
        menulist.append(ui.menuitem(content, value=label_idx, bold=bold))
    ret = ui.menu(menulist)
    ui.echo()
    return ret


def handler_halt(ctx):
    if not ui.blankline():
        ui.echo()
    ui.read()


def handler_popmenu(ctx):
    ui.popmenu()


def handler_backmenu(ctx):
    ui.echo()
    ui.backmenu()


def hander_action_finish(ctx):
    if not ui.blankline():
        ui.echo()
    ui.read("（回车继续）")


def handler_game_fail(ctx):
    if not ui.blankline():
        ui.echo()
    ui.warn("休命。")
    ui.read()
    sys.exit(0)


def handler_ensure_control(ctrl):
    ret = ui.sure(ui.byellow(ctrl.text))
    ctrl.input(ret)


def handler_person_select_control(ctrl):
    person_menu = []
    for c in ctrl.candidates:
        person_menu.append(ui.menuitem(c.name, value=c, goto=ctrl.select))
    if len(person_menu) == 1 and ctrl.canskip:
        ctrl.select(person_menu[0].value)
    else:
        ret = ui.menu(person_menu, title=ui.byellow(ctrl.title), goback=True, backmethod=ctrl.close)


def handler_person_select_multiple_control(ctrl):
    person_menu = []
    for c in ctrl.candidates:
        person_menu.append(ui.menuitem(c.name, value=c, goto=ctrl.select))
    if len(person_menu) == 1:
        ret = [person_menu[0].value]
    else:
        ret = ui.menu(person_menu, title=ui.byellow(ctrl.title), goback=True, backmethod=ctrl.close,
                      multiple=True, multiple_range=[1, ctrl.max_number])
    ctrl.select(ret)


def handler_item_select_control(ctrl):
    ui.menu(item_menu(ctrl), title=ui.byellow(ctrl.title), macros=ctrl.macs, 
            goback=True, backmethod=ctrl.close)


def handler_item_quantity_select_control(ctrl):
    if ctrl.range[0] == 1 and ctrl.range[1] == 1:
        ctrl.select(1)
        return
    if not ui.blankline():
        ui.echo()
    rt = ui.read("%s（%s~%s）：" % (ctrl.text, ctrl.range[0], ctrl.range[1]),
                 handler=lambda x: int(x) if ctrl.validator(x) else None)
    ctrl.select(rt)


def handler_recipe_select_control(ctrl):
    ui.menu(recipe_menu(ctrl), title=ui.byellow(ctrl.title), goback=True, backmethod=ctrl.close)


def handler_skill_select_control(ctrl):
    ui.menu(skill_menu(ctrl), title=ctrl.title, goback=True, backmethod=ctrl.close)


def handler_pos_select_control(ctrl):
    map = ctrl.scenario
    ui.echo()
    ui.map(map, entities=team_info(ctrl),
           coordinates=[{"positions": ctrl.positions},
                        {"positions": context.guide, "color": "yellow"}], show_trace=False)
    ui.echo()
    rt = ui.read("%s（绿色表示可移动格子，坐标用空格分隔，输入#back可返回）：" % ctrl.text,
                 handler=ctrl.validator)
    ui.echo()
    if ctrl.ensure:
        surert = ui.sure(ctrl.ensure_text)
        if not surert:
            rt = None
    ctrl.select(rt)


def handler_person_status_control(ctrl):
    person_status(ctrl)
