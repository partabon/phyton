language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(radius, area)
print(result) # The area of a circle with radius 10 is 314

challenge = 'thirty days of pythoonnn'
print(challenge.strip('n')) # 'irty days of py'