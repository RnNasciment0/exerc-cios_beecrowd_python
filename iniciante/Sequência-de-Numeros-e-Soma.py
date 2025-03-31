v = input().split()
m = int(v[0])
n = int(v[1])
while m > 0 and n > 0:
    if m < n:
        soma = 0
        for c in range(m, n + 1):
            soma += c
            print(c, end=' ')
        print(f'Sum={soma}')

    else:
        soma = 0
        for c in range(n, m + 1):
            soma += c
            print(c, end=' ')
        print(f'Sum={soma}')

    v = input().split()
    m = int(v[0])
    n = int(v[1])
