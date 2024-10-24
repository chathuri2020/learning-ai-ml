import numpy as np

# Create a 2D array
arr1 = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

#Slicing in NumPy works similar to slicing lists in Python. 
# You can select subarrays by specifying start, stop, and step values.

arr2 = arr1[2:]
print(arr2)