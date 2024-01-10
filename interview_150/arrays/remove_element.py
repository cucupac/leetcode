nums = [3, 2, 2, 3]
val = 2

accepted_vals = []
for num in nums:
    if num != val:
        accepted_vals.append(num)

for accepted_val in accepted_vals:
    nums.insert(0, accepted_val)

print("k =", len(accepted_vals))
print("Accepted vals:", accepted_vals)
