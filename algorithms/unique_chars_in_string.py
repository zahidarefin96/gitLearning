"""
Given a string, determine if it consists of all unique characters.

For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
"""


def uniqueCharacters(str):
    # same characters, return false
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if (str[i] == str[j]):
                return False
    # If no duplicate characters, return true
    return True


# Driver Code
test_str = "aabcde"

if (uniqueCharacters(test_str)):
    print(f"The String", test_str, "has all unique characters")
else:
    print("The String", test_str, "contains duplicate characters")
