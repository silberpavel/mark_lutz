bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
print(record)
# {'job': '?', 'pay': '?', 'age': '?', 'name': '?'}

print('------------------------------------------------')

people = [bob, sue] # links in list
for person in people:
    print(person['name'], person['pay'])


print('------------------------------------------------')
for person in people:
    if person['name'] == 'Sue Jones':               #Sue's payment
        print(person['pay'])
print('------------------------------------------------')

names = [person['name'] for person in people]       # Choosing names
print(names)    # ['Bob Smith', 'Sue Jones']

print('------------------------------------------------')

print(list(map((lambda x: x['name']), people)))     # Choosing names

print(sum(person['pay'] for person in people))      # sum all pay


print('------------------------------------------------')

# SQLrequest example
print([rec['name'] for rec in people if rec['age'] >= 45])  # ['Sue Jones']

print( [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]) # [42, 2025]
print('------------------------------------------------')
