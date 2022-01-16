def colunas_sem_repetidos(matriz: list):
    if len(matriz) == 0:
        return True
    colunas = [[] for _ in matriz[0]]
    for linha in matriz:
        for index, item in enumerate(linha):
            if item in colunas[index]:
                return False
            colunas[index] += [item]
    return True


assert colunas_sem_repetidos([]) == True
assert colunas_sem_repetidos([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True
assert colunas_sem_repetidos([[1, 2, 3], [2, 2, 1], [3, 1, 2]]) == False
