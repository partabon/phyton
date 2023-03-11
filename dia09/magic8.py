import random

num = random.randint(1, 9)

print(num)

respuestas = list()
respuestas.append('Yes - definitely.')
respuestas.append('It is decidedly so.')
respuestas.append('Without a doubt.')
respuestas.append('Reply hazy, try again.')
respuestas.append('Ask again later.')
respuestas.append('Better not tell you now.')
respuestas.append('My sources say no.')
respuestas.append('Outlook not so good.')
respuestas.append('Very doubtful.')

pregunta = input('Question: \t')

print('Magic 8 Ball: \t',respuestas[num])