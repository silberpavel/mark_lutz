import string
def read_file(file_name):
    words_list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        str(file)
        file.split()
        print(file)
##        
##        for line in file:
##        
##            line.strip(string.punctuation)
##            line.strip(string.printable)
##            line = str(line.split(' '))
##        
##            line.lower()
##            print(type(line))
##            words_list.append(line)
##            
##        new_words = set(words_list)
##        print(type(new_words))
##        list(new_words)
##        
##        print(type(new_words))
##        print(new_words)
####    for i in words_list:
####        print(i)
##        
##
##
words = read_file('data.txt')
