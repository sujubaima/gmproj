# -- code: utf-8 --

import json

from proj.engine import Event
from proj.entity import Entity
from proj.entity import Person

from proj.runtime import context


equip_pos = ["MainHand", "ViceHand", "Body", "Ounament"]
save_attrs = ["id", "tpl_id", "firstname", "lastname", "showname", "title", "sex",
              "hp", "mp", "injury", "wound", "hp_poison", "mp_poison",
              "dongjing", "gangrou", "zhipu", "neigong",
              "boji", "jianfa", "daofa", "changbing", "qimen", "anqi",
              "criticaltxt", "conversation"]
ability_attrs = ["hp_max", "mp_max", "attack", "defense", "motion", "speed", "exp",
                 "hit_rate", "counter_rate", "dodge_rate", "critical_rate", "anti_damage_rate"]


def team_info(t):
    t_info = {}
    if len(t.members) == 0 or t.scenario is None:
        return None 
    t_info["id"] = t.id
    t_info["members"] = [p.id for p in t.members]
    t_info["scenario"] = t.scenario.tpl_id
    t_info["location"] = t.scenario.location(t)
    return t_info


def person_info(p):
    p_dict = {}
    for attr in save_attrs:
        attr_value = getattr(p, attr)
        if attr_value is not None:
            p_dict[attr] = attr_value
    for attr in ability_attrs:
        p_dict[attr] = getattr(p, attr + "_") 
    p_dict["superskills"] = []
    tmp_dict = {}
    for sknode in p.learned:
        sk, node = sknode.split("-")
        if sk not in tmp_dict:
            tmp_dict[sk] = []
        tmp_dict[sk].append(int(node))
    for k, v in tmp_dict.items():
        v.sort()
        p_dict["superskills"].append({"id": k, "learn": v})
    if p.running is not None:
        p_dict["running"] = {"id": p.running.tpl_id}
    if p.skill_counter is not None:
        p_dict["skill_counter"] = {"id": p.skill_counter.tpl_id}
    if p.studying is not None:
        p_dict["studying"] = {"id": p.studying.id}
    p_dict["equipment"] = []
    for idx, eq in enumerate(p.equipment):
        if eq is None:
            continue
        p_dict["equipment"].append({"id": eq.tpl_id, "position": equip_pos[idx]})
    p_dict["items"] = [] 
    tmp_set = set()
    for itm in p.items:
        if "Equip" in itm.tags:
            p_dict["items"].append({"id": itm.tpl_id, "quantity": 1, "durability": itm.durability_current})
        elif itm.tpl_id not in tmp_set:
            p_dict["items"].append({"id": itm.tpl_id, "quantity": p.quantities[itm.tpl_id]})
            tmp_set.add(itm.tpl_id)
    return p_dict


def save(filepath=None):
    ret = {"timestamp": context.timestamp, 
           "persons": {}, 
           "teams": {}, 
           "events": {},
           "discoveries": context.explorations}
    team_dict = {}
    for entity in Entity.Instances.values():
        if not isinstance(entity, Person):
           continue
        e_info = person_info(entity)
        if e_info is not None:
            ret["persons"][entity.id] = e_info
        if entity.team is not None and entity.team.id not in team_dict:
            team_dict[entity.team.id] = entity.team
    for entity in team_dict.values():
        e_info = team_info(entity)
        if e_info is not None:
            ret["teams"][entity.id] = e_info
    for event in Event.All.values():
        ret["events"][event.id] = {"triggered": event.triggered,
                                   "active": event.active} 
    if filepath is None:
        return
    with open(filepath, "w") as fd:
        fd.write(json.dumps(ret))
    #print(json.dumps(ret["events"]))


def clean_persons():
    for k in Entity.Instances:
        entity = Entity.Instances[k]
        if not isinstance(entity, Person):
           continue
        if entity.team is None:
           continue
        if entity.team.scenario is not None:
           entity.team.scenatio.remove(entity.team)
           entity.team.scenario = None
        entity.team is None
        Entity.Instances.pop(k)
    for k in Entity.Templates:
        if len(Entity.Templates[k]) > 0 and \
           not isinstance(Entity.Templates[k][0], Person):
            continue
        Entity.Templates.pop(k)


def load(filepath=None):
    if filepath is None:
        return
    with open(filepath) as fd:
        ret = json.loads(fd.read())
    context.timestamp = ret["timestamp"]
    context.timestamp_ = ret["timestamp"]
    context.explorations = ret["discoveries"]
    for k, evt in ret["events"].items():
        Event.All[k].triggered = evt["triggered"]
        Event.All[k].active = evt["active"]
    for k in Entity.Templates:
        if len(Entity.Templates[k]) > 0 and \
           not isinstance(Entity.Templates[k][0], Person):
            continue
        Entity.Templates.pop(k)
    for k, p_info in ret["persons"]:
        tpl_id = p_info["tpl_id"]
        if tpl_id not in Entity.Templates:
            Entity.Templates[tpl_id] = []
        if len(Entity.Templates[tpl_id]) == 0:
            obj = Person()
            obj.load(**p_info)
            Entity.Templates[tpl_id].append(obj)
            Entity.Instances[obj.id] = obj
        return Entity.Templates[tpl_id][0]
    for k, t_info in ret["teams"]:
        team = Team()
        team.id = t_info["id"]  
        team.scenario = Map.one(t_info["scenario"])
        team.scenario.locate(team, t_info["location"])
        for pid in t_info["members"]:
            team.include(Entity.All[pid])
