# -- code: utf-8 --

import json

from proj.engine import Event
from proj.entity import Entity
from proj.entity import Person
from proj.entity import Team
from proj.entity import Map
from proj.entity import Battle

from proj.runtime import context


equip_pos = ["MainHand", "ViceHand", "Body", "Ounament"]

save_attrs = ["id", "tpl_id", "firstname", "lastname", "showname", "title", "sex",
              "hp", "mp", "injury", "wound", "hp_poison", "mp_poison", "process",
              "dongjing", "gangrou", "zhipu", "neigong",
              "boji", "jianfa", "daofa", "changbing", "qimen", "anqi",
              "criticaltxt", "conversation", "stash"]

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
    t_info["process"] = t.process
    t_info["active"] = t.id in context.teams
    if t.battle is not None:
        t_info["battle"] = t.battle.id
    return t_info


def battle_info(b):
    b_info = {}
    b_info["id"] = b.id
    b_info["silent"] = b.silent
    b_info["death"] = b.death
    b_info["alive"] = [p.id for p in b.alive]
    b_info["dead"] = [p.id for p in b.dead]
    b_info["turnidx"] = b.turnidx
    b_info["groups"] = []
    for group in b.groups:
        b_info["groups"].append([p.id for p in group])
    b_info["allies"] = b.allies
    b_info["map"] = b.map.tpl_id
    b_info["cdmap"] = b.cdmap
    return b_info


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
        if eq is not None:
            p_dict["equipment"].append({"id": eq.tpl_id, "position": equip_pos[idx]})
    p_dict["items"] = [] 
    tmp_set = set()
    for itm in p.items:
        if "Equip" in itm.tags:
            p_dict["items"].append({"id": itm.tpl_id, "quantity": 1, 
                                    "durability": itm.durability_current})
        elif itm.tpl_id not in tmp_set:
            p_dict["items"].append({"id": itm.tpl_id, "quantity": p.quantities[itm.tpl_id]})
            tmp_set.add(itm.tpl_id)
    p_dict["status"] = []
    for sts in p.status:
        if sts.exertor != p:
            sts_dict = {"id": sts.tpl_id, "name": sts.name, "turns": sts.leftturn}
            if sts.source is not None:
                sts_dict["source"] = sts.source.tpl_id
            if sts.exertor is not None:
                sts_dict["exertor"] = sts.exertor.id
            p_dict["status"].append(sts_dict)
    return p_dict


def save(filepath):
    ret = {"timestamp": context.timestamp, 
           "persons": {}, 
           "teams": {}, 
           "events": {},
           "battles": {},
           "discoveries": context.explorations,
           "script_status": context.script_status,
           "script_branches": context.script_branches}
    team_dict = {}
    for entity in Entity.Instances.values():
        if not isinstance(entity, Person):
           continue
        e_info = person_info(entity)
        if e_info is not None:
            ret["persons"][entity.id] = e_info
        if entity.team is not None and entity.team.id not in team_dict:
            team_dict[entity.team.id] = entity.team
    battle_dict = {}
    for entity in team_dict.values():
        e_info = team_info(entity)
        if e_info is not None:
            ret["teams"][entity.id] = e_info
        if entity.battle is not None and entity.battle.id not in battle_dict:
            battle_dict[entity.battle.id] = entity.battle 
    for entity in battle_dict.values():
        e_info = battle_info(entity)
        if e_info is not None:
            ret["battles"][entity.id] = e_info
    for event in Event.All.values():
        ret["events"][event.id] = {"triggered": event.triggered,
                                   "active": event.active} 
    with open(filepath, "w") as fd:
        fd.write(json.dumps(ret, indent=4))


def clean_persons():
    for k in list(Entity.Instances.keys()):
        entity = Entity.Instances[k]
        if not isinstance(entity, Person):
           continue
        if entity.team is None:
           continue
        if entity.team.scenario is not None:
           entity.team.scenario.remove(entity.team)
           entity.team.scenario = None
        entity.team is None
        Entity.Instances.pop(k)
    for k in list(Entity.Templates.keys()):
        if len(Entity.Templates[k]) > 0 and \
           not isinstance(Entity.Templates[k][0], Person):
            continue
        Entity.Templates.pop(k)
    context.teams = {}


def load(filepath):
    with open(filepath) as fd:
        ret = json.loads(fd.read())
    context.timestamp = ret["timestamp"]
    context.timestamp_ = ret["timestamp"]
    context.explorations = ret["discoveries"]
    context.script_status = ret["script_status"]
    context.script_branches = ret["script_branches"]
    for k, evt in ret["events"].items():
        Event.All[k].triggered = evt["triggered"]
        Event.All[k].active = evt["active"]
    clean_persons()
    for k, p_info in ret["persons"].items():
        tpl_id = p_info["tpl_id"]
        if tpl_id not in Entity.Templates:
            Entity.Templates[tpl_id] = []
        if len(Entity.Templates[tpl_id]) == 0:
            obj = Person()
            obj.load(**p_info)
            Entity.Templates[tpl_id].append(obj)
            Entity.Instances[obj.id] = obj
    battle_dict = {}
    for k, b_info in ret["battles"].items():
        map = Map.template(b_info["map"])
        groups = []
        for group in b_info["groups"]:
            groups.append([Entity.Instances[pid] for pid in group])
        allies = b_info["allies"]
        death = b_info["death"]
        silent = b_info["silent"]
        battle = Battle(map=map, groups=groups, allies=allies, silent=silent, death=death)
        battle.turnidx = b_info["turnidx"]
        battle.cdmap = b_info["cdmap"]
        battle.alive = [Entity.Instances[pid] for pid in b_info["alive"]]
        battle.dead = [Entity.Instances[pid] for pid in b_info["dead"]]
        battle_dict[b_info["id"]] = battle
    for k, t_info in ret["teams"].items():
        team = Team()
        team.id = t_info["id"]  
        team.process = t_info["process"]
        for pid in t_info["members"]:
            team.include(Entity.Instances[pid])
        if t_info["active"]:
            context.teams[team.id] = team
        if "battle" in t_info:
            team.battle = battle_dict[t_info["battle"]]
        team.scenario = Map.one(t_info["scenario"])
        team.scenario.locate(team, t_info["location"])
    p = Person.one("PERSON_YANG_LEI")
    m = Map.one("MAP_WORLD")
    context.PLAYER = Person.one("PERSON_PLAYER")
