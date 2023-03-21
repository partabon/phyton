def add_two_numbers (num1,num2):
    return num1+num2

print(add_two_numbers(7,8))

def area_of_circle(radio):
    pi =3.1416
    return pi*radio**2

print(area_of_circle(7))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num)==int or type(num)==float:
            total += num     # same as total = total + num 
        else:
            return 'un dato no es numérico'
    return total
print(sum_all_nums(2, 3.5, 5,'a')) # 10

def convert_celsius_to_fahrenheit(C):
    return (C*9/5)+32
print('-20 °C = ',convert_celsius_to_fahrenheit(-20),'F°')

def check_season(mes):
    Autumn = ['September', 'October' , 'November']
    Winter= ['December', 'January' , 'February']
    Spring = ['March', 'April' , 'May']
    Summer =['June', 'July' , 'August']
    if mes in Autumn:
        return 'Otoño'
    elif mes in Winter:
        return 'Invierno'
    elif mes in Spring:
        return 'Primavera'
    elif mes in Summer:
        return 'Verano'
    else:
        return 'No es un mes en inglés'

mes= input('Dame un mes en inglés: ')
print(check_season(mes))
