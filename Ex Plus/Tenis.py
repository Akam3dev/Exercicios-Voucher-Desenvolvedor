def tenis():
    lista = []
    pontos = 0

    for i in range(6):
        lista.append(input("V ou P: "))

    for i in range(len(lista)):
        if lista[i] == "V":
            pontos += 1

    if pontos >= 5 and pontos <= 6:
        print(1)
    elif pontos >= 3 and pontos <= 4:
        print(2)
    elif pontos >= 1 and pontos <= 2:
        print(3)
    else:
        print(-1)
tenis()