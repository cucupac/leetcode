nums = [1, 1]

write_index = 0

duplicate_value = None


i = 0
while i < len(nums):
    if nums[i] != duplicate_value:  # do check
        # Past duplicate values, so we can set deplicate value back to None
        duplicate_value = None
        if i < len(nums) - 2:
            if nums[i] != nums[i + 1]:  # count of 1
                nums[write_index] = nums[i]
                write_index += 1
            elif nums[i] == nums[i + 1] and nums[i] != nums[i + 2]:  # count of 2
                # write 2, skip next iteration
                nums[write_index] = nums[i]
                nums[write_index + 1] = nums[i + 1]
                write_index += 2
                i += 1  # skip next iteration
            else:  # greater than 2 count
                duplicate_value = nums[i]
                # write 2, skip next iteration
                nums[write_index] = nums[i]
                nums[write_index + 1] = nums[i + 1]
                write_index += 2
                i += 1  # skip next iteration
        else:
            if i == len(nums) - 2:
                # write 2, skip next iteration
                nums[write_index] = nums[i]
                nums[write_index + 1] = nums[i + 1]
                write_index += 2
                i += 1  # skip next iteration
            elif i == len(nums) - 1:
                nums[write_index] = nums[i]
                write_index += 1
    i += 1


# Remove duplicates
del nums[write_index:]

print("nums:", nums)
