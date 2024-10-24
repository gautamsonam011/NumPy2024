# NumPy Set Operations 

# What is a set?

# A set in mathematics is a collection of unique elements. 

# Create sets in numpy 

# unique() method 

import numpy as np 

arr = np.array([1, 1, 2, 4, 6, 8, 9])
x = np.unique(arr)
print(x)

# Finding Union 
# union1d() method 

arr1 = np.array([1, 2,3 , 5, 7, 8])
arr2 = np.array([3, 5, 7, 9, 4, 3])

newarr = np.union1d(arr1, arr2)
print(newarr)


# Finding Intersection 

# intersection1d() method 

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([3, 5, 7, 9, 4, 2])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

# Finding Difference 

# setdiff1d() method 

set1 = np.array([1, 2, 3, 4])
set2 = np.array([6, 8, 9, 4])

newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)

# Finding Symmetric Difference 

# To find only the values that are NOT present in BOTH sets, use the setxor1d() method. 

set1 = np.array([1, 2, 3, 4, 5])
set2 = np.array([3, 4, 6, 8, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)