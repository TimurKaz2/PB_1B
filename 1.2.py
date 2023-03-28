import numpy as np

a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2]) 

rows = a.shape
print(rows)

re = a.reshape((9,1))
print(re)

re_1 = a.reshape((3,3))
print(re_1)

max_1 = re_1.max(axis = 0)
print(max_1)
max_2 = re_1.max(axis = 1)
print(max_2)

min_1 = re_1.min(axis = 0)
print(min_1)
min_2 = re_1.min(axis = 1)
print(min_2)

sum_1 = re_1.sum(axis = 0)
print(sum_1)
sum_2 = re_1.sum(axis = 1)
print(sum_2)