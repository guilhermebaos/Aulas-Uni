def repetidos(lista):
    return len(lista) != len(set(lista))

assert repetidos(['ola', 'ole', 'abba', 'ole'])
assert not repetidos([3, 2, -5, 0, 1])
