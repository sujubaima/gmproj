# -- coding: utf-8 --

from proj.entity import Terran
from proj.entity import Element

from proj.console import ui
from proj.console import format as fmt
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


def editor_menu(ctrl):
    ret = [ui.menuitem("地形", goto=ctrl.terran),
           ui.menuitem("物件", goto=ctrl.element),
           ui.menuitem("人物", goto=ctrl.person),
           ui.menuitem("擦除", goto=ctrl.erase),
           ui.menuitem("裁扩", goto=ctrl.resize),
           ui.menuitem("坐标", goto=ctrl.coordinate),
           ui.menuitem("缩略", goto=ctrl.thumbnail),
           ui.menuitem("镜头", goto=ctrl.camera),
           ui.menuitem("保存", goto=ctrl.save)]
    return ret


def resize_menu(ctrl): 
    ret = [ui.menuitem("左边界扩展", value=("x", 1, True), goto=ctrl.select),
           ui.menuitem("左边界剪裁", value=("x", -1, True), goto=ctrl.select),
           ui.menuitem("右边界扩展", value=("x", 1, False), goto=ctrl.select),
           ui.menuitem("右边界剪裁", value=("x", -1, False), goto=ctrl.select),
           ui.menuitem("上边界扩展", value=("y", 1, True), goto=ctrl.select),
           ui.menuitem("上边界剪裁", value=("y", -1, True), goto=ctrl.select),
           ui.menuitem("下边界扩展", value=("y", 1, False), goto=ctrl.select),
           ui.menuitem("下边界剪裁", value=("y", -1, False), goto=ctrl.select)]
    return ret


def load_map(arg):
    ret = [ui.menuitem("另存为")]
    for file in os.listdir("%s/../../data/maps" % os.path.dirname(__file__)):
        if not file.endswith(".py") or file.startswith("__init__.py"):
            continue
        ret.append(ui.menuitem(file[:-3], goto=lambda x: load_map_module(x)))
    ui.menu(ret, goback=True)
    
   
def terran_menu(ctrl):
    ret = [ui.menuitem("草地", value="TERRAN_GRASS", goto=ctrl.select),
           ui.menuitem("树林", value="TERRAN_FOREST", goto=ctrl.select),
           ui.menuitem("红花", value="TERRAN_FLOWER_RED", goto=ctrl.select),
           ui.menuitem("黄花", value="TERRAN_FLOWER_YELLOW", goto=ctrl.select),
           ui.menuitem("水域", value="TERRAN_WATER", goto=ctrl.select),
           ui.menuitem("山地", value="TERRAN_MOUNTAIN", goto=ctrl.select),
           ui.menuitem("悬崖", value="TERRAN_CLIFF", goto=ctrl.select),
           ui.menuitem("丘陵", value="TERRAN_HILL", goto=ctrl.select),
           ui.menuitem("密林", value="TERRAN_JUNGLE", goto=ctrl.select),
           ui.menuitem("洼地", value="TERRAN_MARSH", goto=ctrl.select),
           ui.menuitem("沙漠", value="TERRAN_DESERT", goto=ctrl.select),
           ui.menuitem("雪地", value="TERRAN_SNOW", goto=ctrl.select),
           ui.menuitem("道路", value="TERRAN_ROAD", goto=ctrl.select)]
    return ret


def element_menu(ctrl):
    ret = [ui.menuitem("建筑", value="ELEMENT_BUILDING", goto=ctrl.select),
           ui.menuitem("城墙", value="ELEMENT_WALL", goto=ctrl.select),
           ui.menuitem("塔楼", value="ELEMENT_TOWER", goto=ctrl.select),
           ui.menuitem("岩石", value="ELEMENT_ROCK", goto=ctrl.select)]
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
    

def handler_map_editor_control(ctrl):
    if not ui.blankline():
        ui.echo()
    if ctrl.show_coordinates:
        ui.map(map=ctrl.map, coordinates=[{"positions": ctrl.map.all(), "real": ctrl.real_coordinates}],
               entities=entity_info(ctrl.map))
    else:
        ui.map(map=ctrl.map, entities=entity_info(ctrl.map))
    if ctrl.real_coordinates:
        ctrl.real_coordinates = False
        ctrl.show_coordinates = False
    ui.echo()
    ret = ui.menu(editor_menu(ctrl), title="请选择你要进行的操作：", columns=2, width=15)
    return ret


def handler_map_terran_control(ctrl):
    ui.menu(terran_menu(ctrl), keylist=[chr(i) for i in range(ord('a'), ord('a') + 26)], 
            columns=6, width=15, pagesize=26, goback=True, backmethod=ctrl.close)
    ui.echo()
    ui.map(map=ctrl.map, coordinates=[{"positions": ctrl.map.all()}], entities=entity_info(ctrl.map))
    ui.echo()
    ret = ui.read("请输入需要添加地形的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", 
                  handler=lambda x: validate_positions(x, ctrl.map))
    ctrl.input(ret)


def handler_map_element_control(ctrl):
    if not ui.blankline():
        ui.echo()
    ret = ui.read("输入你想要设置的实体名称：")
    ctrl.elename(ret)
    ui.menu(element_menu(ctrl), goback=True, backmethod=ctrl.close)
    ui.echo()
    ui.map(map=ctrl.map, coordinates=[{"positions": ctrl.map.all()}], entities=entity_info(ctrl.map))
    ui.echo()
    ret = ui.read("请输入需要添加元素的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", 
                  handler=lambda x: validate_positions(x, ctrl.map))
    ctrl.input(ret)


def handler_map_thumbnail_control(ctrl):
    if not ui.blankline():
        ui.echo()
    ui.echo()
    ui.thumbnail(map=ctrl.map, entities=entity_info(ctrl.map))
    ui.echo()
    ui.read("（回车继续）")
    ctrl.close()
    
    
def handler_map_camera_control(ctrl):
    ui.echo()
    ui.map(map=ctrl.map, coordinates=[{"positions": ctrl.map.all()}], entities=entity_info(ctrl.map))
    ui.echo()
    ret = ui.read("请输入镜头需要移动至的坐标（x与y用空格分隔）：", 
                  handler=lambda x: validate_position(x, ctrl.map))
    ctrl.input(ret)
    

def handler_map_person_control(ctrl):
    ui.echo()
    person = ui.read("请输入需要添加人物的模板号：")
    ui.echo()
    if not person.startswith("PERSON"):
        return None
    ui.map(map=ctrl.map, coordinates=[{"positions": ctrl.map.all()}], entities=entity_info(ctrl.map))
    ui.echo()
    loc = ui.read("请输入需要添加地形的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", 
              handler=lambda x: validate_positions(x, ctrl.map))
    ctrl.input((person, loc))

    
def handler_map_erase_control(ctrl):
    ui.echo()
    ui.map(map=ctrl.map, coordinates=[{"positions": ctrl.map.all()}], entities=entity_info(ctrl.map))
    ui.echo()
    ret = ui.read("请输入需要添加地形的坐标（x与y用空格分隔，多个坐标用半角逗号分隔）：", 
                  handler=lambda x: validate_positions(x, ctrl.map))
    ctrl.input(ret)
  
  
def handler_map_resize_control(ctrl):
    if not ui.blankline():
        ui.echo()
    ui.menu(resize_menu(ctrl), goback=True, backmethod=ctrl.close)
    ui.echo()
    ret = ui.read("请输入需要扩展或剪裁的值）：")
    ctrl.input(ret)
    
    
def handler_map_save(ctrl):
    editor.list_modules(ctrl, lambda y: editor.save_map(y), newbuild=True)
    ctrl.close()
