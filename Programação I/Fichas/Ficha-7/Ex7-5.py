def maximo2(xs):
    xs = set(xs)
    xs.discard(max(xs))
    return max(xs)


assert maximo2([3, -2, 1, 0, -2, 1]) == 1
assert maximo2([1, 3, 2, 3, 0]) == 2