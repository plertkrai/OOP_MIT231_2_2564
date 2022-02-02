# Tuple

mytuple = ('apple','banana','cherry')
print(mytuple)
print(type(mytuple))  # class 'tuple'

# create tuple with one item
mytuple = ('apple',)
print(mytuple, type(mytuple))

# access to item in tuple
mytuple = ('apple','banana','cherry')
# index
print(mytuple[0])  # apple
print(mytuple[1])  # banana
print(mytuple[2])  # cherry
# negative index
print(mytuple[-1])  # cherry
print(mytuple[-2])  # banana
print(mytuple[-3])  # apple
# range index
mynum = (10,20,30,40,50)
print(mynum)
print(mynum[1:3])  # index 1,2 --> 20,30
print(mynum[-4:-1])  # index -4,-3,-2 --> 20 30 40
# Loop
# for
for x in mynum:
    print(x)

for x in range(len(mynum)):
    print(mynum[x])
# while
i = 0
while i < len(mynum): # 5
    print(mynum[i])
    i+=1
