import re
import time

from proj.console import ui

word = ui.colored("你好", color="red", on_color="on_cyan", attrs=["bold"])

def ra(word):
    tword = re.sub("\033[[0-9]+m", "", word)
    return tword


def rb(word):
    tword = word
    kidx = tword.find("\033[")
    while kidx >= 0:
        tmpword = tword
        tword = tword[kidx:]
        while tword.startswith("\033["):
            tword = tword[tword.find("m") + 1:]
        if kidx >= 0:
            tword = tmpword[:kidx] + tword
        kidx = tword.find("\033[")
        if tword != word:
            tword = tword.replace("\033[0m", "")
    return tword

tlist = []
for i in range(1000):
    t1 = time.time()
    rb(word)
    t2 = time.time()
    tlist.append(t2 - t1)
print(sum(tlist))
