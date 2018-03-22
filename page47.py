
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]


for person in people:
  for (name, value) in person:
    if name == 'name': 
      print(value)