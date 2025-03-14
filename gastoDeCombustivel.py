# Leitura do valor inteiro em segundos
N = int(input())

# Cálculo de horas, minutos e segundos
horas = N // 3600
N %= 3600
minutos = N // 60
segundos = N % 60

# Impressão do resultado formatado
print(f"{horas}:{minutos}:{segundos}")
