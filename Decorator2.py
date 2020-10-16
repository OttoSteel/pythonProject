def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('/h1')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('/table')

    return inner


@table
@header
def say(name, surname, age):
    print('hello', name, surname, age)


# say = table(header(say))
say('Vasya', 'Ivanov', 30)
