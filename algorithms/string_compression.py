"""
Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4".

The function should also be case sensitive, so that a string "AAAaaa" returns "A3a3".
"""


# O(n)
def compress_string(s):
    comp = ""  # comp -> compressed
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s + "1"

    last = s[0]
    cnt = 1  # cnt -> count
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            comp = comp + s[i - 1] + str(cnt)
            cnt = 1
        i += 1

    comp = comp + s[i - 1] + str(cnt)

    return comp


test_str = "AAAABBBBCCDDD"
print(test_str)
print(compress_string(test_str))
