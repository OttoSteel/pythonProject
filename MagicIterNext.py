class Mark:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __next__(self):
        print('Call next marks')
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter

    def __iter__(self):
        return self

class Student:
    def __init__(self, name, surname, marks):
        self.name= name
        self.surname = surname
        self.marks = marks
    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print('Call __iter__')
        self.index = 0
       # return iter(self.name)  ----- итерация через строку
        return iter(self.marks)

    def __next__(self):
        print('Call next Student')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m = Mark([3, 4, 5, 4, 5])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)
