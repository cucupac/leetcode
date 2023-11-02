"""Rotate Array."""

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

nums = [-1, -100, 3, 99]
k = 2


if k < len(nums):
    last_k_elems = nums[-k:]
    non_overflow_elems = nums[: len(nums) - k]
    nums[0 : k + 1] = last_k_elems
    nums[k : len(nums)] = non_overflow_elems
elif k > len(nums):
    new_k = k % len(nums)
    last_k_elems = nums[-new_k:]
    non_overflow_elems = nums[: len(nums) - new_k]
    nums[0 : new_k + 1] = last_k_elems
    nums[new_k : len(nums)] = non_overflow_elems

print(nums)

# The following does not account for cases where k is greater than array length
# ----------------------------------------------------------------------
# What I can do is:
# - identify and store chunk that can shift right
#     - shift that chunck k spaces using list slicing
# - identify and store chunk that must be moved to the left (last k elements)
#     - replace first k elements with this chunk using list slicing


# last_k_elems = nums[-k:]
# non_overflow_elems = nums[: len(nums) - k]
# nums[0 : k + 1] = last_k_elems
# nums[k : len(nums)] = non_overflow_elems

# print(nums)

# The following does not modify in-place
# ----------------------------------------------------------------------
# reordered_nums = [None] * len(nums)

# for i, val in enumerate(nums):
#     overflow = (i + k) - (len(nums) - 1)
#     if overflow > 0:
#         reordered_nums[overflow - 1] = val
#     else:
#         reordered_nums[i + k] = val


# print(reordered_nums)
