# WORKS, BUT IS INEFFICIENT
# citations = [3, 0, 6, 1, 5]

# sorted_citations = sorted(citations)
# n = len(sorted_citations)

# h_index = 0
# for i, num in enumerate(sorted_citations):
#     num_analogs = len(sorted_citations[i:n])
#     if num >= num_analogs:
#         h_index = num_analogs
#         break

# print(h_index)


from math import floor

citations = [1, 3, 1]

h_index = 0

# SORT CITATIONS
sorted_citations = sorted(citations)
n = len(sorted_citations)

# INITIALIZE BOUNDS FOR SEARCH
min_index = 0
max_index = n

found = False
while not found:
    mid_index = floor((min_index + max_index) / 2)

    num_analogs = n - mid_index  # potentially remove

    # FIND LEFT-MOST CASE WHERE NUM > NUMS_ANA (0 -> 1)
    if sorted_citations[mid_index] >= num_analogs:
        if mid_index > 0:
            if sorted_citations[mid_index - 1] < num_analogs + 1:
                print("1:", num_analogs)
                found = True
            else:
                # SEARCH LEFT
                max_index = mid_index
        else:
            print("2:", num_analogs)
            found = True
    else:
        # NUM < NUM OF ANALOGS
        next_num_analogs = n - (mid_index + 1)
        if mid_index < n - 1:
            if sorted_citations[mid_index + 1] >= next_num_analogs:
                print("3:", next_num_analogs)
                found = True
            else:
                # SEARCH RIGHT
                min_index = mid_index
        else:
            print("4:", next_num_analogs)
            found = True
