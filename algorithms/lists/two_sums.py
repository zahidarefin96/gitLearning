"""
Given an array of integers nums and an integer target.
Return two numbers from the array such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same
element twice.

You can return the answer in any order.

Input: [3, 7, 4, 9, 15, 3], 6
Output: 3, 3
"""


def two_sums(arr, k):
    if len(arr) == 2:
        return arr

    sum_set = set()

    for num in arr:
        target = k - num

        if target not in sum_set:
            sum_set.add(num)
        else:
            return [num, target]


target_value = 6
test_arr = [3, 7, 4, 9, 15, 3]  # [3,3]
print(test_arr)
print(two_sums(test_arr, target_value))
