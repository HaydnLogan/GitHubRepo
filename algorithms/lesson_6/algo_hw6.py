"""
1.	Selection Sort
Implement the selection sort algorithm that is sorting in descending order.  """


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_index]:  # ascend or descend controller
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_data = [1, 4, 3, 6, 2]
print(f"    Selection Data:", test_data)
print(f"Selection descends:", selection_sort(test_data))
print()

"""
2.	Bubble Sort
Implement the bubble sort algorithm that is sorting in descending order.  """


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) -1 -i):
            if arr[j] < arr[j + 1]:  # ascend or descend controller
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_data2 = [2, 5, 3, 6, 9]
print(f"    Bubble Data:", test_data2)
print(f"Bubble descends:", bubble_sort(test_data2))
print()

"""
3.	Insertion Sort
Implement the insertion sort algorithm that is sorting in descending order.  """


def insertion_sort(arr):
    for i in range(1, len(arr)):  # starts at index 1
        key = arr[i]
        j = i -1 # compare with previous element

        while j >= 0 and key > arr[j]:  # Key is ascend or descend controller
            arr[j +1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


test_data3 = [1, 4, 3, 6, 2]
print(f"    Insertion Data:", test_data3)
print(f"Insertion descends:", insertion_sort(test_data3))