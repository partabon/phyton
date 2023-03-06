fruits = ['banana', 'orange', 'mango', 'lemon']

fruta = input('Ingresa una fruta en inglés: ')

if fruta in fruits:
    print('Esa fruta ya existe en la lista')
else:
    fruits.append(fruta)
    print(fruits)