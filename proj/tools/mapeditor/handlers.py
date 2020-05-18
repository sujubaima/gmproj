# -- coding: utf-8 --

from proj.entity import Terran
from proj.entity import Element

from proj.console import ui
from proj.console import format as fmt
from proj.tools.mapeditor import orders
from proj.tools.mapeditor import editor

def entity_info(map):
    retlist = []

    for loc, entity in map.loc_entity.items():
        ret = {"location": None,
               "contents": ["", "", ""],
               "trace": [],
               "player": False}
        ret["location"] = loc
 
        if len(entity.members) == 1:
            name_str = entity.leader.name
        else:
            name_str = "%s队" % entity.leader.name
        ret["contents"][0] = ui.colored(name_str,
                                        color="cyan",
                                        attrs=["bold"])
        #ret["contents"][0] += fmt.vaka["direction"][str(entity.direction)]
        retlist.append(ret)
    return retlist

def editor_menu(map):
    ret = [ui.menuitem("地形", goto=lambda x: ui.menu(terran_menu(map), keylist=[chr(i) for i in range(ord('a'), ord('a') + 26)], columns=6, width=15, pagesize=26, goback=True)),
           ui.menuitem("实体", goto=lambda x: ui.menu(element_menu(map), goback=True)),
           ui.menuitem("人物", goto=lambda x: orders.PersonOrder(map=map)),
           ui.menuitem("擦除", goto=lambda x: orders.EraseOrder(map=map)),
           ui.menuitem("裁扩", goto=lambda x: ui.menu(resize_menu(map), goback=True)),
           ui.menuitem("坐标", goto=lambda x: orders.MapEditorOrder(map=map, show_coordinates=True, real_coordinates=True)),
           ui.menuitem("缩略", goto=lambda x: orders.ThumbnailOrder(map=map)),
           ui.menuitem("镜头", goto=lambda x: orders.CameraOrder(map=map)),
           ui.menuitem("保存", goto=lambda x: orders.SaveOrder(map=map))]
    return ret


def resize_menu(map): 
    ret = [ui.menuitem("左边界扩展", goto=lambda x: orders.ResizeOrder(map=map, axis="x", factor=1)),
           ui.menuitem("左边界剪裁", goto=lambda x: orders.ResizeOrder(map=map, axis="x", factor=-1)),
           ui.menuitem("右边界扩展", goto=lambda x: orders.ResizeOrder(map=map, axis="x", factor=1, translation=False)),
           ui.menuitem("右边界剪裁", goto=lambda x: orders.ResizeOrder(map=map, axis="x", factor=-1, translation=False)),
           ui.menuitem("上边界扩展", goto=lambda x: orders.ResizeOrder(map=map, axis="y", factor=1)),
           ui.menuitem("上边界剪裁", goto=lambda x: orders.ResizeOrder(map=map, axis="y", factor=-1)),
           ui.menuitem("下边界扩展", goto=lambda x: orders.ResizeOrder(map=map, axis="y", factor=1, translation=False)),
           ui.menuitem("下边界剪裁", goto=lambda x: orders.ResizeOrder(map=map, axis="y", factor=-1, translation=False))]
    return ret


def load_map(arg):
    ret = [ui.menuitem("另存为")]
    for file in os.listdir("%s/../../data/maps" % os.path.dirname(__file__)):
        if not file.endswith(".py") or file.startswith("__init__.py"):
            continue
        ret.append(ui.menuitem(file[:-3], goto=lambda x: load_map_module(x)))
    ui.menu(ret, goback=True)
    
   
