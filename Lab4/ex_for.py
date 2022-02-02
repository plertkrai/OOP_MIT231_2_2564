# For loop

mylist = [10,20,30,40,50]

for x in mylist:
    if x ==20 or x ==40:
        continue
    print(x)

for x in range(5):  # 0-4
    print(x)

for x in range(1,6):  # 1-5
    print(x)

for x in range(1,20,3):  # 1-19 increment my 3
    print(x)