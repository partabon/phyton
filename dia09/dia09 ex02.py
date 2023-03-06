my_age=98

your_age =int(input('Enter your age: '))

dif_age=abs(my_age-your_age)
if dif_age > 1:
    year_str='years'
else:    
    year_str='year'

if my_age == your_age:
    print('We have the same age.')
else:
    if my_age < your_age :
        print('You are',dif_age,year_str,'older than me.')
    else:
        print('You are',dif_age,year_str,'younger than me.') 


