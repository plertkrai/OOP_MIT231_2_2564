# class example

class Student:
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        print(f'My name is {self.name}, '
              f'I am {self.age} years old and '
              f'I am studying in {self.major}')

# Input data
numstd = int(input('How many your student?: '))
mystudent = []
for x in range(numstd):
    print(f'Student {x+1}:')
    name = input('What is your name?: ')
    age = int(input('How old are you?:'))
    major = input('What is your major?:')
    # create object and store it into list
    mystudent.append(Student(name,age,major))

for x in mystudent:
    print(x.name,x.major,x.age)
    print(x.introduce())

