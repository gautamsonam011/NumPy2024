from numpy import random 

# Generate random number with int data type

x = random.randint(100)
print(x)

# Generate random float 

x = random.rand()
print(x)

# Generate random array 

# randint() and size 

a = random.randint(100, size = (5))

print(a)