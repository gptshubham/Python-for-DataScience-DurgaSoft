import numpy as np

a = np.zeros((10,10))
print(a)

a = np.zeros((10,10),dtype=int)
print(a)

# one-dimensional nd array
a = np.arange(1,101)
print(a)

# two-dimensional nd array
print(a.reshape((10,10)))

# identity matrix
a = np.identity(5)
print(a)

print(type(np))
print(type(a))
help(np.ndarray)

