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

arr = np.array([3, 6, 9, 12])

x = np.lcm.reduce(arr)
print(x)

arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)

# Finding GCD (Greatest Common Denominator) 
# HCF(Highest Common Factor) 

num1 = 6
num2 = 9

x = np.gcd(num1, num2)
print(x)

# Finding GCD in Arrays 

# reduce() method 

arr = np.array([23, 45, 78, 90, 65, 43])

x = np.gcd.reduce(arr)

print(x)