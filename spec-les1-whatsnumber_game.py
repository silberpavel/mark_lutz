# whatisnumber  game
import random

num = random.randrange(1,11)

while True:
    answer = input('Enter number: ')
    if not answer.isdigit():    
        print('Must be a number!')
        continue

    answer = int(answer)
    if answer > num:
        print('Меньше')
    elif answer < num:
        print('Больше')
    else:
        print('Правильно')
        break
