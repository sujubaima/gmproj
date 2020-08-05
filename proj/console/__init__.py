from proj.engine import Message

from proj.console import handlers


def handler(ctx):
    ret = None
    if ctx.style != ctx.Null:
        if ctx.control is not None:
            ctx_arg = ctx.control
        elif ctx.action is not None:
            ctx_arg = ctx.action
        else:
            ctx_arg = ctx
        ret = eval("handlers.handler_%s" % ctx.style)(ctx_arg)
    if ctx.callback is not None:
        ctx.callback(ret)


def init():
    Message.handler = handler 
