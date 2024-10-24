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