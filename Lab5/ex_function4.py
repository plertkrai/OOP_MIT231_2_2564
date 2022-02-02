# lambda function

x = lambda a,b: a+b
y = lambda a,b,c:a*b*c

i,j = 10,20
print(f'Summation of {i} and {j} is {x(i,j)}')

print(f'The result of mutiply 3 values is : {y(10,20,30)}')

# lambda funtion in other function

def myfunc(n):
    return lambda x: x*n

mydouble = myfunc(2)
mytripple = myfunc(3)
print(mydouble(100))
print(mytripple(100))


