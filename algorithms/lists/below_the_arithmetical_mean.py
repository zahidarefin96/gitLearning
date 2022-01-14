"""
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
The arithmetical mean is the sum of all elements divided by the number of elements.

Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

"""


# O(n)
def below_arithmetical_mean(arr):
    arithmetical_mean = sum(arr) / len(arr)
    final_list = []

    for num in arr:
        if num < arithmetical_mean:
            final_list.append(num)
    return final_list


test_list = [1, 3, 5, 6, 4, 10, 2, 3]
print(test_list)
print(f'result:', below_arithmetical_mean(test_list))
