s1 = 'abc'
s2 = s1
print(s1.upper()) # 'ABC' copy of s1
print(s2)  #abc
print(s1)  #abc

# convert str to list
print(list('abc'))  # ['a', 'b', 'c']

##print(list(12345))  # Error 

l = ['a', 'b', 'c', 'd']
print(l)
print(l.pop())   #извлекаем последний элемент
print(l.pop(0))  # 'a'  first
print(l)
print('=================================')
lis = [2, 3, 55, 75, 7, 32, 21, 6, 4]
lis.sort()
print(lis)
print(help(list.sort))
lis.sort(reverse=True)
print(lis)
print('============ list =================')
lis2 = ['d', 'g', 'a', 'b', 'c', 'e']
lis2.sort(reverse=True)
print(lis2)
