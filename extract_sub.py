import numpy as np
A=np.array([ [1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18,], [16,17,18,19,20,21], [18,19,20,21,22,23]])
print(f"Matrix A:\n{A}")
B=np.array([ [1,2,3],[4,5,6],[7,8,9]])
print(f"Matrix B:\n{B}")
sub_matrix=A[2: , ]