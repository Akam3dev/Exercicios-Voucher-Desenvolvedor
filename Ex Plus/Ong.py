def Ong():
    s = int(input("Digite a quantidade de salgados vendidos na semana: "))
    d = int(input("Digite a quantidade de doces vendidos na semana: "))
    b = int(input("Digite a quantidade de bolos vendidos na semana: "))

    d *= 2
    b *= 3

    soma = s + d + b

    if soma >= 150:
        print("B")
    elif soma >= 120:
        print("D")
    else:
        print("N")

Ong()