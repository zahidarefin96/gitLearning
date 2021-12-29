"""
Write a function to check whether two given strings are anagram of each other or not.

An anagram of a string is another string that contains the same characters, only the order of characters can be different.
For example, “abcd” and “dabc” are an anagram of each other.
"""


# def is_anagram(str1, str2):
#     if len(str1) != len(str2):
#         return False
#
#     return sorted(str1) == sorted(str2)
#
#
# s1 = "abcd"
# s2 = "bacd"
# s3 = "aabc"
#
# print(is_anagram(s1, s2))
# print(is_anagram(s2, s3))


# recommended
# O(n)
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    count = {}

    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


s1 = "abcd"
s2 = "bacd"
s3 = "aabc"

print(is_anagram(s1, s2))
print(is_anagram(s2, s3))
