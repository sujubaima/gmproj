class A(object):

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, v):
        self._a = v + 1


aobj = A()
setattr(aobj, "a", 99)
print(aobj.a)
        
