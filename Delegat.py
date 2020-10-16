class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def breathe(self):
        print('Человек дышит')


class Doctor:
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def breathe(self):
        super().breathe()
        print('Доктор дышит')
