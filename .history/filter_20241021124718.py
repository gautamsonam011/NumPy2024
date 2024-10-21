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


arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating filter directly from array 

arr = np.array([43, 67, 89, 54])

filter_arr = arr > 43

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)