import requests
url = 'https://api.thecatapi.com/v1/breeds'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
gatos = response.json()
razas = list()

for gato in gatos:
    r = gato['name']
    razas.append(r)

paises = list()
for gato in gatos:
    p = gato['origin']
    paises.append(p)

#print(paises)

paises_set = set()
paises_set.update(paises)

#Crea un diccionario con los países
dicc_paises = {}
for pais in paises_set:
    dicc_paises[pais]=0
#print(dicc_paises)
for pais in paises:
    if pais in dicc_paises:
        dicc_paises[pais] += 1

pais_list=list()
valores=list()
#print(dicc_paises)
i=0
for pais in dicc_paises:
    pais_list.append(pais)
    valores.append(dicc_paises[pais])
    i +=1
#ordenar método burbuja
n =len(pais_list)
for i in range(n-2):
    for j in range(n-i-1):
        if valores[j]<valores[j+1]:
            aux_valores = valores[j]
            aux_paiss = pais_list[j]
            valores[j]=valores[j+1]
            pais_list[j] =pais_list[j+1]
            valores[j+1]=aux_valores
            pais_list[j+1]= aux_paiss
#almacena los países con el mayor número de razas
lista =list()
for i in range(len(pais_list)):
    lista.append((valores[i], pais_list[i])) 

print('Tabla de Frecuencia de Razas:' )
print(lista)

