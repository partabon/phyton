import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

weights = [74, 78, 69]
df['Weight'] = weights
print(df)

heights = [173, 175, 169]
df['Height'] = heights
print(df)

df['Height'] = df['Height'] * 0.01
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()

df['BMI'] = bmi
print(df)

df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

print(df.Weight.dtype)

df['Birth Year'].dtype # it gives string object , we should change this to number
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype
ages = df['Current Year'] - df['Birth Year']
print(ages)
df['Ages'] = ages
print(df)

mean = (35 + 30)/ 2
print('Mean: ',mean)

print(df[df['Ages'] > 120])


print(df[df['Ages'] > 120])