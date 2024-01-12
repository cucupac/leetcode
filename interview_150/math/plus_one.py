"""
if last not 9, digits[-1] += 1

for any consecutive 9's starting from end, all 9's should go to 0's.
the first non-9 should be incremented by one.

for case where all 9s, all go to zero, append 1 to beginning

how to know the number of consecutive 9s? loop through and check individual

"""
digits = [8, 8, 7, 9, 9, 9, 9, 9, 9]

# last is not 9
if digits[-1] != 9:
    digits[-1] += 1
    raise Exception("Done")


# last is 9
first_non_nine_i = None

for i in range(len(digits) - 1, -1, -1):
    if digits[i] != 9:
        first_non_nine_i = i
        break

if first_non_nine_i is None:
    prepended_one = [1]
    digits[0 : len(digits)] = [0] * len(digits)
    digits = prepended_one + digits
    print(digits)
    raise Exception("Done")

digits[first_non_nine_i] += 1
digits[first_non_nine_i + 1 : len(digits)] = [0] * (len(digits) - 1 - first_non_nine_i)
print(digits)
raise Exception("Done")
