print('---------------- if else ----------------')

import random
n1 = random.randrange(1,11)
n2 = random.randrange(1,11)
# >>> '12.23.3'.replace('.', '',1)
# '1223.3'

answer = input(f'how much {n1} + {n2} ? ')
# float check (20.0 ->digit, 20.3.3 Not digit)
test = answer.replace('.', '', 1)  

if not test.isdigit():   # 
    print('Must be a number!')
else:
    if answer == test:
        answer = int(answer)
    else:
        answer = float(answer)
    
    if answer == n1+n2:
        print('Correct')    
    else:
        print('Not correct')
        






