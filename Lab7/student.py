
from Lab7.person import Person

class Student(Person):
    def __init__(self,fname,lname,age,major):
        super().__init__(fname,lname,age)
        self.major = major

    def student_introduce(self):
        print(f'My name is {self.f_name} {self.l_name}, '
              f'I am {self.age} years old '
              f'and I am studying in {self.major}')