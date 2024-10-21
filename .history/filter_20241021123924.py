# Filtering arrays 

import numpy as np 

arr = np.array([45, 67, 32, 78])

x = [True, False, True, False]

newarr = arr[x]
print(newarr)