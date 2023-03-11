height=int(input('Ingresa tu estatura en cm: '))
credits =float(input('Ingresa cuantos créditos tienes: '))

#If their height is greater than or equal to 137 
# and their credits is greater than or equal to 10, print "Enjoy the ride!"
if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
#Else if their height is less than 137, 
# print "You are not tall enough to ride."
elif height < 137:
    with_taller_person = bool(input('¿Estás con una persona mayor? (True/False) '))
    if height < 100 or not with_taller_person:
        print("You are not tall enough to ride. Chaparro!!" )
    elif height >= 100 and with_taller_person and credits >= 10:
        print("Enjoy the ride! Chaparro!!")
    elif credits < 10:
        print ("You don't have enough credits to ride. Chaparro!!")
#Else, print "Invalid data."
    else:
        print("Invalid data.")
#Else if their credits is less than 10, 
# print "You don't have enough credits to ride."
elif credits < 10:
    print ("You don't have enough credits to ride.")
#Else, print "Invalid data."
else:
    print("Invalid data.")