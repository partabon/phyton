def is_prime(n):
    raiz= int(n**.5)
    for d in range(2,raiz):
        if n/d == n//d:
            return False
    return True

numeros = [1946,1949,1009,1003,11001,240,11]
for i in numeros:
    print (i,is_prime(i))

def all_items_unique(l):
    for i in l:
        if l.count(i) > 1:
            return False
    return True

print(all_items_unique(numeros))

def all_items_same_type(l):
    lista_tipos = list()
    for i in l:
        lista_tipos.append(type(i))
    for tipo in lista_tipos:
        if lista_tipos.count(tipo) != len(l):
            return False
    return True

lista = [1946,1949,1009,1003,11001,240,11,'76']

print('numeros',all_items_same_type(numeros))
print('lista',all_items_same_type(lista))

#ya hay una funcion que verifica eso
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
