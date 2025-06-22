def pegarNumero(fatorial):
    num = ''
    i = 0
    while fatorial[i] != '!':
        num += fatorial[i]
        i += 1
    return int(num)

def quantidadeDeExclamacoes(fatorial):
    qtdExclamacao = 0
    for i in range(1, len(fatorial)):
        if fatorial[i] == '!':
            qtdExclamacao += 1
    return qtdExclamacao


def kFatorial(num, qtdExclamacao):
    k = 1
    resultado = num
    while num - (qtdExclamacao * k) >= 1:
        resultado *= num - (qtdExclamacao * k)
        k += 1
    print(resultado)


numCasos = int(input())
for i in range(numCasos):
    fatorial = input()
    num = pegarNumero(fatorial)
    qtdExclamacao = quantidadeDeExclamacoes(fatorial)
    kFatorial(num, qtdExclamacao)
    