import math

def funcao(x):
    """
    Função que calcula o valor de x^3 - 10.
    
    Args:
        x (float): O valor de x.
    
    Returns:
        float: O resultado da função.
    """
    return math.pow(x, 3) - 10

def bisseccao(a, b, n, k, precisao):
    """
    Função que calcula a raiz de uma função usando o método da bissecção.
    
    Args:
        a (float): O limite inferior do intervalo.
        b (float): O limite superior do intervalo.
        n (int): O número máximo de iterações.
        k (int): O número atual de iterações.
        precisao (float): A precisão desejada.
    
    Returns:
        None
    """
    while abs(b - a) > precisao and k < n:
        k += 1
        x = funcao(a)
        y = (a + b) / 2
        z = funcao(y)
        if x * z < 0:
            b = y
        else:
            a = y
    print("Número de iterações:", k)
    print("Raiz:", y)

def main():
    a = float(input("Digite o intervalo a: "))
    b = float(input("Digite o intervalo b: "))
    precisao = float(input("Digite a precisão: "))
    n = 50
    k = 0
    
    if abs(b - a) < precisao:
        print(a)
    else:
        bisseccao(a, b, n, k, precisao)

if __name__ == "__main__":
    main()