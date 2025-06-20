def encaixaOuNao(num1, num2):
    while num2 > 0:
        if num1 % 10 != num2 % 10:
            print("nao encaixa")
            return
        num1 //= 10
        num2 //= 10
    print("encaixa")


numCasos = int(input())
for i in range(numCasos):
    num1, num2 = map(int, input().split())
    encaixaOuNao(num1, num2)
