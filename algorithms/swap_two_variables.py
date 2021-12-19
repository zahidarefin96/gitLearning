"""
user will input 2 numbers;
user will see --
first number in 2nd position
second number in 1st position
"""

a = int(input('Input your first number: '))
b = int(input('Input your second number: '))

print(f'before swap: ', a, b)

# preferred way 1
temp = a
a = b
b = temp

# preferred way 2
# a = a + b
# b = a - b
# a = a - b

# built-in method, but not preferred
# a, b = b, a

print(f'after swap: ', a, b)
