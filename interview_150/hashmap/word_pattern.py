pattern = "abc"
s = "dog cat dog"
s_list = s.split()

# 1. Ensure strings are same length
n = len(pattern)
if len(s_list) != n:
    print(False)
    raise Exception("Done 1.")

p_to_s_mapping = {}
s_to_p_mapping = {}

for i in range(n):
    mapped_s = p_to_s_mapping.get(pattern[i])

    if mapped_s is None:
        # Add mapping for the first time
        mapped_p = s_to_p_mapping.get(s_list[i])
        if mapped_p is not None and mapped_p != pattern[i]:
            print(False)
            raise Exception("Done 3.")
        p_to_s_mapping[pattern[i]] = s_list[i]
        s_to_p_mapping[s_list[i]] = pattern[i]
    else:
        # It exists, and the current s should be the mapped s (False if not)
        if s_list[i] != mapped_s:
            print(False)
            raise Exception("Done 4.")
print(True)
