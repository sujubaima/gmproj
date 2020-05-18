# -- coding: utf-8 --
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj.console import interzone as interz
from proj.core.zone import Zone

if __name__ == "__main__":

    z = Zone(x=113, y=40, background="/home/work/gmproj/thirdparty/pic2char/bigmap.png")
    z.locate((58, 11), label="北京")
    z.locate((64, 22), label="南京")
    z.locate((66, 23), label="苏州")
    z.locate((65, 26), label="杭州")
    z.locate((38, 25), label="成都")
    z.locate((55, 25), label="武昌")
    z.locate((48, 20), label="武当山")
    z.locate((54, 17), label="少林寺")
    z.locate((56, 17), label="开封")
    z.locate((62, 30), label="泉州")
    #z.locate((63, 29), label="南少林")
    z.locate((58, 28), label="吉州")
    z.locate((59, 26), label="庐山")
    z.locate((45, 17), label="华山")
    z.locate((43, 18), label="终南山")
    z.locate((40, 15), label="崆峒山")
    z.locate((66, 39), label="紫阳岛")
    z.locate((12, 6), label="天山")
    z.locate((10, 18), label="昆仑山")
    z.locate((37, 24), label="青城山")
    z.locate((37, 27), label="峨嵋山")
    z.locate((11, 26), label="须弥寺")
    z.locate((45, 32), label="五瘴林")
    interz.render(z, label_loc_dict={"开封": 1,
                                     "终南山": 3})
