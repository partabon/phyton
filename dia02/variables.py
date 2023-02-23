# 'Día 2: 30 Días de programación en python.
first_name='Luis'
last_name='Villagómez'
full_name='Luis Villagómez'
country ='Mex'
city ='mex'
year =2023
is_true =True
is_light_on =False
first_name, last_name, country='Luis','Villagómez','Mex'
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city ))
print(type(year ))
print(type(is_true))

print(len(first_name))
print(len(first_name)<len(last_name))
num_one=5
num_two=4
total=num_one+num_two
print(total)
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
print(remainder)
exp=num_one**num_two
print(exp)
floor_division=num_one//num_two
print(floor_division)

pi=3.1416
radio=float(input('¿radio? '))
area_of_circle=pi*radio**2
circum_of_circle=2*pi*radio
print('Área = ',area_of_circle,' metros cuadrados')

first_name, last_name, country,age=input('Nombre: '),input('Apellido: '),input('País: '),int(input('Edad: '))
print(first_name)
print(last_name)
print(country)
print(age )