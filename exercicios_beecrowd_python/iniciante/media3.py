nota1, nota2, nota3, nota4 = map(float, input().split())
media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4) / 10
if media >= 6:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif media >= 5:
    exame = float(input())
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    print("Nota do exame: %.1f" % exame)
    if exame >= 6:
        print("Aluno aprovado.")
        print("Media: %.1f" % ((exame + media) / 2))
    else:
        print("Aluno reprovado.")
        print("Media: %.1f" % ((exame + media) / 2))
