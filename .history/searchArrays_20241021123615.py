# Numpy searching arrays 

import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 5])
newarr = np.where(arr == 5)
print(newarr)

# Find the indexes where the values are even 

arr = np.array([1, 2, 3, 4, 6, 8, 56, 43, 24])
newarr = np.where(arr%2 == 0)
print(newarr)

# Find the indexes where the values are odd 

newarr = np.where(arr%2 != 0)
print(newarr)

# OR 

newarr = np.where(arr%2 == 1)
print(newarr)

# Search sorted 

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 9)

print(x)

# search from the right side 

arr = np.array([5, 6, 8, 3])

x = np.searchsorted(arr, 6, side = 'right')
print(x)

# multiple values 

arr = np.array([23, 45, 78, 90, 83, 28])

s = np.searchsorted(arr, [2, 4, 6])
print(s)

s = np.searchsorted(arr, [78, 90, 23])
print(s)

# =======> Numpy Array sort <==============

arr = np.array([3, 6, 0, 7, 8, 2])

print(np.sort(arr))

arr = np.array(['Python', "Java", "HTML", "Django"])

print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

# Sorting a 2-d array 

arr = np.array([[3, 5, 7], [7, 9, 2]])
print(np.sort(arr))

# 3-D 

arr = np.array([[[1, 2], [7, 4], [9, 8]]])
print(np.sort(arr))