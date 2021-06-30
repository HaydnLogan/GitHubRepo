# Algorithms HW1
#  Find max number from 3 values, entered manually from a keyboard.

# using built in functions
# 0(1)  no loops
def maximum(a, b, c):
    list = [a, b, c]
#   return max(list)
    return max(a, b, c)

# not using built in functions
def find_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

x = int(input('number 1: '))
y = int(input('number 2: '))
z = int(input('number 3: '))


print(f'Maximum Number is', maximum(x, y, z))
print(f'Max number is', find_max(x, y, z))
