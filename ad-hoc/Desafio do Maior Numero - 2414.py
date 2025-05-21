lista = list(map(int, input().split()))
maior = -1
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
print(maior)
