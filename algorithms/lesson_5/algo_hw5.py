# Even First
"""  Your input is an array of integers, and you have to reorder its entries so that the even entries
appear first.  You are required to solve it without allocating additional storage (operate with the input array).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]  """


def reorder_evens(arr):
    # j = 0
    #
    # for num in arr:
    #     if num % 2 == 0:
    #         arr[j] = num
    #         j += 1
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1


test_data = [7, 3, 5, 6, 4, 10, 3, 2]
print(test_data)
reorder_evens(test_data)
print(test_data)
# print(reorder_evens([test_data]))
# reorder_evens(test_data)



# Incremental Number
"""  Write a program that takes as input an array of digits encoding a non-negative decimal integer D and updates
the array to represent the integer D +1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].  """

def plus_one(arr):
    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

print()
print("Incremental Number")
test_data2 = [2, 5, 7]
print(test_data2)
print(plus_one(test_data2))
