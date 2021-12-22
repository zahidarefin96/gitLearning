"""
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.

How would you test it? How would you handle edge cases?
"""

"""

# not reccomeneded
def unique_letter(string: str):
    if not string:
        raise ValueError

    string = string.lower()  # Google => google
    for letter in string:  # O(n)
        if string.count(letter) == 1:  # O(n)
            return letter
    return ""


# O(n) * O(n) = O(n^2)

print(unique_letter('llajhgjvv'))

"""


def unique_letter(string: str):
    if not string:
        raise ValueError

    string = string.lower()  # Google => google
    d = {}  # {"g": 2, "o":2, "l":1, "e":1}

    for letter in string:  # O(n)
        if letter not in d:
            d[letter] = 1

        else:
            d[letter] += 1
    print(d)

    for k, v in d.items():  # O(n)
        if v == 1:
            return k

    return ""


print(unique_letter('llajhgjvv'))
