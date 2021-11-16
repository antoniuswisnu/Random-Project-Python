import numpy as np

a = np.array([3,5,7])
a.shape
a.dtype
print(a)
print(a.shape)
print(a.dtype)

b = np.array([[9.2, 5.6, 3], [4, 3.5, 6]])
b.shape
b.dtype
print(b)
print(b.shape)
print(b.dtype)

c = np.array([[2, 3],[5, 8],[7, 2]])
print(c)
print(c.T)
print(c[1,1])
print(c.shape)

d = np.array([[5, 1],[8, 4],[-5, 7]])
print(c+d)
print(c-d)
print(c*d)
print(c//d)
print(np.sum(d))
