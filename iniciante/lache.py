cod, qtd = map(int, input().split())
total = 0
if cod == 1:
    total = 4 * qtd
elif cod == 2:
    total = 4.5 * qtd
elif cod == 3:
    total = 5 * qtd
elif cod == 4:
    total = 2 * qtd
else:
    total = 1.5 * qtd
print("TOTAL: R$ %.2f" % total)
