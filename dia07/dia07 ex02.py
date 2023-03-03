A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

C=A.union(B)
print(C)
D=A.intersection(B)
print(D)
print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print('Diferencia simétrica: ',A.symmetric_difference(B))

del A
del B
#print (A,B)
