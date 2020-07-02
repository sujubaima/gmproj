# -- coding: utf-8 --

from proj import options

class Aka(object):

    def __init__(self, map=None):
        self.d1 = {}
        self.d2 = {}
        if map is not None:
            self.update(map)

    def add(self, k, v):
        self.d1[k] = v
        self.d2[v] = k

    def update(self, map):
        for k, v in map.items():
            self.add(k, v)

    def __getitem__(self, k):
        if k in self.d1:
            return self.d1[k]
        elif k in self.d2:
            return self.d2[k]
        else:
            return k

    def __str__(self):
        return str(self.d1)


YOU = "你"

aka = Aka()
aka.update({"name": "姓名", "sex": "性别",
            "gengu": "根骨", "lidao": "力道", "shenfa": "身法",
            "neigong": "内功", "dongcha": "洞察", "wuxing": "悟性",
            "boji": "搏击", "jianfa": "剑法", "daofa": "刀法",
            "changbing": "长兵", "anqi": "暗器", "qimen": "奇门"})
aka.update({"hp": "气血", "mp": "内力"})

vaka = {}
vaka["sex"] = Aka({"0": "男", "1": "女"})

if options.USE_FULL_WIDTH_FONT:
    #vaka["direction"] = Aka({"1": "→", "2": "↘", "4": "↙",
    #                         "-1": "←", "-2": "↖", "-4": "↗"})
    vaka["direction"] = Aka({"0": "→", "1": "↘", "2": "↙",
                             "3": "←", "4": "↖", "5": "↗"})
else:
    vaka["direction"] = Aka({"0": "→ ", "1": "↘ ", "2": "↙ ",
                             "3": "← ", "4": "↖ ", "5": "↗ "})

def kvstr(obj, k, delim="：", kspan=-1, vspan=-1):
    v = getattr(obj, k)
    kstr = str(aka[k])
    if k in vaka:
        vstr = str(vaka[k][v])
    else:
        vstr = str(v)
    if kspan > len(kstr):
        kstr += " " * (kspan - len(kstr))
    if vspan > len(vstr):
        vstr += " " * (vspan - len(vstr)) 
    return "%s%s%s" % (kstr, delim, vstr)
    

def people(p, about="attrs"):
    ret = [kvstr(p, "name"),
           kvstr(p, "sex"),
           " ".join([kvstr(p, "gengu", vspan=2),
                     kvstr(p, "lidao", vspan=2),
                     kvstr(p, "shenfa", vspan=2)]),
           " ".join([kvstr(p, "neigong", vspan=2), 
                     kvstr(p, "dongcha", vspan=2), 
                     kvstr(p, "wuxing", vspan=2)]),
           " ".join([kvstr(p, "boji", vspan=2),
                     kvstr(p, "jianfa", vspan=2),
                     kvstr(p, "daofa", vspan=2)]),
           " ".join([kvstr(p, "changbing", vspan=2),
                     kvstr(p, "anqi", vspan=2), 
                     kvstr(p, "qimen", vspan=2)])]
    return ret

if __name__ == "__main__":
    import sys
    sys.path.append("/home/work/gmproj")
    print(vaka["sex"][1])
