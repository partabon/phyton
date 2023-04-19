class Statistics:
    def __init__ (self, lista):
        self.l =lista

    def count(self):
        return len(self.l)
    
    def sum(self):
        return sum(self.l)
    
    def min(self):
        return min(self.l)

    def max(self):
        return max(self.l)

    def mean(self):
        n = len(self.l)
        suma = 0
        for i in range(n):
            suma += self.l[i]
        return suma/n

    def median(self):
        l2 = self.l.copy()
        l2.sort()
        #print (l2)
        n= len(self.l)
        if n%2 ==0: #es par
            return (l2[n//2-1]+l2[n//2])/2 #el promedio 
        else:
            return l2[n//2] 

    def mode(self): #el valor que más se repite
        conjunto=set(self.l)
        #print(conjunto)
        lista = list(conjunto)
        #print(lista)
        frecuencia =list()
        for item in lista:
            frecuencia.append(self.l.count(item))
        #print(frecuencia)
        index_maximo = frecuencia.index(max(frecuencia))
        return {'moda':lista[index_maximo],'cuenta': max(frecuencia)}

    def range(self):
        l2 = self.l.copy()
        l2.sort()
        return l2[-1]-l2[0]

    def var(self):
        suma =0 #es la suma de las xi^2
        for item in self.l:
            suma += item**2
        return suma/len(self.l) - (self.mean())**2

    def std(self):
        return (self.var())**.5
    
    def freq_dist(self):
        total_datos = set()
        total_datos.update(self.l)
        #print(len(total_datos))
        #Crea un diccionario con los datos
        dicc_datos = {}
        for linea in total_datos:
            dicc_datos[linea]=0
        #print(dicc_datos)
        for dato in self.l:
                if dato in dicc_datos:
                    dicc_datos[dato] += 1
        datos=list()
        valores=list()
        #print(dicc_datos)
        for dato in dicc_datos:
            datos.append(dato)
            valores.append(dicc_datos[dato])
        #print(datos,valores)
        #ordenar método burbuja
        n =len(datos)
        for i in range(n-2):
            for j in range(n-i-1):
                if valores[j]<valores[j+1]:
                    aux_valores = valores[j]
                    aux_datos = datos[j]
                    valores[j]=valores[j+1]
                    datos[j] =datos[j+1]
                    valores[j+1]=aux_valores
                    datos[j+1]= aux_datos
        #almacena los n datos
        lista =list()
        suma= sum(valores)
        for i in range(len(dicc_datos)):
            lista.append((valores[i]/suma *100, datos[i])) 
        return lista

    def describe(self):
        c = str()
        c += str('\nCount:')+ str(self.count())
        c += str('\nSum: ')+ str(self.sum()) # 744
        c += str('\nMin: ')+ str(self.min()) # 24
        c += str('\nMax: ')+ str(self.max()) # 38
        c += str('\nRange: ')+ str(self.range()) # 14
        c += str('\nMean: ')+ str(self.mean()) # 30
        c += str('\nMedian: ')+ str(self.median()) # 29
        c += str('\nMode: ')+ str(self.mode()) # {'mode': 26, 'count': 5}
        c += str('\nStandard Deviation: ')+ str(self.std()) # 4.2
        c += str('\nVariance: ')+ str(self.var()) # 17.5
        c += str('\nFrequency Distribution: ')+ str(self.freq_dist()) 
        return c
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data= Statistics(ages)
print(data.l)
print(data.mean())
print(data.var())

print(data.describe())