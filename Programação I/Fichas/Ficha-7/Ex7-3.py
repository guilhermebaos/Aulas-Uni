def divisores(n):
    divs = []
    for item in range(1, n + 1):
        if n % item == 0:
            divs += [item]
    return divs


assert divisores(12) == [1, 2, 3, 4, 6, 12]