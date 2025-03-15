# Leitura dos valores de entrada
inicio, fim = map(int, input().split())

# Cálculo da duração do jogo
if inicio < fim:
    duracao = fim - inicio
else:
    duracao = (24 - inicio) + fim

# Saída do resultado
print(f"O JOGO DUROU {duracao} HORA(S)")
