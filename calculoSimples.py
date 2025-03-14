cod1, num1, preco1 = map(float, input().split())
cod2, num2, preco2 = map(float, input().split())
total = preco1 * num1 + num2 * preco2
print("VALOR A PAGAR: R$ %.2f" % total)
