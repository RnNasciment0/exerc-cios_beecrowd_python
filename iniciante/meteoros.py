def main():
    testes = 1
    x1, y1, x2, y2 = map(int, input().split())
    while x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
        # Zera a quantidade de meteoritos que atingiram a fazenda.
        meteoritos = 0
        n = int(input())
        while n > 0:
            m1, m2 = map(int, input().split())  # (m1, m2) - Coordenada do meteorito
            # Caso esteja dentro dos limites da fazenda.
            if x1 <= m1 <= x2 and y2 <= m2 <= y1:
                meteoritos += 1
            n -= 1
        print("Teste", testes)
        print(meteoritos)

        testes += 1
        x1, y1, x2, y2 = map(int, input().split())


if __name__ == "__main__":
    main()
