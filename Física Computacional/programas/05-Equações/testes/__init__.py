from typing import Callable
import numpy as np


# Função que faz e mostra o resultado de uma decomposição LU
def testelu(metodo: Callable, n: int) -> None:
    """
        Testa o método de decomposição LU de matrizes `metodo(Ao)` mostrando os resultados
    """

    # Gerar uma matriz aleatória
    A = np.random.randint(0, 10, (n, n))

    # Meu método
    L, U = metodo(A)

    print("\nMatriz aleatória")
    print(A)

    print("\nMatriz L @ U")
    print(L @ U)

    print("\nMatriz L")
    print(L)

    print("\nMatriz U")
    print(U)

    return



# Função que compara o resultado de um método numérico de resolução de sistemas de equações lineares com os valores determinados pelo numpy
def testelinear(metodo: Callable, n: int) -> None:
    """
        Testa o método de resolução de sistemas de `n` equações lineares `método(Ao, bbo)` contra os valores encontrados pelo numpy para vários sistemas!
    """

    # Um sistema de `n` equações lineares aleatórias.

    # Gerar o sistema
    Ao = np.random.rand(n, n)
    bbo = np.random.rand(n)

    # Meu método
    xx = metodo(Ao, bbo)

    # Numpy
    nn = np.linalg.solve(Ao, bbo)

    # Comparar
    dif = np.max(abs(xx - nn))

    print(f"Para um sistema aleatório este método difere do resultado do numpy no máximo {dif:.3e}.\n")


    # Cinco sistemas de `n` equações lineares aleatórias.

    # Gerar o sistema
    Ao = np.random.rand(n, n)
    bbo = np.random.rand(n, 5)

    # Meu método
    xx = metodo(Ao, bbo)

    # Numpy
    nn = np.linalg.solve(Ao, bbo)

    # Comparar
    dif = np.max(abs(xx - nn))
    print(f"Para cinco sistemas aleatórios este método difere do resultado do numpy no máximo {dif:.3e}.\n")

    return


# Inverter matrizes
def testeinv(metodo: Callable, n: int) -> None:
    """
        Testa o método de inversão de matrizes `metodo(Ao)` contra os valores encontrados pelo numpy para várias matrizes!
    """

    # Gerar uma matriz aleatória

    # Gerar o sistema
    Ao = np.random.rand(n, n)

    # Meu método
    xx = metodo(Ao)

    # Numpy
    nn = np.linalg.inv(Ao)

    # Comparar
    dif = np.max(abs(xx - nn))
    print(f"Para uma matriz aleatória este método difere do resultado do numpy no máximo {dif:.3e}.\n")

    return