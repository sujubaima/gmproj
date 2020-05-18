from proj.core.skill import WuXue

WuXue(name="", style=Wuxue.Neigong
      add_each={"dongcha", 2},
      add_all={"dongcha", 4})

WuXue(name="花拳绣腿", style=Wuxue.Taolu)
ZhaoShi(name="花拳", power=300, cd=0, shape=Shape(Shape.Point, 2, 0), haoqi=70, yinyang=1, style=skill.Qimen, belongs=Skill.search("死缠烂打"))
ZhaoShi(name="绣腿", power=300, cd=0, shape=Shape(Shape.Point, 1, 0), haoqi=240, yinyang=1, style=skill.Qimen, belongs=Skill.search("死缠烂打"))

WuXue(name="死缠烂打", style=Wuxue.Taolu)
ZhaoShi(name="死缠", power=300, cd=0, shape=Shape(Shape.Point, 2, 0), haoqi=70, yinyang=1, style=skill.Boji, belongs=Skill.search("死缠烂打"))
ZhaoShi(name="烂打", power=300, cd=0, shape=Shape(Shape.Point, 1, 0), haoqi=240, yinyang=1, style=skill.Boji, belongs=Skill.search("死缠烂打"))
