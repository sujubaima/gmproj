from proj.core.skill import WuXue

WuXue(name="鹰眼术", style=Wuxue.Neigong
      add_each={"dongcha", 2},
      add_all={"dongcha", 4})

WuXue(name="六骏鞭法", style=Wuxue.Taolu)
ZhaoShi(name="青骓马", power=350, cd=0, shape=Shape(Shape.Point, 3, 0), haoqi=70, yinyang=1, style=skill.Qimen, belongs=Skill.search("六骏鞭法"))
ZhaoShi(name="白蹄乌", power=400, cd=1, shape=Shape(Shape.Line, 1, 3), haoqi=240, yinyang=1, style=skill.Qimen, belongs=Skill.search("六骏鞭法"))
