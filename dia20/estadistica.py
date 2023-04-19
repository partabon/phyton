
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

