
Autumn = ['September', 'October' , 'November']
Winter= ['December', 'January' , 'February']
Spring = ['March', 'April' , 'May']
Summer =['June', 'July' , 'August']

mes= input('Dame un mes en inglés: ')
if mes in Autumn:
    print('Ese mes está en Otoño')
elif mes in Winter:
    print('Ese mes está en Invierno')
elif mes in Spring:
    print('Ese mes está en Primavera')
elif mes in Summer:
    print('Ese mes está en Verano')
else:
    print('No es un mes en inglés')