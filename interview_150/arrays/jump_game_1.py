"""
Solution:
    On first pass, store:
        - max landing position for each value
        - any zero value indexes
    
    Iterating through the 0 indexes, check to see if any of the previous
    values contain larger lands than the zero index iteself.
 """

nums = [2, 3, 1, 1, 4]  # True

lands = {}
zeros = []
for i, val in enumerate(nums):
    lands[i] = {}
    lands[i] = i + val
    if val == 0 and i != len(nums) - 1:
        zeros.append(i)

can_make_through_all = True
for zero_index in zeros:
    can_pass = False
    my_list = list(reversed(nums[:zero_index]))
    for i, sub_list in enumerate(reversed(nums[:zero_index])):
        actual_index = (zero_index - 1) - i
        if lands[actual_index] > zero_index:
            can_pass = True
            break
    if not can_pass:
        can_make_through_all = False
        break

print(can_make_through_all)
