# tuple - update item in tuple
mytuple = (10,20,30,40,50)
print(mytuple)
# change tuple to list
mylist = list(mytuple)
print(mylist)
mylist[0] = 100
print(mylist)
# change list to tuple
mytuple = tuple(mylist)
print(mytuple)
"""
เปลี่ยนแปลงข้อมูลใน mytuple ตำแหน่งที่ 4
ให้มีค่าเท่ากับ 5000
"""
mylist =list(mytuple)
print(mylist)
mylist[4] =5000
mytuple =tuple(mylist)
print(mytuple)
# Add item to tuple
"""
เพิ่มข้อมูล 600 ใน mytuple 
"""
mylist =list(mytuple)
mylist.append(600)
mytuple =tuple(mylist)
print(mytuple)
# remove item in tuple
"""
ลบข้อมูล 30 ใน mytuple 
"""
mylist =list(mytuple)
mylist.remove(30)
mytuple =tuple(mylist)
print(mytuple)
# del keyword
#del mytuple  # delete completly
print(mytuple)

# join tuple
# +
x = (1,2,3)
y = (4,5,6)
z = x+y  # x concatination with y
print(z)

t = z*2
print(t)

# unpack tuple
mytuple = ('apple','banana','cherry')
print(mytuple)

(x,y,z) = mytuple # unpack item to each vaiables
print(x,y,z)

print(t)
# (x,y,z) = t  # Error: Too many values to unpack
# print(x,y,z)

# asterisk
(x,y,*z) = t
print('x=',x)
print('y=',y)
print('z=',z)

(x,*y,z) = t
print('x=',x)
print('y=',y)
print('z=',z)


