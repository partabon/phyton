import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g))  # 23

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))

## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)
print(np.linalg.det(i))

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

print(Z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)

np_arr = np.array(range(0, 11))
print(np_arr + 2)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.histplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()