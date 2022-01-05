"""
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.

Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
"""

test_str = "bbbbbcaaaaa"

print("The original string is: " + test_str)

n = 6
chunks = [test_str[i:i + n]
          for i in range(0, len(test_str), n)]
print(chunks)

a = chunks[0]
b = chunks[1]

temp = a
a = b
b = temp

print(f'after swap:', a, b)
print(f'Final result:', a + b)
