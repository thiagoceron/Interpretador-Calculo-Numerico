import math

def f(x):
    """
    Função que calcula x^2 - 2.
    
    Args:
        x (float): O valor de x.
    
    Returns:
        float: O resultado da função f.
    """
    return math.pow(x, 2) - 2

def f_derivada(x):
    """
    Função que calcula a derivada de f(x).
    
    Args:
        x (float): O valor de x.
    
    Returns:
        float: O resultado da derivada de f.
    """
    return 2 * x

def main():
    x0 = float(input("Digite a aproximação inicial x0: "))
    precisao = float(input("Digite a precisão (delta): "))
    iteracao_max = int(input("Digite o número máximo de iterações: "))

    fx = f(x0)
    f_linha = f_derivada(x0)

    if abs(fx) > precisao:
        iteracao = 0
        while abs(fx) > precisao and iteracao < iteracao_max:
            iteracao += 1
            x0 = x0 - (fx / f_linha)  # Calcula a próxima aproximação
            fx = f(x0)                # Atualiza f(x)
            f_linha = f_derivada(x0)   # Atualiza f'(x)
        raiz = x0
    else:
        raiz = x0

    print("Raiz aproximada:", raiz)
    print("Número de iterações:", iteracao)

if __name__ == "__main__":
    main()