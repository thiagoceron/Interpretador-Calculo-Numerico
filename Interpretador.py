import math

# Define a dictionary to map function names to their corresponding mathematical operations
func_map = {
    'sen': math.sin,
    'cos': math.cos,
    'tg': math.tan,
    'sec': lambda x: 1 / math.cos(x),
    'cosec': lambda x: 1 / math.sin(x),
    'tang': math.tan,
    'e': math.e,
    'raiz': lambda x: x ** 0.5,
    'log': math.log,
    'ln': math.log
}

def bisseccao(a, b, n, k, precisao, func, decimal_places):
    while abs(b - a) > precisao and k < n:
        k += 1
        x = a
        y = (a + b) / 2
        z = func(y)
        if func(x) * z < 0:
            b = y
        else:
            a = y
        print("Número de iterações:", k)
        print("Raiz:", round(y, decimal_places))

def secante(x0, x1, precisao, max_iter, func, decimal_places):
    k = 1
    x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
    if abs(func(x0)) < precisao:
        return x0, k
    if abs(func(x1)) < precisao or abs(x1 - x0) < precisao:
        return x1, k
    while k <= max_iter:
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(func(x2)) < precisao or abs(x2 - x1) < precisao or k > max_iter:
            return round(x2, decimal_places), k
        x0 = x1
        x1 = x2
        k += 1
    print("Número máximo de iterações atingido. Última aproximação:", round(x2, decimal_places))
    return x2, k

def MIL(x0, precisao, func, decimal_places):
    raiz = 0
    x = 0
    k = 1
    if abs(func(x0)) < precisao:
        raiz = x0
        print("Número de interações:", k)
        print("Raiz:", round(raiz, decimal_places))
    else:
        while abs(func(x0)) > precisao and k < 100:
            x = func(x0)
            k += 1
            x0 = x
        print("Número de interações:", k)
        print("Raiz:", round(x0, decimal_places))

def newton(x0, precisao, iteracao_max, func, derivada, decimal_places):
    fx = func(x0)
    f_linha = derivada(x0)
    if abs(fx) > precisao:
        iteracao = 0
        while abs(fx) > precisao and iteracao < iteracao_max:
            iteracao += 1
            x0 = x0 - (fx / f_linha)  # Calcula a próxima aproximação
            fx = func(x0)                # Atualiza f(x)
            f_linha = derivada(x0)   # Atualiza f'(x)
        raiz = round(x0, decimal_places)
    else:
        raiz = round(x0, decimal_places)
    print("Raiz aproximada:", raiz)
    print("Número de iterações:", iteracao)

def regula_falsi(a, b, delta1, delta2, maxIter, func, decimal_places):
    if func(a) * func(b) >= 0:
        print("A condicao f(a) * f(b) < 0 nao eh satisfeita. Saindo.")
        return -1
    x_prev = a
    for iter in range(maxIter):
        M = func(a)
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))
        print(f"Iteracao {iter + 1}: x = {round(x, decimal_places)}")
        if abs((x - x_prev) / x) < delta2:
            epsilon = round(x, decimal_places)
            print(f"Raiz aproximada encontrada: {epsilon}")
            print(f"Numero total de iteracoes: {iter + 1}")
            return 0
        x_prev = x
        if M * func(x) > 0:
            a = x
        else:
            b = x
    print("Numero maximo de iteracoes atingido sem encontrar a raiz com a precisao desejada.")

def main():
    print("Digite a função (ex: x**2 - 2):")
    func_str = input()
    func_name = func_str.split('(')[0].strip()
    if func_name in func_map:
        func = lambda x: func_map[func_name](x)
    else:
        func = eval("lambda x: " + func_str.replace("e", "math.e").replace("cos", "math.cos"))

    print("Escolha o método:")
    print("1. Bisseccao")
    print("2. Secante")
    print("3. MIL")
    print("4. Newton")
    print("5. Regula Falsi")
    escolha = int(input("Digite a opção: "))
    decimal_places = int(input("Digite o número de casas decimais: "))
    if escolha == 1:
        a = float(input("Digite o intervalo a: "))
        b = float(input("Digite o intervalo b: "))
        precisao = float(input("Digite a precisão: "))
        n = 50
        k = 0
        if abs(b - a) < precisao:
            print(a)
        else:
            bisseccao(a, b, n, k, precisao, func, decimal_places)
    elif escolha == 2:
        x0 = float(input("Digite x0: "))
        x1 = float(input("Digite x1: "))
        precisao = float(input("Digite a precisão (precisao): "))
        max_iter = int(input("Digite o número máximo de iterações: "))
        raiz, k = secante(x0, x1, precisao, max_iter, func, decimal_places)
        print("Raiz encontrada:", raiz)
        print("Número de iterações:", k)
    elif escolha == 3:
        x0 = float(input("Digite x0: "))
        precisao = float(input("Digite a precisão: "))
        MIL(x0, precisao, func, decimal_places)
    elif escolha == 4:
        x0 = float(input("Digite a aproximação inicial x0: "))
        precisao = float(input("Digite a precisão (delta): "))
        iteracao_max = int(input("Digite o número máximo de iterações: "))
        derivada_str = input("Digite a derivada da função (ex: 2*x): ")
        derivada_str = derivada_str.replace("sen", "math.sin")
        derivada_str = derivada_str.replace("cos", "math.cos")
        derivada_str = derivada_str.replace("tg", "math.tan")
        # ... add more replacements for other functions ...
        derivada = eval("lambda x: " + derivada_str)
        newton(x0, precisao, iteracao_max, func, derivada, decimal_places)
    elif escolha == 5:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        delta1 = float(input("Digite a precisao delta1: "))
        delta2 = float(input("Digite a precisao delta2: "))
        maxIter = int(input("Digite o numero maximo de iteracoes: "))
        regula_falsi(a, b, delta1, delta2, maxIter, func, decimal_places)
    else:
        print("Opção inválida. Saindo.")

if __name__ == "__main__":
    main()
