strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


anagrams = {}

for word in strs:
    sorted_word = tuple(sorted(word))  # KEY INSIGHT: Standardize all words by sorting

    if not anagrams.get(sorted_word):
        anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word].append(word)


print([val for val in anagrams.values()])


# """ WORKS, BUT IT'S VERY SLOW."""
# char_counts = dict()


# for word in strs:
#     char_counts[word] = Counter(word)

#     hashable_counts = json.dumps(Counter(word), sort_keys=True)
#     if not char_counts.get(hashable_counts):
#         # the list is empty -> the set hasn't been added yet
#         char_counts[hashable_counts] = []
#         char_counts[hashable_counts].append(word)
#     else:
#         # the set has been added
#         char_counts[hashable_counts].append(word)


# print([val for val in char_counts.values()])
