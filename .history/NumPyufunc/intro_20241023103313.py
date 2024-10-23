#  Without ufunc, we can use python's built in zip() method:

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

z = []

for i, j in zip(x, y):
    z.append(i+j)
print(z)   


# Numpy has a ufunc for called add(x, y) that will produce the same result 

import numpy as np 

x = [34, 67, 89, 23, 12, 89]
y = [1, 2, 3, 4, 5, 6]

z = np.add(x, y)
print(z)