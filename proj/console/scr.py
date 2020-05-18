# -- coding: utf-8 -- 
import struct
import curses

from curses.textpad import Textbox


stdscr = None


wrapper = curses.wrapper


AMAP = {"bold": curses.A_BOLD,
        "dark": curses.A_DIM,
        "underline": curses.A_UNDERLINE}
CMAP = {"black": curses.COLOR_BLACK,
        "white": curses.COLOR_WHITE,
        "grey": curses.COLOR_BLACK,
        "red": curses.COLOR_RED,
        "yellow": curses.COLOR_YELLOW,
        "blue": curses.COLOR_BLUE,
        "cyan": curses.COLOR_CYAN,
        "green": curses.COLOR_GREEN,
        "magenta": curses.COLOR_MAGENTA}


CPAIRS = {}


context = {}


class UTF8Textbox(Textbox):

    charbuf = []

    @staticmethod
    def validate(arg):
        if arg <= 32 or arg > 255:
            return arg
        UTF8Textbox.charbuf.append(arg)
        b = struct.pack("B" * len(UTF8Textbox.charbuf), *UTF8Textbox.charbuf)
        ret = None
        try:
            ret = b.decode("utf-8").encode("utf-8")
            UTF8Textbox.charbuf = []
        except Exception as e:
            pass
        return ret

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

    def edit(self, validate=None):
        if validate is None:
            validate = UTF8Textbox.validate
        Textbox.edit(self, validate)

    def gather(self):
        "Collect and return the contents of the window."
        result = ""
        for y in range(self.maxy+1):
            self.win.move(y, 0)
            result += self.win.instr().strip()
            #stop = self._end_of_line(y)
            #if stop == 0 and self.stripspaces:
            #    continue
            #for x in range(self.maxx+1):
            #    if self.stripspaces and x > stop:
            #        break
            #    uchar = unichr(self.win.inch(y, x))
            #    self.win.refresh()
            #     self.win.inch(y, x)
            #    result += uchar
            if self.maxy > 0:
                result += "\n"
        return result


def curses_write(content=""):
    if isinstance(content, Colored):
        for s in content.strlist:
            if not isinstance(s, dict):
                stdscr.addstr(stdscr.getyx()[0], stdscr.getyx()[1], s)
            else:
                flag = 0
                fcolor = s.get("color", "white")
                bcolor = s.get("on_color", "on_black")[3:]
                if (fcolor, bcolor) not in CPAIRS:
                    curses.init_pair(len(CPAIRS) + 1, CMAP[fcolor], CMAP[bcolor])
                    CPAIRS[(fcolor, bcolor)] = len(CPAIRS) + 1
                cpr = CPAIRS[(fcolor, bcolor)]
                flag = 0
                for at in s.get("attrs", []):
                    flag |= AMAP[at]
                stdscr.addstr(stdscr.getyx()[0], stdscr.getyx()[1],
                              s["text"], curses.color_pair(cpr) | flag)
    else:
        stdscr.addstr(stdscr.getyx()[0], 0, content)


def curses_read(content=""):
    curses_write(content)
    editwin = curses.newwin(1, 30, stdscr.getyx()[0], stdscr.getyx()[1])
    stdscr.refresh()
    box = UTF8Textbox(editwin)
    box.edit()
    rs = box.gather()
    stdscr.move(stdscr.getyx()[0] + 1, 0)
    stdscr.refresh()
    return rs.strip()


def curses_select(menu):
    currentyx = stdscr.getyx()
    stdscr.refresh()
    while True:
        stdscr.move(menu.starty, 0)
        menu.render(highlights=[menu.selected])
        ch = stdscr.getch()
        if ch == curses.KEY_DOWN:
            menu.selected += 1
        elif ch == curses.KEY_UP and menu.selected > 1:
            menu.selected -= 1
        elif ch in (curses.KEY_ENTER, 10):
            break
    stdscr.move(currentyx[0], currentyx[1])
    return str(menu.selected)
    #stdscr.refresh()
    #raw_input()


def curses_position(arg):
    return stdscr.getyx()


def curses_refresh(arg):
    pass
