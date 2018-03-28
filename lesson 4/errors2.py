try:
    n = 1
    try:
        s = 'a' > 1
    except:
        print('inner')
        raise Exception('From inner')
    finally:
        print('ok')
except:
    print('outer')
finally:
    print('The end')