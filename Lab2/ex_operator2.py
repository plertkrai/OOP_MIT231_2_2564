# operators
# comparasion operators
# result of comparasion: True, False
x, y = 100, 200
# == equal to
print(x == y)  # False
# > more than
print(x > y)  # False
# < less than
print(x < y)  # True
# >=  more than or equal to
print(10 >= 10)  # ?  True
# <= less than or equal to
print(5 <= 10)  # True

# logical operators
# and, or, not
# and - True if any statments is True
print((10 < 100) and (100 < 1000))  # True
print((10 > 100) and (100 < 1000))  # False
# or - True if one of those statments is True
print((10 > 100) or (100 < 1000))   # True
print((10 > 100) or (100 > 1000))   # False
# not - reverse True-->False, False-->True
x = True
print('The value of x:', x)  # True
print('The value of (not)x:', not x)  # False

# identity operators --> is, is not
x = 'MIT'
y = 'MIT'
print(x is y)  # True
a = 100
b = 100
print(a is b)  # True
print(a is not b)  # False
# compare with memory position
x = [1,2,3,4,5]
y = [1,2,3,4,5]
print('x is y?: ',x is y)  # ?
print('x is not y?: ',x is not y)  # ?
z = x
print('z is x?: ', z is x)

# assignment operators
# =
x = 100
print(x)
# +=
x += 100  # x = x+100
print(x)
# -=

# *=

# /=

# **=

# %=

# //=








