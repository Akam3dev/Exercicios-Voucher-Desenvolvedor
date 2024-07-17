def gisele():
    idades = []
    for i in range(3):
        idades.append(int(input(": ")))

    idades.remove(max(idades))
    idades.remove(min(idades))

    print(idades[0])
gisele()