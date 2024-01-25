storage = dict()

nums = [1, 2, 3, 1]
k = 3

for i, num in enumerate(nums):
    stored_index = storage.get(num)

    if stored_index is not None:
        if i - stored_index <= k:
            print(True)
    storage[num] = i

print(False)
