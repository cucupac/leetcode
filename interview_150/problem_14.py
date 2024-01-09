gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]


"""
SOLUTION 2.

The key insight differentiating solution 1 and 2 is that:

--> If a given start index was found to fail at a circular trip,
    any index between that start index and the point of failure can be excluded.

--> This realization avoids the need to check many starting indexes in between
    a failing starting index and the point of failure, thereby lowering the time complexity.
"""

# LIST VARIABLES
n = len(gas)
possibilities = list(range(n))

# LOOP VAIRABLES
i = 0
i_start = possibilities[0]
departing = True
gas_tank = gas[i_start]

while possibilities:
    if i == i_start and not departing:
        print("WINNER:", i_start)
        break

    if departing:
        departing = False

    # fill up tank each non-start-station stop
    if i != i_start:
        gas_tank += gas[i]

    # check trip viability
    if gas_tank >= cost[i]:
        # go to next station
        gas_tank -= cost[i]
        # increment i
        i = (i + 1) % n
    else:
        # remove i_start from possibilities
        if i >= i_start:
            del possibilities[i_start : i + 1]
        else:
            del possibilities[i_start : len(possibilities)]
            del possibilities[0 : i + 1]

        # update i's
        i = (i + 1) % n
        i_start = i
        gas_tank = gas[i_start]
        departing = True
else:
    print(-1)

"""SOLUTION 1."""

# THIS PASSED 32 of 40 TEST CASES, BUT TIME LIMIT EXCEEDED.

# max_index = len(gas) - 1
# possibilites = gas.copy()


# i_start = 0
# i = 0
# departing = True
# gas_tank = gas[i_start]


# while any(possibilites):
#     if i == i_start and not departing:
#         print("WINNER:", i_start)
#         break

#     if departing:
#         # this iteration is departing -- future iterations are not
#         departing = False

#     # fill up if on the road (already filled up if at i_start)
#     if i != i_start:
#         gas_tank += gas[i]

#     # check next trip
#     if gas_tank >= cost[i]:
#         # go to next station
#         gas_tank -= cost[i]
#         # increment i
#         if i == len(gas) - 1:
#             i = 0
#         else:
#             i += 1
#     else:
#         # remove i_start from possibilities
#         possibilites[i_start] = None
#         if i_start < len(gas) - 1:
#             # try another i_start
#             i_start += 1
#             i = i_start
#             gas_tank = gas[i_start]
#             departing = True
# else:
#     print(-1)
