import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# check the version of numpy 

print(np.__version__)

arr = np.array((2, 4, 6, 7))
print(arr)

# Dimensions in arrays:======> 

# 0-D Arrays:- 

arr = np.array(56)
print(arr)

# 1-D Arrays:- 

arr = np.array([1, 3, 6, 7])
print(arr)

# 2-D Arrays:- 

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D Arrays:- 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [6, 7, 8]], [[4, 6, 8], [6, 9, 2]]])
print(arr)

# Check number of Dimensions

a = np.array(87)
b = np.array([1, 2, 4, 6, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [7, 8, 9]], [[5, 8, 9], [3, 5, 9]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays:- 

arr = np.array([1, 3, 4, 6], ndmin=5)
print(arr)
print('number of dimensions:', arr.ndim)