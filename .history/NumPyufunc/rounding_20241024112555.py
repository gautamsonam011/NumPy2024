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