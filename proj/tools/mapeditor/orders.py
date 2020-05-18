# -- coding: utf-8 --

from proj.engine import Order
from proj.engine import Message as MSG

from proj.entity import Terran
from proj.entity import MapGrid
from proj.entity import Person
from proj.entity import Team


class MapEditorOrder(Order):

    def intialize(self):
        self.real_coordinates = False
        self.show_coordinates = False

    def carry(self):
        MSG(style="map_editor", map=self.map, 
            show_coordinates=self.show_coordinates, real_coordinates=self.real_coordinates)


class ThumbnailOrder(Order):

    def carry(self):
        MSG(style="map_thumbnail", map=self.map).callback = self.callback

    def callback(self, ret):
        MapEditorOrder(map=self.map)

        
class CameraOrder(Order):

    def carry(self):
        MSG(style="map_camera", map=self.map).callback = self.callback
        
    def callback(self, pos):
        if pos is not None:
            self.map.window_center(pos)
        MapEditorOrder(map=self.map)
        

class PersonOrder(Order):

    def carry(self):
        MSG(style="map_person", map=self.map).callback = self.callback
        
    def callback(self, person_loc):
        if person_loc is not None:
            ptpl, loclist = person_loc
            person = Person.one(ptpl)
            if person.team is None:
                person.team = Team()
                person.team.include(person)
            ent = person.team
            for loc in loclist:
                old_ent = self.map.loc_entity.get(loc, None)
                if old_ent is not None:
                    old_ent.include(person)
                else:
                    self.map.loc_entity[loc] = ent
                    self.map.entity_loc[ent.id] = loc
        MapEditorOrder(map=self.map)
    
    
class TerranOrder(Order):
    
    def carry(self):
        MSG(style="map_terran", map=self.map).callback = self.callback
        
    def callback(self, poslist):
        if poslist is not None:
            for pos in poslist:
                self.map.xy[pos[0]][pos[1]].terran = self.terran
            MapEditorOrder(map=self.map)
        else:
            MapEditorOrder(map=self.map)
 
  
class EntityOrder(Order):

    def carry(self):
        MSG(style="map_entity", map=self.map).callback = self.callback
        
    def callback(self, poslist):
        if poslist is not None:
            for pos in poslist:
                self.map.xy[pos[0]][pos[1]].object = self.entity
                self.map.xy[pos[0]][pos[1]].showword = self.name
            MapEditorOrder(map=self.map)
        else:
            MapEditorOrder(map=self.map)


class EntityNameOrder(Order):

    def carry(self):
        MSG(style="map_entity_name").callback = self.callback

    def callback(self, name):
        if name is not None:
            EntityOrder(map=self.map, name=name, entity=self.entity)
        else:
            MapEditorOrder(map=self.map)


class EraseOrder(Order):
 
    def carry(self):
        MSG(style="map_erase", map=self.map).callback = self.callback
        
    def callback(self, poslist):
        if poslist is not None:
            for pos in poslist:
                self.map.xy[pos[0]][pos[1]].object = None
                self.map.xy[pos[0]][pos[1]].terran = Terran.one("TERRAN_BLANK")
                self.map.xy[pos[0]][pos[1]].showword = None
                if pos in self.map.loc_entity:
                    entity = self.map.loc_entity.pop(pos)
                    self.map.entity_loc.pop(entity.id)
            MapEditorOrder(map=self.map)
        else:
            MapEditorOrder(map=self.map)
            
            
class ResizeOrder(Order):

    def initialize(self):
        self.translation = True

    def carry(self):
        MSG(style="map_resize", map=self.map).callback = self.callback
        
    def callback(self, step):
        step = int(step)
        new_width = self.map.x
        new_height = self.map.y
        if self.axis == "x":
            new_width += self.factor * step
        if self.axis == "y":
            new_height += self.factor * step
        if self.translation:
            trans = self.factor * step
        else:
            trans = 0
        new_grids = []
        for i in range(new_width):
            new_grids.append([])
            for j in range(new_height):
                new_grids[i].append(None)
        for i in range(new_width):
            new_grids.append([])
            for j in range(new_height):
                tmp_x = i
                tmp_y = j
                if self.axis == "y":
                    tmp_y -= trans
                if self.axis == "x":
                    tmp_x -= trans
                if tmp_x >= 0 and tmp_x < self.map.x and tmp_y >=0 and tmp_y < self.map.y:
                    new_grids[i][j] = self.map.xy[tmp_x][tmp_y]
                else:
                    new_grids[i][j] = MapGrid()
        self.map.xy = new_grids
        self.map.x = new_width
        self.map.y = new_height
        for k, v in self.map.entity_loc.items():
            person = self.map.loc_entity[v]
            self.map.loc_entity.pop(v)
            if self.axis == "x":
                new_v = (v[0] + trans, v[1])
            if self.axis == "y":
                new_v = (v[0], v[1] + trans)
            self.map.entity_loc[k] = new_v
            self.map.loc_entity[new_v] = person
        self.map.window_x = min(self.map.window_x, self.map.x)
        self.map.window_y = min(self.map.window_y, self.map.y)
        self.map.window_start_x = min(self.map.window_start_x, self.map.x - self.map.window_x)
        self.map.window_start_y = min(self.map.window_start_y, self.map.y - self.map.window_y)
        print(self.map.window_y, self.map.window_start_y, self.map.y)
        MapEditorOrder(map=self.map)
            
class SaveOrder(Order):
    def carry(self):
        MSG(style="map_save", map=self.map).callback = self.callback
        
    def callback(self, ret):
        MapEditorOrder(map=self.map)     
