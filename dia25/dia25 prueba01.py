import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)

s = pd.Series(10, index = [1, 2, 3])
print(s)

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)