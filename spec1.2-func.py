# DRY DON'T REPEAT YOURSELF
def seconds_per_day(days=1): #days=1 default
    s = 24 * days * 60 * 60
    return s

sec = seconds_per_day(3)
print(sec)

# Декопозиция задац - разбить задачу на под задачи (мелкие)
# Decomposition
def area_of_disk(radius):
    '''Help on function:
       
       area_of_disk(number) -> number
       Return area of disk by radius
    '''
    return 3.14 * radius ** 2

# площядь бублика
def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)

area = area_of_disk(20)
ring_area = area_of_ring(20, 5)
print(area)
print(ring_area)

# Облость видемости
x = 10

def fn():
    global x
    print(x)
    x = 20     # global change
    print(x)
    
print(x)   
fn()
print(x)   # will be 20
    
    
print(1, end='*')

print('/n')
print(1,2,3,4,5,6,7,8,9,0)

def fn2(a, b=2, c=3):
    print(a, b, c)

fn2(10, c=30)
    
print('----------------- tuple * ----------------------')

def fn3(*params):
    print(params)
    print(type(params))
    
def fn4(*params):
    for p in params:
        print(p)

fn3(1,2,3,4,5)
fn4(1,2,3,4,5)
print('------------------  dict ** ---------------------')

def fn5(**params):
##    for p, v in params.items():
    for p in params.items(): # values()  keys()
##        print(p, v)
        print(p)


fn5(John=100, Mike=200, Pete=300)





