#12. Declare a function named remove_item. 
# It takes a list and an item parameters. 
# It returns a list with the item removed from it.
def remove_item(l,item):
    if type(l) == list and item in l:
        l2 = l.copy()
        l2.remove(item)
        return l2

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# 13. Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    suma=0
    for i in range(1,n+1):
        suma += i
    return suma
   
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#14.
def sum_of_odds(n):
    suma=0
    for i in range(1,n+1):
        if i % 2 == 1:
            suma += i
    return suma
   
print(sum_of_odds(5))  # 9
print(sum_of_odds(10)) # 
print(sum_of_odds(100)) #

#15.
def sum_of_evens(n):
    suma=0
    for i in range(1,n+1):
        if i % 2 == 0:
            suma += i
    return suma
   
print(sum_of_evens(5))  # 6
print(sum_of_evens(10)) # 
print(sum_of_evens(100)) # 

