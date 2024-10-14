import math

N = 100

def fi(x):
    """
    Função que calcula cos(x) - exp(-x^2) + x.
    
    Args:
        x (float): O valor de x.
    
    Returns:
        float: O resultado da função fi.
    """
    return math.cos(x) - math.exp(-math.pow(x, 2)) + x

def funcao(x):
    """
    Função que calcula exp(-x^2) - cos(x).
    
    Args:
        x (float): O valor de x.
    
    Returns:
        float: O resultado da função.
    """
    return math.exp(-math.pow(x, 2)) - math.cos(x)

def imprimir(k, raiz):
    """
    Função para imprimir o número de interações e a raiz encontrada.
    
    Args:
        k (int): O número de interações.
        raiz (float): A raiz encontrada.
    
    Returns:
        None
    """
    print("Número de interações:", k)
    print("Raiz:", raiz)

def MIL(x0, precisao):
    """
    Método Iterativo de Laplace para encontrar a raiz.
    
    Args:
        x0 (float): Valor inicial.
        precisao (float): A precisão desejada.
    
    Returns:
        None
    """
    raiz = 0
    x = 0
    k = 1

    if abs(fi(x0)) < precisao:
        raiz = x0
        imprimir(k, raiz)
    else:
        while abs(funcao(x0)) > precisao and k < N:
            x = fi(x0)
            k += 1
            x0 = x
        imprimir(k, x0)

def main():
    x0 = 1.5
    precisao = 0.01
    MIL(x0, precisao)

if __name__ == "__main__":
    main()