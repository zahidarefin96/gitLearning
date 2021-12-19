"""
given an integer, return the integer with reversed digits
"""


# 0(1)
def solution(n):
    n_str = str(n)

    if n_str[0] == '-':
        return int('-' + n_str[:0:-1])
    else:
        return int(n_str[::-1])


print(solution(6421))
print(solution(-82))
