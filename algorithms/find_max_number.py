"""

Find max number from 3 values, entered manually from a keyboard.

Example: 124, 21, 32. Result = 124.

"""

# O(n)
a = int(input('Input your first number: '))
b = int(input('Input your second number: '))
c = int(input('Input your third number: '))

if (a >= (b and c)):
    print(f'Max number is ', a)
elif (b >= (a and c)):
    print(f'Max number is ', b)
elif (c >= (a and b)):
    print(f'Max number is ', c)
else:
    print(f'error!')

# built-in function
# print(f'Max number is ', max(a, b, c))
