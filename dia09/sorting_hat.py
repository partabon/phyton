'''š¦ Gryffindor '
'š¦ Ravenclaw'
'š¦” Hufflepuff''
'š Slytherin'##'''

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0 
Slytherin = 0

print('\t 1) Dawn')
print('\t 2) Dusk')
Q1 =int(input('Q1) Do you like Dawn or Dusk 1/2: '))
if Q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif Q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('\t Wrong input')

print('\n\t 1) The Good')
print('\t 2) The Great')
print('\t 3) The Wise')
print('\t 4) The Bold')
Q2 =int(input('Q2)  When Iām dead, I want people to remember me as (1/2/3/4): '))

if Q2 == 1: 
    Hufflepuff += 2
elif Q2 == 2:   
    Slytherin += 2
elif Q2 == 3:
    Ravenclaw += 2
elif Q2 == 4:
    Gryffindor += 2
else:
    print('\t Wrong input')

print('\n\t 1) The violin')
print('\t 2) The trumpet')
print('\t 3) The piano')
print('\t 4) The drum')
Q3 =int(input('Q3) Which kind of instrument most pleases your ear? (1/2/3/4): '))

if Q3 == 1: 
    Slytherin += 4 
elif Q3 == 2:   
    Hufflepuff += 4
elif Q3 == 3:
    Ravenclaw += 4
elif Q3 == 4:
    Gryffindor += 4
else:
    print('\t Wrong input')

nombres = []
nombres.append('š¦ Gryffindor')
nombres.append('š¦ Ravenclaw')
nombres.append('š¦” Hufflepuff')
nombres.append('š Slytherin')

totales = list()
totales.append( Gryffindor)
totales.append(Ravenclaw)
totales.append( Hufflepuff)
totales.append( Slytherin)

maximo = max(totales)
posicion = totales.index(maximo)
print('House with the most points:', nombres[posicion])