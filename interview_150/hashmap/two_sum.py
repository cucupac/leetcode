nums = [2, 7, 11, 15]
target = 9

indexes = dict()

for current_i, num in enumerate(nums):
    needed_amt = target - num
    needed_i = indexes.get(needed_amt)
    if needed_i is not None:
        print([needed_i, current_i])

    indexes[num] = current_i
