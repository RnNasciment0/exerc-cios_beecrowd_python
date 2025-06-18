# Leitura dos três valores inteiros
a, b, c = map(int, input().split())

# Cálculo do maior entre a e b
maior_ab = (a + b + abs(a - b)) // 2

# Cálculo do maior entre o maior_ab e c
maior = (maior_ab + c + abs(maior_ab - c)) // 2

# Impressão do resultado
print(f"{maior} eh o maior")
