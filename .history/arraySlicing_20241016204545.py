import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:5]) # [start:end]

# If dont pass end 

# print([4:]) invalid syntax

# If we don't pass start point

print(arr[:4])

# Negative slicing 

print(arr[-3: -1])
print(arr[-2: -5])