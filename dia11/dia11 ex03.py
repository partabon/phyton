# 8. Declare a function named print_list. 
#It takes a list as a parameter and it prints out each element of the list.
def print_list(l):
    if type(l) == list:
        n=len(l)
        for i in range(n):
            print(l[i])

print_list(['banana', 'orange', 'mango', 'lemon'] )

# 9. Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(l):
    if type(l) == list:
        n=len(l)
        l2 = list()
        for i in range(n):
            l2.append(l[n-1-i])
        return l2
    else:
        return 'no es una lista'
    
print(reverse_list(['banana', 'orange', 'mango', 'lemon'] ))

# 10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l):
    if type(l) == list:
        n=len(l)
        l2 = list()
        for i in range(n):
            l2.append(l[i].capitalize())
        return l2
    else:
        return 'no es una lista'
       
print(capitalize_list_items(['banana', 'orange', 'mango', 'lemon'] ))     

#11.  Declare a function named add_item. 
# It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(l,item):
    if type(l) == list:
        l2 = l.copy()
        l2.append(item)
        return l2

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
