# Inheritance

class Person:
    def __init__(self,fname,lname,age):
        self.f_name = fname
        self.l_name = lname
        self.age = age

    def person_introduce(self):
        print(f'My name is {self.f_name} {self.l_name}, '
              f'I am {self.age} years old.')

# Student inherited from Person
class Student(Person):
    def __init__(self,fname,lname,age,major):
        super().__init__(fname,lname,age)
        self.major = major

    def student_introduce(self):
        print(f'My name is {self.f_name} {self.l_name}, '
              f'I am {self.age} years old '
              f'and I am studying in {self.major}')

# create instance of Person
p = Person('puriwat','lertkrai',35)
p.person_introduce()

# create instance fo Student
s = Student('nattapong','kaewboonma',40,'MIT')
s.person_introduce()
s.student_introduce()