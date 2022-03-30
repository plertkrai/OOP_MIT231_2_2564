class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):  # abstract method
        #print(f'My name is {self.name}.')
        pass

class Teacher(Person):
    def introduce(self):
        print(f'My name is {self.name}, I am a Teacher.')

class Student(Person):
    def introduce(self):
        print(f'My name is {self.name},I am a Student.')

# create instants of class
p = Person('Puriwat Lertkrai')
t = Teacher('Piyapong Seananut')
s = Student('Nattaporn Sungtongtea')

p.introduce()
t.introduce()
s.introduce()