# -- coding: utf-8 --

from proj.console import ui

def transport_menu(targets):
    tmenu = []
    tmenu.append(ui.menuitem("留在原处", value=""))
    for target in targets:
        tmenu.append(ui.menuitem("前往%s" % target["name"], value=(target["scenario"], target["location"])))
    return tmenu

def handler_team_transport(ctx):
    ret = ui.menu(transport_menu(ctx.targets))
    return ret