import numpy as np
def symm(matrix):
    return (matrix == matrix.T).all()
def skew(matrix):
    return (matrix == -matrix.T).all()

matrix=np.array([ [0,1,-2],[-1,0,3],[2,-3,0] ])
if symm(matrix):
    print("Symmetric")
elif skew(matrix):
    print("Skew matrix")
else:
    print("Matrix is neither symmetric nor skew symmetric")