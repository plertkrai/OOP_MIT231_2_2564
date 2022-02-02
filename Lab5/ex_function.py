# function

# 1 - no parameter
def my_func1():
    print('Hello, from my_func1')

# 2 - one parameter
def my_func2(x):
    print('Hello, from my_func2',x)

# 3 - many paremeter
def my_func3(x,y):
    print('Hello, from my_func3',x,y)

# 4 - not sure how many parameter.
def my_func4(*x):  # x --> tuple
    print('Display data form my_func4')
    for i in x:
        print(i)

# 5 - parameter with keyword
def my_func5(x,y,z):
    print('Hello, from my_func5')
    print(x,y,z)

# 6 - keyword with not sure how many parameter
def my_func6(**kwgs):  # kwgs --> dictionary --> key:value
    print('Data from my_func6:')
    for x,y in kwgs.items():
        print(x,y)




# calling functions
my_func1()
my_func2(10)
my_func3(10,20)
my_func4(10,20,30)
my_func4()
my_func5(z=100,y=200,x=300)
my_func6(fname='puriwat',lname='lertkrai',age=35)
