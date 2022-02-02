# Input data

# # String
# name = input("Enter your name: ")
# print(f'Your name is {name}. Type: {type(name)}')
#
# # Integer
# num = int(input('Enter a number: '))
# print(num, type(num))
#
# # Float
# f = float(input('Enter a real number: '))
# print(f, type(f))
#
# # Boolean
# b = bool(input('Enter a boolean: '))
# print(b, type(b))

# Input Multiple value
# x,y,z = input("Enter a 3 number: ").split()
# print(x,y,z, type(x))

# Input Multiple int
# x = list(map(int,input("Enter multiple integers: ").split()))
# print(x, type(x))
# print(x[0], type(x[0]))

# Input Multiple value with List comprehension
x,y,z = [int(x) for x in input("Enter 3 number: ").split()]
print(x,y,z)

mylist = [int(x) for x in input("Enter multi number: ").split()]
print(mylist)


