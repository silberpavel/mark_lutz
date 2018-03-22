# tuple (kortej)
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]


def field(record, label):
  for (fname, fvalue) in record:
    if fname == label:             #  Field search by name
      text = str(record[0][1]) + ' age ' + str(fvalue)
      return text

#print(field(bob, 'name'))
#print(field(sue, 'pay'))

for rec in people:                # print age of people
  print(field(rec, 'age')) 
