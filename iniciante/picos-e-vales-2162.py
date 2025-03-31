cont = 1
numero_de_pontos = int(input())
tamanho_dos_pontos = list(map(int, input().split()))
if numero_de_pontos == 1:
    cont = 1
elif numero_de_pontos == 2:
    for c in range(numero_de_pontos - 1):
        if tamanho_dos_pontos[c] == tamanho_dos_pontos[c + 1]:
            cont = 0
        else:
            cont = 1
elif numero_de_pontos >= 3:
    for c in range(numero_de_pontos - 2):
        if tamanho_dos_pontos[c - 1] == tamanho_dos_pontos[c]:
            cont = 0
        if tamanho_dos_pontos[c] < tamanho_dos_pontos[c + 1] < tamanho_dos_pontos[c + 2]:
            cont = 0
        if tamanho_dos_pontos[c] > tamanho_dos_pontos[c + 1] > tamanho_dos_pontos[c + 2]:
            cont = 0
print(cont)
