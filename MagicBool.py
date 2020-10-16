# class City:
#     def __init__(self, name):
#         name = name.lower()
#         if ' ' in name:
#             list = [str(i).capitalize() for i in name.split()]
#             self.name = ' '.join(list)
#         elif ' ' in name:
#             list = [str(i).capitalize() for i in name.split('-')]
#             self.name = '-'.join(list)
#         else:
#             self.name = name.capitalize()
#
#     def __str__(self):
#         return self.name
#
#     def __bool__(self):
#         if self.name.endswith(('a', 'e', 'i', 'o', 'u')):
#             return False
#         else:
#             return True

class Quadrilateral:
    def __init__(self, *args):
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]

    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        if self.width == self.height:
            return True
        else:
            return False

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"
