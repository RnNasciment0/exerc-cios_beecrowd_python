# Leitura do valor monetário com duas casas decimais
valor = float(input())

# Definição das cédulas e moedas disponíveis
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Conversão do valor para centavos para evitar problemas com ponto flutuante
valor_centavos = int(round(valor * 100))

print("NOTAS:")

# Cálculo da quantidade mínima de cada nota
for nota in notas:
    qtd_notas = valor_centavos // (nota * 100)
    print(f"{qtd_notas} nota(s) de R$ {nota:.2f}")
    valor_centavos %= nota * 100

print("MOEDAS:")

# Cálculo da quantidade mínima de cada moeda
for moeda in moedas:
    qtd_moedas = valor_centavos // int(moeda * 100)
    print(f"{qtd_moedas} moeda(s) de R$ {moeda:.2f}")
    valor_centavos %= int(moeda * 100)
