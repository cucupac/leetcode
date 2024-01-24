# height = [4, 2, 3]
# height = [5, 4, 1, 2]
# height = [0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2]
# height = [4, 2, 0, 3, 2, 5]
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
c_indexes = []
traps = dict()
max_c_h = 0
max_c_i = 0

for i in range(len(height)):
    h = height[i]
    if h > 0:
        if c_indexes:
            trap_counted = False

            if h >= max_c_h:
                # trap formed with height, max_c_h
                trap_solid = sum(height[max_c_i + 1 : i])
                trap_water = (i - max_c_i - 1) * max_c_h - trap_solid
                traps[max_c_i] = trap_water
                # REMOVE ANY TRAPS BETWEEN C_I and I
                for k in range(max_c_i + 1, i):
                    traps[k] = 0
                trap_counted = True
            else:
                for j in range(len(c_indexes) - 1, -1, -1):
                    c_i = c_indexes[j]
                    c_height = height[c_i]
                    if c_height >= h:
                        # trap formed with height, h
                        trap_solid = sum(height[c_i + 1 : i])
                        trap_water = (i - c_i - 1) * h - trap_solid
                        traps[c_i] = trap_water
                        # REMOVE ANY TRAPS BETWEEN C_I and I
                        for k in range(c_i + 1, i):
                            traps[k] = 0
                        trap_counted = True
                        break

            if trap_counted:
                # Prune list
                c_indexes = [c_i for c_i in c_indexes if height[c_i] > h]
                trap_counted = False

        if h > max_c_h:
            max_c_h = h
            max_c_i = i
        c_indexes.append(i)

print(um(traps.values()))
