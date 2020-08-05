# -- coding: utf-8 --

from proj.console import ui

from proj.runtime import context

from proj.entity import Skill


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


def profile(p):
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
    pf.append("  " + ui.fixed(18, n="搏击：%s" % p.boji) + ui.fixed(15, n="剑法：%s" % p.jianfa))
    pf.append("  " + ui.fixed(18, n="刀法：%s" % p.daofa) + ui.fixed(15, n="长兵：%s" % p.changbing))
    pf.append("  " + ui.fixed(18, n="暗器：%s" % p.anqi) + ui.fixed(15, n="奇门：%s" % p.qimen))
    pf.append("")
    pf.append("【战斗数据】")
    pf.append("")
    pf.append("  " + ui.fixed(18, n="攻击力：%s" % p.attack_base) + ui.fixed(15, n="防御力：%s" % p.defense_base))
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
            #print(sts.name)
            af.append("  " + ui.status(sts))
            sts_count += 1
    if sts_count == 0:
        af.append("  无")
    af.append("")
    af.extend(skills(p))
    af.append("")
    ui.pages([pf, af], title=ui.colored("%s %s%s" % (p.title, p.firstname, p.lastname), color="yellow", attrs=["bold"]), goback=True)


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


def skill_equipped(p):
    ret = []
    if p.studying is not None:
        ret.append("【当前修炼】%s：%s（进度：%s/%s）" % (ui.rank(p.studying.belongs), ui.rank(p.studying), 
                                                        p.exp, p.studying.exp))
    else:
        ret.append(ui.colored("【当前修炼】无", color="grey", attrs=["bold"]))
    ret.append("")
    if p.running is not None:
        ret.append("【运行心法】%s" % ui.rank(p.running))
        isk_str = ui.inner_skill(p.running, p)
        for isk in isk_str:
            ret.append("            %s" % isk)
    else:
        ret.append(ui.colored("【运行心法】无", color="grey", attrs=["bold"]))
    ret.append("")
    str_list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", ]
    asc_idx = 0
    for sk in p.skills_equipped:
        if sk is None:
            ret.append(ui.colored("【技能%s】无" % str_list[asc_idx], color="grey", attrs=["bold"]))
        else:
            comments = [ui.skill(sk)]
            for effe in sk.effects:
                comments.append(ui.effect(effe))
            ret.append("【技能%s】%s：%s" % (str_list[asc_idx], ui.rank(sk.belongs), ui.rank(sk)))
            for c in comments:
                ret.append("          %s" % c)
        asc_idx += 1
    ret.append("")
    if p.skill_counter is not None:
        ret.append("【辅助技能】%s：%s" % (ui.rank(p.skill_counter.belongs), ui.rank(p.skill_counter)))
        comments = [ui.skill(p.skill_counter)]
        for effe in p.skill_counter.effects:
            comments.append(ui.effect(effe))
        for c in comments:
            ret.append("            %s" % c)
    else:
        ret.append(ui.colored("【辅助技能】无", color="grey", attrs=["bold"]))
    return ret
        

def trade_menu(p, q):
    tmenu = [ui.menuitem("购买", goto=lambda x: PersonItemChooseOrder(subject=q, object=p, 
                                                                      candidates=p.team.members,
                                                                      persons=[q], order=PersonBuyOrder)),
             ui.menuitem("出售", goto=lambda x: PersonItemChooseOrder(subject=p, object=q, 
                                                                      persons=p.team.members, order=PersonSellOrder)),
             ui.menuitem("制作", goto=lambda x: PersonRecipeChooseOrder(subject=q, persons=p.team.members, 
                                                                        candidates=p.team.members + [q],
                                                                        filter=lambda a, rcp: len(rcp.tags & a.tags) > 0))]
    if "Equip" in q.tags:
        tmenu.append(ui.menuitem("修理", goto=lambda x: PersonItemChooseOrder(subject=p, object=q, quantity=1,
                                                                              persons=p.team.members, order=PersonEquipRepairRecipeOrder,
                                                                              orderarg={"persons": p.team.members},
                                                                              filter=lambda a, b, itm: "Equip" in itm.tags and \
                                                                                                       itm.durability_current != itm.durability)))
        tmenu.append(ui.menuitem("强化", goto=lambda x: PersonItemChooseOrder(subject=p, object=q, quantity=1, 
                                                                              persons=p.team.members, order=PersonEquipInlayChooseOrder,
                                                                              filter=lambda a, b, itm: "Equip" in itm.tags and \
                                                                                                       len(itm.inlays) > 0)))
    tmenu.append(ui.menuitem("离开"))
    return tmenu
 

