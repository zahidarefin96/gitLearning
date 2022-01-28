# O(n)
def group_anagrams(strs):
    hash_map = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in hash_map.keys():
            hash_map[key].append(word)
        else:
            hash_map[key] = []
            hash_map[key].append(word)

    return list(hash_map.values())


test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(test_strs))
