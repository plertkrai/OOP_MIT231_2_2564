# Concept

# define class
class Person:
    # class attribute
    address = "RUTS Saiyai"  # public
    # object (instance) attributes
    def __init__(self):
        #assign value to attributes
        self.name = ""
        self.age = ""
    def introduce(self):
        print(f'Hello, my name is {self.name}')

# create class instant (object)
# p1 = Person("Puriwat",35)
# p2 = Person("Nattaporn",22)
# assing value to attribute
p1 = Person()
p2 = Person()
p1.name = 'Puriwat'
p2.name = 'Nattaporn'
print(p1.address)
print(p2.address)
print(p1.name)
print(p2.name)

# calling method in class
p1.introduce()
p2.introduce()

mylist = [p1,p2]
print(mylist)
print(mylist[1].name)



