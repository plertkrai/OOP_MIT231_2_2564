# Set

myset = {10,20,30,40,50}
print(myset)
print(type(myset))

# for
for x in myset:
    print(x)

# in operator
print(10 in myset)
print(100 in myset)

# add data to set
# add()
myset.add(100)
print(myset)
myset.add(100)  # add duplicate data
print(myset)
# update()
myset2 = {100,200,300}
myset.update(myset2)
print(myset)
# union
myset1 = {'a','b','c'}
myset2 = {10,20,30}
myset3 = myset1.union(myset2)
print(myset3)

# delete data in set
# remove()
myset3.remove(30)
print(myset3)
print(len(myset3))
# myset3.remove(30)
# print(myset3)
# discard()
myset3.discard(10)
print(myset3)
# pop
p = myset3.pop()
print(p)
print(myset3)
