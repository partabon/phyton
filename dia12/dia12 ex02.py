import string
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)

from random import random,randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) 

def list_of_hexa_colors(n):
    cadena='0123456789abcdef'
    salida=[]
    for i in range(n):
        color =''
        for k in range(6):
            num= randint(0,len(cadena)-1)
            color= color + cadena[num]
        salida.append('#'+color)
    return salida

print(list_of_hexa_colors(3))

def list_of_rgb_colors(n):
    lista=[]
    for i in range(n):
        salida =[]  
        for k in range(3):
            num= randint(0,255)
            salida.append(num)
        lista.append('rgb'+ str(tuple(salida)))
    return lista

print(list_of_rgb_colors(4))

def generate_colors(tipo, num):
    if tipo =='hexa':
        print(list_of_hexa_colors(num))
    elif tipo == 'rgb':
        print( list_of_rgb_colors(num))
    else:
        print( 'Error')
    
generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
