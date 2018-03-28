# How to get unique values in the list?
l = [4,22,55,5, 1,22,3,4,5,2,3]
# convert to set
s = set(l)
# and then back to list
l = list(s)
# but it's may be not sorted!
print(l)