def team_menu(p):
    ret = [ui.menuitem("状态", value=p, goto=lambda x: profile(x)),
           ui.menuitem("物品", value=p, 
                       goto=lambda x: PersonItemChooseOrder(subject=x, quantity=1, 
                                                            candidates=x.team.members, 
                                                            order=PersonItemOrder)),
           ui.menuitem("转移", value=p, 
                       goto=lambda x: PersonItemChooseOrder(subject=x, candidates=x.team.members, 
                                                            order=PersonItemTransferOrder)),
           ui.menuitem("技能", value=p, goto=lambda x: PersonSkillOrder(subject=x)),
           ui.menuitem("装备", value=p, goto=lambda x: PersonEquipmentOrder(subject=x)),
           ui.menuitem("配方", value=p, goto=lambda x: PersonRecipeChooseOrder(subject=x)),
           ui.menuitem("切磋"),
           ui.menuitem("离队", validator=lambda x: False)]
    return ret

 
def equip_menu(person):
    emenu = [ui.menuitem("主手卸下", goto=lambda x: PersonEquipOffOrder(subject=person, position=0)),
             ui.menuitem("主手装上", goto=lambda x: PersonItemChooseOrder(subject=person, persons=[person], object=person,
                                                                          quantity=1, order=PersonEquipOnOrder, orderarg={"position": 0},
                                                                          tags=set(["Weapon"]),
                                                                          backmethod=lambda: PersonEquipmentOrder(subject=self.subject, fromoff=True))),
             ui.menuitem("副手卸下", goto=lambda x: PersonEquipOffOrder(subject=person, position=1)),
             ui.menuitem("副手装上", goto=lambda x: PersonItemChooseOrder(subject=person, persons=[person], object=person,
                                                                          quantity=1, order=PersonEquipOnOrder, orderarg={"position": 1},
                                                                          tags=set(["Weapon"]),
                                                                          backmethod=lambda: PersonEquipmentOrder(subject=self.subject, fromoff=True))),
             ui.menuitem("身体卸下", goto=lambda x: PersonEquipOffOrder(subject=person, position=2)),
             ui.menuitem("身体装上", goto=lambda x: PersonItemChooseOrder(subject=person, persons=[person], object=person,
                                                                          quantity=1, order=PersonEquipOnOrder, orderarg={"position": 2},
                                                                          tags=set(["Armor"]),
                                                                          backmethod=lambda: PersonEquipmentOrder(subject=self.subject, fromoff=True))),
             ui.menuitem("饰品卸下", goto=lambda x: PersonEquipOffOrder(subject=person, position=3)),
             ui.menuitem("饰品装上", goto=lambda x: PersonItemChooseOrder(subject=person, persons=[person], object=person,
                                                                          quantity=1, order=PersonEquipOnOrder, orderarg={"position": 3},
                                                                          tags=set(["Ornament"]),
                                                                          backmethod=lambda: PersonEquipmentOrder(subject=self.subject, fromoff=True)))]
    return emenu


