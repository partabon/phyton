sumapares= 0
sumaimpares=0

for i in range(101):
    if i%2==0:
        sumapares +=i
    else:
        sumaimpares +=i

print('The sum of all evens is', sumapares,'. And the sum of all odds is', sumaimpares)