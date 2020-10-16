from functools import wraps

def table(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('/table')

    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner


def say():
    print('hello world')
