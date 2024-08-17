import numpy as np
a=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
b=np.array([ [1,1,1],[2,2,2],[3,3,3] ])
c=np.array([ [5,5,5],[6,6,6],[7,7,7] ])
print(f"A:\n{a}")
print(f"B:\n{b}")
print(f"C:\n{c}")
print(f"After multiplication:\n{np.dot(np.dot(a,b),c)}")
