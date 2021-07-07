"""
The equation for the Fibonacci sequence:
v0 = 0, v1 = 1, vn = vn-1 + vn-2
The task is to display all the numbers from start to n of the Fibonacci sequence vn

Equation:
F0 = 0
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2

1  1  2  3  5  8  13
"""

def fibonacci(n):
    if n < 0:
        return "Not a valid value"
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return  [1, 1]

    index = 3
    fib_1 = 1
    fib_2 = 1

    result = [fib_1, fib_2]

    while index <= n:
        result.append(fib_1 + fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1

    return  result

print(fibonacci(7))
