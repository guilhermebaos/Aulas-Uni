def flatten(lista):
    total = []
    for item in lista:
        if type(item) == list or type(item) == tuple:
            total += flatten(item)
        else:
            total += [item]
    return total


def ocorre(x, ys):
    return x in flatten(ys)


assert ocorre(1, [2, 1, 3])
assert not ocorre(0, [[2, 1], 3])
assert ocorre(1, [[2, 1], 3])
assert ocorre(1, [1, [2, [3, [4, [5, [6, [7, [8]]]]]]]])
