import math

# Leitura dos três valores de ponto flutuante
A, B, C = map(float, input().split())

# Verificação das condições para calcular as raízes
if A == 0 or (B ** 2 - 4 * A * C) < 0:
    print("Impossivel calcular")
else:
    # Cálculo das raízes
    delta = B ** 2 - 4 * A * C
    raiz1 = (-B + math.sqrt(delta)) / (2 * A)
    raiz2 = (-B - math.sqrt(delta)) / (2 * A)

    # Impressão das raízes com 5 casas decimais
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")
