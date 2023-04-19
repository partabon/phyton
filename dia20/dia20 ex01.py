import requests # importing the request module

url = 'http://www.gutenberg.org/files/1112/1112.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
text = response.text # gives all the text from the page


def find_most_common_words(texto,total):
    total_palabras = set()
    print(type(texto))
    palabras = texto.split()
    total_palabras.update(palabras)
    print(len(total_palabras))
    #Crea un diccionario con los palabras
    dicc_palabras = {}
    for linea in total_palabras:
        dicc_palabras[linea]=0
    #print(dicc_palabras)
    palabras_texto = texto.split()
    for palabra in palabras_texto:
        if palabra in dicc_palabras:
            dicc_palabras[palabra] += 1
    palabras=list()
    valores=list()
    #print(dicc_palabras)
    i=0
    for palabra in dicc_palabras:
        palabras.append(palabra)
        valores.append(dicc_palabras[palabra])
        i +=1
    #ordenar método burbuja
    n =len(palabras)
    for i in range(n-2):
        for j in range(n-i-1):
            if valores[j]<valores[j+1]:
                aux_valores = valores[j]
                aux_palabras = palabras[j]
                valores[j]=valores[j+1]
                palabras[j] =palabras[j+1]
                valores[j+1]=aux_valores
                palabras[j+1]= aux_palabras
    #almacena los n palabras
    lista =list()
    for i in range(total):
        lista.append((valores[i], palabras[i])) 
    return lista[:total]

print(find_most_common_words(text,10))