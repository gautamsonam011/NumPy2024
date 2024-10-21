# Numpy searching arrays 

import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 5])
newarr = np.where(arr == 5)
print(newarr)