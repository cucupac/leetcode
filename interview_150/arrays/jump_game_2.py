nums = [1, 3, 0, 1, 3, 0, 0, 1, 2]

max_num = max(nums)
current_index = len(nums) - 1
moves = 0

while current_index > 0:
    # ------------ GET THE NEXT INDEX ------------
    for j in range(
        1, max_num + 1
    ):  # once it runs through all, the next_index will be the "next viable index"
        check_index = current_index - j
        if check_index >= 0:  # if less than 0, don't check
            if nums[check_index] >= j:
                # CAN MAKE IT
                next_index = check_index
        else:
            break
    # ------------ GET THE NEXT INDEX ------------
    current_index = next_index
    moves += 1

print("moves:", moves)
