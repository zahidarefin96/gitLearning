"""
Given an array of integers, write a function to move all 0's to the end
while maintaining the relative order of the other elements.

Input: [0, 4, 0, 3, 12]
Output: [4, 3, 12, 0, 0]
"""


def move_zeros(arr):
    i = 0

    for num in arr:
        if num != 0:
            arr[i] = num
            i = i + 1

    while i < len(arr):
        arr[i] = 0
        i = i + 1

    return arr


test_arr = [0, 4, 0, 3, 12]
print(test_arr)
print(move_zeros(test_arr))
