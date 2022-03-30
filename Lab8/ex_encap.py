# Encapsulation

class Person:
    def __init__(self, name, age):
        # object attributes
        self.name = name  # public
        self._age = age   # protected

    def detail(self):
        print(f'Name: {self.name} Age: {self._age}')

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        # object attribute
        self.major = major

    def student_detail(self):
        print(f'Name: {self.name} '
              f'Age:{self._age} '
              f'Major:{self.major}')

# create instant of Person
p = Person('Puriwat Lertkrai',35)
print(p.name)
#print(p.__age)
# 1. access via public method
p.detail()
# 2. use name mangling
#print(p._Person__age)
#p._Person__age = 40
#print(p._Person_age)

# create instant of Student
std = Student('Nattaporn',23,'MIT')

print(std.name)
# name mangling and inheritance
#print(std._Student_Person_age) (error)
print(std.major)

std.student_detail()
