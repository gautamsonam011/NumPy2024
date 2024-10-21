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