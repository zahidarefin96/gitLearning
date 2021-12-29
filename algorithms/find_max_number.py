"""

Find max number from 3 values, entered manually from a keyboard.

Example: 124, 21, 32. Result = 124.

"""

# O(1) -> Constant time
n1 = int(input('Input your first number: '))
n2 = int(input('Input your second number: '))
n3 = int(input('Input your third number: '))


def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    return n3


print(f'Max number is', find_max(n1, n2, n3))

# built-in function (not recommended)
# print(f'Max number is', max(n1, n2, n3))
