matriz = []
lin = 8
col = 8
cont = 0

for i in range(lin):
    linha = []
    for j in range(col):
        cont += 1
        linha.append(cont)
    matriz.append(linha)

for i in matriz:
    print(i)

lin = int(input("Digite a linha: "))
col = int(input("Digite a coluna: "))

matriz[lin][col] = "X"

print("Nova matriz:")
for i in matriz:
    print(i)