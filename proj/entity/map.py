# -- coding: utf-8 --
from __future__ import division

import math
import random
import time
import importlib

import sys
sys.path.append("/home/work/gmproj")

from proj import options

from proj.entity.common import Entity


class Shape(object):

    Point = 0
    Line = 1
    SmallSector = 2
    BigSector = 3
    Round = 4
    Around = 5

    def __init__(self, style, scope, sputter=0, msputter=1, block=1):
        self.style = style
        self.scope = scope
        self.sputter = sputter
        self.msputter = msputter
        self.block = block

    def attack_range(self, distance=None):
        if self.style == Shape.Point:
            if distance is None:
                return [self.msputter - self.sputter, self.scope + self.sputter]
            else:
                return [distance - self.sputter, distance + self.sputter]
        else:
            return [self.msputter, self.sputter]

    def attack_angle(self):
        if self.style == Shape.Point:
            return math.pi / 180
        elif self.style == Shape.Line:
            return math.pi / 180
        elif self.style == Shape.BigSector:
            return math.pi * 2 / 3
        elif self.style == Shape.SmallSector:
            return math.pi / 3
        else:
            return math.pi * 2

    def __str__(self):
        return "%s.%s,%s,%s,%s" % (self.style, self.block, self.scope, self.sputter, self.msputter)

    @property
    def showword(self):
        if self.block == 1:
            blockstr = "横扫"
        elif self.block == 2:
            blockstr = "冲击"
        else:
            blockstr = "无视"
        if self.style == Shape.Point:
            if self.msputter <= 1:
                ret = "单体%s%s" % (blockstr, self.scope)
            else:
                ret = "单体%s%s至%s" % (blockstr, self.msputter, self.scope)
            if self.sputter > 0:
                ret += "溅射%s" % self.sputter
        elif self.style == Shape.Line:
            if self.msputter <= 1:
                ret = "直线%s%s" % (blockstr, self.sputter)
            else:
                ret = "直线%s%s至%s" % (blockstr, self.msputter, self.sputter)
        elif self.style == Shape.BigSector:
            if self.msputter <= 1:
                ret = "大扇形%s%s" % (blockstr, self.sputter)
            else:
                ret = "大扇形%s%s至%s" % (blockstr, self.msputter, self.sputter)
        elif self.style == Shape.SmallSector:
            if self.msputter <= 1:
                ret = "小扇形%s%s" % (blockstr, self.sputter)
            else:
                ret = "小扇形%s%s至%s" % (blockstr, self.msputter, self.sputter)
        elif self.style == Shape.Round:
            if self.msputter <= 1:
                ret = "超扇形%s%s" % (blockstr, self.sputter)
            else:
                ret = "超扇形%s%s至%s" % (blockstr, self.msputter, self.sputter)
        elif self.style == Shape.Around:
            if self.msputter <= 1:
                ret = "周身%s%s" % (blockstr, self.sputter)
            else:
                ret = "环形%s%s至%s" % (blockstr, self.msputter, self.sputter)
        return ret


#class Terran(object):
#    
#    Plain = "Plain"
#    Grass = "Grass"
#    Forest = "Forest"
#    Mountain = "Mountain"
#    Hill = "Hill"
#    Water = "Water"
#    Jungle = "Jungle"
#    Building = "Building"
#    Wall = "Wall"
#
#    Motivation = {Plain: 1,
#                  Grass: 1,
#                  Forest: 2,
#                  Mountain: -1,
#                  Hill: 4,
#                  Water: -1,
#                  Jungle: -1,
#                  Building: -1,
#                  Wall: -1}
#
#    @staticmethod
#    def motivation(terran):
#        return Terran.Motivation[terran]


class Terran(Entity):

    def handle(self, k, v):
        if options.USE_FULL_WIDTH_FONT and k == "vision_half":
            return
        if not options.USE_FULL_WIDTH_FONT and k == "vision_full":
            return
        elif k in ["vision_half", "vision_full"]:
            self.vision = v.get("effects", {})
            self.character = v.get("character", " ")
            self.thumbnail = v.get("thumbnail", None)
        else:
            setattr(self, k, v)

    def initialize(self):
        self.vision = {}
        self.character = " "
        self.thumbnail = None
        self.motivation = 1
        self.name = None
        
        
