# If statement

print('Start')

x = int(input('Enter a integer: '))
if x > 100:
    print(f' {x} more than 100.')
elif x < 100:
    print(f'{x} less than 100.')
else:
    print(f'{x} equal to 100.')

print('End')

# short hand

print(f'{x} more than 100') if x>100 else print(f'{x} less than 100.') \
    if x <100 else print(f'{x} is 100')