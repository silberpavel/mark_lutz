print('----------  range function  (loop) -----------')
r = range(10)
print(type(r))
print(r)

#print('----------  for  in  -----------')

##for i in range(1, 11):
##    print(i)
print('----------  list  -----------')
print('----------  списки  -----------')

l = [1, 2, 3, 4, 5]
print(l)
for i in ['a', 'b', 'c']:
    print(i)
    
l.append(6)
print(l)
print(l[2])  # 3  # brakets notetion
l[2] = 33
print(l)

print('\n----------  range  -----------')

r2 = range(6)
print(r2[2])

print(type(r2))
print(list(r2))  # change to list format

print(len(r2))

for i in 'abc':
    print(i)
print('abc'[1])

print('Список ссылочный тип а строка не изменяемый тип')
print('\n---------- str does no support assigment  -----------')












