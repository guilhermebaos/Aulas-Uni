def parallel(*res):
    return (sum(r**(-1) for r in res))**(-1)


def series(*res):
    return sum(res)


print(series(5, parallel(10, series(5, 5))))
