import numpy as np
import pandas

import matplotlib.pyplot as plt
import seaborn as sns

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
print(np.linspace(1.0, 5.0, num=10))

print(np.linspace(1.0, 5.0, num=5, endpoint=False))

# Syntax:
# numpy.logspace(start, stop, num, endpoint)
print(np.logspace(2, 4.0, num=4))

# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)

print('First row: ', np_list[0])
print('Second row: ', np_list[1])

print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])