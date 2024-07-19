matriz = []

lin = int(input("Digite a quantidade de linhas: "))
col = int(input("Digite a quantidade de colunas: "))

i = 0
while i < lin:
    linha = []
    j = 0
    while j < col:
        linha.append(69)
        j += 1
    matriz.append(linha)
    i += 1

matriz[2][0] = 96

for i in matriz:
    print(i)

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1