tab = int(input())
while tab > 0:
    preenchida = 0
    pontos = input()
    for ponto in pontos:
        if ponto != ".":
            preenchida += 1
    if preenchida == 0 and tab % 2 != 0:
        print("S")
    elif preenchida == 0 and tab % 2 == 1:
        print("N")
    elif pontos in "X.X":
        print("S")
    elif (pontos in "X...") or (pontos in "...X"):
        print("S")
    elif pontos in "..X..":
        print("N")
        
    tab = int(input())
    
