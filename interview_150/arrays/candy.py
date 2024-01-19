from collections import defaultdict


ratings = [1, 3, 4, 5, 2]


add_amts = defaultdict(int)
add_amt = 0
n = len(ratings)
i = 0

if n < 2:
    print(n)
    raise Exception("done")


def world(i):
    j = i + 1
    total_added = 0
    count = 1
    if j + 1 < n:
        while ratings[j] > ratings[j + 1]:
            if j + 1 == n - 1:
                j += 1
                break
            j += 1

        count += j - (i + 1)

        sub_add_amt = count
        for k in range(count):
            add_amts[i + k] += sub_add_amt
            total_added += sub_add_amt
            sub_add_amt -= 1
        return total_added, count
    total_added += 1
    return total_added, count


while i < n:
    if i == 0:
        # first iteration: no prev
        if ratings[i] > ratings[i + 1]:
            total_added, count = world(i=i)
            add_amt += total_added
            i += count
            continue
    elif i == (n - 1):
        # last iteration: no next
        if ratings[i] > ratings[i - 1]:
            amt = add_amts[i - 1] + 1
            add_amts[i] = amt
            add_amt += amt
    else:
        # middle iteration
        if ratings[i] > ratings[i - 1]:
            amt = add_amts[i - 1] + 1
            if ratings[i] > ratings[i + 1]:
                total_added, count = world(i=i)
                if amt >= count:
                    add_amt += amt + total_added - count
                else:
                    add_amt += total_added
                i += count
                continue
            else:
                add_amts[i] = amt
                add_amt += amt
        elif ratings[i] > ratings[i + 1]:
            total_added, count = world(i=i)
            add_amt += total_added
            i += count
            continue
    i += 1


print(n + add_amt)
