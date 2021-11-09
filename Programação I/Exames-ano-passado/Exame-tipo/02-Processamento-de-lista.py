def satisfies(cond: list, l: list):
    for pair in cond:
        if l.count(pair[0]) != pair[1]:
            return False
    return True


print(satisfies([(3, 4), (4, 2), (5, 1)], [3, 4, 3, 5, 3, 4, 3]))
print(satisfies([(3, 4), (4, 2), (5, 1)], [3, 9, 55, 4, 3, 200, 5, 3, 4, 3]))
print(satisfies([(3, 4), (4, 2), (5, 1)], [3, 4, 3, 5, 3, 4, 3, 5]))
