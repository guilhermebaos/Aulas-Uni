import numpy as np
import sympy as sp
from typing import Callable


def printhelp(obtido: float, esperado: float) -> None:
    """
        Função auxiliar que compara o valor obtido e esperado.
    """

    print(f"Valor obtido: {obtido}.")
    print(f"Valor esperado: {esperado}.")
    print(f"Diferença relativa: {abs(obtido - esperado) / esperado * 100}%")
    print("\n\n")


# Função que compara o resultado de um método numérico de integração com integrais determinados analiticamente
def testeintegral(metodo: Callable, n: int) -> None:
    """
        Testa o método de integração `método(start, end, func, n)` contra alguns integrais determinados analiticamente:
        - Integral de 1 de 0 a 1 = 1
        - Integral de x de 0 a 1 = 1/2
        - Integral de x^2 de 0 a 1 = 1/3
        - Integral de sin(x) de 0 a pi = 2

        Usa `n` passos.
    """
    def f1(x: float) -> float:
        return 1


    i1 = metodo(0, 1, f1, n)
    print("Integral de 1 de 0 a 1")
    printhelp(i1, 1)

    
    def f2(x: float) -> float:
        return x

    i2 = metodo(0, 1, f2, n)
    print("Integral de x de 0 a 1")
    printhelp(i2, 1/2)

    
    def f3(x: float) -> float:
        return x**2

    i3 = metodo(0, 1, f3, n)
    print("Integral de x^2 de 0 a 1")
    printhelp(i3, 1/3)

    
    def f4(x: float) -> float:
        return np.sin(x)

    i4 = metodo(0, np.pi, f4, n)
    print("Integral de sin(x) de 0 a pi")
    printhelp(i4, 2)

    return



def testesympy(start: float, end: float, func: Callable, n: int, metodo: Callable) -> None:
    """
        Testa o método de integração `método(start, end, func, n)` contra a função de integração do sympy.
    """

    isp = sp.integrate.quad(func, start, end)
    ime = metodo(start, end, func, n)
    printhelp(ime, isp)

    return
