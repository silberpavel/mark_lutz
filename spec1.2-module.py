from math import cos
from math import sin as math_sin

myValue = math_sin(45)
value = cos(28)
print(value, '\n', myValue)

print('----------------------------')

import string
print(dir(string))
print('\n', string.printable)
print('\n', string.punctuation)
print('\n', string.ascii_uppercase)

print('Проверка свойство или метод')
#string.ascii_lowercase()
print('Просто вызвать')
print('''    string.ascii_lowercase()
TypeError: 'str' object is not callable''')
print('ЭТО ЗНАЧИТ ЧТО ЭТО НЕ ФУНКЦИЯ, ЭТО СВОЙСТВО')

print('TO DOWNLOAD MODULES')
print('pip install numpy')

import numpy

num1 = numpy.product([1,2,3,4,5])
print(num1)

print('\nTO UNINSTALL MODULES')
print('\npip uninstall numpy')