# sin()
# cos()
# tan()

import numpy as np 

x = np.sin(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)


# Convert degrees into radians 

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)
print(x)


# Radians to degrees 

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)
print(x)

# Finding Angles 

# arcsin(), arccos() and arctan() 

x = np.arcsin(1.0)
print(x)

# Angles of each value in arrays 

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)
print(x)

# Hypotenues 
# Finding hyptenues using pythagoras theorem in numpy 
# hypot()

base = 3
perp = 4

x = np.hypot(base, perp)
print(x)

# Hyperbolic functions 

# sinh(), cosh() and tanh()

x = np.sinh(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)
print(x)