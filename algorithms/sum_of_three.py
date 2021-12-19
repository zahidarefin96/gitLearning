"""
user will see sum of three numbers

example: 123 -> 6
"""

from random import randint

random_number = randint(100, 999)

print(f'Our random number is {random_number}')

"""
solution 1
result = 0
for digit in str(random_number):
    result = result + int(digit)
"""

# O(n)
# solution 2
# random_number = 123
result = 0
while random_number != 0:
    result = result + (random_number % 10)
    random_number = random_number // 10

print(f'Result of the sum is {result}')
