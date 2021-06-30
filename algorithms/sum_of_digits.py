# Algorithms HW1
# Compute the sum of digits in all numbers from 1 to n

def factorial(n):
    result = 0

    if n != 0:
        for i in range(1, n + 1):
            result += i
    print(f'Factorial of {n} is {result}')


number = int(input('Input number: '))
factorial(number)


# 0(1)
def sum2(n):
    return (n * (n +1)) /2

num = int(input("Input number: "))
print(sum2(num))