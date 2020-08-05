# -- coding: utf-8 --


from proj.console import ui

from proj.console.handlers import team_info

from proj.runtime import context



def handler_person_item_transfer(ctx):
    if not ui.blankline():
        ui.echo()
    ui.echo("%s把%s×%s交给了%s" % (ctx.subject.name, ui.rank(ctx.item), ctx.quantity, ctx.object.name))
    ui.read()


def handler_person_item_lost(ctx):
    if not ui.blankline():
        ui.echo()
    ui.echo("%s失去了%s×%s" % (ctx.subject.name, ui.rank(ctx.item), ctx.quantity))
    ui.read()


def handler_person_item_acquire(ctx):
    if not ui.blankline():
        ui.echo()
    if ctx.item is not None:
        ui.echo("%s获得了%s×%s" % (ctx.subject.name, ui.rank(ctx.item), ctx.quantity))
    else:
        ui.echo("%s一无所获" % ctx.subject.name)
    ui.read()


def handler_person_equip_repair(ctx):
    ui.echo("%s耐久度已恢复！" % ui.rank(ctx.item))
    ui.echo()


def handler_person_task_update(ctx):
    ui.warn("奇怪的事件增加了！（事件『%s』有更新）" % ctx.task)
    ui.echo()


def handler_person_attitude_change(ctx):
    ui.warn("%s对你的好感度%s了！" % (ctx.subject.name, "提升" if ctx.delta > 0 else "下降"))
    ui.read()


def handler_person_join_team(ctx):
    ui.warn("%s加入了%s队。" % (ctx.subject.name, ctx.leader.name))
    ui.echo()


def handler_person_exp_gain(ctx):
    ui.echo("%s获得了%s点经验。" % (ctx.subject.name, ctx.exp))
    ui.read()


def handler_person_skill_learn(ctx):
    ui.echo("%s已经习得了技能%s：%s，请给%s安排新的修炼内容。" % (ctx.subject.name, ui.rank(ctx.node.belongs), ui.rank(ctx.node)))
    ui.read()


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
            prefix_str = ctx.talker.name + "："
            prefix = ui.fixed(10, n=(prefix_str if idx == 0 else " "))
            ui.words("%s%s" % (prefix, content))
        ui.read()
        if idx == len(contents) - 1:
            ui.echo()


def handler_world_map(ctrl):
    ui.echo()
    ui.map(ctrl.map, entities=team_info(ctrl.map), show_trace=ctrl.show_trace)
    ui.echo()
    ui.read("（回车继续）")
    ui.echo()
