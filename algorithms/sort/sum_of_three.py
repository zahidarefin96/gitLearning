def sum_of_three(arr):
    arr_set = set()
    arr.sort()

    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1

        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == 0:
                arr_set.add((arr[i], arr[j], arr[k]))
                k = k - 1
                j = j + 1
            elif sum > 0:
                k = k - 1
            else:
                j = j + 1

    return [list(i) for i in arr_set]


test_arr = [-1, 0, 1, 2, -1, -4]
print(test_arr)
print(sum_of_three(test_arr))
