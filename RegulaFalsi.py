import math

def f(x):
    return math.exp(-x**2) - math.cos(x)

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    delta1 = float(input("Digite a precisao delta1: "))
    delta2 = float(input("Digite a precisao delta2: "))
    maxIter = int(input("Digite o numero maximo de iteracoes: "))

    if f(a) * f(b) >= 0:
        print("A condicao f(a) * f(b) < 0 nao eh satisfeita. Saindo.")
        return -1

    x_prev = a

    for iter in range(maxIter):
        M = f(a)
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"Iteracao {iter + 1}: x = {x}")

        if abs((x - x_prev) / x) < delta2:
            epsilon = x
            print(f"Raiz aproximada encontrada: {epsilon}")
            print(f"Numero total de iteracoes: {iter + 1}")
            return 0

        x_prev = x

        if M * f(x) > 0:
            a = x
        else:
            b = x

    print("Numero maximo de iteracoes atingido sem encontrar a raiz com a precisao desejada.")

if __name__ == "__main__":
    main()