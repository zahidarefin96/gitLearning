"""
Given an array of integers (positive and negative) find the largest continuous sum.

Input: [1, 2, -1, 3, 4, 10, 10, -10, -1]
Output: 29 (1 + 2 + -1 + 3 + 4 + 10 + 10 = 29)
"""


# O(n)
def find_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


test_arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]

print(f'test_arr = ', test_arr)

print(find_sum(test_arr))
