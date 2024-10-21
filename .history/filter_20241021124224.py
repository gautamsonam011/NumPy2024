# Filtering arrays 

import numpy as np 

arr = np.array([45, 67, 32, 78])

x = [True, False, True, False]

newarr = arr[x]
print(newarr)

# Creating the Filter array 

arr = np.array([67, 89, 43, 15])

filter_arr = []

for element in arr:

    if element > 43:
        filter_arr.append(True)

    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)