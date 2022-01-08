"""
Given a string, determine if it consists of all unique characters.

For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
"""


# def uniqueCharacters(str):
#     return len(set(str)) == len(str)

# test_str = "aabcde"

# test_str_positive = "abcde"
# test_str_negative = "aabcde"
#
# print(test_str_positive)
# print(uniqueCharacters(test_str_positive))
#
# print(test_str_negative)
# print(uniqueCharacters(test_str_negative))

# O(n) --> n represents the number of characters
def uniqueCharacters(str):
    if len(str) == 1:
        return True

    chars = set()
    for char in str:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True


test_str_positive = "abcde"
test_str_negative = "aabcde"

print(test_str_positive)
print(uniqueCharacters(test_str_positive))

print(test_str_negative)
print(uniqueCharacters(test_str_negative))
