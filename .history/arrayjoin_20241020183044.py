import numpy as np 

arr1 = np.array([1, 2, 3, 4])

arr2 = np.array([4, 5, 6, 7])

arr = np.concatenate((arr1, arr2))

print(arr)

# 2-D 

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

# Joining arrays using stack function 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis = 1)

print(arr)

# Stcking along rows 

# hstack()

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr = np.hstack((arr1, arr2))

print(arr)