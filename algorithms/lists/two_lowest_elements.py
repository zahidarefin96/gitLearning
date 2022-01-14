"""
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.

Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

"""


def find_two_lowest_element(arr):
    arr.sort()
    return arr[:2]


test_list = [198, 3, 4, 9, 10, 9, 2]
print(test_list)
print(f'final:', find_two_lowest_element(test_list))
