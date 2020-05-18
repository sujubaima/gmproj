#-*- coding:utf-8 -*-  
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from PIL import Image  
from proj.console import interaction as inter
from thirdparty.ansiterm.termcolor import colored
  
MAX_WIDTH = 160
MAX_HEIGHT = 40
  
#ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")  
ascii_char = list("~/. ")  
  
def get_char(r, g, b, alpha=256, char_list=None):#alpha透明度  
    if alpha == 0:  
        return ' '  
    length = len(ascii_char)  
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length  
    if char_list is None:
        charlist = ascii_char
    else:
        charlist = char_list
    return charlist[int(gray / unit)] 
  
def charimg(path, width=-1, height=-1, char_list=None):  
    IMG = path
    ew = width
    eh = height
    im = Image.open(IMG)
    if ew == -1 or eh == -1:
        rw, rh = im.size
        if rw * 16 / 9  / rh >= MAX_WIDTH / MAX_HEIGHT:
            final_width = MAX_WIDTH
            final_height = MAX_WIDTH * 9 * rh / 16 / rw
        else:
            final_height = MAX_HEIGHT
            final_width = MAX_HEIGHT * rw * 16 / rh / 9
    else:
        final_width = ew * 16 / 9
        final_height = eh
    #print final_width, final_height
    im=im.resize((final_width, final_height), Image.NEAREST)  
    lines = []
    for i in range(final_height):  
        lines.append([])
        for j in range(final_width):  
            lines[i].append(get_char(*im.getpixel((j, i)), char_list=char_list))
    return lines

def locate(lines, name, pt):
    y, x = pt
    lines[x][y] = "○" 
    nl = inter.length(name)
    label_loc = [(x - 1, y - nl / 2)]
    for loc in label_loc:
        lines[loc[0]][loc[1]] = name
        for i in range(1, nl):
            lines[loc[0]][loc[1] + i] = ""


if __name__ == "__main__":
    #lines = charimg("bigmap.png")
    #locate(lines, colored("北京", color="red", attrs=["bold"]), (int(float(58) * 9 / 8), int(float(len(lines))) / 4))
    lines = charimg("luoming.png")
    for l in lines:
        print("".join(l))
  
   
