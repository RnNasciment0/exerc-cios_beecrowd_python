A = "A"
B = "B"
C = "C"
copos = [0, 0, 0]
lista = []
vezes = int(input())
posicao = input()
if posicao == A:
    copos[0] = 1
elif posicao == B:
    copos[1] = 1
else:
    copos[2] = 1
for c in range(vezes):
    a = int(input())
    lista.append(a)
for num in lista:
    if num == 1:
        temp = copos[0]
        copos[0] = copos[1]
        copos[1] = temp
    elif num == 2:
        temp = copos[1]
        copos[1] = copos[2]
        copos[2] = temp
    else:
        temp = copos[2]
        copos[2] = copos[0]
        copos[0] = temp

if copos[0] == 1:
    print("A")
elif copos[1] == 1:
    print("B")
else:
    print("C")
