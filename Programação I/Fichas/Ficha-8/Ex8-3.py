def pseudo_magic(matriz: list):
    soma = sum(matriz[0])

    colunas = [[] for _ in matriz]
    for line in matriz:
        if sum(line) != soma:
            return False

        for index, item in enumerate(line):
            colunas[index] += [item]

    for c in colunas:
        if sum(c) != soma:
            return False

    return True


assert pseudo_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
assert not pseudo_magic([[2, 7, 6], [9, 5, 1], [4, 3, 18]])
