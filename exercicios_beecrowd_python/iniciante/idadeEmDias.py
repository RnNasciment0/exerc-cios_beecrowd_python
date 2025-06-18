# Leitura do valor inteiro (idade em dias)
dias = int(input())

# Cálculo de anos, meses e dias
anos = dias // 365
dias %= 365
meses = dias // 30
dias %= 30

# Impressão do resultado formatado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
