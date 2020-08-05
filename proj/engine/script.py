# -- coding: utf-8 --

import importlib

from proj import data

from proj.engine.frame import Message as MSG
from proj.engine.frame import Control
from proj.engine.frame import Mutable


def run(lines, name=None, fromlabel=None, fromidx=0, timeflow=0, **kwargs):
    jscript = JsonScript(lines, name=name, **kwargs)
    jscript.run(fromidx=fromidx, fromlabel=fromlabel,timeflow=timeflow)
    return jscript


def conditions(lines, **kwargs):
    return JsonScript([], **kwargs).conditions(lines)


class JsonScript(object):

    def __init__(self, lines, name=None, plot=None, **kwargs):
        if plot is None:
            self.plot = Mutable()
        else:
            self.plot = plot
        self.plot.load(**kwargs)
        self.name = name
        self.lines = lines
        self.labels = {}
        for idx, line in enumerate(self.lines):
            if "label" in line:
                self.labels[line["label"]] = idx

    def by_label(self, label):
        if label not in self.labels:
            return None
        return self.lines[self.labels[label]]

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

    def action(self, line, ac_class=None):
        actions = importlib.import_module("proj.builtin.actions")
        if ac_class is None:
            ac_instance = eval("actions.%s" % line["type"][7:])
        else:
            ac_instance = eval("actions.%s" % ac_class)
        ac = ac_instance(**self.entitify(line))
        ac.do()
        return ac  
    
    def control(self, line, ac_class=None):
        controls = importlib.import_module("proj.console.controls")
        if ac_class is None:
            ac_instance = eval("controls.%s" % line["type"][8:])
        else:
            ac_instance = eval("controls.%s" % ac_class)
        ac = ac_instance(**self.entitify(line))
        ac.run()
        return ac
        
    def conditions(self, lines):
        conditions = importlib.import_module("proj.builtin.conditions")
        final_result = True
        for condstr in lines:
            condition = eval("conditions.%s" % condstr["type"])(**self.entitify(condstr))
            final_result = final_result and condition.check() == condition.expect
        return final_result
        
    def run(self, fromidx=0, fromlabel=None, timeflow=0):
        MSG = importlib.import_module("proj.engine.frame").Message
        controls = importlib.import_module("proj.console.controls")
        idx = fromidx
        if fromlabel is not None:
            idx = self.labels[fromlabel]
        while idx < len(self.lines):
            line = self.lines[idx]
            if line["type"].startswith("Action."):
                self.action(line)
            elif line["type"].startswith("Control."):
                control = self.control(line)
            elif line["type"] == "Block":
                run(script, name=self.name, plot=self.plot)
            elif line["type"] == "Include":
                run(getattr(data.scripts, line["script"]), name=line["script"], 
                    fromlabel=line.get("from", None), plot=self.plot, **self.entitify(line))
            elif line["type"] == "Set":
                self.plot.load(**self.entitify(line))
            elif line["type"] == "Conditions":
                final_result = self.conditions(line["conditions"])
                rststr = str(final_result).lower()
                if rststr in line["result"]:
                    idx = self.labels[line["result"][rststr]]
                else:
                    idx += 1   
                continue
            elif line["type"] == "Branch":
                control = controls.BranchControl(subject=self.plot.subject, branches=line["branches"],
                    labels=self.labels, name=self.name, script=self.lines)
                control.run()
                idx = control.idx
                continue
            elif line["type"] == "Pause":
                self.action(line, ac_class="PauseAction")
            if "next" in line:
                idx = self.labels[line["next"]]
            else:
                idx += 1  
            if line.get("break", False):
                return

