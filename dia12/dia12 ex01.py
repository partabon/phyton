import string
print(string.ascii_letters)
print(string.digits)

from random import randbytes,random,randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) 

def random_user_id():
    cadena=string.ascii_letters + string.digits
    user_id =''
    for i in range(6):
        n = randint(0,len(cadena)-1)
        #print(cadena[n])
        user_id = user_id + cadena[n]
    return user_id


print(random_user_id())

def user_id_gen_by_user():
    largo =int(input('Numero de carácteres: '))
    num_IDs =int(input('Número de IDs: '))
    cadena=string.ascii_letters + string.digits
    total_user_IDs = ''
    for j in range(num_IDs):
        user_id =''
        for i in range(largo):
            n = randint(0,len(cadena)-1)
            #print(cadena[n])
            user_id = user_id + cadena[n]
        total_user_IDs = total_user_IDs+'\n'+ user_id 
    return total_user_IDs

print(user_id_gen_by_user()) # user input: 5 5
#print(user_id_gen_by_user()) # 16 5

def rgb_color_gen():
    salida=[]
    for k in range(3):
        n= randint(0,255)
        salida.append(n)
    return 'rgb'+ str(tuple(salida))

print(rgb_color_gen())

