    
    
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


def clean_text(name):
    with open('./data/'+name+".txt") as f:
            texto = f.readlines() 
    #cambiar todo a minúsculas línea por línea
    texto2 = list()
    for i in range(len(texto)):
        texto2.append(texto[i].lower())
    #quitar guiones, comas, puntos, comillas, etc.
    cadena ="\t–-,\"\'[]():."
    for letra in cadena:
        for i in range(len(texto)):
            texto2[i] = texto2[i].replace(letra,' ')
    with open('./data/'+name+"2.txt",'w') as f:
        f.writelines(texto2)
    return 



import stop_words
def remove_support_words(name):
    with open('./data/'+name+"2.txt") as f:
            texto = f.readlines() 
    soporte = stop_words.stop_words
    texto2=list()
    for i in range(len(texto)):
        cadena = texto[i].split(' ')
        for palabra in soporte:
            ocurrencias = cadena.count(palabra) 
            if ocurrencias > 0:
                for i in range(ocurrencias):
                    cadena.remove(palabra)
        texto2.append(' '.join(cadena))
    with open('./data/'+name+"3.txt",'w') as f:
        f.writelines(texto2)
    return 

clean_text('obama_speech')
remove_support_words('obama_speech')
print ('obama:',find_most_common_words('obama_speech3',12))

clean_text('donald_speech')
remove_support_words('donald_speech')
print ('Donald:',find_most_common_words('donald_speech3',12))

clean_text('michelle_obama_speech')
remove_support_words('michelle_obama_speech')
print ('michelle_obama_speech',find_most_common_words('michelle_obama_speech3',12))

clean_text('melina_trump_speech')
remove_support_words('melina_trump_speech')
print ('melina_trump_speech',find_most_common_words('melina_trump_speech3',12))

def check_text_similarity(name1, name2):
    #voy a usar un índice que vi en internet
    # sería texto1 Ո texto2 / texto1 Ս texto2
    # este índice va de 0 a 1
    # entre más cerca este de 1 mayor la similitud
    #Usaré la versión de los discursos que está depurada
    with open('./data/'+name1+"3.txt") as f:
        texto1 = f.readlines() 
    with open('./data/'+name2+"3.txt") as f:
        texto2 = f.readlines()
        #dos conjuntos:
    total_palabras1 =set()   
    for linea in texto1:
        palabras = linea.split()
        total_palabras1.update(palabras)
    print('palabras únicas ',name1, len(total_palabras1))
    total_palabras2 =set()   
    for linea in texto2:
        palabras = linea.split()
        total_palabras2.update(palabras)
    print('palabras únicas ',name2, len(total_palabras2))
    interseccion = total_palabras1.intersection(total_palabras2)
    union = total_palabras1.union(total_palabras2)
    print(len(interseccion),len(union))
    similitud = len(interseccion )/ len(union )
    return similitud

print('\nsimilaridad: ',check_text_similarity('melina_trump_speech', 'michelle_obama_speech'))
print('\nsimilaridad: ',check_text_similarity('obama_speech', 'donald_speech'))