class Element(Entity):

    def handle(self, k, v):
        if options.USE_FULL_WIDTH_FONT and k == "vision_half":
            return
        if not options.USE_FULL_WIDTH_FONT and k == "vision_full":
            return
        elif k in ["vision_half", "vision_full"]:
            self.vision = v.get("effects", {})
            self.character = v.get("character", "/")
            self.thumbnail = v.get("thumbnail", self.character)
        else:
            setattr(self, k, v)

    def initialize(self):
        self.vision = {}
        self.character = "/"
        self.thumbnail = "/"
        self.name = None
    

class Dim2Dict(dict):
    
    def __setitem__(self, key, value):
        k, subk = key
        if k not in self:
            super(Dim2Dict, self).__setitem__(k, {})
        self[k][subk] = value
        

    def __getitem__(self, key):
        k, subk = key
        return super(Dim2Dict, self).__getitem__(k)[subk]


class MapGrid(object):

    def __init__(self):
        self.terran = Terran.one("TERRAN_BLANK")
        self.object = None
        self.showword = None
        
    def title(self):
        if self.showword is not None:
            return self.showword 
        elif self.object is not None:
            return self.object.name
        else:
            return ""

 
class Map(Entity):
    """
    六边形网格地图的封装，写的年代有点早了，代码乱的一笔，有时间再整理吧，
    反正主要就是那几个寻路和范围计算的函数
    """

    def initialize(self):
       
        self.xy = []

        self.center_x = 0
        self.center_y = 0

        self.window_start_x = 0
        self.window_start_y = 0

        self.entity_loc = {}
        self.loc_entity = {}

        self.start_locs = []
        self.transport_locs = {}

        self.pathblocked = set()
        
    def handle(self, k, v):
        if k == "width":
            self.x = v
        elif k == "height":
            self.y = v
        elif k == "terrans":
            self.tmpdict["terrans"] = v
        elif k == "objects":
            self.tmpdict["objects"] = v
        elif k == "start_locations":
            for info in v:
                loc_list = []
                for pt in info:
                    pt_t = eval(pt)
                    loc_list.append(pt_t)
                self.start_locs.append(loc_list)
        elif k == "transport_locations":
            for loc, scene in v.items():
                loc = eval(loc)
                self.transport_locs[loc] = scene
        elif k == "persons":
            pmod = importlib.import_module("proj.entity.person")
            tmod = importlib.import_module("proj.entity.team")
            for info in v:
                p = pmod.Person.one(info["id"])
                #if p.team is None:
                #    team = tmod.Team()
                #    team.include(p)
                #else:
                team = p.team
                loc = eval(info["location"])
                old_ent = self.loc_entity.get(loc, None)
                if old_ent is not None:
                    old_ent.include(p)
                else:
                    self.loc_entity[loc] = team
                    self.entity_loc[team.id] = loc
                team.scenario = self
        else:
            setattr(self, k, v)
        
    def finish(self):
        if self.x is None or self.y is None:
            return
        for i in range(self.x):
            self.xy.append([])
            for j in range(self.y):
                self.xy[i].append(MapGrid())
                
        if "terrans" in self.tmpdict:
            v = self.tmpdict.pop("terrans")
            for info in v:
                terran = Terran.one(info["style"])
                for pt in info["points"]:
                    pt_t = eval(pt)
                    self.xy[pt_t[0]][pt_t[1]].terran = terran
            
        if "objects" in self.tmpdict:
            v = self.tmpdict.pop("objects")
            for info in v:
                name = info["name"]
                obj = Element.one(info["style"])
                for pt in info["points"]:
                    pt_t = eval(pt)
                    self.xy[pt_t[0]][pt_t[1]].showword = name
                    self.xy[pt_t[0]][pt_t[1]].object = obj
        if self.window_x is None:
            self.window_x = self.x
        self.window_x = min(8, self.window_x, self.x)

        if self.window_y is None:
            self.window_y = self.y
        self.window_y = min(9, self.window_y, self.y)

    def window(self):
        ret = []
        for i in range(self.window_start_x, self.window_start_x + self.window_x):
            tmp = []
            for j in range(self.window_start_y, self.window_start_y + self.window_y):
                tmp.append(self.xy[i][j])
            ret.append(tmp)
        return ret

    #def center(self):
    #    return (self.center_x - self.window_start_x, self.center_y - self.window_start_y)

    def all(self):
        ret = []
        for i in range(self.window_start_x, self.window_start_x + self.window_x):
            for j in range(self.window_start_y, self.window_start_y + self.window_y):
                ret.append((i, j))
        return ret

    def grid(self, pos):
        return self.xy[pos[0]][pos[1]]

    def window_center(self, new_loc):
        self.center_x = new_loc[0]
        self.center_y = new_loc[1]
        window_size_w = self.window_x // 2
        window_size_h = self.window_y // 2
        self.window_start_x = min(max(self.center_x - window_size_w, 0), self.x - self.window_x)
        self.window_start_y = min(max(self.center_y - window_size_h, 0), self.y - self.window_y)

    def point_to_window(self, pt):
        x, y = pt
        return (x - self.window_start_x, y - self.window_start_y)

    def point_to_real(self, pt):
        x, y = pt
        return (x + self.window_start_x, y + self.window_start_y)

    def in_window(self, pt):
        x, y = pt
        if x >= self.window_start_x and x < self.window_start_x + self.window_x and \
           y >= self.window_start_y and y < self.window_start_y + self.window_y:
            return True
        else:
            return False

    def set_terran(self, xylist, terran, showword=None):
        for x, y in xylist:
            self.xy[x][y].terran = terran
            if showword is not None:
                self.xy[x][y].showword = showword

    def set_object(self, xylist, obj, showword=None):
        for x, y in xylist:
            self.xy[x][y].object = obj
            if showword is not None:
                self.xy[x][y].showword = showword
 
    def is_on_map(self, pt):
        x, y = pt
        return x >= 0 and x < self.x and y >= 0 and y < self.y

    def can_move(self, subject, pt):
        grid = self.xy[pt[0]][pt[1]]
        return grid.terran.tpl_id in subject.movitivity and \
               ("OBJECTS" in subject.movitivity or grid.object is None) and \
               ("PERSONS" in subject.movitivity or pt not in self.loc_entity)

    def can_stay(self, subject, pt, ignore_people=False):
        grid = self.xy[pt[0]][pt[1]]
        return grid.terran.tpl_id in subject.locativity and \
               ("OBJECTS" in subject.locativity or grid.object is None) and \
               (ignore_people or "PERSONS" in subject.locativity or pt not in self.loc_entity)

    def people_around(self, p, filter=None):
        zoc = 0
        for x, y in self.circle(self.entity_loc[p.id], 1):
            if (x, y) in self.loc_entity:
                if filter is None or filter(self.xy[x][y]):
                    zoc += 1
        return zoc

    def offset_xy(self, x, y):
        if y % 2 == 1:
           x += 0.5
        y = y * math.sqrt(3) / 2
        return (x, y)

    def normal_xy(self, x, y):
        y = int(round(y * 2 / math.sqrt(3)))
        if y % 2 == 1:
           x -= 0.5
        x = int(round(x))
        return (x, y)

    def center_point(self, pt_list):
        cent_x = 0
        cent_y = 0
        for pt in pt_list:
            offset_x, offset_y = self.offset_xy(pt[0], pt[1])
            cent_x += offset_x
            cent_y += offset_y
        cent_x, cent_y = self.normal_xy(cent_x / len(pt_list), cent_y / len(pt_list))
        return (cent_x, cent_y)

    def around(self, pt):
        x, y = pt
        if y % 2 == 0:
            k = -1
        else:
            k = 1
        tmpret = [(x, y - 1), (x + k, y - 1), (x - 1, y), 
                  (x + 1, y), (x, y + 1), (x + k, y + 1)]
        ret = []
        for rx, ry in tmpret:
            if self.is_on_map((rx, ry)) and self.xy[rx][ry].object is None:
                ret.append((rx, ry))
        return ret

    def neighbour(self, pt, dire):
        x, y = pt
        if y % 2 == 0:
            k = -1
        else:
            k = 1
        tmpret = [(x + 1, y), (max(x + k, x), y + 1), (min(x + k, x), y + 1),
                  (x - 1, y), (min(x + k, x), y - 1), (max(x + k, x), y - 1)]
        return tmpret[dire]

    def on_map(self, pt):
        x, y = pt
        return x >= 0 and x < self.x and y >= 0 and y < self.y

    def on_border(self, pt):
        x, y = pt
        return x == 0 or x == self.x - 1 or y == 0 or y == self.y - 1

    def connectivity(self, pt, person, r=None, enable_zoc=True, filter=None):
        """
        搜索所有可能移动的格子
        因为有ZOC机制的存在，每次有角色移动都要重新搜索
        后续可以优化：
        地图初始化的时候计算出一个静态表，后续只要对角色移动过的区域进行更新即可
        不过现在这个实现的效率也还行啦，先这么用吧
        """
        x, y = pt
        kmap = {}
        # zmap用于记录zoc信息，总共两个字段，分别是与敌人的距离与该点处于谁的控制下
        zmap = {}
        last_k = -1
        new_k = 0
        if r is None:
            total_set = self.all()
        else:
            total_set = self.range_grids(self.location(person), r)
        while new_k != last_k:
            last_k = new_k
            fmap = {}
            for (i, j) in total_set: 
                p = (i, j)
                #if filter is not None and not filter(i, j):
                #   continue
                if p not in fmap:
                    fmap[p] = 1
                    self.connect_static((i, j), (x, y), fmap, kmap, zmap, person, enable_zoc=enable_zoc, filter=filter)
            new_k = sum([itm[0] for itm in kmap.values()])
        #for (i, j) in zmap:
        #    if zmap[(i, j)] > 0 and (i, j) in kmap:
        #        kmap[(i, j)] = (max(person.motion, kmap[(i, j)][0]), kmap[(i, j)][1])
        #for k, v in kmap.items():
        #    print(k, v)
        return kmap

    def connect_static(self, pta, ptb, fmap, kmap, zmap, person, enable_zoc=True, filter=None):
        """
        静态寻路算法，用于战斗中计算所有可移动格子
        """
        i, j = pta
        x, y = ptb
        if enable_zoc and (i, j) not in zmap:
            zmap[(i, j)] = (sys.maxsize, None)
            for zoc_loc, zoc_p in self.loc_entity.items():
                if zoc_p.group_ally & person.group_ally != 0:
                    continue
                zoc_distance = self.distance(zoc_loc, (i, j))
                if zoc_distance <= zoc_p.zoc_scope:
                    zmap[(i, j)] = (zoc_distance, zoc_p)
                    break
        if (i, j) == (x, y):
            kmap[(i, j)] = (0, None)
            return 
        if filter is not None and not filter(i, j):
            return
        min_steps = 100
        min_grid = None
        max_person = None
        for ap in self.around((i, j)):
            if ap not in fmap:
                fmap[ap] = 1
                self.connect_static(ap, (x, y), fmap, kmap, zmap, person, enable_zoc=enable_zoc, filter=filter)
            # 此处可能成环，需要加一个判断，即邻接点最短路径的上一个值不等于自己
            if ap in kmap and kmap[ap][0] < min_steps and kmap[ap][1] != (i, j):
                min_steps = kmap[ap][0]
                min_grid = ap
        if min_grid is not None:
            if enable_zoc and (i, j) in zmap and zmap[(i, j)][0] != sys.maxsize and \
               zmap[min_grid][0] >= zmap[(i, j)][0]:   
                steplen = zmap[(i, j)][1].zoc_value
            else:
                steplen = 1            
            kmap[(i, j)] = (min_steps + steplen, min_grid)
                
    def _connect_static(self, pta, ptb, fmap, kmap, zmap, person, enable_zoc=True, filter=None):
        """
        静态寻路算法，用于战斗中计算所有可移动格子
        """
        i, j = pta
        x, y = ptb
        # 自身格子不判断zoc，可以防止某些角色（如陈挺之）的zoc_scope > 1时，其他单位无法逃离zoc主体
        if (i, j) == (x, y):
            kmap[(i, j)] = (0, None, None)
            return 
        if enable_zoc and (i, j) in self.loc_entity:
            loc_p = self.loc_entity[(i, j)]
            if loc_p.group_ally & person.group_ally == 0:
                zmap[(i, j)] = (0, loc_p)
            #return
        if filter is not None and not filter(i, j):
            return
        all_connect = False
        all_in_map = True
        min_steps = 100
        min_grid = None
        need_zoc = False
        zoc_min = 100
        max_person = None
        for ap in self.around((i, j)):
            if ap in zmap:
                if zoc_min > zmap[ap][0]:
                    zoc_min = zmap[ap][0]
                if max_person is None or \
                   zmap[ap][1].zoc_value > max_person.zoc_value or \
                   zmap[ap][1].zoc_scope > max_person.zoc_scope:
                    max_person = zmap[ap][1]
            if ap not in fmap:
                fmap[ap] = 1
                self.connect_static(ap, (x, y), fmap, kmap, zmap, person, enable_zoc=enable_zoc, filter=filter)
            if ap in kmap:
                # all_connect = True
                # 此处可能成环，需要加一个判断，即邻接点最短路径的上一个值不等于自己
                if kmap[ap][0] < min_steps and kmap[ap][1] != (i, j):
                    all_connect = True
                    min_steps = kmap[ap][0]
                    min_grid = ap
            else:
                all_in_map = False
        #if zoc_min >= 0 and zoc_min < zoc_scope:
        #    zmap[(i, j)] = zoc_min + 1
        if max_person is not None and zoc_min >= 0 and zoc_min < max_person.zoc_scope:
            zmap[(i, j)] = (zoc_min + 1, max_person)
        if all_connect:
            if enable_zoc and (i, j) in zmap and zmap[(i, j)][0] > 0:             
                #kmap[(i, j)] = (max(person.motion - zmap[(i, j)] + 1, min_steps + 1), min_grid)
                #kmap[(i, j)] = (min_steps + zoc_scope + 1 - zmap[(i, j)], min_grid)
                #kmap[(i, j)] = (min_steps + 2, min_grid)
                kmap[(i, j)] = (min_steps + 1 + zmap[(i, j)][1].zoc_value, min_grid, max_person.name if max_person is not None else None)
            else:
                kmap[(i, j)] = (min_steps + 1, min_grid, max_person.name if max_person is not None else None)

    def connect_dynamic(self, pta, ptb, p, last=None, steps=-1):
        """
        动态寻路算法，用于大地图NPC即时行动
        """
        path = {}
        cachelist = []
        cachekey = set()
        if last is not None:
            path[last] = None
        path[pta] = last
        tmppt = pta
        step = 0
        while tmppt != ptb and step != steps:
            tmp_block = False
            for ap in self.around(tmppt):
                if ap in self.loc_entity:
                    tmp_block = True
                if (ap, ptb) in self.pathblocked or ap in path:
                    continue
                if not self.can_move(p, ap) and ap != ptb:
                    continue
                v = self.distance(ap, ptb) 
                if ap not in cachekey:
                    ist = len(cachelist)
                    for idx, itm in enumerate(cachelist):
                        if v >= itm[1]:
                            ist = idx
                            break
                    cachelist.insert(ist, (ap, v, step))
                    cachekey.add(ap)
                path[ap] = tmppt
            # 若被人堵住则原地等待
            if len(cachelist) == 0 and tmp_block:
                cachelist.append((tmppt, self.distance(tmppt, ptb), step))
                path[tmppt] = tmppt
            # 若是死路则跳出循环，开始反向寻路
            elif len(cachelist) == 0:
                self.pathblocked.add((tmppt, ptb))
                break
            # 若有可尝试的路径，则选出评分最高的一条继续前进
            cpop = cachelist.pop()
            tmppt = cpop[0]
            step = cpop[2] + 1
        ret = []
        idx = 0
        while (steps < 0 and tmppt is not None) or (steps > 0 and idx <= step):
            ret.append(tmppt)
            tmppt = path[tmppt]
            idx += 1
        if steps > step and tmppt is not None:
            ret = self.connect_dynamic(ret[0], ptb, p, last=None, steps=(steps - step)) + ret[1:]
        return ret

    def _direction(self, pta, ptb):
        x, y = pta
        i, j = ptb
        of_x, of_y = self.offset_xy(x, y)
        of_i, of_j = self.offset_xy(i, j)
        tmp_i = of_i - of_x
        tmp_j = of_j - of_y
        # 右
        if tmp_j == 0 and tmp_i >= 0:
            # return 1
            return 0
        # 左
        if tmp_j == 0 and tmp_i < 0:
            # return -1
            return 3
        # 右下
        if tmp_j > 0 and tmp_i >= 0:
            #return 2
            return 1
        # 左下
        if tmp_j > 0 and tmp_i < 0:
            # return 4
            return 2
        # 右上
        if tmp_j < 0 and tmp_i >= 0:
            # return -4
            return 5
        # 左上
        if tmp_j < 0 and tmp_i < 0:
            #return -2
            return 4

    def direction(self, pta, ptb):
        angle = self.angle(pta, (pta[0] + 1, pta[1]), ptb)
        direction = int(((angle + 13 * math.pi / 6) * 3 // math.pi ) % 6)
        return direction

    def _sector(self, pta, ptb, r, angle):
        x, y = pta
        i, j = ptb
        r = 4
        of_x, of_y = self.offset_xy(x, y)
        of_i, of_j = self.offset_xy(i, j) 
        ret = []
        new_start = None
        k = angle * 3 / math.pi
        for s in range(r):
            idx = 1
            a =  angle / (s * k + k)
            new_x, new_y = of_i + s * (of_i - of_x), of_j + s * (of_j - of_y)
            ret.append(self.normal_xy(new_x, new_y))
            new_x, new_y = self.offset_xy(ret[-1][0], ret[-1][1])
            tmp_i = new_x - of_x
            tmp_j = new_y - of_y
            while idx <= s * k + k:
                rangle = idx * a
                ret.append(self.normal_xy(tmp_i * math.cos(rangle) - tmp_j * math.sin(rangle) + of_x,
                                          tmp_i * math.sin(rangle) + tmp_j * math.cos(rangle) + of_y))
                idx += 1
        return ret

    def sector(self, pta, ptb, r, angle, mr=1, filter=None, block=0, allow_object=False):
        """
        使用余弦定理来求扇形格子
        因为浮点数运算精度的问题，有较小概率出现数据误差较大的情况
        添加了修正值，在现有地图大小应该不会出问题
        """
        x, y = pta
        i, j = ptb
        angle_map = {}
        distance_map = {}
        ret = []
        a_angle = angle + math.pi / 180
        blk_list = []
        #for a in range(-1, self.x + 1):
        #    for b in range(self.y):
        for (a, b) in self.range_grids(pta, r, x_overbolder=True):
            if not self.in_range((a, b), (x, y), r):
                continue
            if a == -1 and b % 2 == 0:
                continue
            if a == self.x and b % 2 == 1:
                continue
            d = self.distance((a, b), (x, y))
            distance_map[(a, b)] = d
            if d > r or d < mr:
                continue
            if (a, b) != (x, y):
                e = self.angle((x, y), (i, j), (a, b))
            else:
                e = 0
            angle_map[(a, b)] = e
            if e <= a_angle:
                filter_pass = filter is None or filter(a, b)
                if block and not (a in (-1, self.x) or self.xy[a][b].object is None):
                    blk_list.append((e - math.pi / 180, d))
                #elif (a in (-1, self.x) or self.xy[a][b].can_attack()) and filter_pass:
                elif (a in (-1, self.x) or (allow_object or self.xy[a][b].object is None)) and filter_pass:
                    ret.append((a, b))
        if block != 0 and len(blk_list) > 0:
            tmpret = []
            blk_list.sort(key=lambda x: x[0])
            for pt in ret:
                min_d = r
                for blk in blk_list:
                    if blk[1] < min_d:
                        min_d = blk[1]
                    if block == 1 and angle_map[pt] >= blk[0] and distance_map[pt] >= min_d:
                        tmpret.append(pt) 
                        break
                    elif block == 2 and angle_map[pt] - math.pi / 180  == blk[0] and distance_map[pt] >= blk[1]:
                        tmpret.append(pt)
                        break
            for pt in tmpret:
                ret.remove(pt)
        return ret

    def shape_scope(self, pt, shape):
        x, y = pt
        if shape.style == Shape.Around and shape.block != 1:
            return [(-1, -1)]
        else:
            block = 0 if shape.block == 0 else 2
            ret = self.sector((x, y), (x + 1, y), shape.scope, math.pi * 2, mr=shape.msputter, block=block)
            return ret

    def shape(self, pta, ptb, shape):
        x, y = pta
        i, j = ptb
        of_x, of_y = self.offset_xy(x, y)
        of_i, of_j = self.offset_xy(i, j)
        if shape.style == Shape.Point:
            #return self.circle((i, j), shape.sputter)
            return self.sector((i, j), (i + 1, j), shape.sputter, math.pi * 2, mr=0, block=shape.block)
        elif shape.style == Shape.Line:
            #ret = []
            #for s in range(shape.sputter):
            #    ret.append(self.normal_xy(of_i + s * (of_i - of_x), of_j + s * (of_j - of_y)))
            #return ret
            return self.sector((x, y), (i, j), shape.sputter, math.pi / 180, mr=shape.msputter, block=shape.block)
        elif shape.style == Shape.BigSector:
            return self.sector((x, y), (i, j), shape.sputter, math.pi * 2 / 3, mr=shape.msputter, block=shape.block)
        elif shape.style == Shape.SmallSector:
            return self.sector((x, y), (i, j), shape.sputter, math.pi / 3, mr=shape.msputter, block=shape.block)
        elif shape.style == shape.Around:
            return self.sector((x, y), (i, j), shape.sputter, math.pi * 2, mr=shape.msputter, block=shape.block)
        #elif shape.style == Shape.Around:
        #    return self.circle((x, y), shape.sputter, mr=shape.msputter)

    def circle(self, pt, r, mr=1, filter=None, allow_object=False):
        x, y = pt
        ret = self.sector((x, y), (x + 1, y), r, math.pi *2, 
                          mr=mr, filter=filter, allow_object=allow_object)
        return ret

    def vector(self, pta, ptb):
        x1, y1 = pta
        x2, y2 = ptb
        of_x1, of_y1 = self.offset_xy(x1, y1)
        of_x2, of_y2 = self.offset_xy(x2, y2)
        return (of_x2 - of_x1, of_y2 - of_y1)

    def distance(self, pta, ptb, precision=8):
        x1, y1 = pta
        x2, y2 = ptb
        of_x1, of_y1 = self.offset_xy(x1, y1)
        of_x2, of_y2 = self.offset_xy(x2, y2)
        return int(math.ceil(round(math.sqrt(math.pow(of_x2 - of_x1, 2) + math.pow(of_y2 - of_y1, 2)), precision)))

    def angle(self, pta, ptb, ptc, precision=8):
        x, y = pta
        i, j = ptb
        a, b = ptc
        of_x, of_y = self.offset_xy(x, y)
        of_a, of_b = self.offset_xy(a, b)
        of_i, of_j = self.offset_xy(i, j)
        vector_a = (of_i - of_x, of_j - of_y)
        vector_b = (of_a - of_x, of_b - of_y)
        vlength = lambda x: math.sqrt(x[0] * x[0] + x[1] * x[1])
        vdot = lambda x, y: x[0] * y[0] + x[1] * y[1]
        costh = vdot(vector_a, vector_b) / (vlength(vector_a) * vlength(vector_b))
        #costh = round(costh, precision)
        costh = max(min(costh, 1), -1)
        if round(vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0], precision) < 0:
            ret = 2 * math.pi - math.acos(costh)
        else:
            ret = math.acos(costh)
        if ret >= math.pi * 2:
            ret -= math.pi * 2
        return round(ret, precision)

    def locate(self, p, pt):
        x, y = pt
        self.remove(p)
        self.entity_loc[p.id] = (x, y)
        self.loc_entity[(x, y)] = p
        
    def remove(self, p):
        if p.id in self.entity_loc:
            ploc = self.entity_loc.pop(p.id)
            self.loc_entity.pop(ploc)

    def location(self, p):
        return self.entity_loc[p.id]
        
    def in_range(self, pt, center, range):
        x_pt, y_pt = pt
        x_center, y_center = center
        return abs(x_center - x_pt) <= range and abs(y_center - y_pt) <= range

    def range_grids(self, pt, r, x_overbolder=False):
        x, y = pt
        ret = []
        x_lower = max(-1 if x_overbolder else 0, x - r)
        x_upper = min(self.x + 1 if x_overbolder else self.x, x + r + 1)
        y_lower = max(0, y - r)
        y_upper = min(self.y, y + r + 1)
        for i in range(x_lower, x_upper):
            for j in range(y_lower, y_upper):
                ret.append((i, j))
        return ret

    def move_scope(self, p, motion=None, enable_zoc=True, style="move"):
        loc = self.location(p)
        if motion is None:
            real_motion = p.motion
        else:
            real_motion = motion
        #if style == "move":
        #    filter = lambda x, y: self.in_range((x, y), loc, real_motion) and self.xy[x][y].can_move(p)
        #elif style == "fly" or style == "flydown":
        #    filter = lambda x, y: self.in_range((x, y), loc, real_motion) and self.xy[x][y].can_attack()
        filter = lambda x, y: self.in_range((x, y), loc, real_motion) and self.can_move(p, (x, y))
        #t1 = time.time()
        kmap = self.connectivity(loc, p, r=real_motion, enable_zoc=enable_zoc, filter=filter)
        #t2 = time.time()
        #print("connect: %s" % (t2 - t1))
        allinscope = []
        for (i, j) in self.range_grids(loc, real_motion):
                pts = (i, j)
                if pts not in kmap:
                    continue

                # 注掉的那一行为判断走完当前格行动力为负则不能走，这样一来ZOC
                # 机制有点严格，故改成判断走完上一格还剩余行动力，则这
                # 一格也可以走到

                #if kmap[pts][0] <= real_motion and pts != loc:
                if pts != loc and kmap[kmap[pts][1]][0] < real_motion:
                    #if style == "fly":
                    #    allinscope.append(pts)
                    #elif self.xy[i][j].can_move(p):
                    if self.can_stay(p, (i, j)):
                        allinscope.append(pts)
        return allinscope, kmap

    def move_trace(self, tgt, loc, kmap):
        current = tgt
        ret = []
        while True:
            c = kmap.get(current, None)
            if c is None or c[1] is None:
                break
            if c[1] in ret:
                print ("如果看到这行字，请截图发给我，因为怀疑此处有个bug但出现概率很低")
                print (ret)
                break
            ret.append(current)
            current = c[1]
        ret.append(loc)
        return ret


if __name__ == "__main__":
    #from proj.console.termcolor import colored
    #
    #a = colored("白老师", color="red") + colored("(9, 9)", color="cyan", attrs=["bold"])
    # print length(a)
    #m = Map()
    # print m.distance((1, 7), (0, 5))
    # print m.angle((1, 7), (1, 6), (0, 5))
    # print m.distance((1, 7), (7, 5))
    
    #m = Map(x=100, y=100)
    #t1 = time.time()
    #startpt = (0, 0)
    #last = None
    #while startpt != (99, 99):
    #    rst = m.connect_dynamic(startpt, (99, 99), None, last=last, steps=1)
    #    print(rst)
    #    startpt = rst[0]
    #    last = rst[1]
    #t2 = time.time()
    ##print(rst)
    #print("Time used: %s" % (t2 - t1)) 
    m = Map()
    print(m.angle((3, 3), (4, 3), (1, 4)))
