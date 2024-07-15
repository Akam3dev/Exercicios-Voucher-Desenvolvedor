'''numero = int(input("Digite um numero: "))

for i in range(11):
    print(i * numero)
'''
'''
cidades = []
while len(cidades) < 10:
    nome = input("Digite o nome da cidade: ")
    cidades.append(nome)
cidades.reverse()
print(cidades)
'''
'''
nomes = []
while len(nomes) < 10:
    nome = input("Digite um nome: ")
    nomes.append(nome)
print(nomes)
'''
'''
terminar = False
notas = []
while terminar == False:
    nota = int(input("Digite a nota ou -1 para terminar: "))
    if nota == -1:
        terminar = True
        media = sum(notas) / len(notas)
    notas.append(nota)
print(media)
'''
'''
palavra = ["f", "e", "l", "i", "c", "i", "d", "a", "d", "e"]
contador = 0
while contador < len(palavra):
    print(f"Posição {contador} da lista: {palavra[contador]}")
    contador = contador + 1
'''
'''
x = 10
for i in range(x):
    print("*" * i)
'''
'''
numeros = int(input("Digite um valor: "))
if numeros % 2 != 0:
    for i in range(0, 11):
        if i % 2 != 0:
            print(i)
else:
    for i in range(0, 11):
        if i % 2 == 0:
            print(i)
'''
vet1 = []
vet2 = []
i = 0
while i < 5:
    valor = int(input(f"Entre com um numero na posição {i}: "))
    vet1.append(valor)
    vet2.append(vet1[i] * 5)
    i = i + 1

print(f"Vetor1 = {vet1}")
print(f"Vetor2 = {vet2}")