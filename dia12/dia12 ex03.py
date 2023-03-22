
from random import random,randint

def shuffle_list(l):
    #intercambia parejas al azar
    lista =l.copy()
    for i in range(len(lista)):
        temp = lista[i]
        n2 =randint(0,len(l)-1)
        lista[i] = lista[n2]
        lista[n2] = temp
    return lista

fruits = ['banana', 'orange', 'mango', 'lemon']

print(shuffle_list(fruits))

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
print(shuffle_list(fruits))

def array_seven():
    array =list()
    for i in range(10):
        array.append(i)
    #print(array)
    #quita tres números
    for i in range(3):
        n1= randint(0,len(array)-1)
        del array[n1]
    return array

for k in range(10):
    print(array_seven())