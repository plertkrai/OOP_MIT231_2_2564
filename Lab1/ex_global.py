# global vairable and global keyword
print('Start')
x = 'MIT'


def myfunc():
    x = 'RUTS'  # local variable
    print('I am studying at '+x)


def myfunc2():
    global x
    x = 'Saiyai'
    print('I am student at '+x)

myfunc()
print(x)
myfunc2()
print(x)
print('End')

# ประกาศตัวแปร ชื่อ a มีค่าเท่ากับ 100

# พิมพ์ตัวแปร a ทาง output

# พิมพ์ชนิดตัวแปร a ทาง output


