import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it

print(type (table))
#print(table[0])

#with open('./tabla0_uci.txt','a') as f:
tabla_1 =list()
for td in table.find('tr').find_all('td'):
    tabla_1.append( td.text)

print(len(tabla_1))
#print(tabla_1[0])
#print(tabla_1[1])
#print(tabla_1[2])
print('----',tabla_1[30])
print('----',tabla_1[100])
print('----',tabla_1[20])    
print('----',tabla_1[17])  
print('----',tabla_1[18]) 
print('----',tabla_1[19])
print('----',tabla_1[-2])
print('----',tabla_1[-1])

with open('./tabla0_uci.txt','w') as f:
    k=17
    for i in range(30):
        f.write('<<<< '+str(i+k)+' '+str(tabla_1[i+k].count('Data Sets'))+' '+str(len(tabla_1[i+k]))+' ' +str(tabla_1[i+k])+ '\n')

etiquetas = list()
for i in range(19,26):
    etiquetas.append(tabla_1[i])

print(etiquetas)
k = 26
intervalo =9
dicc_list=list()
while k < len(tabla_1):
    dicc = {}
    for j in range(7):
        valor = tabla_1[k+2+j].replace('\xa0','')
        dicc[etiquetas[j]] = valor
    dicc_list.append(dicc)
    k+=intervalo

print(dicc_list[0])
print(dicc_list[1])
print(dicc_list[-1])

import json
with open('./ics_uci_edu.json', 'w', encoding='utf-8') as f:
    json.dump(dicc_list, f, ensure_ascii=False, indent=4)
