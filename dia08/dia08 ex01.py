dog = {}
dog['name']='petocha'
dog['color']='gris'
dog['breed']='schnauzer'
dog['legs']=4
dog['age']=13

print(dog)

student = { 'first_name': 'Luis',
            'last_name':'Villagómez', 
            'gender':'mascuino',
            'age': 88,
            'marital_status' : 'bachellor',
            'skills' :['Java','Pascal','Basic','C','C++','VisualBasic','HTML','CSS','XML','JavaScript'],
            'country' :'mex',
            'city' : 'Cuajimalpa',
            'address' :{ 'street' : 'Pastores',
                       'zipcode' : '05210'
            }
}

print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('Trotar')
student['skills'].append('Reír')
print(student['skills'])

claves=student.keys()
print(claves)
valores=student.values()
print(valores)
list_tuples=student.items()
print(list_tuples)
student.pop('age')
student.popitem()
del student['gender']
print(student)
del dog