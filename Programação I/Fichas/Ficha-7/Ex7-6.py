def perfeito(n):
    soma_divs = 0
    for item in range(1, n):
        if n % item == 0:
            soma_divs += item
    return soma_divs == n


assert perfeito(6)
assert not perfeito(10)
