from proj.engine import Message

from proj.console import handlers


def handler(ctx):
    ret = None
    if ctx.style != ctx.Null:
        ret = eval("handlers.handler_%s" % ctx.style)(ctx)
    if ctx.callback is not None:
        ctx.callback(ret)


def init():
    Message.handler = handler 