def terran_menu(map):
    ret = [ui.menuitem("草地", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_GRASS"))),
           ui.menuitem("树林", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_FOREST"))),
           ui.menuitem("红花", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_FLOWER_RED"))),
           ui.menuitem("黄花", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_FLOWER_YELLOW"))),
           ui.menuitem("水域", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_WATER"))),
           ui.menuitem("山地", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_MOUNTAIN"))),
           ui.menuitem("悬崖", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_CLIFF"))),
           ui.menuitem("丘陵", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_HILL"))),
           ui.menuitem("密林", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_JUNGLE"))),
           ui.menuitem("洼地", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_MARSH"))),
           ui.menuitem("沙漠", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_DESERT"))),
           ui.menuitem("雪地", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_SNOW"))),
           ui.menuitem("道路", goto=lambda x: orders.TerranOrder(map=map, terran=Terran.one("TERRAN_ROAD")))]
    return ret


def element_menu(map):
    ret = [ui.menuitem("建筑", goto=lambda x: orders.EntityNameOrder(map=map, entity=Element.one("ELEMENT_BUILDING"))),
           ui.menuitem("城墙", goto=lambda x: orders.EntityNameOrder(map=map, entity=Element.one("ELEMENT_WALL"))),
           ui.menuitem("塔楼", goto=lambda x: orders.EntityNameOrder(map=map, entity=Element.one("ELEMENT_TOWER"))),
           ui.menuitem("岩石", goto=lambda x: orders.EntityNameOrder(map=map, entity=Element.one("ELEMENT_ROCK")))]
    return ret
    
    
def validate_position(pos, map):
    x, y = pos.split()
    x = int(x)
    y = int(y)
    real_pos = map.point_to_real((x, y))
    return real_pos
    
    
def validate_positions(poslist, map):
    ret = []
    tmplist = poslist.split(",")
    for tmp in tmplist:
        x, y = tmp.split()
        if x.find("-") >= 0:
            xsplit = x.split("-")
            xlist = list(range(int(xsplit[0]), int(xsplit[1]) + 1))
        else:
            xlist = [int(x)]
        if y.find("-") >= 0:
            ysplit = y.split("-")
            ylist = list(range(int(ysplit[0]), int(ysplit[1]) + 1))
        else:
            ylist = [int(y)]
        for xi in xlist:
            for yi in ylist:
                real_pos = map.point_to_real((xi, yi))
                ret.append(real_pos)
    return ret
    

def handler_map_editor(ctx):
    ui.echo()
    if ctx.show_coordinates:
        ui.map(map=ctx.map, coordinates=ctx.map.all(), real_coordinates=ctx.real_coordinates,
               entities=entity_info(ctx.map))
    else:
        ui.map(map=ctx.map, entities=entity_info(ctx.map))
    ui.echo()
    ret = ui.menu(editor_menu(ctx.map), title="请选择你要进行的操作：", columns=2, width=15)
    return ret


def handler_map_thumbnail(ctx):
    ui.echo()
    ui.thumbnail(map=ctx.map, entities=entity_info(ctx.map))
    ui.echo()
    ui.read("（回车继续）")
    
    
def handler_map_camera(ctx):
    ui.echo()
    ui.map(map=ctx.map, coordinates=ctx.map.all(), entities=entity_info(ctx.map))
    ui.echo()
    ret = ui.read("请输入镜头需要移动至的坐标（x与y用空格分隔）：", handler=lambda x: validate_position(x, ctx.map))
    return ret
    

def handler_map_terran(ctx):
    ui.echo()
    ui.map(map=ctx.map, coordinates=ctx.map.all(), entities=entity_info(ctx.map))
    ui.echo()
    ret = ui.read("请输入需要添加地形的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", handler=lambda x: validate_positions(x, ctx.map))
    return ret
    
 
def handler_map_entity(ctx):
    ui.echo()
    ui.map(map=ctx.map, coordinates=ctx.map.all(), entities=entity_info(ctx.map))
    ui.echo()
    ret = ui.read("请输入需要添加元素的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", handler=lambda x: validate_positions(x, ctx.map))
    return ret


def handler_map_entity_name(ctx):
    ret = ui.read("输入你想要设置的实体名称：")
    return ret


def handler_map_person(ctx):
    ui.echo()
    person = ui.read("请输入需要添加人物的模板号：")
    ui.echo()
    if not person.startswith("PERSON"):
        return None
    ui.map(map=ctx.map, coordinates=ctx.map.all(), entities=entity_info(ctx.map))
    ui.echo()
    loc = ui.read("请输入需要添加地形的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", handler=lambda x: validate_positions(x, ctx.map))
    return (person, loc)

    
def handler_map_erase(ctx):
    ui.echo()
    ui.map(map=ctx.map, coordinates=ctx.map.all(), entities=entity_info(ctx.map))
    ui.echo()
    ret = ui.read("请输入需要添加地形的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", handler=lambda x: validate_positions(x, ctx.map))
    return ret
  
  
def handler_map_resize(ctx):
    ui.echo()
    ret = ui.read("请输入需要扩展或剪裁的值）：")
    return ret
    
    
def handler_map_save(ctx):
    editor.list_modules(ctx, lambda y: editor.save_map(y), newbuild=True)
    return True
