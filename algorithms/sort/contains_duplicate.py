# O(1)
def contains_duplicate(nums):
    if len(nums) > 1:
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True

    return False


test_nums_positive = [1, 5, 7, 8, 5, 0, 9]
test_nums_negative = [1, 6, 5, 3, 8, 10, 9]
print(contains_duplicate(test_nums_positive))  # True
print(contains_duplicate(test_nums_negative))  # False
