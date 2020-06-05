# -- coding: utf-8 --

import os
import re
import sys
import traceback

from proj import options
from proj.console import message as msg
from proj.console import format as fmt

from proj.engine import Message

from proj.runtime import context

from thirdparty.ansiterm import termcolor

import platform

if platform.system() != "Windows":
    import readline

from thirdparty import colorama

# 通过colorama模块来做linux与windows下的控制台颜色适配
colorama.init()


if sys.version_info.major != 2:
    raw_input = input

if sys.version_info.major != 2:
    unicoded = lambda x, coding="utf-8": x
else:
    unicoded = lambda x, coding="utf-8": x.decode(coding)


class EncodedOutputStream(object):
    """
    针对某些不支持UTF-8编码的平台，需要包装一下标准输入输出
    其实没有什么卵用，因为不同编码对字符的显示效果差别太大了
    所以UTF-8都不支持的平台，俺为什么要做适配？
    /"""
    def __init__(self, target):
        self.target = target
        self.src_encoding= "utf-8"
        self.dst_encoding = self.target.encoding
        self.errors = "replace"
        self.encoding = self.src_encoding

    def write(self, content):
        #if type(content) == str:
        content = unicoded(content, coding=self.src_encoding)
        content = content.encode(self.dst_encoding, self.errors).decode(self.dst_encoding)
        self.target.write(content)

    def flush(self):
        self.target.flush()


class EncodedInputStream(object):
    """
    针对某些不支持UTF-8编码的平台，需要包装一下标准输入输出
    其实没有什么卵用，因为不同编码对字符的显示效果差别太大了
    所以UTF-8都不支持的平台，俺为什么要做适配？
    """
    def __init__(self, source):
        self.source = source
        self.dst_encoding= "utf-8"
        self.src_encoding = self.source.encoding
        self.encoding = self.dst_encoding
        self.errors = "replace"

    def readline(self):
        content = self.source.readline()
        #if type(content) == str:
        content = unicoded(content, coding=self.src_encoding)
        return content.encode(self.dst_encoding, self.errors)


if sys.stdout.encoding.lower() not in ("utf-8", "cp65001"):
    sys.stdout = EncodedOutputStream(sys.stdout)

if sys.stdin.encoding.lower() not in ("utf-8", "cp65001"):
    sys.stdin = EncodedInputStream(sys.stdin)


class Colored(object):

    """
    用来适配正常显示与curses显示
    """
    def __init__(self, text="", color=None, on_color=None, attrs=None):
        self.strlist = []
        if isinstance(text, Colored):
            for st in text.strlist:
                self.strlist.append(st)
        else:
            self.strlist.append(self.makedict(text, color, on_color, attrs))
            
    def makedict(self, text="", color=None, on_color=None, attrs=None):
        news = {"text": text,
                "color": color,
                "on_color": on_color,
                "attrs": attrs}
        return news

    def __str__(self):
        ret = ""
        for s in self.strlist:
            ret += termcolor.colored(**s)
        return ret

    def __add__(self, other):
        ret = Colored()
        for stri in self.strlist:
            ret.strlist.append(stri)
        if isinstance(other, Colored):
            tmp = other.strlist
        else:
            tmp = [self.makedict(other)]
        strl = ret.strlist[-1]
        strf = tmp[0]
        if strf["color"] == strl["color"] and \
           strf["on_color"] == strl["on_color"] and \
           strf["attrs"] == strl["attrs"]:
            #ret.strlist[-1] = self.makedict(**{"text": strl["text"] + strf["text"],
            #                                   "color": strl["color"],
            #                                   "on_color": strl["on_color"],
            #                                   "attrs": strl["attrs"]})
            ret.strlist[-1]["text"] = strl["text"] + strf["text"]
        else:
            ret.strlist.append(strf)
        for stri in tmp[1:]:
            ret.strlist.append(stri)
        return ret

    def __radd__(self, other):
        ret = Colored()
        if isinstance(other, Colored):
            for stri in other.strlist:
                ret.strlist.append(stri)
        else:
            ret.strlist.append(self.makedict(other))
        strl = ret.strlist[-1]
        strf = self.strlist[0]
        if strf["color"] == strl["color"] and \
           strf["on_color"] == strl["on_color"] and \
           strf["attrs"] == strl["attrs"]:
            ret.strlist[-1] = self.makedict(**{"text": strl["text"] + strf["text"],
                                               "color": strl["color"],
                                               "on_color": strl["on_color"],
                                               "attrs": strl["attrs"]})
            for stri in self.strlist[1:]:
                ret.strlist.append(stri)
        else:
            for stri in self.strlist:
                ret.strlist.append(stri)
        return ret
        
    def __mul__(self, other):
        ret = Colored()
        for i in range(other):
            ret = ret + self
        return ret
        
    def __rmul__(self, other):
        ret = Colored()
        for i in range(other):
            ret = self + ret
        return ret


