def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


def acm(num):
    resultado = 0
    i = 1
    while num >= 10:
        numAtual = num
        resultado += fatorial(i) * (num % 10)
        num //= 10
        i += 1
    resultado += fatorial(i) * num
    print(resultado)


num = int(input())
while num != 0:
    acm(num)
    num = int(input())
