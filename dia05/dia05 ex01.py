lista = []
lista =[2,3,3,1,3,3,3]
print(len(lista))
l=len(lista)
print(lista[0],lista[l//2],lista[l-1])
lista = ['luis',88,1.70,'ninguno','Cuajimalpa']
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies)
print(len(it_companies))
l=len(it_companies)
print(it_companies[0],it_companies[l//2],it_companies[l-1])
it_companies[4]='Triplayera'
print(it_companies)
it_companies.append('OpenAI')
print(it_companies)
l=len(it_companies)
it_companies.insert(l//2,'La Venta')
print(it_companies)
it_companies[4]=it_companies[4].upper()
print(it_companies)
print('#; '.join(it_companies))
print('Microsoft' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
del it_companies[:3]
print(it_companies)
#19
del it_companies[-3:]
print(it_companies)
#20
l=len(it_companies)
del it_companies[l//2]
print(it_companies)