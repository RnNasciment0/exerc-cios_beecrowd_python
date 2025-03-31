def inverter(str):
    return str[::-1]


gritos = numero = 0
while gritos != 3:
    acao = input()
    if acao == "caw caw":
        print(numero)
        gritos += 1
        numero = 0
    else:
        acaoInvertida = inverter(acao)
        for i in range(len(acaoInvertida)):
            if acaoInvertida[i] == "*":
                numero = numero + 2**i