def skill_equip_menu(person):
    smenu = [ui.menuitem("技能一卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=0)),
             ui.menuitem("技能一装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=0)),
             ui.menuitem("技能二卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=1)),
             ui.menuitem("技能二装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=1)),
             ui.menuitem("技能三卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=2)),
             ui.menuitem("技能三装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=2)),
             ui.menuitem("技能四卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=3)),
             ui.menuitem("技能四装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=3)),
             ui.menuitem("技能五卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=4)),
             ui.menuitem("技能五装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=4)),
             ui.menuitem("技能六卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=5)),
             ui.menuitem("技能六装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=5)),
             #ui.menuitem("技能七卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=6)),
             #ui.menuitem("技能七装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=6)),
             #ui.menuitem("技能八卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=7)),
             #ui.menuitem("技能八装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=7)),
             #ui.menuitem("技能九卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=8)),
             #ui.menuitem("技能九装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=8)),
             ui.menuitem("运行心法卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=-1)),
             ui.menuitem("运行心法装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=-1)),
             ui.menuitem("辅助技能卸下", goto=lambda x: PersonSkillOffOrder(subject=person, position=-1)),
             ui.menuitem("辅助技能装备", goto=lambda x: PersonSkillOnOrder(subject=person, position=-1)),
             ui.menuitem("更换当前修炼", goto=lambda x: PersonSkillOnOrder(subject=person, position=-1)),]
    return smenu


def recipe_menu(subject, persons, recipes, filter=None, sub=False):
    str_list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", ]
    rmenu = []
    for idx, recipe in enumerate(recipes):
        if filter is not None and not filter(subject, recipe):
            continue
        enabled = recipe.check(persons)
        if len(recipe.materials) == 0:
            comments = ["无"]
        else:
            comments = ["，".join(["任意%s" % ui.tag(k) if isinstance(k, str) else ui.rank(k, grey=not enabled) + 
                                   ui.colored("×%s" % v, color=None if enabled else "grey", attrs=None if enabled else ["bold"]) \
                                   for k, v in recipe.materials])]
        showword = ("方案%s" % str_list[idx]) if sub else recipe.name
        if enabled:
            if subject not in persons:
                showword += "（费用：%s）" % ui.colored(str(25 + recipe.tmpdict.get("money", 0)), 
                                                        color="yellow", attrs=["bold"])
            rmenu.append(ui.menuitem(showword, value=recipe, comments=comments))
        else:
            rmenu.append(ui.menuitem(showword + "（材料不足）", value=recipe, comments=comments, \
                                     validator=lambda x: False))
    return rmenu
              

def item_menu(persons, obj, tags=None, showmoney=False, moneystyle=0, show_comments=True, filter=None):
    smenu = []
    for person in persons:
        for itm in person.items:
            show_state = 0
            if filter is not None:
                show_state = filter(person, obj, itm, tags)
            if show_state == 2:
                continue
            suffix_list = []
            if len(persons) > 1:
                suffix_list.append("持有人：%s" % ui.colored(person.name, attrs=["bold"]))
            if "Equip" in itm.tags:
                suffix_list.append("数量：1，耐久度：%s/%s" % (itm.durability_current, itm.durability))
            else:
                suffix_list.append("数量：%s" % person.quantities[itm.tpl_id])
            if showmoney and itm.tpl_id != "ITEM_MONEY":
                suffix_list.append("价值：%s" % ui.colored(itm.money if moneystyle == 0 else int(itm.money * 0.4), color="yellow", attrs=["bold"]))
            if itm in person.equipment:
                suffix_list.append(ui.colored("装备中", color="green"))
            suffix = "（%s）" % "，".join(suffix_list)
            if show_state == 1:
                mitem = ui.menuitem(ui.rank(itm) + ui.colored(suffix, color="grey", attrs=["bold"]), value=(itm, person), validator=lambda x: False)
            elif show_comments:
                comments = ui.item(itm)
                mitem = ui.menuitem(ui.rank(itm) + suffix, comments=comments, value=(itm, person))
            else:
                mitem = ui.menuitem(ui.rank(itm) + suffix, value=(itm, person))
            smenu.append(mitem)
    return smenu


def skill_menu(person):
    smenu = []
    for sk in person.skills:
        sk_str = "%s：%s" % (ui.rank(sk.belongs), ui.rank(sk))
        comments = [ui.skill(sk)]
        for effe in sk.effects:
            comments.append(ui.effect(effe))
        smenu.append(ui.menuitem(sk_str, comments=comments, value=sk))
    return smenu
    

def superskill_menu(superskill, person):
    ret = []
    for idx, nd in enumerate(superskill.nodes):
        learn_sts = superskill.learn_status(person, idx)
        enable = True
        if learn_sts == -1:
            nd_str = nd.name + ui.nodecond(nd)
            enable = False
        elif learn_sts == 0:
            nd_str = nd.name + "（已习得）"
            enable = False
        elif nd == person.studying:
            nd_str = nd.name + "（修炼中）"
            enable = False
        else:
            nd_str = nd.name
        comments = [nd.description]
        grey = not enable
        for nt in nd.tags:
            if nt.startswith("SKILL_"):
                sk = Skill.one(nt)
                if "Neigong" not in sk.style:
                    comments.append(ui.skill(sk, grey=grey))
                    for effe in sk.effects:
                        comments.append(ui.effect(effe, grey=grey))
                else:
                    for effe in sk.effects:
                        comments.append(ui.effect(effe.exertion, grey=grey))
        if enable:
            ret.append(ui.menuitem(nd_str, value=nd, comments=comments))
        else:
            ret.append(ui.menuitem(nd_str, value=nd, comments=comments, validator=lambda x: False))
    return ret
    

def handler_person_speak(ctx):
    if not ui.blankline():
        ui.echo()
    if ctx.content is None:
        ui.read("（回车继续）")
        ui.echo()
        return
    if isinstance(ctx.content, list):
        contents = ctx.content
    else:
        contents = [ctx.content]
    for idx, content in enumerate(contents):
        content = content.format(**context.strdict)
        if ctx.talker is None:
            ui.words(content)
        else:
            #print(ctx.talker, content)
            #prefix_str = (ctx.talker.name + "：") if idx == 0 else " "
            prefix_str = ctx.talker.name + "："
            #prefix = ui.fixed(ui.strwidth(prefix_str), n=(prefix_str if idx == 0 else " "))
            prefix = ui.fixed(10, n=(prefix_str if idx == 0 else " "))
            ui.words("%s%s" % (prefix, content))
        ui.read()
        if idx == len(contents) - 1:
            ui.echo()
    
    
def handler_person_dialog_branch(ctx):
    menulist = []
    ui.echo("%s：" % ctx.subject.name)
    for b in ctx.branches:
        bold = ctx.name not in context.script_status or \
               b not in context.script_status[ctx.name]
        menulist.append(ui.menuitem(ctx.conversation[b]["content"], value=b, bold=bold))
    ret = ui.menu(menulist)
    ui.echo()
    return ret
    
    
def handler_person_item_choose(ctx):
    showname = "物品一览：%s队" if len(ctx.persons) > 1 else "物品一览：%s"
    if ctx.back:
        ui.popmenu()
    ret = ui.menu(item_menu(ctx.persons, ctx.object, tags=ctx.tags, filter=ctx.filter, 
                            showmoney=ctx.showmoney, moneystyle=ctx.moneystyle), 
                  title=ui.colored(showname % ctx.subject.name, color="yellow", attrs=["bold"]), 
                  goback=True, backmethod=ctx.backmethod)
    return ret


def handler_person_item_object(ctx):
    person_menu = []
    for c in ctx.candidates:
        person_menu.append(ui.menuitem(c.name, value=c))
    if len(person_menu) == 1:
        return person_menu[0].value
    else:
        ret = ui.menu(person_menu, title="你选择你要作用的人物：", goback=True)
        return ret


def handler_person_item_quantity(ctx): 
    ui.echo()
    qrange = ctx.qrange(ctx.subject, ctx.object, ctx.item)
    rt = ui.read("请输入你要%s的数目（%s~%s）：" % (ctx.action, qrange[0], qrange[1]), 
                 handler=lambda x: int(x) if x.isdigit() and ctx.filter(ctx.subject, ctx.object, ctx.item, int(x)) else None)
    return rt
    

def handler_person_item_transfer(ctx):
    if not ui.blankline():
        ui.echo()
    ui.echo("%s把%s×%s交给了%s" % (ctx.subject.name, ui.rank(ctx.item), ctx.quantity, ctx.object.name))
    ui.read()


def handler_person_item_acquire(ctx):
    if not ui.blankline():
        ui.echo()
    if ctx.item is not None:
        ui.echo("%s获得了%s×%s" % (ctx.subject.name, ui.rank(ctx.item), ctx.quantity))
    else:
        ui.echo("%s一无所获" % ctx.subject.name)
    ui.read()
    
    
def handler_person_item_equip(ctx):
    if not ui.blankline():
        ui.echo()
    ui.echo("%s装备了【%s】" % (ctx.subject.name, ui.rank(ctx.item)))
    ui.read()
    
    
def handler_person_item_lost(ctx):
    if not ui.blankline():
        ui.echo()
    ui.echo("%s失去了%s×%s" % (ctx.subject.name, ui.rank(ctx.item), ctx.quantity))
    ui.read()


def handler_person_recipe_choose(ctx):
    if ctx.title is None:
        showname = ui.colored("配方一览：%s" % "、".join([p.name for p in ctx.candidates]), color="yellow", attrs=["bold"])
    else:
        showname = ctx.title
    if ctx.recipes is not None:
        recipes = ctx.recipes
    else:
        recipes = []
        for p in ctx.candidates:
            recipes.extend(p.recipes)
    ret = ui.menu(recipe_menu(ctx.subject, persons=ctx.persons, recipes=recipes, sub=ctx.sub, filter=ctx.filter), title=showname, goback=True)
    return ret
    
    
def handler_person_recipe_ensure(ctx):
    showname = "当前配方含有可选材料，请选择本次使用的材料："
    ret = ui.menu(recipe_menu(ctx.subject, persons=ctx.persons, recipes=ctx.recipes, sub=True), title=showname, goback=True)
    return ret
    
    
def handler_person_recipe_learn(ctx):
    ui.warn("%s习得了配方：%s" % (ctx.subject.name, ctx.recipe.name))
    ui.read()


def handler_person_study_skill(ctx):
    ui.echo()
    ui.superskill(ctx.superskill, ctx.subject)
    ui.echo()
    ret = ui.menu(superskill_menu(ctx.superskill, ctx.subject), 
                  title="请选择你要学习的节点：", goback=True, backmethod=ctx.backmethod)
    return ret
    
    
def handler_person_trade(ctx):
    ui.echo("%s：" % ctx.subject.name)
    ui.menu(trade_menu(ctx.subject, ctx.object), columns=2, width=15)
    
    
def handler_person_equipment(ctx):
    panel = ["",
             ui.colored("装备一览：%s" % ctx.subject.name, color="yellow", attrs=["bold"]),
             ""]
    panel.extend(equipment(ctx.subject))
    if ctx.fromoff:
        ui.popmenu()
    elif ctx.fromon:
        ui.popmenu()
        ui.popmenu()
    ui.menu(equip_menu(ctx.subject), title="请选择你要进行的操作：", 
            uppanel=panel, goback=True, columns=2, width=19)


def handler_person_equip_inlay_choose(ctx):
    imenu = []
    for idx, inlay in enumerate(ctx.item.inlays):
        enabled = "filled" not in inlay
        if enabled:
            name_str = inlay["name"]
            comments = ["接受材料：%s" % "、".join([ui.tag(acp) for acp in inlay["accept"]])]
            validator = lambda x: True
        else:
            name_str = inlay["name"]
            comments = ["已强化：%s" % ui.rank(inlay["filled"])]
            comments.extend([ui.effect(effe, grey=True) for effe in inlay["filled"].effects])
            validator = lambda x: False
        imenu.append(ui.menuitem(name_str, value=idx, comments=comments, validator=validator,
                                 goto=lambda x: PersonItemChooseOrder(subject=ctx.subject, object=ctx.object, quantity=1,
                                                                      persons=ctx.subject.team.members, order=PersonEquipStrengthenOrder,
                                                                      orderarg={"equip": ctx.item, "position": x},
                                                                      filter=lambda a, b, itm: len(itm.tags & ctx.item.inlays[x]["accept"]) != 0)))
    ret = ui.menu(imenu, title="请选择你要强化的部位：", goback=True)
    return ret


def handler_person_skill(ctx):
    panel=["",
           ui.colored("技能一览：%s" % ctx.subject.name, color="yellow", attrs=["bold"]),
           ""]
    panel.extend(skill_equipped(ctx.subject))
    if ctx.fromoff:
        ui.popmenu()
    elif ctx.fromon:
        ui.popmenu()
        ui.popmenu()
    ui.menu(skill_equip_menu(ctx.subject), title="请选择你要进行的操作：", 
            uppanel=panel, goback=True, pagesize=8, columns=2, width=23)


def handler_person_skill_choose(ctx):
    ret = ui.menu(skill_menu(ctx.subject), title="请选择你要装备的技能：", goback=True)
    return ret
    
    
def handler_person_task_update(ctx):
    ui.warn("奇怪的事件增加了！（事件『%s』有更新）" % ctx.task)
    ui.echo()
    
    
def handler_person_attitude_change(ctx):
    ui.warn("%s对你的好感度%s了！" % (ctx.subject.name, "提升" if ctx.delta > 0 else "下降"))
    ui.read()
    
    
def handler_person_join_team(ctx):
    ui.warn("%s加入了%s队。" % (ctx.subject.name, ctx.leader.name))
    ui.echo()
    
def handler_person_equip_repair(ctx):
    ui.echo("%s耐久度已恢复！" % ui.rank(ctx.item))
    ui.echo()
    
def handler_person_exp_gain(ctx):
    ui.echo("%s获得了%s点经验。" % (ctx.subject.name, ctx.exp))
    ui.read()
    
def handler_person_skill_learn(ctx):
    ui.echo("%s已经习得了技能%s：%s，请给%s安排新的修炼内容。" % (ctx.subject.name, ui.rank(ctx.node.belongs), ui.rank(ctx.node)))
    ui.read()
