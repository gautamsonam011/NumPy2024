#  Without ufunc, we can use python's built in zip() method:

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

z = []

for i, j in zip(x, y):
    z.append(i+j)
print(z)    