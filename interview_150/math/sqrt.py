from math import floor, ceil


def sqrt(x):
    factor = floor(x / 2)

    while True:
        quo = x / factor

        if factor == quo:
            return factor
        elif factor > quo:
            if (factor - quo) <= 0.01:
                if ceil(quo) == floor(factor):
                    # test quotient
                    sqrt = ceil(quo)
                    if sqrt * sqrt == x:
                        return sqrt
                return floor(quo)
            elif (factor - quo) > 0.01:
                sub_amt = (factor - quo) * 0.5
                factor = factor - sub_amt
        else:
            add_amt = (quo - factor) * 0.5
            factor = factor + add_amt


answer = sqrt(2147395599)
print(answer)
