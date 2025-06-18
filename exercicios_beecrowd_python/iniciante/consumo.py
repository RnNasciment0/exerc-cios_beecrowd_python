# Leitura da distância total percorrida (inteiro) e do total de combustível gasto (float)
X = int(input())
Y = float(input())

# Cálculo do consumo médio
consumo_medio = X / Y

# Impressão do resultado com 3 casas decimais
print(f"{consumo_medio:.3f} km/l")
