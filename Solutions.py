# class Counter:
#     def start_from(self, value=0):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def display(self):
#         print(f'Текущее значение счетчика = {self.value}')
#
#     def reset(self):
#         self.value = 0

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, another):
        if isinstance(another, Point):
            return (((self.x - another.x) ** 2) + ((self.y - another.y) ** 2)) ** 0.5
        else:
            print('Передана не точка')
            return None

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
print(p1.get_distance(p2)) # вернёт 5.0
g = p1.get_distance(10) # Распечатает "Передана не точка", вернет None