"""
ให้เขียนโปรแกรมรับค่าตัวเลข 10 จำนวน จากนั้นให้กำหนดฟังก์ชั่นต่อไปนี้
1. ฟังก์ชันสำหรับหาค่ามากที่สุด  --> find_max()
2. ฟังก์ชันสำหรับหาค่าน้อยที่สุด  --> find_min()
3. ฟังก์ชันสำหรับหาค่าผลรวมของข้อมูลทั้งหมด --> find_total()
4. ฟังก์ชั่นที่แสดงเฉพาะเลขคู่จากข้อมูลทั้งหมด --> find_Even()
"""

# input data from user
num = [int(x) for x in input('Enter integer:').split()]
print('Value in list: ',num)
def find_max(x):
    print(f'The max value in list: {max(x)}')
def find_min(x):
    print(f'The minimum value in list: {min(x)}')
def find_total(x):
    total = 0
    for i in x:
        total += i
    print(f'The total value in list: {total}')
def find_even(x):
    even = []
    for i in x:
        if i%2==0:
            even.append(i)
    print(f'The even number in list: {even}')

# call function
find_max(num)
find_min(num)
find_total(num)
find_even(num)
