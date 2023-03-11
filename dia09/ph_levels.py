ph =float(input('Ingresa un valor entre 0 y 14: '))

if ph <0:
    print('valor fuera de rango')
elif ph <7:
    print('Ácido')
elif ph == 7:
    print('Neutral')
elif ph < 14:
    print('Básico')
else:
    print('valor fuera de rango')