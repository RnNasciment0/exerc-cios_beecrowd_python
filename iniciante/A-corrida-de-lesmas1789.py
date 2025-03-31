def maisRapida(list):
    maisVeloz = list[0]
    nivelDaMaisVeloz = 0
    for i in range(1, len(list)):
        if list[i] > maisVeloz:
            maisVeloz = list[i]
    if maisVeloz < 10:
        nivelDaMaisVeloz += 1
    elif 10 <= maisVeloz < 20:
        nivelDaMaisVeloz += 2
    else:
        nivelDaMaisVeloz += 3
    return nivelDaMaisVeloz


while True:
    try:
        numeroDeLesmas = int(input())
        lesmas = list(map(int, input().split()))
        nivelDaMaisRapida = maisRapida(lesmas)
        print(nivelDaMaisRapida)
    except EOFError:
        break

