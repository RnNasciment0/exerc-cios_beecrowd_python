# Leitura do valor inteiro
N = int(input())

# Exibir o valor lido
print(N)

# Lista de notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Cálculo da quantidade mínima de cada nota
for nota in notas:
    quantidade = N // nota  # Número de notas desse valor
    print(f"{quantidade} nota(s) de R$ {nota},00")
    N %= nota  # Atualiza o valor restante
