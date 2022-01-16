def soma_colunas_par(matriz: list):
    colunas = [[] for _ in matriz[0]]
    for linha in matriz:
        for index, item in enumerate(linha):
            colunas[index] += [item]
    for c in colunas:
        if sum(c) % 2 != 0:
            return False
    return True


print(soma_colunas_par([[1, 2], [3, 4]]))
print(soma_colunas_par([[1, 1], [3, 4]]))
