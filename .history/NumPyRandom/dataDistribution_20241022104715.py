from numpy import random

x = random.choice([3, 5, 2, 8], p=[0.1, 0.3, 0.8, 0.0], size=(100))

print(x)