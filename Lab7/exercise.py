"""
ให้สร้าง class Animal โดยประกอบด้วย attributes 3 ตัว คือ
ืname age และ breed

ให้สร้าง class Dog โดยที่ Dog สืบทอดจาก class Animal
ให้สร้าง class Cat โดยที่ Cat สืบทอดจาก class Animal

โดยมี class Dog Cat จะมีฟังก์ชั่นชื่อ make_sound()
dog --> "Hong Hong Hong"
cat --> "Meaw Meaw Meaw"

จากนั้นให้ทำการรับข้อมูลจากผู้ใช้เป็นข้อมูล dog 1 ตัว และ cat 1 ตัว
"""

class Animal:
    def __init__(self,name,age,breed):
        # object attributes
        self.name = name
        self.age = age
        self.breed = breed

    def display_animal(self):
        print(f'name:{self.name} age:{self.age} breed:{self.breed}')

class Dog(Animal):
    def make_sound(self):
        print('Hong Hong Hong')

class Cat(Animal):
    def make_sound(self):
        print('Meaw Meaw Meaw')

dog1 = Dog('Lulu',5,'Bangkeaw')
cat1 = Cat('samock',5,'Thai')

dog2 = Animal('Lala',3,'Pluge')

dog1.display_animal()
cat1.display_animal()
dog2.display_animal()


