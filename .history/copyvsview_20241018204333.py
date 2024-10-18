import numpy as np 

# Copy 

arr = np.array([2, 4, 6, 8, 9])
x = arr.copy()
arr[0] = 45
print(arr)
print(x)

# View 

arr = np.array([3, 5, 8, 9, 1])
x = arr.view()
arr[0] = 78

print(arr)
print(x)

# make changes in the view: - 

arr = np.array([34, 67, 98, 21, 45, 90])
x = arr.view()

x[0] = 74

print(arr)
print(x)