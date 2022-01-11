"""
Given an array of integers, return true if the following conditions are fulfilled:
- length of the array is bigger than or equal to 3
- there exists some index i such that:
a[0] < a[1] < ... < a[i]
a[i] > a[i+1] > ... > a[a.size-1]

Basically, find if there is an increasing subarray followed by a decreasing subarray
[3, 5, 5] -> false
[3, 4, 5, 2] -> true
"""


def is_mountain(arr):
    if len(arr) < 3:
        return False

    i = 1
    while i < len(arr) and arr[i] > arr[i - 1]:
        i = i + 1
    if i == len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i - 1]:
        i = i + 1

    return i == len(arr)


test_arr_positive = [3, 4, 5, 2]
test_arr_negative = [3, 5, 5]

print(test_arr_positive)
print(f'result:', is_mountain(test_arr_positive))

print(test_arr_negative)
print(f'result:', is_mountain(test_arr_negative))
