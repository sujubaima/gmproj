# -- coding: utf-8 --
import os
import sys
import importlib
import json

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../../"))

from proj import engine
from proj.engine import Message

from proj.entity import Map
from proj.entity import Terran

from proj.tools.mapeditor import handlers
from proj.tools.mapeditor.orders import MapEditorOrder
from proj.tools.mapeditor import globals

from proj.console import ui
    

def handler(ctx):
    ret = None
    if ctx.style != ctx.Null:
        ret = eval("handlers.handler_%s" % ctx.style)(ctx)
    if ctx.callback is not None:
        ctx.callback(ret)
 
 
def blank_map(arg):
    name = ui.read("请输入你想要建立的地图的名字：")
    ui.echo()   
    rt = ui.read("请输入你想要建立的地图大小（第一个数字为宽，第二个为高，中间使用空格分隔）：")
    x, y = rt.split()
    x = int(x)
    y = int(y)
    globals.MAP = Map(name=name, width=x, height=y, window_y=7)
    
    
def load_map(arg):
    globals.MAP = Map.one(arg)
    
    
def save_map(arg):
    globals.MAP.tpl_id = arg
    tmplist = []
    for m in dir(globals.MAP_MODULE):
        if not m.startswith("MAP_"):
            continue
        
        if m != globals.MAP.tpl_id:
            tmplist.append((m, getattr(globals.MAP_MODULE, m)))
    tmplist.append((globals.MAP.tpl_id, tojson(globals.MAP)))
    fpath = "%s/../../data/maps/%s.py" % (os.path.dirname(__file__), globals.MAP_MODULE.__name__.split(".")[-1])
    with open(fpath, "w") as fd:
        fd.write("# -- encoding: utf-8 --\n")
        fd.write("\n")
        for t, m in tmplist:
            fd.write("%s = \\\n" % t)
            fd.write(json.dumps(m, indent=4))
            fd.write("\n\n")
            
            
def tojson(map):
    ret = {}
    ret["width"] = map.x
    ret["height"] = map.y
    ret["name"] = map.name
    ret["terrans"] = []
    ret["objects"] = []
    ret["persons"] = []
    ret["start_locations"] = []
    ret["transport_locations"] = {}
    terran_map = {}
    object_map = {}
    for sl in map.start_locs:
        ret["start_locations"].append([])
        for slp in sl:
            ret["start_locations"][-1].append(str(slp))
    for tl, scene in map.transport_locs.items():
        ret["transport_locations"][str(tl)] = scene 
    for i in range(map.x):
        for j in range(map.y):
            if map.xy[i][j].terran.tpl_id != "TERRAN_BLANK":
                if map.xy[i][j].terran.tpl_id not in terran_map:
                    terran_map[map.xy[i][j].terran.tpl_id] = []
                terran_map[map.xy[i][j].terran.tpl_id].append(str((i, j)))
            if map.xy[i][j].object is not None:
                if (map.xy[i][j].showword, map.xy[i][j].object.tpl_id) not in object_map:
                    object_map[(map.xy[i][j].showword, map.xy[i][j].object.tpl_id)] = []
                object_map[(map.xy[i][j].showword, map.xy[i][j].object.tpl_id)].append(str((i, j)))
    for k, v in terran_map.items():
        ret["terrans"].append({"style": k, "points": v})
    for k, v in object_map.items():
        ret["objects"].append({"name": k[0], "style": k[1], "points": v})
    for k, v in map.loc_entity.items():
        for m in v.members:
            ret["persons"].append({"id": m.tpl_id, "location": str(k)})
    return ret
            
    
def list_maps(arg, map_func, newbuild=False):
    ret = []
    if newbuild:
        ret.append(ui.menuitem("新建地图", goto=lambda x: new_map(x, map_func)))
    nomod = False
    try:
        globals.MAP_MODULE = importlib.import_module("proj.data.maps.%s" % arg)
    except Exception as e:
        nomod = True
    if not nomod:
        for m in dir(globals.MAP_MODULE):
            if not m.startswith("MAP_"):
                continue
            ret.append(ui.menuitem(m, value=m, goto=lambda x: map_func(x)))
    ui.echo()
    ui.menu(ret, title="请选择目标地图：", goback=True)
  
  
def list_modules(arg, map_func, newbuild=False):
    ret = []
    if newbuild:
        ret.append(ui.menuitem("新建地图组", goto=lambda x: new_module(x, map_func)))
    for file in os.listdir("%s/../../data/maps" % os.path.dirname(__file__)):
        if not file.endswith(".py") or file.startswith("__init__.py"):
            continue
        ret.append(ui.menuitem(file[:-3], goto=lambda x: list_maps(x, map_func, newbuild)))
    ui.echo()
    ui.menu(ret, title="请选择目标地图组：", goback=True)
    
    
def new_module(arg, map_func):
    rt = ui.read("请输入你想要新建的地图组名：")
    fpath = "%s/../../data/maps/%s.py" % (os.path.dirname(__file__), rt)
    if not os.path.exists(fpath):
        with open(fpath, "w") as fd:
            pass
    globals.MAP_MODULE = importlib.import_module("proj.data.maps.%s" % rt)
    fpath = "%s/../../data/maps/__init__.py" % os.path.dirname(__file__)
    recorded = False
    with open(fpath) as fd:
        for line in fd:
            if line == "from proj.data.maps.%s import *" % rt:
                recored = True
                break
    if not recorded:
        with open(fpath, "a") as fd:
            fd.write("\nfrom proj.data.maps.%s import *\n" % rt)
    list_maps(arg, map_func, True)
   

def new_map(arg, map_func):
    rt = ui.read("请输入你想要新建的地图名：")
    globals.MAP.tpl_id = rt
    map_func(rt)
    
    
main_menu = [ui.menuitem("空白地图", goto=blank_map),
             ui.menuitem("载入地图", goto=lambda x: list_modules(x, lambda y: load_map(y))),
             ui.menuitem("退出", goto=lambda x: sys.exit(0))]
             

if __name__ == "__main__":
    
    Message.handler = handler
    
    ui.echo()
    ui.menu(main_menu, title="欢迎使用地图编辑器！")
    
    MapEditorOrder(map=globals.MAP)
    
    engine.start(events=False)
