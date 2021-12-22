"""

When a user enters a number n, find the sum of digits in all numbers from 1 to n.

Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

"""


# O(n)
def sumOfDigits(x):
    sum = 0
    while (x != 0):
        sum = sum + x % 10
        x = x // 10

    return sum


n = int(input('Input your number: '))
print("Sum of digits in numbers from 1 to", n, "is", sumOfDigits(n))
