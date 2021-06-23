# User inputs two numbers.  One number is assigned to a variable, the other # is assigned
# The tast is to invert the variables, so that the first variable contains the second number,
# is in the second variable.


def swap_ab(a, b):
#   temp = a  #Ver1
#   a = b
#   b = temp

#   a = a + b  # Ver2  use this one
#   b = a - b
#   a = a - b

    a, b = b, a # Ver3

    print(f'a = {a}, b = {b}')


a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'a = {a}, b = {b}')
swap_ab(a, b)

