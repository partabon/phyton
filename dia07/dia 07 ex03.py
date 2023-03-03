age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set=set(age)

print(len(age))
print(len(age_set))
# string: una lista ordenada de carácteres, modificable
# list:   un grupo ordenado de objetos, modificable
# tuple:  un grupo ordenado de objetos, no modificable
# set:    un grupo de objetos, todos únicos, modificable

sentencia = 'I am a teacher and I love to inspire and teach people'
lista = sentencia.split()
conjunto = set()
conjunto.update(lista)
print(lista)
print(conjunto)
print('palabras únicas: ',len(conjunto))
