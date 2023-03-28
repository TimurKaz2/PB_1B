import numpy as np

a = np.array([[4, 2], [9, 1]])
b = np.array([[5, 3], [2, 5]]) 

c = np.vstack((a, b))
print(c)

srez = c[:-1,0]
print(srez)

max = srez.max()
print(max)
min = srez.min()
print(min)
sum = srez.sum()
print(sum)

d = np.hstack((a, b))
print(d)

srez_1 = d[0,:-1]
print(srez_1)

max_1 = srez_1.max()
print(max_1)
min_1 = srez_1.min()
print(min_1)
sum_1 = srez_1.sum()
print(sum_1)