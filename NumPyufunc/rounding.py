# Rounding Decimals 

# There are primarily five ways of rounding off decimals in numpy 

# truncation
# fix 
# rounding 
# floor 
# ceil 

# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions 

import numpy as np 

arr = np.trunc([-3.6565443, 7.32435, 6.435354])
print(arr)

arr = np.fix([54.5342, -6.45342, 78.4353, 12.4564])
print(arr)

# Rounding 

# around() 

arr = np.around([23.5689, 65.896, 5.790])
print(arr)

# Floor 

# The floor() function rounds off decimal to nearest lower integer 

arr = np.floor([-5.6533, 34.3234, 56.6443])
print(arr)


# Ceil 

# The ceil() function rounds off decimal to nearest upper integer 

arr = np.ceil([32.5467, 7.8967, -65.4353])
print(arr)