numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

non_positive_numbers = [i for i in numbers if i <= 0] 
print(non_positive_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ number for row in list_of_lists for row2 in row for number in row2]
print(flattened_list)

list_tuples = [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(list_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_list= [[pais[0].upper(),pais[0][0:3].upper(),pais[1].upper()] for row in countries for pais in row ]
print(flat_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_dir= [{'country':pais[0].upper(),'city': pais[1].upper()} for row in countries for pais in row ]
print(flat_dir)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated = [ nombre[0] + ' ' + nombre[1] for row in names for nombre in row ]
print(concatenated)

calculate_slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)

print(calculate_slope(8,2,-4,-1))

y_intercept = lambda x1,y1,x2,y2 : y1 - calculate_slope(x1,y1,x2,y2) * x1
print(y_intercept(8,2,-4,-1))