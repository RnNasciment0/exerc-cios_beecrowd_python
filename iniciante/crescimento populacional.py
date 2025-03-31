import math
casosDeTestes = int(input())
for i in range(casosDeTestes):
    dados = list(map(str, input().split()))
    pA, pB, g1, g2 = int(dados[0]), int(dados[1]), float(dados[2])/100, float(dados[3])/100
    populacaoA = pA
    populacaoB = pB
    anos = 0
    while populacaoA <= populacaoB and anos <= 100:
        populacaoA += math.trunc(populacaoA*g1)
        populacaoB += math.trunc(populacaoB*g2)
        anos += 1

    if anos <= 100:
        print("%d anos." % anos)
    else:
        print("Mais de 1 seculo.")
