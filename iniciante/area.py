# Definição do valor de pi
pi = 3.14159

# Leitura dos valores de entrada
A, B, C = map(float, input().split())

# Cálculo das áreas
triangulo = (A * C) / 2
circulo = pi * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B ** 2
retangulo = A * B

# Impressão dos resultados formatados com 3 casas decimais
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
