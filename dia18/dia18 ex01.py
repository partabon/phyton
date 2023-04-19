import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

#words = paragraph.split()
regex_pattern =r'[^., ]+'

words= re.findall(regex_pattern,paragraph)
words.sort()
print(words)

set_words = set()
set_words.update(words)
#print(set_words)

list_words = list(set_words)
list_words.sort()
print(list_words)

ocurrencias = list()
for i in range(len(list_words)):
    ocurrencias.append(0)

for j in range(len(words)):
    for i in range(len(list_words)):
        if list_words[i] == words[j]: 
            ocurrencias[i]+=1

print(ocurrencias)

# ordena las palabras y sus ocurrencias (método burbuja)
n =len(list_words)
for i in range(n-2):
    for j in range(n-i-1):
        if ocurrencias[j]<ocurrencias[j+1]:
            aux_ocurrencias = ocurrencias[j]
            aux_words = list_words[j]
            ocurrencias[j]=ocurrencias[j+1]
            list_words[j] =list_words[j+1]
            ocurrencias[j+1]=aux_ocurrencias
            list_words[j+1]= aux_words
    

dicc ={}
for i in range(len(list_words)):
    dicc[list_words[i]] = ocurrencias[i] 

print(dicc)
