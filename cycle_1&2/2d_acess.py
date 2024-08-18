import numpy as np
arrays=np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(f"elements without 1st row \n{arrays[1:]}")
print(f"Elements without last column\n{arrays[:,:-1]}")
print(f"Elements from 1&2nd column of 2&3rd row\n{arrays[1:3, 0:2]}")
print(f"2nd and 3rd elements from 1st row\n{arrays[0,1:3]}")
