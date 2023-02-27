fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('eggs','meat','milk','cream','cheese')

food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

food_stuff_lt= list(food_stuff_tp)
print(food_stuff_lt)
l=len(food_stuff_tp)
print(food_stuff_lt[l//2])
print(food_stuff_tp[l//2])

print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)