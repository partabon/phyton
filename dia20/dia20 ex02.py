import requests
url = 'https://api.thecatapi.com/v1/breeds'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
gatos = response.json()
#print(gatos[:1])  
print(type(gatos[0]))
print(type(gatos))
print(len(gatos))
raza = list()

for gato in gatos:
    r = gato['name']
    raza.append(r)
#print(raza)

weight=list()

for gato in gatos:
    w = gato['weight']['metric']
    we = w.split(' - ')
    #print(we)
    if we[0].isnumeric and we[1].isnumeric:
        weight.append((float(we[0])+float(we[1]))/2)
print(len(weight))
#print(weight)

life_span = list()

for gato in gatos:
    ls = gato['life_span']
    life = ls.split(' - ')
    #print(life)
    if life[0].isnumeric and life[1].isnumeric:
        life_span.append((float(life[0])+float(life[1]))/2)

from estadistica import *
print(len(life_span))
#print(life_span)
#print(weight)
print('\nPeso de los gatos en kg' )
print('min =', min(weight),raza[weight.index( min(weight))] )
print('max =', max(weight),raza[weight.index( max(weight))])
print('media =', calculate_mean(weight))
print('mediana =', calculate_median(weight))
print('desviación estándar =', calculate_std(weight))

#print(life_span)
print('\nVida de los gatos en años:' )
print('min =', min(life_span),raza[life_span.index( min(life_span))])
print('max =', max(life_span),raza[life_span.index( max(life_span))])
print('media =', calculate_mean(life_span))
print('mediana =', calculate_median(life_span))
print('desviación estándar =', calculate_std(life_span))



