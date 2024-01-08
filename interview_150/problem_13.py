import math

nums = [1, 2, 3, 4]


single_zero_index = None
single_zero_answer = None
answers = []
nums_length = len(nums)
total_product = math.prod(nums)

# Check for single 0
for i, num in enumerate(nums):
    if num == 0:
        if single_zero_index is not None:
            # return
            raise Exception("all zeros")
        else:
            single_zero_index = i

# Get answer for zero index
if single_zero_index is not None:
    nums.pop(single_zero_index)
    single_zero_answer = math.prod(nums)
    nums.insert(single_zero_index, 0)

print(single_zero_index)
print(single_zero_answer)

# Construct answers
for i, num in enumerate(nums):
    if single_zero_index is not None and i == single_zero_index:
        answers.append(single_zero_answer)
    else:
        answers.append(int(total_product * num**-1))

print(answers)
