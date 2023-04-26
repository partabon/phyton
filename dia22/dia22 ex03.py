import requests # importing the request module

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
#print(response.headers)     # headers information
html_doc = response.text # gives all the text from the page
#print(text)


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
#print(soup.section)

#print(soup.a)
#print(soup.find_all('a'))
#print(soup.find_all('section'))
#print(soup.get_text())

tables = soup.find_all('table')
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
print('tipo de tables:',type (tables))
print(len(tables))
#print(tables)
table = tables[0] # the result is a list, we are taking out data from it

#print(table[0])
print('tipo de table:',type(table))
print(len(table))
#print(table)
#print(table[''])

tabla_1 =list()
for td in table.find_all('td'):
    tabla_1.append( td.text)

print(tabla_1)
print(len(tabla_1)) #listado de presidentes

tabla_2 =list()
for td in table.find_all('th'):
    tabla_2.append( td.text)

print(tabla_2)
print(len(tabla_2))

def limpiar(s):
    s2 =str(s)
    if s2.count('[') > 0:
        i = s2.find('[')
        s2 = s2[0:i]
    s2 = s2.replace('\n\n',' ')    
    s2 = s2.replace('\n','')
    return s2

etiquetas = list()
for i in range(7):
    etiquetas.append(limpiar(tabla_2[i]))

del etiquetas[1]
etiquetas.insert(3,'color')
print(etiquetas)

k=0
intervalo =7
n =1
dicc_list=list()
while k < len(tabla_1):
    dicc = {}
    for j in range(7):
        if j != 3:
            if j ==0:
                valor = n 
            else:
                valor =limpiar(tabla_1[k+j])
            dicc[etiquetas[j]] = valor
    dicc_list.append(dicc)
    n+=1
    k+=intervalo

print('\n')
print(dicc_list[-3:])

import json
with open('./wikipedia_presidents_usa.json', 'w', encoding='utf-8') as f:
    json.dump(dicc_list, f, ensure_ascii=False, indent=4)
