nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]

nums2 = [1, 2, 2]

m = 6
n = 3
garbage_collection = []
insertion_info = []  # list(index, value)
replace_info = []

# Disovery
for i, elem_1 in enumerate(nums1):
    if i < (m + n):
        for j, elem_2 in enumerate(nums2):
            if elem_2 is not None:
                if elem_2 < elem_1:
                    insertion_info.append((i + len(insertion_info), elem_2))
                    garbage_collection.append(j)
                elif elem_1 == 0 and i >= m:
                    replace_info.append(elem_2)
                    garbage_collection.append(j)
        # Garbage collect array 2
        for index in garbage_collection:
            nums2[index] = None
        garbage_collection = []

# Implementation
# Insert into nums1
for insert in insertion_info:
    nums1.insert(insert[0], insert[1])
    del nums1[-1]

# Replace
if replace_info:
    nums1[-len(replace_info) :] = replace_info


print(nums1)
