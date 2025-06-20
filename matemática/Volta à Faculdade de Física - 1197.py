while True:
    try:
        velocidade, tempo = map(int, input().split())
        distancia = velocidade * tempo * 2
        print(f"{distancia}")
    except EOFError:
        break
