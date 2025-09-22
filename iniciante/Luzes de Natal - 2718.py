def contarLampadas(numBin):
    qtd = 0
    cont = 0
    binString = str(binario)
    for i in range(len(binString)):
        if binString[i] == "1":
            cont += 1
        else:
            if qtd < cont:
                qtd = cont
            cont = 0
    qtd = cont
    return qtd



numCasos = int(input())
for i in range(numCasos):
    numDecimal = int(input())
    binario = bin(numDecimal)
    qtd = contarLampadas(binario)
    print(qtd)
