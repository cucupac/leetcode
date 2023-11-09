prices = [7, 1, 5, 3, 6, 4]

global_max_profit = 0
local_min = prices[0]
for i, price in enumerate(prices):
    # track previous min
    if price < local_min:
        local_min = price
    # calculate profit against previous min
    local_max_profit = price - local_min
    if local_max_profit > global_max_profit:
        global_max_profit = local_max_profit

print(global_max_profit)


# # This works, but time limit exceeded.
# global_max_profit = 0
# for i, i_price in enumerate(prices):
#     if i > 0:
#         local_max_profit = i_price - min(prices[:i])
#         if local_max_profit > global_max_profit:
#             global_max_profit = local_max_profit
# print(global_max_profit)


# # This works, but time limit exceeded.
# max_profit = 0
# for i, i_price in enumerate(prices):
#     for j_price in prices[i + 1 :]:
#         profit = j_price - i_price
#         if profit > max_profit:
#             max_profit = profit

# print(max_profit)
