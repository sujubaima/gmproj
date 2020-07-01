# -- code: utf-8 --
import json

from proj.engine import Event
from proj.entity import Entity
from proj.entity import Person


equip_pos = ["MainHand", "ViceHand", "Body", "Ounament"]
save_attrs = ["id", "firstname", "lastname", "showname", "title", "sex",
              "dongjing", "gangrou", "zhipu", "neigong",
              "boji", "jianfa", "daofa", "changbing", "qimen", "anqi",
              "criticaltxt", "conversation"]
ability_attrs = ["hp_max", "mp_max", "attack", "defense", "motion",
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
    ret = {"persons": {}, "teams": {}, "events": {}}
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


def load():
    pass
