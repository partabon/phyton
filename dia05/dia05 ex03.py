ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('Min=',ages[0])
print('Max=',ages[-1])
print('Mediana=',ages[len(ages)//2])
suma= sum(ages)
promedio =suma/len(ages)
print('Promedio=',promedio)
print('Rango=',ages[-1]-ages[0])
print('Min - promedio= %.2f' %(abs(ages[0]-promedio)))
print('Max - promedio= {:.2f}'.format(abs(ages[-1]-promedio)))