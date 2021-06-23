# Algorithms HW1
#  Find max number from 3 values, entered manually from a keyboard.


def maximum(a, b, c):
    list = [a, b, c]
    return max(list)


x = int(input('number 1: '))
y = int(input('number 2: '))
z = int(input('number 3: '))


print(f'Maximum Number is', maximum(x, y, z))
