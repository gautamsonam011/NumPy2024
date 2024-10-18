import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array(['Python', 'Java', 'C#', 'JavaScript'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5], dtype = 'S')
print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well. 

arr = np.array([1, 2, 3, 4], dtype = 'i4')
print(arr)