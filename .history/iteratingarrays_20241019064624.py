import numpy as np 

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

# Iterating 2-D arrays 

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)

# Iterating 3-D arrays 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)