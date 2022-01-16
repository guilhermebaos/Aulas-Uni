def nulas(matriz: list):
    dim = len(matriz)
    if dim == 0:
        return [0, 0]
    linhas_nulas = sum(1 for linha in matriz if linha.count(0) == dim)

    colunas = [[] for _ in range(dim)]
    for linha in matriz:
        for index, item in enumerate(linha):
            colunas[index] += [item]
    colunas_nulas = sum(1 for coluna in colunas if coluna.count(0) == dim)

    return [linhas_nulas, colunas_nulas]


assert nulas([[1]]) == [0, 0]
assert nulas([[1, 0, 3], [0, 0, 0], [5, 0, 6]]) == [1, 1]
assert nulas([[1, 0, 0], [0, 0, 0], [5, 0, 0]]) == [1, 2]
