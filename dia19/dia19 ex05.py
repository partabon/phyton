    
    
def find_most_common_words(name,total):
    with open('./data/'+name) as f:
            texto = f.readlines()  
    total_palabras = set()
    for linea in texto:
        palabras = linea.split()
        total_palabras.update(palabras)
    print(len(total_palabras))
    #Crea un diccionario con los palabras
    dicc_palabras = {}
    for linea in total_palabras:
        dicc_palabras[linea]=0
    #print(dicc_palabras)
    for linea in texto:
        palabras_linea = linea.split()
        for palabra in palabras_linea:
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
    #almacena los n palabras que se hablan en el mayor número de países
    lista =list()
    for i in range(total):
        lista.append((valores[i], palabras[i])) 
    return lista[:total]

#print(find_most_common_words('obama_speech.txt', 10))
w= find_most_common_words('obama_speech.txt', 10)
for k in w:
    print(k)

#print(find_most_common_words('donald_speech.txt', 10))
w= find_most_common_words('donald_speech.txt', 10)
for k in w:
    print(k)

print(find_most_common_words('michelle_obama_speech.txt', 10))

print(find_most_common_words('melina_trump_speech.txt', 10))

