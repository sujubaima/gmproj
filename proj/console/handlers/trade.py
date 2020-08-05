# -- coding: utf-8 --

from proj.console import ui


def trade_menu(ctrl):
    tmenu = [ui.menuitem("购买", goto=ctrl.buy),
             ui.menuitem("出售", goto=ctrl.sell),
             ui.menuitem("制作", goto=ctrl.make)]
    if "Equip" in ctrl.object.tags:
        tmenu.append(ui.menuitem("修理", goto=ctrl.repair))
        tmenu.append(ui.menuitem("强化", goto=ctrl.strengthen))
    tmenu.append(ui.menuitem("离开", goto=lambda x: ctrl.close()))
    return tmenu



def handler_trade_control(ctrl):
    ui.menu(trade_menu(ctrl), columns=2, width=15)


def handler_item_inlay_select_control(ctrl):
    imenu = []
    for idx, inlay in enumerate(ctrl.item.inlays):
        enabled = "filled" not in inlay
        if enabled:
            name_str = inlay["name"]
            comments = ["接受材料：%s" % "、".join([ui.tag(acp) for acp in inlay["accept"]])]
            validator = lambda x: True
        else:
            name_str = inlay["name"]
            comments = ["已强化：%s" % ui.rank(inlay["filled"])]
            comments.extend([ui.effect(effe, grey=True) for effe in inlay["filled"].effects if effe.name is not None])
            validator = lambda x: False
        imenu.append(ui.menuitem(name_str, value=idx, comments=comments, validator=validator, goto=ctrl.select))
    ret = ui.menu(imenu, title="请选择你要强化的部位：", goback=True, backmethod=ctrl.close)
    return ret
