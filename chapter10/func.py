def apply(func: object, value: object) -> object:
    return func(value)

def outer():
    def inner():
        print('This is inner')
    print('This is outer, invoking inner')
    return inner

def myfunc(*args):
    for arg in args:
        print(arg, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for arg in args:
            print(arg, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()
