def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_list = [2, 1, 6, 9, 7, 3]
print(test_list)
print(bubble_sort(test_list))
