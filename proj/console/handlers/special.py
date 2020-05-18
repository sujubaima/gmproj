# -- coding: utf-8 --

from proj.console import ui

from proj.console.orders import SuperSkillReadOrder

from proj.entity import Item
from proj.entity import Skill

def handler_superskill_choose(ctx):
    skmenu = []
    for sk in ctx.superskills:
        comments = [Item.one("ITEM_%s" % sk.tpl_id[11:]).description]
        skmenu.append(ui.menuitem(ui.rank(sk), value=sk, comments=comments, 
                                  goto=lambda x: SuperSkillReadOrder(superskill=x)))
    skmenu.append(ui.menuitem("离开"))
    ret = ui.menu(skmenu, title="请选择你要翻阅的武学：")
    return ret
    

def handler_superskill_read(ctx):
    if not ui.blankline():
        ui.echo()
    ui.superskill(ctx.superskill)
    ui.echo()
    for idx, nd in enumerate(ctx.superskill.nodes):
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
    ret = ui.menu([], title="请选择你的行动：", shownone=False, goback=True)
    return ret
