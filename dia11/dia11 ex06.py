# Ejercicios nivel 2
# 3.Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode, 
#calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(l):
    n = len(l)
    suma = 0
    for i in range(n):
        suma += l[i]
    return suma/n

def calculate_median(l):
    l2 = l.copy()
    l2.sort()
    #print (l2)
    n= len(l)
    if n%2 ==0: #es par
       return (l2[n//2-1]+l2[n//2])/2 #el promedio 
    else:
       return l2[n//2] 


def calculate_mode(l): #el valor que más se repite
    conjunto=set(l)
    #print(conjunto)
    lista = list(conjunto)
    #print(lista)
    frecuencia =list()
    for item in lista:
        frecuencia.append(l.count(item))
    #print(frecuencia)
    index_maximo = frecuencia.index(max(frecuencia))
    return lista[index_maximo]

def calculate_range(l):
    l2 = l.copy()
    l2.sort()
    return l2[-1]-l2[0]

def calculate_variance(l):
    suma =0 #es la suma de las xi^2
    for item in l:
        suma += item**2
    return suma/len(l) - (calculate_mean(l))**2

def calculate_std(l):
    return (calculate_variance(l))**.5


numeros=[2,5,3,4,4,4,5,1,1,3]

print('media =',calculate_mean(numeros))
print('mediana =',calculate_median(numeros))
print('rango =',calculate_range(numeros))
print('moda =',calculate_mode(numeros))

numeros=[1, 9.7, 0.5, 8.7, 7, 5.9, 16]
print('\nmedia =',calculate_mean(numeros))
print('variancia =',calculate_variance(numeros))
print('desviacion estándar =',calculate_std(numeros))