def input_func_(tip):
    words(tip)
    return raw_input()


def select_func_(menu):
    multiple = getattr(menu, "multiple", False)
    if multiple and menu.multiple_num < 0:
        return read(msg.CHOICE_MULTIPLE_NO_LIMIT)
    elif multiple:
        return read(msg.CHOICE_MULTIPLE % menu.multiple_num)
    else:
        return read(msg.CHOICE)
        

# 在使用curses绘制UI的前提下有些基本操作需要特殊实现
# 不过curses真他妈难用，我觉得用原始的交互就挺好的
# 不接受反驳
#if options.USE_CURSES:
#    from proj.console import scr
#    output_func = scr.curses_write
#    input_func = scr.curses_read
#    select_func = scr.curses_select
#    position_func = scr.curses_position
#    refresh_func = scr.curses_refresh
#    colored = Colored
#else:
output_func = lambda x: sys.stdout.write(str(x))
if platform.system() == "Linux":
    input_func = lambda x="": raw_input(x)
else:
    input_func = input_func_
select_func = select_func_
position_func = lambda x: (0, 0)
refresh_func = lambda x: None
colored = termcolor.colored


UNICODE_WIDTH = [
    (126, 1), (159, 0), (687, 1), (710, 0), (711, 1),
    (727, 0), (733, 1), (879, 0), (1154, 1), (1161, 0),
    (4347, 1), (4447, 2), (7467, 1), (7521, 0), (8369, 1),
    (8426, 0), (9000, 1), (9002, 2), (11021, 1), (12350, 2),
    (12351, 1), (12438, 2), (12442, 0), (19893, 2), (19967, 1),
    (55203, 2), (63743, 1), (64106, 2), (65039, 1), (65059, 0),
    (65131, 2), (65279, 1), (65376, 2), (65500, 1), (65510, 2),
    (120831, 1), (262141, 2), (1114109, 1),
]


WINDOWS_CHARS = set([215, 923, 936, 966, 1044, 1051, 1078, 8593, 8595, 8592, 
                     8594, 8598, 8599, 8601, 8600, 
                     8730, 8741, 8745, 8978, 9532, 9660, 9675, 9679])


def charwidth(o):
    """
    用于计算字符的显示宽度，仅支持UTF-8 
    """
    if o in WINDOWS_CHARS and options.USE_FULL_WIDTH_FONT:
        return 2
    if o == 0xe or o == 0xf:
        return 0
    for num, wid in UNICODE_WIDTH:
        if o <= num:
            return wid
    return 1


def strwidth(word):
    """
    用于计算字符串的显示宽度，仅支持UTF-8
    """
    # 需要先把颜色效果控制码给除掉
    # 后续考虑统一用Colored对象而不是colored方法来包装字符串
    # 现阶段就先不改了
    #tword = word
    #kidx = tword.find("\033[")
    #while kidx >= 0:
    #    tmpword = tword
    #    tword = tword[kidx:]
    #    while tword.startswith("\033["):
    #        tword = tword[tword.find("m") + 1:]
    #    if kidx >= 0:
    #        tword = tmpword[:kidx] + tword
    #    kidx = tword.find("\033[")
    #    if tword != word:
    #        tword = tword.replace("\033[0m", "")

    # la = len(tword.decode("UTF-8").encode("UTF-32")) / 4 - 1
    # lb = len(tword)
    # return (lb - la) / 2 + la

    tword = re.sub("\033\[[0-9]+m", "", word)
    # charwidth这个方法暂时来看是最准的
    l = 0
    for o in unicoded(tword):
        l += charwidth(ord(o))
    return l
    
    
def _strwidth(word):
    check = ""
    if isinstance(word, Colored):
        for st in word.strlist:
            check += st["text"]
    else:
        check = word
    l = 0
    for o in unicoded(check):
        l += charwidth(ord(o))
    return l           


def fixed(width, n="", bg=" ", color=None, on_color=None, attrs=None):
    bg_d = (width - strwidth(n)) // strwidth(bg)
    bg_m = (width - strwidth(n)) % strwidth(bg)
    return n + colored(" " * bg_m + bg * bg_d, color=color, on_color=on_color, attrs=attrs)


