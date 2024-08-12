import numpy as np
arr=np.array([ [1,2,3],[4,5,6],[7,8,9]])
x_mull=np.multiply(arr,np.multiply(arr,arr))
print(f"Matrix cube using multiply():\n{x_mull}")
print(f"Matrix cube using X * X * X\n{arr*arr*arr}")
print(f"power \n{np.power(arr,3)}")
print(f"** operator \n{arr ** 3}")

print(f"Identity matrix \n{np.identity(arr.shape[0])}")
print("Matrix to different powers")
print(f"power 2: {np.power(arr,2)}")
print(f"power 3: {np.power(arr,3)}")
print(f"power 4: {np.power(arr,4)}")