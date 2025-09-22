def soma(num):
    if num == 0:
        return 1
    else:
        return num + soma(num-1)



def mostrar(num, resultado, caso):
    if resultado > 1:
        print(f"Caso {caso}: {resultado} numeros")
        print("0", end=" ")
        for i in range(num+1):
            for j in range(0, i):
                print(i, end=" ")
        print("\n")
    else:
        print(f"Caso {caso}: {resultado} numero")
    print("0", end=" ")
    for i in range(num+1):
        for j in range(0, i):
            print(i, end=" ")
    print("\n")



while True:
    try:
        caso = 1
        num = int(input())
        resultado = soma(num)
        mostrar(num, resultado, caso)
        caso += 1




    except EOFError:
        break
