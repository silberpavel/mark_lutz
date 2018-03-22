# Lists Списки
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

bob[0].split()[-1]  # получить фамилию Боба
# ‘Smith’

sue[2] *= 1.25  # повысить оклад Сью на 25%
# sue [‘Sue Jones’, 45, 50000.0, ‘hardware’]

people = [bob, sue]  # ссылки в списке списков
for person in people:
    print(person)

people[1][0]
# ‘Sue Jones’

for person in people:
    print(person[0].split()[-1])    # вывести фамилию
    person[2] *= 1.20               # увеличить оклад на 20%
# Smith
# Jones

for person in people:
    print(person[2])  # проверить новый размер оклада
# 36000.0
# 60000.0

'''Для добавления новых записей в базу данных вполне достаточно ис-
пользовать обычные операции над списками, такие как append и extend:'''
people.append([‘Tom’, 50, 0, None])
len(people)
# 3
people[-1][0]
# ‘Tom’

# Обращение к полям по именам
NAME, AGE, PAY = range(3)  # 0, 1 и 2
bob = ['Bob Smith', 42, 10000]
PAY, bob[PAY]
# (2, 10000)




for person in people:
    print(person[0][1], person[2][1]) # имя, оклад
# Bob Smith 10000
# Sue Jones 20000

[person[0][1] for person in people] # выборка имен
# [‘Bob Smith’, ‘Sue Jones’]

for person in people:
    for (name, value) in person:
        if name == 'name': print(value) # поиск требуемого поля

'''Еще лучше было бы реализовать функцию, выполняющую всю работу за нас:'''
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:              # поиск поля по имени
        return fvalue