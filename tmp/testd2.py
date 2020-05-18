class Dim2Dict(dict):

    def __init__(self):
        self.d = {}
    
    def __setitem__(self, key, value):
        k, subk = key
        if k not in self.d:
            self.d[k] = {}
        self.d[k][subk] = value
        

    def __getitem__(self, key):
        k, subk = key
        return self.d[k][subk]

def setdict(d, key, value):
    k, subk = key
    if k not in d:
        d[k] = {}
    d[k][subk] = value


def getdict(d, key):
    k, subk = key
    return d[k][subk]


if __name__ == "__main__":
    t = Dim2Dict()
    t[(1, 2)] = "test"
    print t[(1, 2)]
    
