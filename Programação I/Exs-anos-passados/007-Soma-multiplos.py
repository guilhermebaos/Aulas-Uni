def soma_multiplos(n: int):
    return sum(x for x in range(n + 1) if x % 3 == 0 or x % 5 == 0)


assert soma_multiplos(10) == 33
