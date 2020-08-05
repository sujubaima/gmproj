# -- coding: utf-8 --

from proj.console import ui

from proj.entity import Item
from proj.entity import Skill

def handler_superskill_select_control(ctrl):
    skmenu = []
    for sk in ctrl.superskills:
        comments = [Item.one("ITEM_%s" % sk.tpl_id[11:]).description]
        skmenu.append(ui.menuitem(ui.rank(sk), value=sk, comments=comments, goto=ctrl.select))
    skmenu.append(ui.menuitem("离开", goto=ctrl.close))
    ui.menu(skmenu, title=ctrl.title)
    

def handler_superskill_control(ctrl):
    if not ui.blankline():
        ui.echo()
    ui.superskill(ctrl.superskill)
    ui.echo()
    for idx, nd in enumerate(ctrl.superskill.nodes):
        comments = [nd.description]
        for nt in nd.tags:
            if nt.startswith("SKILL_"):
                sk = Skill.one(nt)
                if "Neigong" not in sk.style:
                    comments.append("%s" % ui.skill(sk))
                    for effe in sk.effects:
                        comments.append(ui.effect(effe))
                else:
                    for effe in sk.effects:
                        comments.append(ui.effect(effe.exertion))
        ui.echo(ui.colored("【%s】- " % (idx + 1) + nd.name, attrs=["bold"]))
        for c in comments:
            ui.echo("       " + c)
    ret = ui.menu([], title=ctrl.title, shownone=False, goback=True, backmethod=ctrl.close)
    return ret
