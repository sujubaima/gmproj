# -- coding: utf-8 --

import importlib

from proj import data

from proj.engine.frame import Message as MSG
from proj.engine.frame import Order
from proj.engine.frame import Mutable

from proj.runtime import context


def _run(lines):
    for line in lines:
        if line["type"].startswith("Action."):
            action(line)
        elif line["type"].startswith("Order."):
            order(line)
            
def run(lines, script_name=None, timeflow=0, **kwargs):
    ScriptRunner(lines, name=script_name, timeflow=timeflow, **kwargs).run()
            

class ScriptRunner(object):

    def __init__(self, lines, name=None, timeflow=0, plot=None, **kwargs):
        self.sub = False
        if plot is None:
            self.plot = Mutable()
        else:
            self.plot = plot
            self.sub = True
        self.plot.load(**kwargs)
        self.name = name
        self.timeflow = timeflow
        self.lines = lines
        self.labels = {}
        for idx, line in enumerate(self.lines):
            if "label" in line:
                self.labels[line["label"]] = idx

    def entitify_(self, v):
        plot = self.plot
        if v.startswith("{") and v.endswith("}"):
            vp = v[:v.find("_")]
            entities = importlib.import_module("proj.entity")
            cls = eval("entities.%s%s" % (vp[1], vp[2:].lower()))
            return cls.one(v[1:-1])
        elif v.startswith("(") and v.endswith(")"):
            return eval(v)
        else:
            return v     
        
    def entitify(self, d):
        if isinstance(d, dict):
            ret = {}
            for k, v in d.items():
                ret[k] = self.entitify(v)
        elif isinstance(d, list):
            ret = [self.entitify(vitm) for vitm in d]
        elif isinstance(d, str):
            ret = self.entitify_(d)
        else:
            ret = d
        return ret

    def action(self, line):
        actions = importlib.import_module("proj.builtin.actions")
        ac = eval("actions.%s" % line["type"][7:])(**self.entitify(line))
        ac.do()
        return ac  
    
    def order(self, line):
        orders = importlib.import_module("proj.console.orders")
        return eval("orders.%s" % line["type"][6:])(**self.entitify(line))
        
    def conditions(self, lines):
        conditions = importlib.import_module("proj.builtin.conditions")
        final_result = True
        for condstr in lines:
            condition = eval("conditions.%s" % condstr["type"])(**self.entitify(condstr))
            final_result = final_result and condition.check() == condition.expect
        return final_result
        
    def block(self, line):
        run(line["scripts"], script_name=self.name, plot=self.plot)
           
    def run(self, fromidx=0):
        MSG = importlib.import_module("proj.engine.frame").Message
        idx = fromidx
        while idx < len(self.lines):
            line = self.lines[idx]
            order = None
            if line["type"].startswith("Action."):
                self.action(line)
            elif line["type"].startswith("Order."):
                self.order = order(line)
            elif line["type"] == "Block":
                self.block(line)
            elif line["type"] == "Include":
                run(getattr(data.scripts, line["script"]), script_name=line["script"], plot=self.plot)
            elif line["type"] == "Set":
                self.plot.load(**self.entitify(line))
            elif line["style"] == "Conditions":
                final_result = self.conditions(line["conditions"])
                rststr = str(final_result).lower()
                if rststr in line["result"]:
                    idx = self.labels[line["result"][rststr]]
                else:
                    idx += 1   
                continue                    
            elif line["style"] == "Branch":
                MSG(style=MSG.SessionBranch, subject=s.subject, branches=line["branches"], 
                    name=self.name).callback = self.callback
                break
            if "next" in line:
                idx = self.labels[line["next"]]
            else:
                idx += 1  
            if line.get("breaking", False):
                return
            if line.get("interrupting", False) and order is not None:
                order.callback = lambda: self.run(fromidx=idx)
                return             
        if idx >= len(self.lines) and not self.sub:
            context.timeflow(self.timeflow)
            MSG(style=MSG.Show, wait=True)
