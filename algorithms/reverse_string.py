"""
Given a string. Returns a reversed string.

example: abcde -> edcba
"""


# O(n)
def reverse_string(s):
    reversed = ""
    index = len(s) - 1

    while index >= 0:
        reversed += s[index]
        index -= 1

    return reversed


# test_str = "string"
test_str = input("Input your word to reverse: ")
print(test_str)
print(reverse_string(test_str))
