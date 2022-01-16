def permutacao(a: int, b: int):
    a, b = str(a), str(b)
    numeros = [chr(n) for n in range(49, 58)]

    freq_a = [a.count(num) for num in numeros]
    freq_b = [b.count(num) for num in numeros]

    return freq_a == freq_b


assert permutacao(7, 7)
assert permutacao(122, 212)
assert not permutacao(122, 21)
