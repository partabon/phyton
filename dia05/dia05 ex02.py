#21
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
it_companies.pop(0)
print(it_companies)
#22
l=len(it_companies)
it_companies.pop(l//2)
print(it_companies)
#23
it_companies.pop()
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#print(it_companies)
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
lenguajes =front_end+back_end
print(lenguajes)
#27
full_stack=front_end+back_end
n=full_stack.index('Redux')
full_stack=full_stack[0:n]+['Python' , 'SQL']+full_stack[n+1:]
print(full_stack)
