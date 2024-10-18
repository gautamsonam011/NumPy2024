import numpy as np 

arr = np.array([2, 4, 6, 8, 9])
x = arr.copy()
arr[0] = 45
print(arr)
print(x)