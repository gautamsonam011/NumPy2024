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


for x in arr:
    for y in x:
        for z in y:
            print(z) 

# Iterating arrays using nditer()

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

# Iterating array with different data type 

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags = ['buffered'], op_dtypes=['S']):
    print(x)


# Iterating with different step size 

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)

# Enumerated iteration using ndenumerate()

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

# 2D
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 

for idxm, x in np.ndenumerate(arr):
    print(idx, x)