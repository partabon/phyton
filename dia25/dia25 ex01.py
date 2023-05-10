import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np


df = pd.read_csv('hacker_news.csv')

print(df.head()) # give five rows we can increase 
# the number of rows by passing argument to the head()
#  method

print(df.tail()) # tails give the last five rows, 
#we can 
#increase the rows by passing argument to tail method
print(df.columns)

serie_panda =pd.Series(df.columns)
print(serie_panda)
print(df.shape) # as you can see 10000 rows and three columns

#print(df[df['title'].count('python')>0])
print(df[df['title'].str.contains("python")])
print(df[df['title'].str.contains("Python")])
print(df[df['title'].str.contains("JavaScript")])

print(df.describe())
