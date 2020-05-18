# -- coding: utf-8 --

import importlib

from proj import data


PLAYER = None

teams = {}

battles = []

map = None

strdict = {}

tasks_status = {}
tasks_index = []
tasks = {}

attitudes = {}
discoveries = {}

conversation_status = {}

timestamp = 0
timestamp_ = 0
time_delta_ = 0

variables = {}


def timeflow(duration):
    global time_delta_, timestamp
    time_delta_ = duration
    timestamp += duration


def duration():
    global time_delta_
    return time_delta_


def spoken(conv, idx):
    global conversation_status
    if conv not in conversation_status:
        conversation_status[conv] = set()
    conversation_status[conv].add(idx)
    

def _relationship(enta, entb):
    if enta.id not in attitudes:
        attitudes[enta.id] = {}
    if entb.id not in attitudes[enta.id]:
        attitudes[enta.id][entb.id] = 50
    return attitudes[enta.id][entb.id]


def relationship(enta, entb):
    if enta.leader.tpl_id == "PERSON_ZHAO_SHENJI" and \
       entb.leader.tpl_id == "PERSON_YANG_LEI":
        return 10
    if enta.leader.tpl_id == "PERSON_YANG_LEI" and \
       entb.leader.tpl_id == "PERSON_ZHAO_SHENJI":
        return 10
    return 50


def load_discoveries():
    for d in dir(data.discovery):
        if not d.startswith("DISCOVERY"):
            continue 
        obj = getattr(data.discovery, d)
        tool_tag = obj.get("tools", None)
        for plc in obj["places"]:
            scenario = plc.get("scenario", "ALL")
            if scenario not in discoveries:
                discoveries[scenario] = []
            newdis = {"item": obj["item"]}
            if tool_tag is not None:
               newdis["tools"] = set(tool_tag.split(","))
            if "terrans" in plc:
                newdis["terrans"] = plc["terrans"]
            if "locations" in plc:
                newdis["locations"] = set(map(lambda x: eval(x), plc["locations"]))
            #if "tools" in plc:
            #    newdis["tools"] = set(plc["tools"].split(","))
            if "rate" in plc:
                newdis["rate"] = plc["rate"]
            if "quantity" in plc:
                newdis["quantity"] = plc["quantity"]
            if "range" in plc:
                newdis["range"] = plc["range"]
            discoveries[scenario].append(newdis)


load_discoveries()

