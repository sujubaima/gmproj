import time

import testd2

if __name__ == "__main__":
   t = {}
   #t = Dim2Dict()

   t_1 = time.time()
   for i in range(1000):
       #t[i] = {}
       #t.append([])
       for j in range(1000):
           #t[i][j] = (i, j) 
           #t[(i, j)] = (i, j)
           #t[i].append((i,j))
           testd2.setdict(t, (i, j), (i, j))
   t_2 = time.time()

   for i in range(1000):
       for j in range(1000):
           #a = t[i][j]
           #a = t[(i, j)]
           a = testd2.getdict(t, (i, j))

   t_3 = time.time()

   print "write time: %s" % (t_2 - t_1)
   print "read time: %s" % (t_3 - t_2)
