def find_most_common_words(name,total):
    with open('./data/'+name + ".txt") as f:
            texto = f.readlines()  
    total_palabras = set()
    for linea in texto:
        palabras = linea.split()
        total_palabras.update(palabras)
    print(len(total_palabras))
    with open('./data/salida.txt','w') as f:
        f.write(str(total_palabras))
        f.close()
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
    #almacena los n palabras
    lista =list()
    for i in range(total):
        lista.append((valores[i], palabras[i])) 
    return lista[:total]

print(find_most_common_words('romeo_and_juliet',10))