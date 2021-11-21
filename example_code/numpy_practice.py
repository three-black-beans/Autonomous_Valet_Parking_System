import numpy as np
import matplotlib.pyplot as plt

# numpy code practice
# https://numpy.org/doc/stable/user/quickstart.html
# Numpy QuickStart

a = np.arange(15).reshape(3, 5)

print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]


print(a.shape)
# (3, 5)

print(a.ndim)
# 2
# ndim: the number of axes (dimensions) of the array.

print(a.dtype)
# int32
print(a.dtype.name)
# int32

print(a.itemsize)
# 4

print(a.size)
# 15

print(type(a))
# class 'numpy.ndarray'

b = np.array([(1,2,3), (4,5,6)])

print(b)
# [[1 2 3]
#  [4 5 6]]

print(np.zeros((3,4)))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print(np.ones((3,4)))
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

print(np.empty((2,3)))
# [[ 6.95247365e-310  6.95247365e-310  0.00000000e+000]
#  [ 1.08694442e-322  2.33419537e-313 -9.32288463e-311]]

print(np.arange(10,30,5))
# [10 15 20 25]

print(np.linspace(0,2,9))
# 9 numbers from 0 to 2
# [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]


A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A * B)
# elementwise product
# [[2 0]
#  [0 4]]

print(A @ B)
# matrix product
# [[5 4]
#  [3 4]]

print(A.dot(B))
# another matrix product
# [[5 4]
#  [3 4]]

def f(x,y):
    return 10 * x + y

b = np.fromfunction(f, (5,4), dtype=int)

print(b)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]

c = b.view()
c is b
# False
c.base is b
# True

rg = np.random.default_rng(1)
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 10000)
plt.hist(v, bins=50, density=True)
plt.show()
(n, bins) = np.histogram(v, bins=50, density=True)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()