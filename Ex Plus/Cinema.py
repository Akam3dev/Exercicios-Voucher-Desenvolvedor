def Cinema():
    id1 = int(input(": "))
    id2 = int(input(": "))

    valor = 0

    if id1 >= 60:
        valor += 20
    elif id1 >= 18 and id1 <= 59:
        valor += 30
    else:
        valor += 15

    if id2 >= 60:
        valor += 20
    elif id2 >= 18 and id2 <= 59:
        valor += 30
    else:
        valor += 15

    print(valor)
Cinema()