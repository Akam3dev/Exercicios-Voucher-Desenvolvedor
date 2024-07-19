matriz = []
matriz2 = []
lin = 3
col = 3

i = 0
while i < lin:
    linha2 = []
    linha = []
    j = 0
    while j < col:
        num = int(input(": "))
        num2 = num * 5
        linha.append(num)
        linha2.append(num2)
        j += 1
    matriz.append(linha)
    matriz2.append(linha2)
    i += 1

for i in matriz:
    print(i)

for k in matriz2:
    print(k)