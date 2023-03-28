import numpy as np

a = np.array([[2, 8], [1, -6]])
b = np.array([[3, 2 ,7], [4, 1, 8], [6, 3, 7]])
c = np.array([[4, 3, 2, 7], [6, 1, 1, -2], [7, 5, 8, 1], [9, 5, -3, -5]])


print(np.transpose(a))
print(np.transpose(b))
print(np.transpose(c))

print(np.linalg.inv(a))
print(np.linalg.inv(b))
print(np.linalg.inv(c))

print(np.linalg.det(a))
print(np.linalg.det(b))
print(np.linalg.det(c))

vect_1 = np.linalg.norm(b, 3, axis = 1) 
print(vect_1)

vect_2 = np.linalg.norm(c, 3, axis = 0) 
print(vect_2)