import time


def register(cls, name):
    setattr(cls, name, property(lambda self: cls.getproperty(self, name)))


class TestDynamicProperty(object):

    def __init__(self, val):
        self.val = val

    def getproperty(self, name):
        return "valueof%s, %s" % (name, self.val)


register(TestDynamicProperty, "akey")    
register(TestDynamicProperty, "bkey")
register(TestDynamicProperty, "ckey")


if __name__ == "__main__":
    t1 = time.time()
    for i in range(1000):
        klass = TestDynamicProperty(98)
    t2 = time.time()
    print("初始化1000个动态property类耗时：%ss" % (t2 - t1))
    print(klass.akey)
    print(klass.bkey)
    print(klass.ckey)
    print(klass.bkey)
    print(klass.akey)
