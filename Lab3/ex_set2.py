# set

x = {10, 20, 30, 40, 50}
y = {20, 40, 60, 70, 80}

# intersection
z = x.intersection(y)
print(f'Intersection between x and y is {z}')
# intersection update
#x.intersection_update(y)
#print(x)

# symatric differance
z = x.symmetric_difference(y)
print(f'ข้อมูลที่แตกต่างกันของ x และ y คือ {z}')
print(f'ข้อมูลที่แตกต่างกันของ x ={x} และ y={y} \n คือ {z}')

print(x.issuperset(y))
z = x.union(y)
print('z = ',z)
print('x = ',x)
print('y = ',y)
print(z.issuperset(x))
print(z.issuperset(y))
print(x.issuperset(z))
