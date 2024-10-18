import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array(['Python', 'Java', 'C#', 'JavaScript'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5], dtype = 'S')
print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well. 

arr = np.array([1, 2, 3, 4], dtype = 'i4')
print(arr)
print(arr.dtype)

# what if a value can not be converted 

# arr = np.array(['a', '3', '6'], dtype = 'i') invalid literal for int() with base 10: 'a'
# print(arr)

# Converting data type on existing arrays 

arr = np.array([3.5, 7.9, 2.4, 8.9])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

new = arr.astype(int)
print(new)
print(new.dtype)

arr = np.array([1, 0, 4, 7])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

