def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


def qtdPilhas(numR, numV):
    tamanhoDaPilha = 0
    if numR > numV:
        tamanhoDaPilha = mdc(numR, numV)
    elif numR < numV:
        tamanhoDaPilha = mdc(numV, numR)
    else:
        tamanhoDaPilha = numR
    print(tamanhoDaPilha)


numCasos = int(input())
for i in range(numCasos):
    qtdFigurinhasRicardo, qtdFigurinhasVicente = map(int, input().split())
    qtdPilhas(qtdFigurinhasRicardo, qtdFigurinhasVicente)
