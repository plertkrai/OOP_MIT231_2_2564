# Dictionary  key:value

car = {'brand': 'toyota', 'model': 'cross', 'year': '2021'}
print(car)
print(type(car))
print(f'Length of dict car: {len(car)}')

# access data in dict
# refer to key
print(car['brand'])  # toyata
print(car['model'])  #
print(car['year'])  #
# get key of dict
kcar = car.keys()
print(f'keys of car: {kcar}')
# get value of dict
vcar = car.values()
print(f'values of car: {vcar}')

# get()
print(car.get('brand'))

# loop
# display key
for x in car:
    print(x)
for x in car.keys():
    print(x)
# display value
for x in car:
    print(car[x])
for x in car.values():
    print(x)
# display item
x = car.items()
print(x)
for x in car.items():
    print(x)

# change data in dict
car['year'] = 2022
print(car)
car.update({'model':'camry'})
print(car)

# add new item to dict
car['color'] = 'red'
print(car)
car.update({'engine':'2000 cc'})
print(car)

# delete item in dict
car.pop('brand')  # del brand
print(car)
car.popitem()  # del last item in dict
print(car)
# del keyword
del car['year']
print(car)
# del car  # del completely
# print(car)
# clear()
car.clear()
print(car)




