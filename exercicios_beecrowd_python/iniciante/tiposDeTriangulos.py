# Leitura dos valores de entrada
A, B, C = map(float, input().split())

# Ordena os lados em ordem decrescente
A, B, C = sorted([A, B, C], reverse=True)

# Verifica se forma um triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verifica o tipo de triângulo
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
