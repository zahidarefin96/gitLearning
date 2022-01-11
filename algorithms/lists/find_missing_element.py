"""
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random
element.
Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the
second array.

Input: [1,2,3,4,5,6,7], [3,7,2,1,4,6]
Output: 5 is the missing number
"""

import collections


# O(n)
def find_missing_number(arr1, arr2):
    dict = collections.defaultdict(int)

    for num in arr2:
        dict[num] += 1

    for num in arr1:
        if dict[num] == 0:
            return num
        else:
            dict[num] -= 1


test_arr1 = [1, 2, 3, 4, 5, 6, 7]
test_arr2 = [1, 2, 3, 4, 5, 6]

print(f'test_arr1 =', test_arr1)
print(f'test_arr2 =', test_arr2)
print(f'missing number is :', find_missing_number(test_arr1, test_arr2))
