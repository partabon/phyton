# Exercises: Level 2
# 12. Declare a function called categorize_countries that returns a list 
# of countries with some common pattern (you can find the countries list 
# in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import countries_js
#print (countries_js.countries)

def categorize_countries(patron):
  return list(filter(lambda c: c.count(patron)>0, countries_js.countries))

print(categorize_countries('land')) 
print(categorize_countries('ia')) 
print(categorize_countries('Island')) 
print(categorize_countries('stan')) 

# 13. Create a function returning a dictionary, where keys stand for starting 
# letters of countries and values are the number of country names starting with that letter.
abecedario = list('abcdefghijklmnopqrstuvwxyz'.upper())
#print (abecedario)

def cuenta_countries(letra):
  return len(list(filter(lambda c: c.startswith(letra), countries_js.countries)))

def diccionario_countries():
  return [{letra : cuenta_countries(letra)} for letra in abecedario]

#print(cuenta_countries('A'))
print(diccionario_countries())

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries 
# from the countries.js list in the data folder.
def get_first_ten_countries():
   return list(filter(lambda c: countries_js.countries.index(c)<10, countries_js.countries))

print(get_first_ten_countries())
# esto podía haberse hecho de una forma más simple así:
print(countries_js.countries[:10])

# 15. Declare a get_last_ten_countries function that returns the last ten countries 
# in the countries list.
def get_last_ten_countries():
   largo =len(countries_js.countries)
   return list(filter(lambda c: countries_js.countries.index(c)>(largo-11), countries_js.countries))

print(get_last_ten_countries())
# esto podía haberse hecho de una forma más simple así:
print(countries_js.countries[-10:])