prices = [7, 1, 5, 3, 6, 4]

# prices = [1, 2, 3, 4, 5]

# prices = [7, 6, 4, 3, 1]

# prices = [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]


total_profit = 0
local_max_profit = 0
local_min = prices[0]
for i, price in enumerate(prices):
    # track previous min
    if price < local_min:
        local_min = price
    # calculate profit against previous min
    local_profit = price - local_min
    if local_profit > local_max_profit:
        local_max_profit = local_profit
        if i < len(prices) - 1:
            if prices[i + 1] <= prices[i]:
                total_profit += local_profit
                local_max_profit = 0
                local_min = prices[i]
        else:
            total_profit += local_profit


print(total_profit)
