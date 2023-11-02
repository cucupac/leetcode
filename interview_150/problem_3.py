nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

"""Initial answer"""
# indexes_to_remove = []
# nums_count = 0
# for i, num in enumerate(nums):
#     if num == nums[i - 1] and i > 0:
#         indexes_to_remove.append(i)
#     nums_count += 1

# removal_count = 0
# for index in indexes_to_remove:
#     del nums[index - removal_count]
#     removal_count += 1

# print("k:", nums_count - removal_count)
# print("nums:", nums)

"""More efficient answer"""

# Doesn't even engage in computation if no length -> it can do the same if len(nums) = 1
if not nums:
    print(0)

write_index = 1  # Position to overwrite duplicates

for read_index in range(1, len(nums)):
    if nums[read_index] != nums[read_index - 1]:
        nums[write_index] = nums[read_index]
        write_index += 1

# Truncate the remaining duplicates
del nums[write_index:]

print(write_index)
