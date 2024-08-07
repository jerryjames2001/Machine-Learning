import numpy as np
arr1=np.array([1,2,3,4])
print(f"Matrix :{arr1}")
print(f"Diagonal matrix\n{np.diag(arr1)}")

arr2=np.array([ [1,2,3],[4,5,6],[7,8,9]])
print(f"2D square matrix:\n{arr2}")
print(f"2D diagonal elements: {np.diag(arr2)}")

arr3=np.array([ [1,2,3],[4,5,6]])
print(f"Non square matrix:\n{arr3}")
print(f"Non square diagonal{np.diag(arr3)}")