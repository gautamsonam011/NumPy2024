from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns


# Normal Distribution 

# random.normal() method 


x = random.normal(size = (2, 3))
print(x)

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.

x = random.normal(loc = 1, scale = 2, size = (2, 3))
print(x)

# Visualization of normal distribution 

sns.distplot(random.normal(size = (1000), hist = False))
plt.show()