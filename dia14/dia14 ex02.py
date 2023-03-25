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

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

# Declare a function called get_string_lists which takes 
# a list as a parameter and then returns a list containing 
# only string items.

# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.