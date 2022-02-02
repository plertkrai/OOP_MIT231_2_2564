# list uing loop

mylist = [10,20,30,40,50]
print(mylist)

for x in mylist:
    print(x, end=' ')

# loop with index
print('\n')

for x in range(len(mylist)):
    print(mylist[x], end=' ')

print('\n')
for x in range(len(mylist)):
    if mylist[x] % 3 == 0:
        print(mylist[x], end=' ')

print('\n')

# while loop
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1
