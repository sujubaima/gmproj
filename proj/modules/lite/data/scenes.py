# -- coding: utf-8 --

from proj.core.place import Scene

SCENE_1_1 = Scene(name="成都-大街")
SCENE_1_1.additem("金钱", prob=25, range=(1, 100), quantity=99999999)
SCENE_1_1.additem("飞刀", prob=15, quantity=1)
SCENE_1_1.additem("金疮药", prob=20, quantity=999)
SCENE_1_1.additem("裋褐", prob=100, quantity=1)
SCENE_1_1.additem("《神鸾经》", prob=1, quantity=1)

SCENE_1_2 = Scene(name="成都-天府客栈-大厅")

SCENE_1_2_1 = Scene(name="成都-天府客栈-二楼东厢房")
SCENE_1_2_1.additem("金钱", prob=25, quantity=1)

SCENE_1_2_2 = Scene(name="成都-天府客栈-二楼西厢房")
SCENE_1_2_2.additem("金钱", prob=25, quantity=2)
SCENE_1_2_2.additem("玉手镯", prob=5, quantity=1)
SCENE_1_2_2.additem("鸳字剑", prob=1, quantity=1)

SCENE_1_2_3 = Scene(name="成都-天府客栈-厨房")

SCENE_1_3 = Scene(name="成都-青羊宫")

SCENE_1_3_1 = Scene(name="成都-青羊宫-东厢房")

SCENE_1_3_2 = Scene(name="成都-青羊宫-西厢房")

SCENE_1_3_3 = Scene(name="成都-青羊宫-炼丹室")

if __name__ == "__main__":
    for i in range(20):
        a, b, c = SCENE_1_2_2.search()
        for n in a, b, c:
            for m in n:
                 "%s, %s" % (i, m)
