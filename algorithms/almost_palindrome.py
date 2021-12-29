"""
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

The string will only contain lower-case characters a-z and it's not a palindrome.

For example:
"radkar" is almost a palindrome.
"radrio" is not almost a palindrome.
"""


# O(n)
def is_almost_palindrome(s):
    for i in range(len(s)):
        t_str = s[:i] + s[i + 1:]
        if t_str == t_str[::-1]:
            return True

    return False


test_str = "radkar"
print(is_almost_palindrome(test_str))
