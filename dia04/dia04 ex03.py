#26
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
#27
i1=sentence.find('because')
l=len('because ')
sentence2 = sentence[0:i1]+sentence[i1+3*l:]
print(sentence2)
#otra forma:
print(sentence.replace('because ',''))
#28
cadena='Coding For All'
print(cadena.startswith('Coding '))
#29
print(cadena.endswith('Coding '))
#30
cadena2='   Coding For All      '
print(cadena.strip(' '))
#31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#32
arreglo= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(arreglo))
#33
sentence ='I am enjoying this challenge.\nI just wonder what is next.'
print(sentence)
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(radius, area)
print(result) # The area of a circle with radius 10 is 314
#34
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))