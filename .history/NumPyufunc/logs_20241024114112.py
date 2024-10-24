# Logs:---------> 

# Numpy provides functions to perform log at the base 2, e and 10. 

# Log at Base 2 
# Use the log2() function to perform log at the base 2. 

import numpy as np 

arr = np.arange(1, 10)
print(np.log2(arr))

# Log at Base 10 

# Use the log10() function to perform log at the base 10. 

arr = np.arange(1, 10)
print(np.log10(arr))


# Natural log, or log at base e 

# use the log() function to perform log at the base e 

arr = np.arange(1, 10)
print(np.log(arr))

# Log at any base 
# frompyfunc() function 
# math.log() 

from math import log 

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))