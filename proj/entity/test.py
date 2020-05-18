import math

base = 100
rate = 1.2

degree = 10

def test(x):
    if x >= 0:
        return base * math.pow(rate, x)
    else:
        return base + base / math.pow(rate, degree) - base / math.pow(rate, (degree + x))

for i in range(-1 * degree, degree):
     test(i)
