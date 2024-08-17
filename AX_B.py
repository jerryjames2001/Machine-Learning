import numpy as np
a=np.array([ [2,1,-2],[3,0,1],[1,1,-1] ])
b=np.array([-3,5,-2])
x=np.linalg.solve(a,b)
print(f"Matrix A:\n{a}")
print(f"Matrix B: {b}")
print(f"Matrix x: {x}")