def _fixed(width, n="", bg=" "):
    return n + bg * (width - strwidth(n))


def string_replaced(line):
    idx = line.find("${")
    while idx >= 0:
        edx = line[idx:].find("}") + idx
        line = line.replace(line[idx:edx + 1], eval(line[idx + 2:edx]))
        idx = line.find("${")
    return line


lastblank = False


def blankline():
    return lastblank
 
 
def checkblank(content):
    global lastblank
    lastblank = len(content) == 0
    

def words(content="", fcolor=None, bcolor=None, attrs=[]):
    output_func(colored(content))


def echo(content="", fcolor=None, bcolor=None, attrs=[]):
    """
    最基本的打印功能
    """
    global lastblank
    if isinstance(content, list):
        for line in content: 
            output_func(line + "\n")
            checkblank(line)
    else:
        output_func(content + "\n")
        checkblank(content)


def warn(content=""):
    """
    有点黄的打印功能
    """
    echo(colored(content, color="yellow", attrs=["bold"]))


def read(tip="", fcolor=None, bcolor=None, attrs=None,
         handler=None, canceler=None, errmsg=msg.ERROR_INPUT_INVALID):
    """
    读取用户输入操作
    """
    while True:
        rd = input_func(colored(tip, color=fcolor, on_color=bcolor, attrs=attrs))
        if rd == msg.CANCEL:
            if canceler is not None:
                rd = canceler()
            else:
                rd = None
            break
        if handler is not None:
            try:
                rd = handler(rd)
            except Exception as e:
                #print(traceback.format_exc(e))
                rd = None
            if rd is None:
                warn(errmsg)
                echo()
                continue
        break
    checkblank(tip)
    return rd


def sure(content=msg.CONFIRMATION, fcolor=None, bcolor=None, attrs=["bold"]):
    """
    用户确认操作
    """
    while True:
        sr = read("%s（是/否）：" % content)
        if sr not in ["是", "否", "1", "0", ""]:
            warn(msg.ERROR_CHOICE_INVALID)
            echo()
        else:
            break
    return sr == "是" or sr == "1" or sr == ""


def deal(tip, fcolor=None, bcolor=None, attrs=["bold"]):
    while True:
        ret = read(tip, fcolor, bcolor, attrs)
        if sure():
            break
    echo()
    return ret


def text(context, goback=True):
    echo(context)
    menu([], goback=goback, shownone=False)


def richtext(func, goback=True):
    func()
    menu([], goback=goback, shownone=False)


class Interactive(object):
    """
    可交互控件，需要实现以下方法
    方法render用于描绘控件
    方法input用于等待接收用户的输入并返回
    方法handle用于对输入内容进行处理或预处理
    方法done会调用input和handle，并将处理过的用户输入返回

    一般用法：
    i = Interactive()
    i.render()
    rt = i.done() # 可对rt进一步处理
    或者
    rt = i.input() # 直接取回原始输入进行处理
    """
    def render(self, *args, **kwargs):
        pass

    def input(self):
        pass

    def handle(self, input):
        pass

    def done(self):
        return self.handle(self.input())

    def refresh(self, *args, **kwargs):
        self.render(*args, **kwargs)
        return self.done()


# 实现菜单后退的最懒操作
BACK_MENU = []


class Pages(Interactive):

    def __init__(self, panel, title=None, goback=False, backmethod=None):
        self.panel = panel
        self.page = 0

        self.title = title

        self.goback = goback

        self.controls = {}

        if backmethod is None:
            self.backmethod = backmenu
        else:
            self.backmethod = backmethod

    def render(self, page=0):
        if not blankline():
            echo()
        if self.title is not None:
            echo(self.title)
            echo()
        self.page = page
        echo(self.panel[self.page])
        echo()
        if page > 0:
            echo(msg.CHOICE_FORMAT % ("-", msg.PREVIOUS_PAGE))
            self.controls["-"] = lambda: self.refresh(page - 1)
        if len(self.panel) > page + 1:
            echo(msg.CHOICE_FORMAT % ("+", msg.NEXT_PAGE))
            self.controls["="] = lambda: self.refresh(page + 1)
            self.controls["+"] = lambda: self.refresh(page + 1)
        if self.goback:
            echo(msg.CHOICE_FORMAT % ("0", msg.GOBACK))
            self.controls["0"] = lambda: self.backmethod()
        if len(self.controls) > 0:
            echo()

    def input(self):
        while True:
            ac = select_func(self)
            if ac not in self.controls.keys():
                warn(msg.ERROR_CHOICE_INVALID)
                echo()
            else:
                break
        return ac

    def handle(self, ac):
        self.controls[ac]()
        return ac


