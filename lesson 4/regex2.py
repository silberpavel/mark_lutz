import re

s = 'Python Programming. for the Absolute. bigenner'

ss = 'abc.test@gmail.com'

r = re.findall(r'@\w+.\w+', ss)   # r -> raw line (not Python code)

# simbol class []
# [for] all 'f' all 'o' all 'r'
# [for] all 'f' all 'o' all 'r'
# [^for] not 'f' not 'o' not 'r'
# [a-zA-Z0-9]  == \w    IT'S SAME
# \w+ one or more  IT'SAME \w{1,}
# \w* 0 or more  IT'SAME \w{0,}
# \w{3}  ['Pyt', 'hon', 'Pro', 'gra', 'mmi', 'for', 'the', 'Abs', 'olu', 'big', 'enn']

# '.' любой символ
# '\.' только точка

# ^\w+ с начала строки одно вхождение ['Python']
# \w+$ последние слово ['bigenner']


# [^a-zA-Z0-9]  == \W    IT'S SAME

print(r)






