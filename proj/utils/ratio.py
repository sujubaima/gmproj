# -- coding: utf-8 --

import math
import random

def random_gap(base, gap):
    if base >= 0:
        return random.randint(int(base * (1 - gap)), int(base * (1 + gap)))
    else:
        return random.randint(int(base * (1 + gap)), int(base * (1 - gap)))


def if_rate(ratio):
    return random.randint(1, 10000) <= ratio * 10000


class Exponential(object):

    def __init__(self, middle=None, lower=None, upper=None, degree=50, base=1):
        self.middle = middle
        self.lower = lower
        self.upper = upper
        self.degree = degree
        self.base = base
        if self.middle is None:
            self.middle = math.pow(self.lower * self.upper, 0.5)
        elif self.upper is None:
            self.upper = self.middle * self.middle / self.lower
        elif self.lower is None:
            self.lower = self.middle * self.middle / self.upper
        self.uprate = math.pow(float(self.upper) / self.middle, 1.0 / self.degree)
        self.downrate = math.pow(float(self.middle) / self.lower, 1.0 / self.degree)

    def value(self, exponent, base=None):
        if base is None:
            base = self.base
        if exponent >= 0:
            return base * self.middle * math.pow(self.uprate, exponent)
        else:
            return base * (self.middle + self.middle / math.pow(self.downrate, self.degree) - \
                           self.middle / math.pow(self.downrate, (self.degree + exponent)))
