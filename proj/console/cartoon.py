# -- coding: utf-8 --

from proj.console import ui

from proj.entity import Person

def profile(p):
    ui.echo()
    ui.echo("%s %s" % (p.title, p.name))
    ui.echo()
    ui.echo("【基本情况】")
    ui.echo()
    ui.echo("  " + ui.fixed(15, n="气血：%s/%s" % (p.hp, p.hp_limit)))
    ui.echo("  " + ui.fixed(15, n="内力：%s/%s" % (p.mp, p.mp_limit)))
    ui.echo("  " + ui.fixed(15, n="外伤：%s" % p.injury))
    ui.echo("  " + ui.fixed(15, n="内伤：%s" % p.wound))
    ui.echo("  " + ui.fixed(15, n="风毒：%s" % p.poison_hp))
    ui.echo("  " + ui.fixed(15, n="瘀毒：%s" % p.poison_mp))
    ui.echo()
    ui.echo("【人物特质】")
    ui.echo()
    ui.echo("  " + ui.fixed(15, n="灵动：%s%%" % (50 + p.dongjing)) + ui.fixed(10, n="沉静：%s%%" % (50 - p.dongjing)))
    ui.echo("  " + ui.fixed(15, n="刚猛：%s%%" % (50 + p.gangrou)) + ui.fixed(10, n="柔易：%s%%" % (50 - p.gangrou)))
    ui.echo("  " + ui.fixed(15, n="颖悟：%s%%" % (50 + p.zhipu)) + ui.fixed(10, n="朴拙：%s%%" % (50 - p.zhipu)))
    ui.echo()
    ui.echo("【武学能力】")
    ui.echo()
    ui.echo("  " + ui.fixed(15, n="内功：%s" % p.neigong))
    ui.echo("  " + ui.fixed(15, n="搏击：%s" % p.boji) + ui.fixed(15, n="剑法：%s" % p.jianfa))
    ui.echo("  " + ui.fixed(15, n="刀法：%s" % p.daofa) + ui.fixed(15, n="长兵：%s" % p.changbing))
    ui.echo("  " + ui.fixed(15, n="暗器：%s" % p.anqi) + ui.fixed(15, n="奇门：%s" % p.qimen))
    ui.echo()
    ui.echo("【当前状态】")
    for sts in p.status:
        if sts.name is not None:
            ui.echo(sts.name)
    ui.echo()
    ui.echo("【主运心法】")
    ui.echo()
    ui.echo("【习得武学】")
    ui.echo()
    for sk in p.skills:
        ui.echo("  %s：%s" % (sk.belongs.name, sk.name))


if __name__ == "__main__":
    pa = Person.one("PERSON_ZHAO_SHENJI")
    pb = Person.one("PERSON_TIAN_WEI")
    #profile(pb)

    ui.echo()
    ui.echo(" " + ui.colored(" Ω ", attrs=["underline"]) + " " + "   " + ui.colored("  ^  ", attrs=["underline"]))
    ui.echo(" " + "├_┤" + " " + "   " + "║" + "║║║" + "║")
    ui.echo("q" + ui.colored("¯V¯", attrs=["underline"]) + "p" + "   " + "q" + ui.colored("¯Y¯", attrs=["underline"]) + "p")
    ui.echo(" U U " + "   " + " U U ")

    ui.echo()
    ui.echo(" " + ui.colored("-Π-", attrs=["underline"]) + " " + "   " + " " + ui.colored("\\V/", attrs=["underline"]) + " ")
    ui.echo(" " + "├_┤" + " " + "   " + "/" + "├_┤" + "\\")
    ui.echo("q" + ui.colored("¯Ÿ¯", attrs=["underline"]) + "p" + "   " + "q" + ui.colored("¯¯¯", attrs=["underline"]) + "p")
    ui.echo(ui.colored("/", attrs=["underline"]) + "_" + ui.colored(" ", attrs=["underline"]) + "_" + ui.colored("\\", attrs=["underline"]) + "   " + " Ш Ш ")

    ui.echo()
    ui.echo(" " + ui.colored("┼─┼", attrs=["underline"]) + " " + "   " + " " + ui.colored("(¯)", attrs=["underline"]) + " ")
    ui.echo(" " + "├_┤" + " " + "   " + "(" + "╞ ╡" + ")")
    ui.echo("q" + ui.colored("¯Y¯", attrs=["underline"]) + "p" + "   " + "q" + ui.colored("¯Y¯", attrs=["underline"]) + "p")
    ui.echo(" U U " + "   " + ui.colored("/", attrs=["underline"]) + "_" + ui.colored(" ", attrs=["underline"]) + "_" + ui.colored("\\", attrs=["underline"]))

    ui.echo()
    ui.echo(" " + ui.colored("Ω Ω", attrs=["underline"]) + " " + "   " + " " + ui.colored("mmm", attrs=["underline"]) + " ")
    ui.echo("´" + "╞ ╡" + "`" + "   " + " " + "├_┤" + " ")
    ui.echo("q" + ui.colored("¯¯¯", attrs=["underline"]) + "p" + "   " + "q" + ui.colored("¯ˇ¯", attrs=["underline"]) + "p")
    ui.echo(" U U " + "   " + " U U ")

    ui.echo()
    ui.echo(" " + ui.colored("(\\ ", attrs=["underline"]) + " " + "   " + " " + "┌─┐" + " ")
    ui.echo("§" + "╞ ╡" + " " + "   " + " " + "├_┤" + " ")
    ui.echo("q" + ui.colored("¯¯¯", attrs=["underline"]) + "p" + "   " + "q" + ui.colored("¯╪¯", attrs=["underline"]) + "p")
    ui.echo(" U U " + "   " + " U U ")

    #ui.echo()
    #ui.echo(ui.colored("  ^  ", attrs=["underline"]))
    #ui.echo("║" + "║║║" + "║")
    #ui.echo("q" + ui.colored("¯Y¯", attrs=["underline"]) + "p")
    #ui.echo(" U U ")

    #ui.echo()
    #ui.echo(" " + ui.colored("\\V/", attrs=["underline"]) + " ")
    #ui.echo("/" + "├_┤" + "\\")
    #ui.echo("q" + ui.colored("¯¯¯", attrs=["underline"]) + "p")
    #ui.echo(" Ш Ш ")

    #ui.echo()
    #ui.echo(" " + ui.colored("(¯)", attrs=["underline"]) + " ")
    #ui.echo("(" + "╞ ╡" + ")")
    #ui.echo("q" + ui.colored("¯¯¯", attrs=["underline"]) + "p")
    #ui.echo(ui.colored("/", attrs=["underline"]) + "_" + ui.colored(" ", attrs=["underline"]) + "_" + ui.colored("\\", attrs=["underline"]))

    #ui.echo()
    #ui.echo(" " + ui.colored("mmm", attrs=["underline"]) + " ")
    #ui.echo(" " + "├_┤" + " ")
    #ui.echo("q" + ui.colored("¯ˇ¯", attrs=["underline"]) + "p")
    #ui.echo(" U U ")

    ui.echo()

