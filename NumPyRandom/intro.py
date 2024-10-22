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

# Generate a 2-D 

x = random.randint(100, size = (3, 5))
print(x)

# Floats the rand() method also allow you to specify the shape of the array 

a = random.rand(5)
print(a)

# 2-D 

arr = random.rand(3, 4)
print(arr)

# Generate random number from array 

# choice() 

x = random.choice([3, 5, 8, 2])
print(x)

arr = random.choice([4, 6, 8, 3, 1], size=(3, 3))
print(arr)