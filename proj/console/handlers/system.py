# -- coding: utf-8 --
import sys

from proj.engine import Message
from proj.engine import Event

from proj.runtime import context

from proj.console import message as msg
from proj.console import ui


def handler_show(ctx):
    if not ui.blankline():
        ui.echo()
    if ctx.text is not None:
        ui.echo(ctx.text)
        ui.echo()
    if ctx.wait:
        ui.read("（回车继续）")


def handler_conv(ctx):
    for p, con in ctx.conv:
        if p is None:
            con()
        elif isinstance(con, list):
            options = []
            for itm in con:
                evt = Event.get(itm[1].split(":")[-1])
                options.append({"text": itm[0],
                                "handle": lambda x: x.turn("on"),
                                "value": evt})
            Message(style=Message.Options, subject=p, options=options)
        else:
            if len(p) > 0:
                Message(style=Message.Show, text=msg.DIALOG_FORMAT % (p, con))
            else:
                Message(style=Message.Show, text=con)


def handler_options(ctx):
    opt_menu = []
    for i in range(len(ctx.options)):
        op = ctx.options[i]
        opt_menu.append(ui.menuitem(showword=op["text"],
                                    value=op.get("value", i),
                                 goto=op["handle"]))
    ui.menu(opt_menu)


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
