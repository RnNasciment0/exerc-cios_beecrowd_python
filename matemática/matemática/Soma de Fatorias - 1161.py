def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def somaFatorial(a, b):
    soma = a + b
    return soma


while True:
    try:
        m, n = map(int, input().split())
        x, y = factorial(m), factorial(n)
        print(somaFatorial(x, y))
    except EOFError:
        break


