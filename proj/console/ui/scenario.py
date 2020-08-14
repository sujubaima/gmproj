# -- coding: utf-8 --
from __future__ import division

import time

from proj import options

from proj.console.ui import common as ui
from proj.console import format as fmt

from proj.entity.map import Terran
from proj.entity.map import Map as EntityMap
from proj.entity.constants import BattleGroup
from proj.entity.constants import BattleEvent


GROUP_COLOR = {BattleGroup.Player: "cyan",
               BattleGroup.Friends: "cyan",
               BattleGroup.Enemies: "red",
               BattleGroup.Thirds: "magenta"}


GWIDTH = 18
GHEIGHT = 3

HOR = "-"

VER = "|"


class Map(ui.Interactive):
    """
    地图封装控件
    """

    def __init__(self, map, gwidth=None, gheight=None):
        self.map = map
        if gwidth is None:
            self.gwidth = GWIDTH
        else:
            self.gwidth = gwidth
        if gheight is None:
            self.gheight = GHEIGHT
        else:
            self.gheight = gheight

    def colorvision(self, pt):
        if pt.object is not None:
            return pt.object.character, pt.object.vision
        elif pt.terran is not None:
            return pt.terran.character, pt.terran.vision
        else:
            return " ", {}

    def render(self, entities=None, coordinates=None, show_trace=True):
        #t1 = time.time()
        if coordinates is None:
            coordinates = []
        if entities is None:
            entities = []
        entity_info = {}
        trace_info = []
        for p in entities:
            loc = self.map.point_to_window(p["location"])
            entity_info[loc] = p
            if p["trace"] is not None:
                trace_info.extend(p["trace"])
        grids = self.map.window()
        plines = []
        for j in range(self.map.window_y):
            plines.append(HOR * (self.gwidth // 2 + 1) + HOR * (self.map.window_x * (self.gwidth + 1) + 1))
            real_j = j + self.map.window_start_y
            if self.map.window_start_x > 0:
                bg_before, bg_before_color = self.colorvision(self.map.xy[self.map.window_start_x - 1][real_j])
            else:
                bg_before = " "
                bg_before_color = {}
            line_contents = []
            for idx in range(self.gheight):
                line_contents.append(ui.fixed((self.gwidth // 2 + 1) * (real_j % 2), bg=bg_before, **bg_before_color) + VER)
            for i in range(self.map.window_x):
                contents = []
                for idx in range(self.gheight):
                    contents.append("")
                g = grids[i][j]
                terran_char, terran_color = self.colorvision(g)
                real_coor = self.map.point_to_real((i, j))
                if show_trace and real_coor in trace_info:
                    contents[0] = ui.colored("(%s, %s)" % (i, j), color="blue", attrs=["bold"])
                for coor_info in coordinates:
                    if coor_info["positions"] is None or real_coor not in coor_info["positions"]:
                        continue
                    if coor_info.get("reality", False):
                        coor = real_coor
                    else:
                        coor = (i, j)
                    contents[0] += ui.colored("(%s, %s)" % coor, color=coor_info.get("color", "green"), attrs=["bold"])
                    #break
                if (i, j) in entity_info:
                    for idx in range(self.gheight):
                        contents[idx] += entity_info[(i, j)]["contents"][idx]
                elif g.object is not None:
                    contents[0] += ui.colored(g.title(), attrs=["bold"])
                elif real_coor in self.map.transport_locs:
                    if self.map.tpl_id == "MAP_WORLD":
                        showstr = EntityMap.one(self.map.transport_locs[real_coor]).name
                        contents[0] += ui.colored(showstr, attrs=["bold"])
                    else:
                        showstr = "前往" + EntityMap.one(self.map.transport_locs[real_coor]).name
                        contents[0] += ui.colored(showstr, color="grey", attrs=["bold"])
                for idx in range(self.gheight):
                    line_contents[idx] += ui.fixed(self.gwidth, n=contents[idx], bg=terran_char, **terran_color) + VER
            if self.map.window_start_x + self.map.window_x < self.map.x - 1:
                bg_before, bg_before_color = self.colorvision(self.map.xy[self.map.window_start_x + self.map.window_x][real_j])
            else:
                bg_before = " "
                bg_before_color = {}
            for idx in range(self.gheight):
                line_contents[idx] += ui.fixed((self.gwidth // 2 + 1) * ((real_j + 1) % 2), bg=bg_before, **bg_before_color)
            for l in line_contents:
                plines.append(l)
        plines.append(HOR * (self.gwidth // 2 + 1) + HOR * (self.map.window_x * (self.gwidth + 1) + 1))
        ui.echo(plines)
        #t2 = time.time()
        #print("Time used: %s" % (t2 - t1))

    def input(self):
        pass

    def handle(self, ac):
        pass


class MapThumbnail(ui.Interactive):

    def __init__(self, map):
        self.map = map
        self.gwidth = 2

    def colorvision(self, pt):
        if pt.object is not None:
            return pt.object.character, pt.object.vision
        elif pt.terran is not None:
            if pt.terran.thumbnail is not None:
                return pt.terran.thumbnail, pt.terran.vision
            else:
                return pt.terran.character, pt.terran.vision
        else:
            return " ", {}

    def _render(self, entities=None):
        t1 = time.time()
        if entities is None:
            entities = []
        entity_info = {}
        for p in entities:
            loc = p["location"]
            entity_info[loc] = p
        grids = self.map.xy
        plines = []
        for j in range(self.map.y):
            content_line = (self.gwidth // 2 + 1) * (j % 2) * " "
            for i in range(self.map.x):
                g = grids[i][j]
                content = ""
                terran_char, terran_color = self.colorvision(g)
                if len(content) == 0 and (i, j) in entity_info:
                    if not entity_info[(i, j)]["player"]:
                        content += ui.colored("P", color="cyan", attrs=["bold"])
                    else:
                        content += ui.colored("P", color="white", on_color="on_red", attrs=["bold"])
                elif len(content) == 0 and g.object is not None:
                    content += ui.colored(g.object.thumbnail, **g.object.vision)
                content_line += ui.fixed(self.gwidth, n=content, bg=terran_char, **terran_color)
            content_line += ui.fixed((self.gwidth // 2 + 1) * ((j + 1) % 2), bg=" ")
            plines.append(content_line)
        ui.echo(plines)
        #t2 = time.time()
        #print("Time used: %s" % (t2 - t1))

    def render(self, entities=None):
        """
        对略缩图渲染速率进行少量优化
        """
        #t1 = time.time()
        if entities is None:
            entities = []
        entity_info = {}
        for p in entities:
            loc = p["location"]
            entity_info[loc] = p
        grids = self.map.xy
        plines = []
        for j in range(self.map.y):
            content_line = (self.gwidth // 2) * (j % 2) * " "
            fix_count = 0
            last_g = None
            last_content = None
            for i in range(self.map.x):
                g = grids[i][j]
                content = ""
                if len(content) == 0 and (i, j) in entity_info:
                    if not entity_info[(i, j)]["player"]:
                        content += ui.colored("P", color="cyan", attrs=["bold"])
                    else:
                        content += ui.colored("P", on_color="on_red", attrs=["bold"])
                elif len(content) == 0 and g.object is not None:
                    content += ui.colored(g.object.thumbnail, **g.object.vision)
                elif (i, j) in self.map.transport_locs:
                    if self.map.transport_locs[(i, j)] == "MAP_WORLD":
                        content += ui.colored("出", on_color="on_cyan")
                    else:
                        content += ui.colored("场", on_color="on_cyan")
                if last_g is not None:
                    if content != last_content or g.object is not None or \
                       g.terran != last_g.terran or (i, j) in self.map.transport_locs:
                        terran_char, terran_color = self.colorvision(last_g)
                        content_line += ui.fixed(self.gwidth * fix_count, n=last_content, 
                                                 bg=terran_char, **terran_color)
                        fix_count = 0
                fix_count += 1
                last_g = g
                last_content = content
            terran_char, terran_color = self.colorvision(last_g)
            content_line += ui.fixed(self.gwidth * fix_count, n=last_content, 
                                     bg=terran_char, **terran_color)
            content_line += ui.fixed((self.gwidth // 2) * ((j + 1) % 2), bg=" ")
            plines.append(content_line)
        ui.echo(plines)
        #t2 = time.time()
        #print("Time used: %s" % (t2 - t1))


def map(map, gwidth=None, gheight=None, entities=None, coordinates=None, show_trace=True):
    m = Map(map, gwidth=gwidth, gheight=gheight)
    m.render(entities=entities, coordinates=coordinates,
             show_trace=show_trace)
    return m.done()


def thumbnail(map, entities=None):
    m = MapThumbnail(map)
    m.render(entities=entities)
    return m.done()
