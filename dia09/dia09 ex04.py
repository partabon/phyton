score= float(input('Califición: '))

if 100 >= score and score >= 90 :
    print('Sacaste A')
elif 89 >= score and score >= 70 :
    print('Sacaste B')
elif 69 >= score and score >= 60 :
    print('Sacaste C')
elif 59 >= score and score >= 50 :
    print('Sacaste D')
elif 49 >= score and score >= 0 :
    print('Sacaste F')
else:
    print('Score no válido')