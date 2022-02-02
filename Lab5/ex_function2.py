# function and return value

def sum_a(x,y):
    print("Result from function: ",x+y)

def sum_b(x,y):
    return x+y

def find_max(num):  # num --> class 'list'
    print("The maximum value in list is: ",max(num))

def find_min(num):
    # m = min(num)
    # return m
    return min(num)

# calling funcion
sum_a(10,20)
res = sum_b(10,20)
print('Result from sum_b: ',res)
print('Result from sum_b: ',sum_b(50,50))

mylist = [12,65,34,77,99,154]
find_max(mylist)
print('The minimum value in list is :',find_min(mylist))

