person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#Check if the person dictionary has skills key, 
# if so print out the middle skill in the skills list.
if 'skills' in person:
    n=len(person['skills'])
    print(person['skills'][n//2])
# * Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.

if 'skills' in person:
    if 'Python' in person['skills']:
        print('La persona tiene la habilidad en Python')
    else:
        print('La persona no tiene la habilidad en Phython')

# * If a person skills has only JavaScript and React, 
# print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - 
# for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] :
    print('He is a backend developer')
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills'] :
    print('He is a fullstack developer')
else:
    print('unknown title')


# * If the person is married and if he lives in Finland,
#  print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married']: 
    casado='is married.'
else:
    casado='is not married.'

print(person['first_name'], person['last_name'], 'lives in',person['country'], '. He',casado)
