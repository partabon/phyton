r =float(input('Ingresa el radio '))

pi=3.1416
area= pi*r**2
p=2*pi*r
print('El área del círculo es ',area)
print('El perímetro del círculo es ',p)

print('de la recta y=2x-2')
pendiente =2
x_intercept= 1     #cuando y=0
y_intercept= -2            #cuando x=0

x1,y1 =float(input('x1 ')),float(input('y1 '))
x2,y2 =float(input('x2 ')),float(input('y2 '))

m=(y2-y1)/(x2-x1)

print(pendiente ==m)