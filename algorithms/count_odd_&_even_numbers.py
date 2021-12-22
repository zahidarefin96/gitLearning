"""

Count odd and even numbers. Count odd and even digits of the whole number.

Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

"""

# O(n^2)
a = int(input('Input your number: '))

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f'Even:', even, 'Odd:', odd)
