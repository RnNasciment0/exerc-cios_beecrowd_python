def acimaDaMedia(notas, media, qtdAlunos):
    qtdAcimaDaMedia = 0
    for nota in notas:
        if nota > media:
            qtdAcimaDaMedia += 1
    porcentagem = (qtdAcimaDaMedia / qtdAlunos) * 100
    print(f"{porcentagem:.3f}%")


numCasos = int(input())
for i in range(numCasos):
    qtdAlunoENotas = list(map(int, input().split()))
    media = sum(qtdAlunoENotas[1:]) / qtdAlunoENotas[0]
    acimaDaMedia(qtdAlunoENotas[1:], media, qtdAlunoENotas[0])
