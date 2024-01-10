from collections import Counter


"""Beats 70% of people on time complexity, 38% of people with space complexity."""

# ransomNote = "aa"
# magazine = "ab"

# r_dict = Counter(ransomNote)
# m_dict = Counter(magazine)

# for char in r_dict:
#     available_count = m_dict.get(char)
#     if available_count:
#         if r_dict[char] <= available_count:
#             continue
#         else:
#             print(False)
#             raise Exception("Done.")
#     else:
#         print(False)
#         raise Exception("Done.")
# print(True)


"""Beats 44% of people on time complexity, 11% of people with space complexity."""
# r_dict = dict()
# m_dict = dict()

# # Construct counts 2 * O(N)
# for char in ransomNote:
#     if not r_dict.get(char):
#         r_dict[char] = 1
#     else:
#         r_dict[char] += 1

# for char in magazine:
#     if not m_dict.get(char):
#         m_dict[char] = 1
#     else:
#         m_dict[char] += 1

# for char in r_dict:
#     available_count = m_dict.get(char)
#     if available_count:
#         if r_dict[char] <= available_count:
#             continue
#         else:
#             print(False)
#             raise Exception("Done.")
#     else:
#         print(False)
#         raise Exception("Done.")
# print(True)
