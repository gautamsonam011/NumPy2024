x = [21, 2 , 3, 5]
y = [3, 5, 7, 45]
z = []

for i, j in zip(x, y):
    z.append(i+j)

print(z)    

# Create our own function 

import numpy as np 

def myadd(x, y):
    return x+y 

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]))

print(type(myadd))
print(type(np.add))
print(type(np.concatenate))

# print(type(np.myadd))

if type(np.add) == np.ufunc:
    print('add is ufunc')

else:
    print('add is not ufunc')    

# Absolute 

arr = np.array([-3, 5, 6, -7, -2])

newarr = np.absolute(arr)
print(newarr)

newarr = np.abs(arr)
print(newarr)



arr = np.array([8, 6, -3, 2, 9])

newarr = np.absolute(arr)
print(newarr)


# Finding Union 

arr = np.array([1, 2, 3, 1, 1, 6, 8])
x = np.unique(arr)
print(x)

arr1 = np.array([2, 4, 6, 7, 9, 2, 4, 6])
arr2 = np.array([4, 6, 8, 2, 1, 6, 8, 3])

newarr = np.union1d(arr1, arr2)
print(newarr)

from numpy import random 

x = random.randint(100)
print(x)

x = random.rand()
print(x)

x = random.randint(100, size = (5))
print(x)

x = random.randint(100, size=(3, 5))
print(x)

# Floats 

x = random.rand(5)
print(x)

x = random.rand(3, 4)
print(x)