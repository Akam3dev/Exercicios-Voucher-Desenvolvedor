def piloto():
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))

    try:
        if (b - a) < (c - b):
            print("1")
        elif (b - a) > (c - b):
            print("-1")
        else:
            print("0")

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
    except ValueError:
        print("NÃO PODEKRL")
    
piloto()