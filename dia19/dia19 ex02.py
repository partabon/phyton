import json

def most_spoken_languages(filename, num):
    with open(filename, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)
        #print(type(countries_data))
        #print(countries_data[0])
        #print(type(countries_data[0]))
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
    for i in range(n):
        lista.append((valores[i], lenguajes[i])) 
    return lista[:num]

print(most_spoken_languages(filename='./data/countries_data.json', num=10))

print(most_spoken_languages(filename='./data/countries_data.json', num=3))