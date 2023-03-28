#Exercises: Level 1
# 1. Explain the difference between map, filter, and reduce.
# los tres reciben como argumentos una función y un iterable
# map: aplica la función a cada elemento del iterable
#      regresa otro iterable con el mismo número de elementos
# filter: no hace cambios a los elementos del iterable, sólo los escoge 
#         de acuerdo a la función que se usa como criterio.
#         regresa otro iterable con un número menor o igual de elementos.
#reduce  aplica la función a todos los elementos del iterable,
#        regreando un resultado, que es un esalar, y no iterable como en map y filter.

# 2. Explain the difference between higher order function, closure and decorator
# higher order function: una función dentro de otra.
# closure: una función que encapsula a otra, y que regresa a ésta.
# decorator: una función con una función interna llamada wraper, 
#            que se aplica a otra función posterior usando @.

# 3. Define a call function before map, filter or reduce, see examples.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    

long_names = filter(lambda name: len(name)>6, names)
print(list(long_names))        

import functools
total = functools.reduce(lambda x,y : x+y, numbers)
print(total)   

# 4. Use for loop to print each country in the countries list.
for countrie in countries:
    print(countrie)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for num in numbers:
    print(num)