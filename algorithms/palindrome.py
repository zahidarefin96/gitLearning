"""
A palindrome is a word that reads the same in reverse.

For example radar is a palindrome, radix is not a palindrome.
"""


# O(1)
def is_palindrome(s):
    return s == s[::-1]


# str = "radar"
str = (input('Input your word to verify palindrome: '))
if is_palindrome(str):
    print(f'{str} is a palindrome')
else:
    print(f'{str} is not a palindrome')
