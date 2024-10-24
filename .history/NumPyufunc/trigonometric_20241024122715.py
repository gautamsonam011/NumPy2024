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