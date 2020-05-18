# -- coding: utf-8 --

import importlib

from proj.runtime import context


def entitify_(v):
    if v.startswith("{") and v.endswith("}"):
        vp = v[:v.find("_")]
        entities = importlib.import_module("proj.entity")
        cls = eval("entities.%s%s" % (vp[1], vp[2:].lower()))
        return cls.one(v[1:-1])
    elif v.startswith("(") and v.endswith(")"):
        return eval(v)
    else:
        return v
        
        
def entitify(d):
    if isinstance(d, dict):
        ret = {}
        for k, v in d.items():
            ret[k] = entitify(v)
    elif isinstance(d, list):
        ret = [entitify(vitm) for vitm in d]
    elif isinstance(d, str):
        ret = entitify_(d)
    else:
        ret = d
    return ret


def action(line):
    actions = importlib.import_module("proj.builtin.actions")
    action = eval("actions.%s" % line["type"][7:])(**entitify(line))
    action.do()
    
    
def order(line):
    orders = importlib.import_module("proj.console.orders")
    eval("orders.%s" % line["type"][6:])(**entitify(line))
    
    
def conditions(lines):
    conditions = importlib.import_module("proj.builtin.conditions")
    final_result = True
    for condstr in lines:
        condition = eval("conditions.%s" % condstr["type"])(**entitify(condstr))
        final_result = final_result and condition.check() == condition.expect
    return final_result
    
    
def run(lines):
    for line in lines:
        if line["type"].startswith("Action."):
            action(line)
        elif line["type"].startswith("Order."):
            order(line)
