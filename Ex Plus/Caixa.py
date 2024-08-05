def caixa():
    c3 = int(input("1: "))
    c2 = int(input("2: "))
    c1 = int(input("3: "))

    if (c2 + c3) < c1:
        print("1")
    elif c2 < c1 or c3 < c1:
        print("2")
    else:
        print("3")

caixa()