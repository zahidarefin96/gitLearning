# O(n * log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1

    return merged_array


list_to_sort = [5, 4, 1, 9, 11, 2]
print(list_to_sort)
print(merge_sort(list_to_sort))
