# Leitura dos valores de entrada
A, B = map(int, input().split())

# Verifica se A é múltiplo de B ou B é múltiplo de A
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
