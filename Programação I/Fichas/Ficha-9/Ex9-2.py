def flatten(lista):
    total = []
    for item in lista:
        if type(item) == list or type(item) == tuple:
            total += flatten(item)
        else:
            total += [item]
    return total


def dist(xs):
    return list(set(xs))
