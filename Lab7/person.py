class Person:
    def __init__(self,fname,lname,age):
        self.f_name = fname
        self.l_name = lname
        self.age = age

    def person_introduce(self):
        print(f'My name is {self.f_name} {self.l_name}, '
              f'I am {self.age} years old.')
