import numpy as np
ss=3
arr1=np.random.randint(1,10,size=(ss,ss))
print(f"Matrix:\n{arr1}")
print(f"Inverse of matrix: \n{np.linalg.inv(arr1)}")
print(f"Matrix rank: {np.linalg.matrix_rank(arr1)}")
print(f"Matrix Determinant: {np.linalg.det(arr1)}")
print(f"Matrix as 1D array: {arr1.flatten()}")
eigenvalues, eigenvectors = np.linalg.eigh(arr1)
print(f"Eigen values: {eigenvalues}")
print(f"Eigen vectors: \n{eigenvectors}")