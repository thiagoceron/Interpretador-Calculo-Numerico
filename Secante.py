import math

def f(x):
    """
    Função que calcula o valor de x^3 - 0.5.
    
    Args:
        x (float): O valor de x.
    
    Returns:
        float: O resultado da função.
    """
    return math.pow(x, 3) - 0.5

def secante(x0, x1, precisao, max_iter):
    """
    Função que calcula a raiz de uma função usando o método da secante.
    
    Args:
        x0 (float): O primeiro ponto inicial.
        x1 (float): O segundo ponto inicial.
        precisao (float): A precisão desejada.
        max_iter (int): O número máximo de iterações.
    
    Returns:
        tuple: Uma tupla contendo a raiz encontrada e o número de iterações.
    """
    k = 1
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

    if abs(f(x0)) < precisao:
        return x0, k

    if abs(f(x1)) < precisao or abs(x1 - x0) < precisao:
        return x1, k

    while k <= max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        if abs(f(x2)) < precisao or abs(x2 - x1) < precisao or k > max_iter:
            return x2, k

        x0 = x1
        x1 = x2
        k += 1

    print("Número máximo de iterações atingido. Última aproximação:", x2)
    return x2, k

def main():
    x0 = float(input("Digite x0: "))
    x1 = float(input("Digite x1: "))
    precisao = float(input("Digite a precisão (precisao): "))
    max_iter = int(input("Digite o número máximo de iterações: "))

    raiz, k = secante(x0, x1, precisao, max_iter)
    print("Raiz encontrada:", raiz)
    print("Número de iterações:", k)

if __name__ == "__main__":
    main()