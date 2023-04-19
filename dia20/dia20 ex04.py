import requests
url = 'https://restcountries.com/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:2])  # we sliced only the first country, remove the slicing to see all countries
print(type(countries))
print(type(countries[0]))
print(len(countries[0]['languages']))
print(countries[0]['languages'])
print(countries[0]['languages'][0])
print(countries[0]['languages'][0]['name'])
print(countries[0]['area'])
print(countries[0]['name'])

# by area
def most_larger_countries():
    #crearemos dos listas, una con paises y la otra con valores
    paises =list()
    valores=list()

    for pais in countries:
        #print(pais['area'],pais['name'])
        paises.append(pais["name"])
        if 'area' in pais:
            valores.append(pais['area'])
        else:
            valores.append(0)

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
    for i in range(len(paises)):
        lista.append((paises[i],valores[i])) 
    return lista


#Sort out the ten most populated countries.
paises_lst = most_larger_countries()
print('los diez países más grandes son:' )
print(paises_lst [:10])

#Sort out the ten most spoken languages by location.
def most_spoken_languages():
    total_lenguajes_list = list()
    for pais in countries:
        for lenguaje in pais['languages']:
            #print(lenguaje)
            total_lenguajes_list.append(lenguaje)
    #print(total_lenguajes_list) 
    
    total_lenguajes2 =list()
    for i in range(len(total_lenguajes_list)):
        l= total_lenguajes_list[i]
        #print(l['name'])
        total_lenguajes2.append(l['name'])
        
    total_lenguajes =set()
    #print(total_lenguajes2)
    total_lenguajes.update(total_lenguajes2)
    #print(total_lenguajes)
    #Crea un diccionario con los lenguajes
    dicc_lenguajes = {}
    for pais in total_lenguajes:
        dicc_lenguajes[pais]=0

    lenguajes=list()

    for lenguaje in total_lenguajes2:
        if lenguaje in dicc_lenguajes:
             dicc_lenguajes[lenguaje] += 1

    #print(dicc_lenguajes)
    lenguajes=list()
    valores=list()
    i=0

    for lenguaje in dicc_lenguajes:
        lenguajes.append(lenguaje)
        valores.append(dicc_lenguajes[lenguaje])

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
    for i in range(len(lenguajes)):
        lista.append((lenguajes[i], valores[i])) 
    return lista

lenguajes = most_spoken_languages()
print('los diez lenguajes hablados en el mayor número de países son:' )
print(lenguajes [:10])
print('número total de lenguajes en el mundo:', len(lenguajes))