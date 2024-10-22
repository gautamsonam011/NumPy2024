# Normal Distribution 

# random.normal() method 

from numpy import random 

x = random.normal(size = (2, 3))
print(x)

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.

x = random.normal(loc = 1, scale = 2, size = (2, 3))
print(x)