matriz = []
lin = 3
col = 3
c = 0

for i in range(lin):
    linha = []
    for j in range(col):
        c += 1
        linha.append(c)
    matriz.append(linha)

for i in matriz:
    print(i)