# Access Array Elements:--------> 

import numpy as np 

arr = np.array([1, 3, 5, 7])

print(arr[0])

print(arr[2])

print(arr[0] + arr[3])

# Access 2-D Arrays:-----> 

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(('2nd element on 1st row:', arr[0, 1]))

# Access 3-D Arrays:------> 

arr = np.array([[[1, 2, 3], [5, 6, 7]], [[3, 5, 7], [9, 7, 8]], [[4, 2, 3], [1, 9, 6]]])

print(arr[0, 1, 2])
print(arr[1, 1, 2 ])
print(arr[2, 0, 0])