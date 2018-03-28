# DRY DON'T REPEAT YOURSELF
def seconds_per_day(days=1): #days=1 default
    s = 24 * days * 60 * 60
    return s
if __name__ == '__name__':
    print(seconds_per_day())
sec = seconds_per_day(3)
##print(sec)

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
##print(area)
##print(ring_area)
