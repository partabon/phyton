import json

def most_populated_countries(filename, total):
    with open(filename, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)
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
    for i in range(total):
        lista.append({'country': paises[i],'population': valores[i]}) 
    return lista


print(most_populated_countries(filename='./data/countries_data.json', total=10))

print(most_populated_countries(filename='./data/countries_data.json', total=3))