class MenuItem(object):
    """
    菜单项封装控件
    """
    def __init__(self, showword, bold=True, comments=None, value=None, goto=None, validator=None):
        self.showword = showword
        self.value = value
        self.goto = goto
        self.validator = validator
        self.comments = comments
        self.choosable = True
        self.bold = bold
        self.highlight = False

        self.idx = 0
        self.key = None

        if self.value is None:
            self.value = self.showword

    def _comment(self):
        if self.comments is not None:
            for c in self.comments:
                echo()
                #words(fixed(width, n="       〈%s〉" % c))
                if not self.choosable:
                    comment_str = colored("       %s" % c, color="grey", attrs=["bold"])
                else:
                   comment_str = "       %s" % c
                words(fixed(width, n=comment_str))

    def render(self, pagesize=9, columns=1, width=50, total=100):
        """
        显示菜单项，多列显示模式暂不支持附注
        """
        colidx = self.idx % columns
        if not self.choosable:
            words(fixed(width, n=colored(msg.CHOICE_FORMAT % (self.key, self.showword), color="grey", attrs=["bold"])))           
        else:
            bcolor = "on_blue" if self.highlight else None
            attrs = ["bold"] if self.bold else None
            words(fixed(width, n=colored(msg.CHOICE_FORMAT % (self.key, self.showword), on_color=bcolor, attrs=attrs)))
        if self.comments is not None:
            for c in self.comments:
                echo()
                #words(fixed(width, n="       〈%s〉" % c))
                if not self.choosable and c.find("\033[") < 0:
                    comment_str = colored("       %s" % c, color="grey", attrs=["bold"])
                else:
                    comment_str = "       %s" % c
                words(fixed(width, n=comment_str))
        if colidx == columns - 1 or self.idx == total - 1 or self.idx == pagesize - 1:
            echo()
            #self.comment()


