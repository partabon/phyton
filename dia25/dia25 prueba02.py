import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)


df = pd.read_csv('weight-height.csv')
#rint(df)

print(df.head()) # give five rows we can increase 
# the number of rows by passing argument to the head()
#  method

print(df.tail()) # tails give the last five rows, 
#we can 
#increase the rows by passing argument to tail method

print(df.shape) # as you can see 10000 rows and three columns
print(df.columns)
heights = df['Height'] # this is now a series
weights = df['Weight'] # this is now a series
print(len(heights) == len(weights))
print(weights.describe())



