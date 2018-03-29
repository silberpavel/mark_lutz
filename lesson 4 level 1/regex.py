import re

regexp = 'a'
s = 'vasyA@mail.ru'

##match = re.match(regexp, s)   # начинается ли 's' с буквы 'v' 
##print(match.group())

##match = re.search(regexp, s)   # search 'a' in 's' 
##print(match.group(), match.start(), match.end())  # a 1 2

##match = re.findall(regexp, s, re.I)   # re.I ignore register
##print(match)  # ['a', 'a', 'a']
##
##split = re.split('-', '10-20-30-40', maxsplit=2)
##print(split)

sub = re.subn('a', 'b', s)   #replacement a to b in s
print(sub)

pattern = re.compile(regexp, re.I)
pattern.match(s)
pattern.search(s)
pattern.findall(s)
pattern.split(s)
pattern.subn('b', s)







