#https://github.com/codebasics/py/blob/master/numpy/nditer.ipynb

import numpy as np
a = np.arange(12).reshape(4,3)
print(a)

for row in a:
    for cell in row:
        print(cell)



# Define two arrays of the same shape
c = np.array([1, 2, 3])
d = np.array([10, 20, 30])

# Use nditer to iterate over both arrays
for x, y in np.nditer([c, d]):
    print(x, y)


# Iterate over the array in C order (row-major)
for x in np.nditer(a, order='C'):
    print(x)



f = np.array([[1, 2, 3],
              [4, 5, 6]])

# Iterate over the array in Fortran order (column-major)
for x in np.nditer(f, order='F'):
    print(x)


h = np.array([['a', 'b', 'c'], 
              [4, 5, 6]])

# Iterate with Fortran-style order and external_loop flag
for x in np.nditer(h, flags=['external_loop'], order='F'):
    print(x)




# Define a 2D array
h = np.array([[10, 20, 30], 
              [4, 5, 6]])

# Iterate over the array, modify each element in place
for x in np.nditer(h, op_flags=['readwrite']):
    x[...] = x * x

# Print the modified array
print(h)
