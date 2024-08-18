import numpy as np
arr1=np.arange(1,5)
print(f"Array elements are {arr1}")
#inserting value 10 at index 2
arr1=np.insert(arr1,2,10)
print(f"After insertion elements are: {arr1}")

arr2=np.array([ [1,2,3],[4,5,6]])
print(f"Array elements are\n{arr2}")
arr2=np.insert(arr2 , 2 , [7,8,9] , axis=0)
print(f"After insertion elements are:\n{arr2}")
