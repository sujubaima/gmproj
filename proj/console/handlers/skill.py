# -- coding: utf-8 --

from proj.console import ui

from proj.entity import Skill


def skill_equipped(ctrl):
    p = ctrl.person
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
    str_list = ["一", "二", "三", "四", "五", "六"]#, "七", "八", "九", ]
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


def skill_equip_menu(ctrl):
    str_list = ["一", "二", "三", "四", "五", "六"]#, "七", "八", "九"]
    smenu = []
    for idx, numstr in enumerate(str_list):
        smenu.append(ui.menuitem("技能%s%s" % (numstr, "卸下"), value=idx, goto=ctrl.skill_off))
        smenu.append(ui.menuitem("技能%s%s" % (numstr, "装备"), value=idx, goto=ctrl.skill_on))
    smenu.append(ui.menuitem("运行心法卸下", goto=ctrl.skill_unrun))
    smenu.append(ui.menuitem("运行心法装备", goto=ctrl.skill_run))
    smenu.append(ui.menuitem("辅助技能卸下", value=-1, goto=ctrl.skill_off))
    smenu.append(ui.menuitem("辅助技能装备", value=-1, goto=ctrl.skill_on))
    smenu.append(ui.menuitem("更换当前修炼", goto=ctrl.skill_study))
    return smenu


def superskill_menu(ctrl):
    superskill = ctrl.superskill
    person = ctrl.person
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
            ret.append(ui.menuitem(nd_str, value=nd, comments=comments, goto=ctrl.select))
        else:
            ret.append(ui.menuitem(nd_str, value=nd, comments=comments, validator=lambda x: False))
    return ret


def handler_skill_control(ctrl):
    panel=["",
           ui.byellow("技能一览：%s" % ctrl.person.name),
           ""]
    panel.extend(skill_equipped(ctrl))
    ui.menu(skill_equip_menu(ctrl), title="请选择你要进行的操作：",
            uppanel=panel, keylist=[chr(i) for i in range(ord('a'), ord('a') + 26)], 
            pagesize=26, columns=2, width=23, goback=True, backmethod=ctrl.close)


def handler_skill_node_select_control(ctrl):
    ui.echo()
    ui.superskill(ctrl.superskill, ctrl.person)
    ui.echo()
    ret = ui.menu(superskill_menu(ctrl),
                  title="请选择你要学习的节点：", goback=True, backmethod=ctrl.close)
