# -- coding: utf-8 --
from __future__ import division

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../../"))

import platform

from proj.console import ui
from proj import options

from proj.entity import Superskill
from proj.entity import Person

HOR = "─"
VER = "│"
LT = "┌"
RT = "┐"
LB = "└"
RB = "┘"
BTL = "┤"
BTR = "├"
BTB = "┬"
BTT = "┴"
BTC = "┼"

DLT = "▼"

HEIGHT = 3
WIDTH = 18
GAP = 9


def grid(n=""):
    return n + " " * (WIDTH - ui.strwidth(n))


def to_layers(superskill):
    """
    计算各个节点的层级以及在层级中的显示位置。
    这个地方的实现我偷懒了，默认nodes的配置都是入度为零的节点在前，
    且图内没有环
    """
    connections = []
    layers = []
    nodemap = {}
    for idx, node in enumerate(superskill.nodes):
        if idx not in nodemap:
            nodemap[idx] = 0
        for next in node.next:
            if next not in nodemap:
                nodemap[next] = 0
            nodemap[next] = max(nodemap[next], nodemap[idx] + 1)
    for k, v in nodemap.items():
        if v > len(layers) - 1:
            layers.extend([[]] * (v - len(layers) + 1))
            connections.extend([{}] * (v - len(connections) + 1))
        layers[v].append(k)
    for idx, l in enumerate(layers):
        for subidx, k in enumerate(l):
            if len(superskill.nodes[k].next) == 0:
                continue
            #connections[idx][len(connections[idx])] = \
            #                         [(nodemap[itm], layers[nodemap[itm]].index(itm)) for itm in superskill.nodes[k].next]
            connections[idx][subidx] = [(nodemap[itm], layers[nodemap[itm]].index(itm)) for itm in superskill.nodes[k].next]
    #print(layers, connections)
    return layers, connections
                                     
                                     
