from numpy import random

x = random.choice([3, 5, 2, 8], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

# x = random.choice([43, 56, 78, 32, 54], p=[0.1, 0.4, 0.6, 0.0, 0.0], size=(3, 3)) probabilities do not sum to 1
# print(x)