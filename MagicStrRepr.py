# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         if gender == 'male' or gender == 'female':
#             self.gender = gender
#         else:
#             print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
#             self.gender = 'male'
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f'Гражданин {self.surname} {self.name}'
#         elif self.gender == 'female':
#             return f'Гражданка {self.surname} {self.name}'
class Vector:
    def __init__(self, *args):
        self.values = [i for i in (args) if isinstance(i, int)]

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return 'Пустой вектор'
v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"