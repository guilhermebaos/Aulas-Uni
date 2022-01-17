def real_roots(a, b, c):
    vertice = -b / (2 * a)
    binomial = b**2 - 4 * a * c
    if binomial < 0:
        return []
    elif binomial == 0:
        return [vertice]
    else:
        return [vertice + binomial**0.5, vertice - binomial**0.5]


print(real_roots(1, -2, 1))