def superskill(superskill, subject=None):
    layers, connections = to_layers(superskill)
    ui.echo()
    ui.echo("当前武学：%s" % ui.rank(superskill))
    ui.echo()
    dires = set()
    for i in range(len(layers)):
        layer = layers[i]
        last = layers[i - 1]
        connection = connections[i - 1]
        #maxgap = max(3, len(last) + len(dires) + 2)
        maxgap = max(3, len(connection) + len(dires) + 2)
        epts = set()
        spts = []        
        for j in range(len(last)):
            bst = (GAP + WIDTH + 2) * j + WIDTH // 2 + 1
            spts.append(bst)
        for bst in dires:
            spts.append(bst)
        dires.clear()
        if i != 0:
            for j_raw in range(-1, maxgap):
                tmpstr = []
                tmpepts = set()
                if j_raw >= 0 and j_raw < len(connection):
                    j = sorted(connection.keys())[j_raw]
                    tmppts = set()
                    bst = spts[j]
                    tmppts.add(bst)
                    for cy in connection[j]:
                        ly, nd = cy
                        if ly >= i + 1:
                            nd = len(connection)
                            if nd not in connections[i]:
                                connections[i][nd] = []
                            connections[i][nd].append(cy)
                        #ben = (GAP + WIDTH + 2) * nd + WIDTH // 2 + 1 - len(last) + 2 * j
                        #ben = (GAP + WIDTH + 2) * nd + WIDTH // 2 + 1 - (2 * j // 2 if j % 2 == 0 else -2 * (j // 2 + 1)) 
                        if nd == j:
                            ben = (GAP + WIDTH + 2) * nd + WIDTH // 2 + 1
                        elif j > nd:
                            ben = (GAP + WIDTH + 2) * nd + WIDTH // 2 + 1 + 2 * ((j - nd) // 2 + 1)
                        else:
                            ben = (GAP + WIDTH + 2) * nd + WIDTH // 2 + 1 - 2 * ((nd - j) // 2 + 1)
                        epts.add(ben)
                        tmppts.add(ben)
                        tmpepts.add(ben)
                        if ly >= i + 1:
                            dires.add(ben)
                    horst, horen = min(tmppts), max(tmppts)
                    tmpstr = [" "] * horst + [HOR] * (horen - horst + 1)
                    for tmppt in tmppts:
                        if tmppt == horst and tmppt == horen:
                            tmpstr[tmppt] = VER
                        elif tmppt == bst:
                            if tmppt in tmpepts:
                                if tmppt == horst:
                                    tmpstr[tmppt] = BTR
                                elif tmppt == horen:
                                    tmpstr[tmppt] = BTL
                                else:
                                    tmpstr[tmppt] = BTC
                            else:
                                if tmppt == horst:
                                    tmpstr[tmppt] = LB
                                elif tmppt == horen:
                                    tmpstr[tmppt] = RB
                                else:
                                    tmpstr[tmppt] = BTT
                        else:
                            if tmppt == horst:
                                tmpstr[tmppt] = LT
                            elif tmppt == horen:
                                tmpstr[tmppt] = RT
                            else:
                                tmpstr[tmppt] = BTB
                # 分支后竖线
                for ept in sorted(epts):
                    if ept >= len(tmpstr): 
                        tmpstr += [" "] * (ept - ui.strwidth("".join(tmpstr))) + \
                                  [VER if j_raw != maxgap - 1 or ept in dires else DLT]
                    elif tmpstr[ept] == " ":
                        tmpstr[ept] = VER if j_raw != maxgap - 1 or ept in dires else DLT
                # 分支前竖线
                for k in sorted(connection.keys()):
                    if j_raw > k:
                        continue
                    vpt = spts[k] 
                    if vpt >= len(tmpstr):
                        tmpstr += [" "] * (vpt - len(tmpstr)) + [VER]
                    elif tmpstr[vpt] == " ":
                        tmpstr[vpt] = VER
                ui.echo("".join(tmpstr))
        tmpstr = [LT] + [HOR] * WIDTH  + [RT] + ([" "] * GAP + [LT] + [HOR] * WIDTH  + [RT]) * (len(layer) - 1)
        for ept in dires:
            if ept >= len(tmpstr):
                tmpstr += [" "] * (ept - len(tmpstr)) + [VER]
            elif tmpstr[ept] == " ":
                tmpstr[ept] = [VER]
        ui.echo("".join(tmpstr))
        for j in range(HEIGHT):
            strlist = []
            for lyt in layer:
                if j == 0:
                    ctstr = "【%s】" % (lyt + 1) + superskill.nodes[lyt].name
                #elif j == 1:
                #    ctstr = ui.nodecond(superskill.nodes[lyt])
                elif j == HEIGHT - 1 and subject is not None:
                    learn_st = superskill.learn_status(subject, lyt)
                    if learn_st == 0:
                        ctstr = ui.colored("（已习得）", color="yellow")
                    elif learn_st == -1:
                        ctstr = ui.colored("（条件不足）", color="red")
                    elif subject.studying != superskill.nodes[lyt]:
                        ctstr = ui.colored("（可学习）", color="green")
                    else:
                        ctstr = "经验：%s/%s" % (subject.exp, superskill.nodes[lyt].exp)
                else:
                    ctstr = ""
                strlist.append(VER + grid(ctstr) + VER)
            strlist = (" " * GAP).join(strlist)
            tmpstr = []
            strlen = ui.strwidth(strlist)
            for ept in dires:
                if ept >= strlen:
                    tmpstr += [" "] * (ept - strlen) + [VER]
                elif tmpstr[ept] == " ":
                    tmpstr[ept - strlen] = [VER]
            ui.echo(strlist + "".join(tmpstr))
        strlist = (" " * GAP).join([LB + HOR * WIDTH  + RB] * len(layer))
        tmpstr = []
        strlen = ui.strwidth(strlist)
        for ept in dires:
            if ept >= strlen:
                tmpstr += [" "] * (ept - strlen) + [VER]
            elif tmpstr[ept] == " ":
                tmpstr[ept - strlen] = [VER]
        ui.echo(strlist + "".join(tmpstr))

        

if __name__ == "__main__":
    superskill(Superskill.one("SUPERSKILL_HUANGLUKUZHUJIAN"), Person.one("PERSON_GENG_ZHUQIAO"))
