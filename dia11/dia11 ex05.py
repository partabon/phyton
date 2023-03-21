# Exercises: Level 2
# 1. Declare a function named evens_and_odds . 
# It takes a positive integer as parameter 
# and it counts number of evens and odds in the number.

def evens_and_odds(n):
    suma_par=0
    suma_non=0
    for i in range(0,n+1):
        if i % 2 == 0: #par
            suma_par += 1
        else:
            suma_non += 1
    return 'The number of odds are ' + str(suma_non)+'\nThe number of evens are '+str(suma_par)
    
print(evens_and_odds(100))


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n
    
print(factorial(3))
print(factorial(7))
print(factorial(20))

def is_empty(k):
    if len(k) == 0:
        return True
    else:
        return False
    
numbers = [2, 3, 7, 9]
print(is_empty(numbers))