class Menu(Interactive):
    """
    菜单封装控件
    """
    def __init__(self, items, title=None, uppanel=[], inpanel=[],
                 goback=False, validator=None, 
                 keylist=None, backmethod=None, multiple=False, multiple_num=-1, 
                 columns=1, width=50):

        self.selected = 1
        
        self.items = items
        self.title = title
        self.goback = goback
        self.validator = validator
        self.uppanel = uppanel
        self.inpanel = inpanel

        self.acset = {}
        self.disabled = set()
        self.controls = {}
        self.keylist = keylist
        
        self.page = 0
        self.pagesize = 9
        
        self.columns = columns
        self.width = width

        self.multiple = multiple
        self.multiple_num = multiple_num

        if backmethod is None:
            self.backmethod = backmenu
        else:
            self.backmethod = backmethod

        for i in range(len(self.items)):
            self.items[i].idx = i

        if self.keylist is None:
            self.keylist = [str(i) for i in range(1, 10)]

    def validate(self, itm):
        if self.validator is not None and not self.validator(itm):
            ret = False
        elif itm.validator is not None and not itm.validator(itm):
            ret = False
        else:
            ret = True
        itm.choosable = ret
        return ret

    def render(self, page=0, pagesize=9, shownone=True, highlights=None):
        self.starty = position_func(self)[0]
        self.page = page
        self.pagesize = pagesize
        for l in self.uppanel:
            echo(l)
        if not blankline():
            echo()
        if self.title is not None:
            echo(self.title)
            echo()
        for l in self.inpanel:
            echo(l)
        if not blankline():
            echo()
        if shownone and len(self.items) == 0:
            echo(colored(msg.NONE, color="grey", attrs=["bold"]))
        for itm in self.items[page * pagesize: page * pagesize + pagesize]:
            itm.key = self.keylist[itm.idx % pagesize]
            itm.highlight = highlights is not None and idx in highlights
            if not self.validate(itm):
                self.disabled.add(itm.key)
            itm.render(pagesize=pagesize, columns=self.columns, width=self.width, total=len(self.items))
            self.acset[itm.key] = itm
        if len(self.acset) != 0 or shownone:
            echo()
        if page > 0:
            echo(msg.CHOICE_FORMAT % ("-", msg.PREVIOUS_PAGE))
            self.controls["-"] = lambda: self.refresh(page - 1, pagesize, shownone)
        if len(self.items) > page * pagesize + pagesize:
            echo(msg.CHOICE_FORMAT % ("+", msg.NEXT_PAGE))
            self.controls["="] = lambda: self.refresh(page + 1, pagesize, shownone)
            self.controls["+"] = lambda: self.refresh(page + 1, pagesize, shownone)
        if self.goback:
            echo(msg.CHOICE_FORMAT % ("0", msg.GOBACK))
            self.controls["0"] = lambda: self.backmethod()
        if len(self.controls) > 0:
            echo()
        BACK_MENU.append((self, [page, pagesize, shownone]))

    def check_length(self, ac_list):
        if len(ac_list) == 0:
            warn(msg.ERROR_CHOICE_INVALID)
            echo()
            return False
        if not self.multiple and len(ac_list) > 1:
            warn(msg.ERROR_CHOICE_INVALID)
            echo()
            return False
        if self.multiple and self.multiple_num > 0 and len(ac_list) > self.multiple_num:
            warn(msg.ERROR_CHOICE_TOO_MUCH)
            echo()
            return False
        return True

    def input(self):
        while True:
            valid = True
            ac_raw = select_func(self)
            ac_list = ac_raw.split()
            valid = self.check_length(ac_list)
            if not valid:
                continue
            for ac in ac_list:
                if ac not in self.acset and ac not in self.controls.keys():
                    warn(msg.ERROR_CHOICE_INVALID)
                    echo()
                    valid = False
                elif ac in self.disabled:
                    warn(msg.ERROR_CHOICE_DISABLED)
                    echo()
                    valid = False
                if not valid:
                    break
            if not valid:
                continue
            elif self.multiple:
                echo()
                echo(msg.CHOICE_MULTIPLE_ENSURE % "、".join(ac_list))
                echo()
                ret = sure(msg.CONFIRMATION)
                echo()
                if ret:
                    break
            else:
                break
        #echo()
        return ac_list

    def handle(self, ac_list):
        ret = []
        for ac in ac_list:
            if ac in self.acset:
                #BACK_MENU.append((self, [self.page, self.pagesize, self.shownone]))
                #itm = self.items[self.page * self.pagesize + int(ac) - 1]
                itm = self.acset[ac]
                if not self.multiple and itm.goto is not None:
                    return itm.goto(itm.value)
                    #goto_ret = itm.goto(itm.value)
                    #if goto_ret != '\0':
                    #    return goto_ret
                ret.append(itm.value)
            else:
                BACK_MENU.pop()
                #return self.controls[ac]()
                if ac != '0':
                    return self.controls[ac]()
                else:
                    self.controls[ac]()
                #return '\0'
        if self.multiple:
            return ret
        elif len(ret) > 0:
            return ret[0]
        else:
            return None


def menuitem(showword, bold=True, comments=None, value=None, goto=None, validator=None):
    return MenuItem(showword, bold=bold, comments=comments, value=value, goto=goto, validator=validator)


def menu(items, title=None, page=0, pagesize=9, uppanel=[], inpanel=[],
         goback=False, shownone=True, keylist=None,
         validator=None, highlights=None, backmethod=None, 
         multiple=False, multiple_num=-1, columns=1, width=50):
    m = Menu(items, title=title, goback=goback, uppanel=uppanel, inpanel=inpanel, validator=validator, 
             keylist=keylist, backmethod=backmethod, multiple=multiple, multiple_num=multiple_num, 
             columns=columns, width=width)
    m.render(page=page, pagesize=pagesize, shownone=shownone, highlights=highlights)
    return m.done()


def pages(contents, title=None, goback=False, backmethod=None, page=0):
    c = Pages(contents, title=title, goback=goback, backmethod=backmethod)
    c.render(page=page)
    return c.done()


def backmenu():
    bm = BACK_MENU.pop()
    bm[0].render(*bm[1])
    return bm[0].done()
    
    
def popmenu():
    BACK_MENU.pop()


def cleanmenu():
    BACK_MENU = []


class MenuGroup(Interactive):
    pass


if __name__ == "__main__":
    from proj.entity import Person

    p1 = Person.one("PERSON_SONG_TIANYONG")
    p2 = Person.one("PERSON_XIE_HUI")
    p3 = Person.one("PERSON_ZHAO_SHENJI")
    pmenu = [menuitem(p1.name, value=p1),
             menuitem(p2.name, value=p2),
             menuitem(p3.name, value=p3)]
    ret = menu(pmenu, multiple=True, multiple_num=2)
