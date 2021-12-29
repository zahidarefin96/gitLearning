"""

When a user enters a number n, find the sum of digits in all numbers from 1 to n.

Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

"""


# O(n) -> linear time
# def sum(n):
#     final_result = 0
#     for x in range(1, n + 1):
#         final_result = final_result + x
#     return final_result


# Recommended
# O(1) -> Constant time
def sum(n):
    final_result = (n * (n + 1)) / 2
    return final_result


number = int(input('Input your number: '))
print(f'Sum of digits is:', sum(number))
