# getter and setter method

class Person:
    def __init__(self,name,age,email):
        # object attributes
        self.__name = name  # private members
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age= age
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

# create instant of Person
p = Person('Sam Puriwat',35,'puriwat.l@rmutsv.ac.th')
print(p.get_name())
p.set_name('Sam Lertkrai')
print(p.get_name())
print(p.get_email())
print(p.get_age())


