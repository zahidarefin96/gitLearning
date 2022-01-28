# O(n)
def is_valid_parenthesis(s):
    parenthesis = {'(': ')', '[': ']', '{': '}'}
    control = []

    for i in s:
        if i in parenthesis:
            control.append(parenthesis[i])
        elif control.pop() != i:
            return False

    if len(control) == 0:
        return True
    else:
        return False


test_string_positive = '{()[]}'
test_string_negative = '{([)]}'
print(is_valid_parenthesis(test_string_positive))
print(is_valid_parenthesis(test_string_negative))
