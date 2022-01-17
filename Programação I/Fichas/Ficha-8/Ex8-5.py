def split(a):
    evens, odds = [], []
    for item in a:
        if item % 2 == 0:
            evens += [item]
        else:
            odds += [item]
    return evens, odds


print(split([1, 2, 3, 4, 5, 6]))
