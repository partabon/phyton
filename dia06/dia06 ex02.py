hermanos=('Miguel','Condorito')
hermanas = ('Lourdes', 'Adriana','Vitola')

fratelos=hermanos+hermanas
print (fratelos)
print('num fratelos= ', len(fratelos))
padres=('Melona','Melón')
familia=padres+fratelos
print(familia)

padres2=familia[:2]
fratelos2=familia[2:]
print(padres2)
print (fratelos2)
print (familia[0])
print (familia[1])