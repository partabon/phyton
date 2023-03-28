#Exercises: Level 2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map to create a new list by changing each country to uppercase in the countries list
countries_upper_cased = map(lambda name: name.upper(), countries)
print(list(countries_upper_cased))

# 2. Use map to create a new list by changing each number to its square in the numbers list
numbers_squared = map(lambda x: x*x, numbers)
print(list(numbers_squared))

# 3. Use map to change each name to uppercase in the names list
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

# 4. Use filter to filter out countries containing 'land'.
countries_land = filter(lambda c: c.count('land')>0, countries)
print(list(countries_land))   

# 5. Use filter to filter out countries having exactly six characters.
countries_6 = filter(lambda c: len(c)==6, countries)
print(list(countries_6)) 

# 6. Use filter to filter out countries containing six letters and more in the country list.
countries_6mas = filter(lambda c: len(c)>=6, countries)
print(list(countries_6mas)) 

# 7. Use filter to filter out countries starting with an 'E'
countries_conE = filter(lambda c: c.startswith('E'), countries)
print(list(countries_conE)) 

# 8. Chain two or more list iterators 
# (eg. arr.map(callback).filter(callback).reduce(callback))
# lo anterior es sintaxis de JavaScript, pero parece que no es posible 
# hacerlo en Python en una sola línea,
# Hay formas de hacerlo usando librerías externas (como PyFunctional, 
# http://github.com/EntilZha/PyFunctional), pero eso está fuera del 
# alcance de este curso, y ya le dediqué mucho tiempo a este problema
numbers_squared = list(map(lambda x: x*x, numbers))
numbers_squared_big = list(filter(lambda num: num >15, numbers_squared))
print(numbers_squared_big)

# 9. Declare a function called get_string_lists which takes 
# a list as a parameter and then returns a list containing 
# only string items.
def get_string_lists(l):
    l2=list.copy(l)
    return list(map(lambda x: str(x), l2))

print(get_string_lists(numbers))

# 10. Use reduce to sum all the numbers in the numbers list.
import functools
total = functools.reduce(lambda x,y : x+y, numbers)
print(total) 

# 11. Use reduce to concatenate all the countries and to produce 
# this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland 
# are north European countries
# usaremos sólo los 5 primeros países y les añadiremos coma
from functools import reduce
cadena = reduce(lambda x,y: ', '.join([x,y]),countries[:-1])
print(cadena)
cadena_final = cadena +' and ' + countries[-1] + ' are north European countries'
print(cadena_final)
