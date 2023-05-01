import numpy as np

random_float = np.random.random()
print(random_float)

random_floats = np.random.random(5)
print(random_floats)

for i in range(5):
    random_int = np.random.randint(0, 11)
    print(random_int,'\t')

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,12, size=100)
print(random_int)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)