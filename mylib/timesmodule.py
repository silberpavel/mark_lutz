def seconds_per_day(days=1): #days=1 default
    s = 24 * days * 60 * 60
    return s
if __name__ == '__name__':
    print(seconds_per_day())
sec = seconds_per_day(3)