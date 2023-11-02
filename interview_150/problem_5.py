"""Majority Element."""

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


"""Initial Solution."""
nums = [3, 2, 3]

majority_condition = len(nums) / 2

vals_count = {}

for val in nums:
    if not vals_count.get(val):
        vals_count[val] = 1
    else:
        vals_count[val] += 1

    if vals_count[val] > majority_condition:
        print(val)
        break

"""
More efficient solution.
The number must have a positvie count.
There can only be one majority.
Any number that is not the current candidate is a vote against the current candidate.
Any number that is the current candidate is a vote for the current candidate.
This approach tallies all votes across all candidates, thereby arriving at the majority element.
"""
count = 0
candidate = None

for num in nums:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1

print(candidate)
