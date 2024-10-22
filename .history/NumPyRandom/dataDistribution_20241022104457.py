from numpy import random 

x = random.choice([1, 2, 3, 4], p=[0.1, 0.3, 0.5, 0.7], size = (100))
print(x)