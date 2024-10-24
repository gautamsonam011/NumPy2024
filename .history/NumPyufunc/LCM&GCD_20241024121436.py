# Finding LCM (Lowest common multiple) 

import numpy as np 

num1 = 34
num2 = 87

x = np.lcm(num1, num2)
print(x)

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)

# Finding LCM in arrays reduce() method 

arr = np.array([23, 56, 87, 32])

x = np.lcm.reduce(arr)
print(x)