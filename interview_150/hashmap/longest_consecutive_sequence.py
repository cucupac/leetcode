# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

# nums = [100, 4, 200, 1, 3, 2]

# nums = [1, 2, 0, 1]

# nums = [0, 0, -1]

nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

# nums = [9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]


if len(nums) == 0:
    print(0)
    raise Exception("Done.")

pruned_nums = sorted(set(nums))

longest_count = 1
current_count = 1

nums_dict = dict()

for i, num in enumerate(pruned_nums):
    if i > 0:
        if num == pruned_nums[i - 1] + 1:
            # sequence followed: increase current count
            current_count += 1
            if i == len(pruned_nums) - 1 and current_count > longest_count:
                # if last elem update longest count if need be
                longest_count = current_count
        else:
            # sequence broken: udpate longest if need be; reset current_count
            if current_count > longest_count:
                longest_count = current_count
            current_count = 1

print(longest_count)
