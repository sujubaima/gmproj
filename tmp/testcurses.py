# -- coding: utf-8 --
import os
import sys
import curses
import locale
import struct

from curses.textpad import Textbox
from curses.textpad import rectangle

locale.setlocale(locale.LC_ALL, '')

tmp = []

scr = None

class MyTextbox(Textbox):

    def _insert_printable_char(self, ch):
        (y, x) = self.win.getyx()
        if y < self.maxy or x < self.maxx:
            if self.insert_mode:
                oldch = self.win.inch()
            # The try-catch ignores the error we trigger from some curses
            # versions by trying to write into the lowest-rightmost spot
            # in the window.
            try:
                self.win.addstr(ch)
            except curses.error:
                pass
            if self.insert_mode:
                (backy, backx) = self.win.getyx()
                #if curses.ascii.isprint(oldch):
                self._insert_printable_char(oldch)
                self.win.move(backy, backx)

    def do_command(self, ch):
        "Process a single editing command."
        (y, x) = self.win.getyx()
        self.lastcmd = ch
        if ch == curses.ascii.SOH:                           # ^a
            self.win.move(y, 0)
        elif ch in (curses.ascii.STX,curses.KEY_LEFT, curses.ascii.BS,curses.KEY_BACKSPACE):
            uchar_1 = unichr(self.win.inch(y, x - 2) if x >= 2 else 1)
            uchar_2 = unichr(self.win.inch(y, x - 1) if x >= 2 else 1)
            if u'\u4e00' <= uchar_1 and uchar_1 <= u'\u9fff' and u'\u4e00' <= uchar_2 and uchar_2 <= u'\u9fff':
                mv_step = 2
            else:
                mv_step = 1
            if x > mv_step - 1:
                self.win.move(y, x - mv_step)
            elif y == 0:
                pass
            elif self.stripspaces:
                self.win.move(y-1, self._end_of_line(y-1))
            else:
                self.win.move(y-1, self.maxx)
            if ch in (curses.ascii.BS, curses.KEY_BACKSPACE):
                self.win.delch()
                if mv_step == 2:
                    self.win.delch()
        elif ch == curses.ascii.EOT:                           # ^d
            self.win.delch()
        elif ch == curses.ascii.ENQ:                           # ^e
            if self.stripspaces:
                self.win.move(y, self._end_of_line(y))
            else:
                self.win.move(y, self.maxx)
        elif ch in (curses.ascii.ACK, curses.KEY_RIGHT):       # ^f
            uchar = unichr(self.win.inch(y, x))
            if u'\u4e00' <=  uchar and uchar <= u'\u9fff': 
                mv_step = 2
            else:
                mv_step = 1
            if x < self.maxx - mv_step + 1:
                self.win.move(y, x + mv_step)
            elif y == self.maxy:
                pass
            else:
                self.win.move(y+1, 0)
        elif ch == curses.ascii.BEL:                           # ^g
            return 0
        elif ch == curses.ascii.NL:                            # ^j
            if self.maxy == 0:
                return 0
            elif y < self.maxy:
                self.win.move(y+1, 0)
        elif ch == curses.ascii.VT:                            # ^k
            if x == 0 and self._end_of_line(y) == 0:
                self.win.deleteln()
            else:
                # first undo the effect of self._end_of_line
                self.win.move(y, x)
                self.win.clrtoeol()
        elif ch == curses.ascii.FF:                            # ^l
            self.win.refresh()
        elif ch in (curses.ascii.SO, curses.KEY_DOWN):         # ^n
            if y < self.maxy:
                self.win.move(y+1, x)
                if x > self._end_of_line(y+1):
                    self.win.move(y+1, self._end_of_line(y+1))
        elif ch == curses.ascii.SI:                            # ^o
            self.win.insertln()
        elif ch in (curses.ascii.DLE, curses.KEY_UP):          # ^p
            if y > 0:
                self.win.move(y-1, x)
                if x > self._end_of_line(y-1):
                    self.win.move(y-1, self._end_of_line(y-1))
        elif y < self.maxy or x < self.maxx:
            self._insert_printable_char(ch)
        return 1

    

def validate(arg):
    global tmp
    if arg <= 32 or arg > 255:
        return arg
    tmp.append(arg)
    b = struct.pack("B" * len(tmp), *tmp)
    ret = None
    try:
        scr.refresh()
        ret = b.decode("utf-8").encode("utf-8")
        tmp = []
    except Exception as e:
        pass
    #scr.refresh()
    #print type(ret)
    return ret
    
    
def main(myscreen):
    global scr
    scr = myscreen
    curses.init_pair(1, 7, 0)
    myscreen.addstr(0, 0, "你")
    myscreen.addstr(0, myscreen.getyx()[1], "好←", curses.color_pair(1) | curses.A_BLINK)
    myscreen.addstr(0, myscreen.getyx()[1], "吗")
    myscreen.refresh()

    #myscreen.move(2, 0)
    editwin = curses.newwin(1,30, myscreen.getyx()[0], myscreen.getyx()[1])
    #rectangle(myscreen, 1, 0, 3, 1 + 30 + 1)
    myscreen.refresh()

    box = MyTextbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit(validate)

    # Get resulting contents
    message = box.gather()

    #a = myscreen.getstr()
    #myscreen.addstr(1, 0, a)
    #myscreen.refresh()
    myscreen.addstr(4, 0, message)
    myscreen.getch()
    curses.endwin()


curses.wrapper(main)
