def felizOuTriste(num1, num2, num3):
    if num1 < num2:
        if num2 < num3:
            if num3 - num2 < num2 - num1:
                print(":(")
            else:
                print(":)")
        elif num2 > num3:
            print(":(")
        else:
            print(":(")
    elif num1 > num2:
        if num2 < num3:
            print(":)")
        elif num2 > num3:
            if num1 - num2 > num2 - num3:
                print(":)")
            else:
                print(":(")
        else:
            print(":)")
    else:
        if num2 < num3:
            print(":)")
        elif num2 > num3:
            print(":(")
        else:
            print(":(")
    return None


temDia1, temDia2, temDia3 = map(int, input().split())
felizOuTriste(temDia1, temDia2, temDia3)
