print('===== Dict ======')
d = {'a': 100, 'b': 200, 'c': 300}

print(d['a'])  # get value by key

d['x'] = 500   # add new

print(' dictionery NOT SORTED !!!  ')
print(d)

#Check if exists
print('y' in d)   # False
# better option
print(d.get('y', 0)) # 0 default if exists
print(d.get('x', 0)) #

print('=======================')
for k, v in d.items():   # d.values() d.keys()
    print(k, v)
    
    
print('=======================')

print('slices')

ls = [1, 2, 4,2, 43,5,3,3]
print(ls[2:3])
print(ls[:4])
print(ls[4:])
print(30 not in ls)
# copy of the list ls[:]
ls2 = ls[:]
print(ls2)
print('===========  dict generator ============')
print(' syntax sugar')

##ls3 = []
##for i in [2, 3, 4]:
##    ls3.append(i**2)

ls3 = [i**2 for i in [2, 3, 4]]
print(ls3)   # [4, 9, 16]

# Еще условие
ls3 = [i**2 for i in [2, 3, 4] if i > 2]
print(ls3)   # [9, 16]















