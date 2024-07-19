matriz = []

lin = 4
col = 4

i = 0
while i < lin:
    linha = []
    j = 0
    while j < col:
        print(f"Coluna {j}, linha: {i}")
        linha.append(int(input(": ")))
        j += 1
    matriz.append(linha)
    i += 1

for i in matriz:
    print(i)