#!/usr/bin/python3

a1 = 30
print(a1)

dir(a1)
'''
>>> dir(a1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
'''

type(a1)
'''>>> type(a1)
<class 'int'>'''

if a1 == 0:
    print('Zero')
else:
    print('more')

print('-----------------------------------------------')

# Numbers
w =123
fw = 123.34
type(w)   # <class 'int'>
type(fw)  # <class 'float'>
print(type(fw))
print('-----------------------------------------------')

#help(a1)    # doc
<<<<<<< HEAD
print('-----------------------------------------------')

a = 10.5
b = 5
c=3
print(c**3)     # 27
print(a//b) # deviding, 
print('------------------ Binary_operations ------------------------')

d=5
print(5&6)  # 4
print(d^2)  # 7

print('------------------ Hex ------------------------')

print(0x16) #22

print(0b111001)  # 57

print('------------------ import math ------------------------')
import math
print(math.sqrt(64))

print('------------------ globals ------------------------')
# print(dir(globals))

print('------------------ builtins ------------------------')
# print(dir(__builtins__))


=======

a = 5
b = 2

print(a//b)
print(a&b)
>>>>>>> c8eb3306e5324111c5e5948962c0e441c05f0a0c

print('-----------------------------------------------')







