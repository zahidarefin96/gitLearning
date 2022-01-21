"""
Write a program that takes as input an array of digits encoding a non-negative decimal integer D and
updates the array to represent the integer D + 1.

For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0]
"""


# O(n)
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
        # arr.insert(0, 1)

    return arr


test_arr_124 = [1, 2, 4]
test_arr_129 = [1, 2, 9]
test_arr_999 = [9, 9, 9]
print(f'original arr:', test_arr_124)
print(f'result:', plus_one(test_arr_124))
print(f'original arr:', test_arr_129)
print(f'result:', plus_one(test_arr_129))
print(f'original arr:', test_arr_999)
print(f'result:', plus_one(test_arr_999))
