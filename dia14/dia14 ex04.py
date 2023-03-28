
from countries_data import countries_data
#Sort countries by name, 

def countries_by_name():
    paises =list()
    i=0

    for pais in countries_data:
        paises.append(pais["name"])
        i +=1

    #ordenar método burbuja
    n =len(paises)
    for i in range(n-2):
        for j in range(n-i-1):
            if paises[j]>paises[j+1]:
                aux_paises = paises[j]
                paises[j] =paises[j+1]
                paises[j+1]= aux_paises

    #almacena los países por orden alfabético
    lista =list()
    for p in paises:
        lista.append(p) 
    return lista
print('países por orden alfabético:')
print(countries_by_name())

#by capital, 
def countries_by_capital():
    #crearemos dos listas, una con paises y la otra con capitales
    paises =list()
    capitales=list()
    i=0

    for pais in countries_data:
        paises.append(pais["name"])
        capitales.append(pais["capital"])
        i +=1

    #ordenar método burbuja
    n =len(paises)
    for i in range(n-2):
        for j in range(n-i-1):
            if capitales[j]>capitales[j+1]:
                aux_capitales = capitales[j]
                aux_paises = paises[j]
                capitales[j]=capitales[j+1]
                paises[j] =paises[j+1]
                capitales[j+1]=aux_capitales
                paises[j+1]= aux_paises

    #almacena los países con sus capitales ordenadas alfabéticamente
    lista =list()
    for i in range(len(paises)):
        lista.append([capitales[i],paises[i]]) 
    return lista

print('países con su capital por orden alfabético:')
print(countries_by_capital())




# by population
def most_populated_countries():
    #crearemos dos listas, una con paises y la otra con valores
    paises =list()
    valores=list()
    i=0

    for pais in countries_data:
        paises.append(pais["name"])
        valores.append(pais["population"])
        i +=1

    #ordenar método burbuja
    n =len(paises)
    for i in range(n-2):
        for j in range(n-i-1):
            if valores[j]<valores[j+1]:
                aux_valores = valores[j]
                aux_paises = paises[j]
                valores[j]=valores[j+1]
                paises[j] =paises[j+1]
                valores[j+1]=aux_valores
                paises[j+1]= aux_paises

    #almacena los n países más poblados
    lista =list()
    for p in paises:
        lista.append(p) 
    return lista

print('países ordenados por población:')
print(most_populated_countries())

#Sort out the ten most spoken languages by location.
def most_spoken_languages():
    total_lenguajes = set()
    for pais in countries_data:
        total_lenguajes.update(pais["languages"])
    
    #Crea un diccionario con los lenguajes
    dicc_lenguajes = {}
    for pais in total_lenguajes:
        dicc_lenguajes[pais]=0

    for pais in countries_data:
        lenguajes_pais = pais["languages"]
        for lenguaje in lenguajes_pais:
            if lenguaje in dicc_lenguajes:
                dicc_lenguajes[lenguaje] += 1

    lenguajes=list()
    valores=list()
    i=0

    for lenguaje in dicc_lenguajes:
        lenguajes.append(lenguaje)
        valores.append(dicc_lenguajes[lenguaje])
        i +=1

    #ordenar método burbuja
    n =len(lenguajes)
    for i in range(n-2):
        for j in range(n-i-1):
            if valores[j]<valores[j+1]:
                aux_valores = valores[j]
                aux_lenguajes = lenguajes[j]
                valores[j]=valores[j+1]
                lenguajes[j] =lenguajes[j+1]
                valores[j+1]=aux_valores
                lenguajes[j+1]= aux_lenguajes

    #almacena los n lenguajes que se hablan en el mayor número de países
    lista =list()
    for l in lenguajes:
        lista.append(l) 
    return lista

lenguajes = most_spoken_languages()
print('los diez lenguajes hablados en el mayor número de países son:' )
print(lenguajes [:10])

#Sort out the ten most populated countries.
paises = most_populated_countries()
print('los diez países más poblados son:' )
print(paises [:10])
