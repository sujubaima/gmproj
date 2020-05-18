# -- coding: utf-8 --

import unicodedata
def chr_width(c):
    w = unicodedata.east_asian_width(c.decode("utf-8")) 
    print w
    if w in ('F','W','A'):
        return 2
    else:
        return 1


if __name__ == "__main__":
    b = chr_width("⌒")
    #b = chr_width("←")
    print b
