# -- coding: utf-8 --

import importlib
import math

from proj import data

from proj.entity import Force
from proj.entity import Person


PLAYER = None

teams = {}

battles = {}

map = None

strdict = {}

tasks_status = {}
tasks_index = []
tasks = {}

attitudes = {"force": {}, "person": {}}
discoveries = {}

script_status = {}
script_branches = {}

timestamp = 0
timestamp_ = 0
time_delta_ = 0

variables = {}

explorations = {}

guide_dest = None
guide = None


def timeflow(duration):
    global time_delta_, timestamp
    time_delta_ = duration
    timestamp += duration


def duration():
    global time_delta_
    return time_delta_


def executed(script, label):
    global script_status
    if script not in script_status:
        script_status[script] = set()
    script_status[script].add(label)


def relay_init(enttype, enta, entb):
    if enttype == "force":
        return 50
    else:
        atd_ceil = min(100, int(10 + relationship("force", enta.force, entb.force)))
        diff = (enta.dongjing - entb.dongjing,
                enta.gangrou - entb.gangrou,
                enta.zhipu - entb.zhipu)
        diff_dis = diff[0] * diff[0] + diff[1] * diff[1] + diff[2] * diff[2]
        print(diff_dis)
        diff_rate = math.sqrt(diff_dis / 30000)
        return int(atd_ceil - (atd_ceil / 2) * diff_rate) 
    

def relationship(enttype, enta, entb, val=None):
    entdict = attitudes[enttype]
    if enta.id not in entdict:
        entdict[enta.id] = {}
    if entb.id not in entdict[enta.id]:
        entdict[enta.id][entb.id] = relay_init(enttype, enta, entb)
    if val is None:
        return entdict[enta.id][entb.id]
    else:
        entdict[enta.id][entb.id] += val


#def relationship(enta, entb):
#    if enta.leader.tpl_id == "PERSON_ZHAO_SHENJI" and \
#       entb.leader.tpl_id == "PERSON_YANG_LEI":
#        return 10
#    if enta.leader.tpl_id == "PERSON_YANG_LEI" and \
#       entb.leader.tpl_id == "PERSON_ZHAO_SHENJI":
#        return 10
#    return 50


def load_discoveries():
    for d in dir(data.discovery):
        if not d.startswith("DISCOVERY"):
            continue 
        obj = getattr(data.discovery, d)
        tool_tag = obj.get("tools", None)
        for idx, plc in enumerate(obj["places"]):
            scenario = plc.get("scenario", "ALL")
            if scenario not in discoveries:
                discoveries[scenario] = []
            newdis = {"id": "%s,PLACE-%s" % (d, idx), "item": obj["item"]}
            if tool_tag is not None:
               newdis["tools"] = set(tool_tag.split(","))
            if "terrans" in plc:
                newdis["terrans"] = plc["terrans"]
            if "locations" in plc:
                newdis["locations"] = set(map(lambda x: eval(x), plc["locations"]))
            if "rate" in plc:
                newdis["rate"] = plc["rate"]
            if "quantity" in plc:
                newdis["quantity"] = plc["quantity"]
            if "range" in plc:
                newdis["range"] = plc["range"]
            if "refresh" in plc:
                newdis["refresh"] = plc["refresh"]
            discoveries[scenario].append(newdis)


def load_attitudes():
    for f in dir(data.force):
        if not f.startswith("FORCE"):
            continue
        obj = getattr(data.force, f)
        fsu = Force.one(f)
        for k, v in obj["relationship"].items():
            fob = Force.one(k) 
            relationship("force", fsu, fob, v - 50)


def load_strdict():
    for p in dir(data.person):
        if not p.startswith("PERSON"):
            continue
        pen = Person.one(p)
        strdict["%s_NAME" % pen.tpl_id] = pen.name
        

def init():
    load_strdict()
    load_attitudes()
    load_discoveries()
