n = float(input())
n *= 100
cem = n // 10000
cinquenta = (n % 10000) // 5000
vinte = ((n % 10000) % 5000) // 2000
dez = (((n % 10000) % 5000) % 2000) // 1000
cinco = ((((n % 10000) % 5000) % 2000) % 1000) // 500
dois = ((((n % 10000) % 5000) % 2000) % 500) // 200
um = (((((n % 10000) % 5000) % 2000) % 500) % 200) // 100
mcinquenta = ((((((n % 10000) % 5000) % 2000) % 500) % 200) % 100) // 50
mvintecinco = (((((((n % 10000) % 5000) % 2000) % 500) % 200) % 100) % 50) // 25
mdez = ((((((((n % 10000) % 5000) % 2000) % 500) % 200) % 100) % 50) % 25) // 10
mcinco = (((((((((n % 10000) % 5000) % 2000) % 500) % 200) % 100) % 50) % 25) % 10) // 5
mum = ((((((((((n % 10000) % 5000) % 2000) % 500) % 200) % 100) % 50) % 25) % 10) % 5) // 1

print('NOTAS:')
print(int(cem), 'nota(s) de R$ 100.00')
print(int(cinquenta), 'nota(s) de R$ 50.00')
print(int(vinte), 'nota(s) de R$ 20.00')
print(int(dez), 'nota(s) de R$ 10.00')
print(int(cinco), 'nota(s) de R$ 5.00')
print(int(dois), 'nota(s) de R$ 2.00')
print('MOEDAS:')
print(int(um), 'moeda(s) de R$ 1.00')
print(int(mcinquenta), 'moeda(s) de R$ 0.50')
print(int(mvintecinco), 'moeda(s) de R$ 0.25')
print(int(mdez), 'moeda(s) de R$ 0.10')
print(int(mcinco), 'moeda(s) de R$ 0.05')
print(int(mum), 'moeda(s) de R$ 0.01')
