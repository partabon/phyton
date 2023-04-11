
def cuentalineas(name):
    f = open('./data/'+name)
    print(type(f))
    lines = f.readlines()
    #print(type(lines))
    #print(lines)
    f.close()
    return len(lines)

print('líneas de obama:',cuentalineas('obama_speech.txt'))
print('líneas de michelle:',cuentalineas('michelle_obama_speech.txt'))
print('líneas de trump:',cuentalineas('donald_speech.txt'))
print('líneas de melina:',cuentalineas('melina_trump_speech.txt'))

def cuentapalabras(name):
    f = open('./data/'+name)
    lines = f.readlines()
    palabras=0
    for renglon in lines:
        #print(renglon.split())
        palabras +=len(renglon.split())
    f.close()
    return palabras

print('palabras de obama:',cuentapalabras('obama_speech.txt'))
print('palabras de michelle:',cuentapalabras('michelle_obama_speech.txt'))
print('palabras de trump:',cuentapalabras('donald_speech.txt'))
print('palabras de melina:',cuentapalabras('melina_trump_speech.txt'))
