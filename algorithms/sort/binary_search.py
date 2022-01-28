# O(log n)
def binary_search(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

    return -1


test_arr = [1, 4, 7, 9, 11, 15, 19, 27, 91]
print(test_arr)
print(binary_search(test_arr, 7))  # 2
print(binary_search(test_arr, 44))  # -1
