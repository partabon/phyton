#calcula las raíces de la ecuación cuadrática
a= float(input('a= '))
b= float(input('b= '))
c= float(input('c= '))
raiz1= (-b+(b**2-4*a*c)**.5)/(2*a)
raiz2= (-b-(b**2-4*a*c)**.5)/(2*a)
print('raiz1 =',raiz1)
print('raiz2 =',raiz2)