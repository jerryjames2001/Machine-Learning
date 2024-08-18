import numpy as np
x=np.array([[1,2],[3,4]])
y=np.random.rand(*x.shape)
print(f"Result x2 + 2y: \n{x*2+2*y}")