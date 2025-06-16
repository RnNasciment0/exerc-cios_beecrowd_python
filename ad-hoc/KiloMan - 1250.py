numCasos = int(input())
for i in range(numCasos):
    numDeVezesAtingido = 0
    numTiros = int(input())
    alturaDosTiros = list(map(int, input().split()))
    sequenciaDePulos = str(input())
    for i in range(len(sequenciaDePulos)):
        if sequenciaDePulos[i] == 'J':
            if alturaDosTiros[i] > 2:
                numDeVezesAtingido += 1
        else:
            if alturaDosTiros[i] <= 2:
                numDeVezesAtingido += 1
    print(numDeVezesAtingido)
