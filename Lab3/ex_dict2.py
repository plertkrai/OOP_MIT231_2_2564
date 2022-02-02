# Nested Dictionaries

car1 = {'brand':'toyota','model':'cross','year':'2021'}
car2 = {'brand':'honda','model':'hrv','year':'2021'}
car3 = {'brand':'gratewall','model':'haval 6','year':'2021'}

print(car1)
print(car2)
print(car3)

# nested dict
mycar = {'car1':car1,
         'car2':car2,
         'car3':car3}

print(mycar['car1'])

for x,y in mycar.items():
    print(f'{x}:{y}')

# แสดงข้อมูลทั้งหมดใน dict car
print(mycar)
# แสดงข้อมูลเฉพาะ key ของ dict car
print(mycar.keys())
# แสดงข้อมูลเฉพาะ value ของ dict car
print(mycar.values())