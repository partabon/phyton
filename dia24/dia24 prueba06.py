import numpy as np
import pandas

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
plt.show()

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)

for l in lst:
    print(l)

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)
odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)
even_numbers = np.arange(2, 20, 2)
print(even_numbers)