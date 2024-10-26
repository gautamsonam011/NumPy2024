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