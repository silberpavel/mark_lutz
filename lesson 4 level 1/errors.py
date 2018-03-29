try:
    age = input('Enter your age: ')
    long = 20
    short = 2
    total = long * 3 + short * 2
    #x = 'a' > 1
    print(total)
    
    if age < 28:
        raise Exception('Не подходите по возврасту')
    print(' Возвраст ок!')
    
except (NameError, TypeError) as e:
    if type(e) == NameError:
        print('oi!')
    else:
        print('ai!')
except ValueError as e:
    print(e)
    
except Exception as e:
    print(e)
    
except:
    print('...!')

finally: 
    print('The end')