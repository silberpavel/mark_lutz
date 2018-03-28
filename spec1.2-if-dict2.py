hello = {
        'ru' : 'Добрый день',
        'en' : 'Good day',
        'de' : 'Gutten tag',
        'dk' : 'God dag',
        'default' : 'Unknown language'
    }

s = input('Введите код: ')
greet = hello.get(s, hello['default'])
print(greet)







