# Algorithms HW1
# Count odd and even numbers.  Count odd and even digits of the whole number.


def odd_numbers(n):
    if n == 0:
        return 0
    elif (n % 10) % 2 == 0:  # remainder operator
        return odd_numbers(n // 10)
    elif (n % 10) % 2 == 1:
        # Include the digit and recurse for remaining...
        return (n % 10) + 10 * odd_numbers(n // 10)


def eve_numbers(n):
    if n == 0:
        return 0
    elif (n % 10) % 2 == 1:
        return eve_numbers(n // 10)
    elif (n % 10) % 2 == 0:
        # Include the digit and recurse for remaining...
        return (n % 10) + 10 * eve_numbers(n // 10)


def countEvenOdd(n):
    even_count = 0
    odd_count = 0
    while n > 0:
        rem = n % 10
        if rem % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n = int(n / 10)

    print("Even count : ", even_count)
    print(" Odd count : ", odd_count)


n = int(input('Input number: '))
t = countEvenOdd(n)
odd_numbers(n)
eve_numbers(n)


print(f'Odd numbers of {n} are', odd_numbers(n))
print(f'Even numbers of {n} are', eve_numbers(n))
