f = open('./data/email_exchanges_big.txt')
print(type(f))
lines = f.readlines()
print(type(lines))
#print(lines)
f.close()

email_set = set()

for l in lines:
    if l.startswith('From'):
        palabras = l.split(' ')
        #print(palabras)
        palabra2 =palabras[1].replace('\n','')
        #print(palabra2)
        email_set.add(palabra2)
    
email_list =list(email_set)
#print(email_set)
print(email_list)
