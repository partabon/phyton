import numpy as np
import pandas

import matplotlib.pyplot as plt
import seaborn as sns


from scipy import stats

np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis,keepdims = True))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
