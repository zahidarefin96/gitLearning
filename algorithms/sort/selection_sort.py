# O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


list_to_sort = [4, 6, 1, 2, 9, 7]
print(list_to_sort)
print(selection_sort(list_to_sort))
