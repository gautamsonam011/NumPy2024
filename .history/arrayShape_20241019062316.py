import numpy as np 

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# (row, column) => (2, 4)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array:', arr.shape)

# Reshaping arrays ==========>

# Reshape from 1-D to 2-D:- 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# Reshape from 1-d to 3-d 

newarr1 = arr.reshape(2, 3, 2)
print(newarr1)

# can we reshape into any shape ?

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(3, 3) cannot reshape array of size 8 into shape (3,3)
newarr = arr.reshape(1, 2)
print(newarr)