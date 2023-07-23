from typing import Callable
import numpy as np

def printhelp(obtido: float, esperado: float, space: bool=True) -> None:
    """
        Função auxiliar que compara o valor obtido e esperado.
    """

    print(f"Valor obtido: {obtido}.")
    print(f"Valor esperado: {esperado}.")
    print(f"Diferença relativa: {abs(obtido - esperado) / esperado * 100:.2e}%")
    if space:
        print("\n\n")


# Função que compara o resultado de um método numérico de integração com integrais determinados analiticamente
def testeintegral(metodo: Callable, n: int) -> None:
    """
        Testa o método de integração `método(start, end, func, n)` contra alguns integrais determinados analiticamente:
        - Integral de x de 0 a 1 = 1/2
        - Integral de x^2 de 0 a 1 = 1/3
        - Integral de x^4 - 2x + 1 de 0 a 2 = 4.4
        - Integral de sin(x) de 0 a pi = 2

        Usa `n` passos.
    """
    
    real = 1/2
    f = lambda x: x
    i = metodo(0, 1, f, n)
    print("Integral de x de 0 a 1")
    printhelp(i, real)
    
    real = 1/3
    f = lambda x: x**2
    i = metodo(0, 1, f, n)
    print("Integral de x^2 de 0 a 1")
    printhelp(i, real)
    
    real = 4.4
    f = lambda x: x**4 - 2 * x + 1
    i = metodo(0, 2, f, n)
    print("Integral de x^4 - 2x + 1 de 0 a 2")
    printhelp(i, real)
    
    real = 2
    f = lambda x: np.sin(x)
    i = metodo(0, np.pi, f, n)
    print("Integral de sin(x) de 0 a pi")
    printhelp(i, real, space=False)

    return

    
# Função que compara o resultado de um método numérico de integração com integrais determinados analiticamente
def testeintegral2d(metodo: Callable, n: tuple[int, int]) -> None:
    """
        Testa o método de integração `método(xlim, ylim, func, n)` contra alguns integrais determinados analiticamente.
        
        O domínio é sempre um quadrado de lado 1 no 1º quadrante do plano xOy com um vértice na origem:
        - Integral de x = 1/2
        - Integral de x^2 + y^2 = 2/3
        - Integral de xy + sin(x) + cos(2y) = 5/4 + sin(2)/2 - cos(1)

        Usa `n` passos.
    """
    
    real = 1/2
    f = lambda x, y: x
    i = metodo([0, 1], [0, 1], f, n)
    print("Integral de x num quadrado com x, y em [0, 1]")
    printhelp(i, real)
    
    real = 2/3
    f = lambda x, y: x**2 + y**2
    i = metodo([0, 1], [0, 1], f, n)
    print("Integral de x^2 + y^2 num quadrado com x, y em [0, 1]")
    printhelp(i, real)
    
    real = 5/4 + np.sin(2)/2 - np.cos(1)
    f = lambda x, y: x*y + np.sin(x) + np.cos(2*y)
    i = metodo([0, 1], [0, 1], f, n)
    print("Integral de xy + sin(x) + cos(2y) num quadrado com x, y em [0, 1]")
    printhelp(i, real)

    return