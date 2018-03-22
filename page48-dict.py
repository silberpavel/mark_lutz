# dict object
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print(bob['name'], sue['pay']) 
#('Bob Smith', 40000)

print(bob['name'].split()[-1])  # Smith

sue['pay'] *= 1.10
print(sue['pay'])  # 44000.0


# zip lists
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
print(list(zip(names, values)))
# list
# [('name', 'Sue Jones'), ('age', 45), ('pay', 40000), ('job', 'hdw')]   

sue = dict(zip(names, values))
print(sue)
# dict
# {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}  