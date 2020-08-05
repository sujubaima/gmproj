# -- coding: utf-8 --

from proj.engine import Control
from proj.engine import Message as MSG

from proj.entity import Terran
from proj.entity import Element
from proj.entity import MapGrid
from proj.entity import Person
from proj.entity import Team

from proj.console.controls import ThumbnailControl


class MapEditorControl(Control):

    def intialize(self):
        super(MapEditorControl, self).initialize()
        self.real_coordinates = False
        self.show_coordinates = False

    def launch(self):
        MSG(style="map_editor_control", control=self)

    @Control.listener
    def terran(self, arg):
        control = TerranControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def element(self, arg):
        control = ElementControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def person(self, arg):
        control = PersonControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def erase(self, arg):
        control = EraseControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def thumbnail(self, arg):
        control = ThumbnailControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def camera(self, arg):
        control = CameraControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def coordinate(self, arg):
        self.real_coordinates = True
        self.show_coordinates = True
        self.launch()

    @Control.listener
    def resize(self, arg):
        control = ResizeControl(map=self.map)
        control.run()
        self.launch()

    @Control.listener
    def save(self, arg):
        control = SaveControl(map=self.map)
        control.run()
        self.launch()


class ThumbnailControl(Control):

    def launch(self):
        MSG(style="map_thumbnail_control", control=self)

        
class CameraControl(Control):

    def launch(self):
        MSG(style="map_camera_control", control=self)
        
    @Control.listener
    def input(self, pos):
        if pos is not None:
            self.map.window_center(pos)
        self.close()
        

class PersonControl(Control):

    def launch(self):
        MSG(style="map_person_control", control=self)

    @Control.listener
    def input(self, person_loc):
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
        self.close()
    
    
class TerranControl(Control):
    
    def launch(self):
        MSG(style="map_terran_control", control=self)

    @Control.listener
    def select(self, terran):
        self.terran =Terran.one(terran)
       
    @Control.listener
    def input(self, poslist):
        if poslist is not None:
            for pos in poslist:
                self.map.xy[pos[0]][pos[1]].terran = self.terran
        self.close()
 
  
class ElementControl(Control):

    def launch(self):
        MSG(style="map_element_control", control=self)

    @Control.listener
    def elename(self, name):
        self.name = name

    @Control.listener
    def select(self, element):
        self.entity = Element.one(element)
        
    @Control.listener
    def input(self, poslist):
        if poslist is not None:
            for pos in poslist:
                self.map.xy[pos[0]][pos[1]].object = self.entity
                self.map.xy[pos[0]][pos[1]].showword = self.name
        self.close()


class EraseControl(Control):
 
    def launch(self):
        MSG(style="map_erase_control", control=self)
        
    @Control.listener
    def input(self, poslist):
        if poslist is not None:
            for pos in poslist:
                self.map.xy[pos[0]][pos[1]].object = None
                self.map.xy[pos[0]][pos[1]].terran = Terran.one("TERRAN_BLANK")
                self.map.xy[pos[0]][pos[1]].showword = None
                if pos in self.map.loc_entity:
                    entity = self.map.loc_entity.pop(pos)
                    self.map.entity_loc.pop(entity.id)
        self.close()
            
            
class ResizeControl(Control):

    def launch(self):
        MSG(style="map_resize_control", control=self)

    @Control.listener
    def select(self, opt):
        self.axis, self.factor, self.translation = opt
        
    @Control.listener
    def input(self, step):
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
        self.map.window_start_x = min(self.map.window_start_x, 
                                      self.map.x - self.map.window_x)
        self.map.window_start_y = min(self.map.window_start_y, 
                                      self.map.y - self.map.window_y)
        self.close()
           
 
class SaveControl(Control):

    def launch(self):
        MSG(style="map_save_control", control=self)
