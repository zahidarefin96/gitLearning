# O(n^2)
def product_of_array_n2(arr):
    n = len(arr)
    result = [1] * n

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                result[i] = result[i] * arr[j]

    return result


# O(n)
def product_of_array_n(arr):
    result = [1] * len(arr)

    for i in range(0, len(arr) - 1):
        result[i + 1] = result[i] * arr[i]

    for i in range(0, len(arr) - 1):
        result[-1 - i] *= result[0]
        result[0] *= arr[-1 - i]

    return result


test_arr = [1, 2, 3, 4]
print(product_of_array_n2(test_arr))
print(product_of_array_n(test_arr))
