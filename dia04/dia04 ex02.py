#16
company="Coding For All"
print(company[-1])
#17
company="Coding For All"
print(company[10])
#18
cadena='Python for Everyone'
cadena =cadena.title()
arreglo = cadena.split(' ')
print(arreglo)
print(arreglo[0][0]+arreglo[1][0]+arreglo[2][0])
#19
cadena='Coding For All'
cadena =cadena.title()
arreglo = cadena.split(' ')
print(arreglo)
print(arreglo[0][0]+arreglo[1][0]+arreglo[2][0])
#20
cadena='Coding For All'
print(cadena.index('C'))
#21
print(cadena.index('F'))
#22
print(cadena.rindex('l'))
#23
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
#24
print(sentence.rfind('because'))
#25
i1=sentence.find('because')
i2=sentence.rindex('because')
l=len('because')
sentence2 = sentence[0:i1-1]+sentence[i2+l:]
print(sentence2)