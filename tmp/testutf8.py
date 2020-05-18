# -- coding: utf-8 --
import struct

a = "如"
b = struct.pack("BBB", 229, 166, 130)
print b.decode("utf-8")
