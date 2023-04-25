import requests # importing the request module

url = 'http://www.bu.edu/president/boston-university-facts-stats/' # text from a website

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

tables = soup.find_all('section')
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
print(type (tables))
print(len(tables))
#print(tables[1])
table = tables[1] # the result is a list, we are taking out data from it

#print(table[0])
print(type(table))
print(table)
#with open('./tabla0_uci.txt','a') as f:
tabla_1 =list()
for td in table.find_all("h5"):
    tabla_1.append( td.text)

print(tabla_1)
print(len(tabla_1))

tabla_2 =list()
for td in table.find_all('p'):
    tabla_2.append( td.text)

print(tabla_2)
print(len(tabla_2))

tabla_3 =list()
for td in table.find_all('span'):
    tabla_3.append( td.text)

print(tabla_3)
print(len(tabla_3))


dicc = {}
for i in range(len(tabla_2)):
    dicc[tabla_2[i]] = tabla_3[i]

import json
with open('./boston_university.json', 'w', encoding='utf-8') as f:
    json.dump(dicc, f, ensure_ascii=False, indent=4)
