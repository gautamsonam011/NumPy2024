# Summations 

# What is the difference between summation and addition? 

# Addition is done between two arguments whereas summation happens over n elements. 

import numpy as np 

# add()  function

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

newarr = np.add(arr1, arr2)

print(newarr)

# sum() function

arr1 = np.array([34, 5, 7, 8, 21])
arr2 = np.array([23, 67, 8, 9, 22])

newarr = np.sum([arr1, arr2])
print(newarr)

# Summation over an axis 

# axis = 1

arr1 = np.array([21, 34, 67, 90, 54, 32])
arr2 = np.array([45, 78, 98, 65, 43, 32])

newarr = np.sum([arr1, arr2], axis=1)
print(newarr) 


# Cummulative Sum 

# cumsum() function 

arr = np.array([21, 45, 67, 89, 44, 32])

newarr = np.cumsum(arr)
print(newarr)


# Products 

# To find the product of the elements in an array, use the prod() function. 
# 1*2*3 = 6

arr = np.array([21, 45, 67, 89, 43, 56])

x = np.prod(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])
print(x)

# Product over an axis 

# axis=1

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 1])

newarr = np.prod([arr1, arr2], axis=1)
print(newarr)