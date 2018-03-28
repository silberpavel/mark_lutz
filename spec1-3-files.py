##f = open('test.txt', 'r', encoding='utf-8')
# r -> read, r+ -> read+write
# w -> write, w+ -> write+read
# w, w+  *все уничтожается (то что было)
# a -> write, a+ -> write+read    *cursor at the content end 
# encoding='utf-8'    *all language

##f.close()

#with open('test.txt', 'r', encoding='utf-8') as f:
    # как только выходим из блока, сам закрывается.
##    print(f.read(5))    # Line
##    print(f.read(3))    # one
##    print(f.read())     # read all file
    
##    s = f.readline() # read line
##    while s:
##        print(s)
##        s = f.readline()

##    lines = f.readlines()
##print(lines)    # List
##    for line in lines:
##        print(line)

print('-------------- блок with лучше ------------------------')
count = 0
with open('test.txt', 'a', encoding='utf-8') as f:
##    count += 1
    f.write(f'\nLine {count}') # 'a' --> cursor at the end
    print(f.closed) # true -> file closed
    print(f.mode) # в каком режиме
    print(f.name) # file name
print('--------------------------------')


import csv
with open('data.csv', 'a', encoding='utf-8', newline='\n') as f:
##    reader = csv.reader(f, delimiter=',')
    writer = csv.writer(f, delimiter=',')
##    for row in reader:
##        print(row)
    writer.writerow(['Pete', 'Herrison', 21, '369-85-47'])











