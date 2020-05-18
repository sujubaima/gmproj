# -- coding: utf-8 --

from proj.console import control as inter
from proj.core.zone import Zone

from thirdparty.pic2char import pic2char


TERRAN_CHAR = {Zone.PLAIN: " ",
               Zone.MOUNTAIN: "Δ",
               Zone.FOREST: "Ψ",
               Zone.WATER: "~",
               Zone.DESERT: ".",
               Zone.SNOW: "*",
               Zone.ROTTEN: "η",
               Zone.LOCATION: "○"}


def render(zone, ascii_list=None, label_loc_dict=None):
    if label_loc_dict is None:
        label_loc_dict = {}
    lines = []
    if zone.background is not None:
        lines = pic2char.charimg(zone.background, char_list=ascii_list)
    else:
        for i in range(zone.y):
            lines.append([])
            for j in range(zone.x):
                lines.append(" ")
    for i in range(zone.y):
        for j in range(zone.x):
            if zone.xy[j][i] is not None:
                lines[i][j] = TERRAN_CHAR[zone.xy[j][i]]
    lb_pts = set()
    for (x, y), label in zone.labels.items():
        nl = inter.length(label)
        labels = [(x - nl / 2, y - 1), (x + 2, y), (x - nl / 2, y + 1),
                  (x - nl - 1, y)] 
        if label in label_loc_dict:
            lb = labels[label_loc_dict[label]]
            y_pts = [(lb[0] + i, lb[1]) for i in range(nl)]
        else:
            for lb in labels:
                label_here = True
                y_pts = [(lb[0] + i, lb[1]) for i in range(nl)]
                for pt in y_pts:
                    if pt in lb_pts or zone.xy[pt[0]][pt[1]] == Zone.LOCATION:
                        label_here = False
                        break
                if label_here:
                    break
        #lines[y_pts[0][1]][y_pts[0][0]] = label
        for idx in range(len(y_pts)):
            ptx, pty = y_pts[idx]
            if idx == 0:
                lines[pty][ptx] = label
            else:
                lines[pty][ptx] = ""
            lb_pts.add((ptx, pty))
    for l in lines:
        inter.echo("".join(l))
