# List

mylist = ['apple', 'banana', 'cherry']
print(mylist)
print(type(mylist))

# accessing to items in list
# index
print(mylist[0])  # apple
print(mylist[1])  # banana
print(mylist[2])  # cherry
#print(mylist[3])

# negative index
print(mylist[-1], mylist[2])  # cherry
print(mylist[-2], mylist[1])  # cherry
print(mylist[-3], mylist[0])  # cherry

# range index [:]
mylist = ['apple', 'banana', 'cherry', 'orange', ' grap']
# display --> cherry,orange
print(mylist[2:4])
# display --> banana,cherry,orange
print(mylist[1:4])
# blank at start
print(mylist[:4])  # display 0 to 3
# blank at stop
print(mylist[3:])  # display 3 to end
#print(mylist[:-4])  # diplay -1 to -2

# change data in list
# chanage index 1 to 'papaya'
mylist[1] = 'papaya'  # banana --> papaya
print(mylist)
mylist[-1] = 'mango'  # grap --> mango
print(mylist)


# add new item to list
mynum = [20, 10, 30, 40, 100]
print(mynum)
# append() -- add new item at last
mynum.append(50)
print(mynum)
# insert()  -- insert new item at specific index
mynum.insert(2, 200)  # add 200 to index 2
print(mynum)
mynum[2:3] = [70, 80]
print(mynum)

# delete item in list
# remove()
mynum.remove(100)
print(mynum)
mynum.append(20)
print(mynum)
mynum.remove(20)
print(mynum)

# pop() using index
mynum.pop(0)  # delete item at index 0
print(mynum)
mynum.pop()  # delete last item in list
print(mynum)

# del keyword
del mynum[0]
print(mynum)

del mynum
#print(mynum)

# clear()
mynum = [1,2,3,4,5]
print(mynum)
mynum.clear()  # make list to empty
print(mynum)







