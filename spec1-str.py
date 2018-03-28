n1 = 2
n2 = 3

# s = str(n1) + ' + ' + str(n2) + ' = ' + str(n1 + n2)

# s = '{} + {} = {}'.format(n1, n2, n1+n2)  # template
s = f'{n1} + {n2} = {n1+n2}'
print(s)

w = input('Введите сторону прямоугольника: ')
h = input('Введите другую сторону прямоугольника: ')

w = int(w)
h = int(h)

s = f'Площядь прямоугольника {w} x {h} = {w*h}'
# Will return string {w} {h}
# DATA FROM OUTSIDE ALWAYS BE STRING! IF NOT UKAZANO
# Все приходит строками
print(s)


