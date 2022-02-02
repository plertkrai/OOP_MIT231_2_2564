# comprehension

mylist = ['apple','banana','cherry','orange','mango']
print(mylist)
# สร้าง list ใหม่ ที่มีข้อมูลผสมด้วยอักขระ a
# loop for
newlist = []

for x in mylist:
    if 'a' in x:
        newlist.append(x)

print(newlist)

# comprehension
newlist2 = [x for x in mylist if 'a' in x]
print(newlist2)

mynum = [20,30,50,100,321,400,10,505]
print(mynum)
# เลือกเฉพาะข้อมูลที่มากกว่าหรือเท่ากับ 100
newnum = [x for x in mynum if x >= 100]
print(newnum)

# เลือกเฉพาะข้อมูลที่มากกว่า 50 และน้อยกว่า 500 เก็บไว้ในตัวแปร newnum2
newnum2 =[x for x in mynum if x > 50 and x < 500 ]
print(newnum2)

# sorting data in list
print(mynum)
mynum.sort()  # ascending l->h
print(mynum)
mynum.sort(reverse=True) # descending h-l
print(mynum)
