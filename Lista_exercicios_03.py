# 1. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
# iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após contagem.
'''
i = 10
while i > -1:
    print(i)
    i -= 1
print("FIM!")
'''
# 2. Crie um programa que determine o mostre os 5 primeiros números ímpares, considerando
# números maiores que 0.
'''
numero = 1

while numero < 10:
    if numero % 2 != 0:
        print(numero)
        numero += 2
'''
# 3. Crie um programa que determine o mostre os 10 primeiros números pares, considerando
# números maiores que 0.
'''
numeros = 2
contador = 1

while contador < 11:
    if numeros % 2 == 0:
        print(numeros)
        numeros += 2
    contador += 1
'''
# 4. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira vez deve
# usar a estrutura de repetição for e a segunda while.
'''
contador = 1
while contador < 101:
    print(contador)
    contador += 1

for i in range(1,101):
    print(i)
'''
# 5. Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em
# 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).
'''
numero = 0
while numero <= 100000:
    print(numero)
    numero += 1000
'''
# 6. Escreva um programa que peça ao usuário para digitar 10 valores e some-os.
'''
valores = []
while len(valores) < 10:
    valores.append(int(input("Digite um valor: ")))
print(f"A soma dos numeros é: {sum(valores)}")
'''
# 7. Escreva um programa que leia 10 inteiros e imprima sua média.
'''
numeros = []
while len(numeros) < 10:
    numeros.append(int(input("Digite um numero: ")))
print(f"A média é: {sum(numeros) / len(numeros)}")
'''
# 8. Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
'''
numeros = []
while len(numeros) < 10:
    valor = int(input("Digite um numero positivo: "))
    if valor > 0:
        numeros.append(valor)
print(f"A média é: {sum(numeros) / len(numeros)}")
'''
# 9. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
'''
numeros = []
contador = 0
while contador < 10:
    numeros.append(int(input("Digite um numero: ")))
    contador += 1
print(f"Maior valor = {max(numeros)}, menor valor = {min(numeros)}")
'''
# 10. Crie um programa que leia um número inteiro N e depois imprima os N primeiros números.
# naturais ímpares.
'''
numeros = int(input("digite quantos numeros: "))
i = 1
cont = 0
while cont < numeros:
    print(i)
    i += 2
    cont += 1
'''
# 11. Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50
# primeiros números pares.
'''
contador = 0
pares = []
i = 2

while contador <= 49:
    if i % 2 == 0:
        pares.append(i)
        i += 2
        contador += 1
print(f"Soma = {sum(pares)}")
'''
# 12. Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais
# de 0 até N em ordem crescente.
'''
valor = int(input("Digite o valor: "))
i = 0

while i <= valor:
    print(i)
    i += 1
'''
# 13. Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais
# de 0 até N em ordem decrescente.
'''
valor = int(input("Digite o valor: "))

while valor >= 0:
    print(valor)
    valor -= 1
'''
# 14. Crie um programa que leia um número inteiro positivo par N e imprima todos os números
# pares de 0 até N em ordem crescente.
'''
numeros = int(input("digite o numero: "))
i = 0
cont = 0
while cont < numeros and i <= numeros:
    print(i)
    i += 2
    cont += 1
'''
# 15. Crie um programa que leia um número inteiro positivo par N e imprima todos os números
# pares de 0 até N em ordem decrescente.
'''
numeros = int(input("Digite o número: "))
i = numeros if numeros % 2 == 0 else numeros - 1
cont = 0
while cont < numeros and i >= 0:
    print(i)
    i -= 2
    cont += 1
'''
# 16. Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os
# números ímpares de 1 até N em ordem crescente.
'''
numeros = int(input("digite o numero: "))
i = 1
cont = 0
while cont < numeros and i <= numeros:
    print(i)
    i += 2
    cont += 1
'''
# 17. Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros
# números naturais.
'''
n = int(input("Insira um número inteiro positivo: "))
while n < 0:
    soma = (n * (n + 1)) // 2
    print("A soma dos", n, "primeiros números naturais é:", soma)
'''
# 18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A
# quantidade de números a serem lidos deve será fornecida pelo usuário.
'''
quantia = int(input("Digite a quantidade de numeros: "))
numeros = []

while len(numeros) < quantia:
    numeros.append(int(input("Digite um numero: ")))
print(f"Maior numero: {max(numeros)}")
'''
# 19. Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um
# dos algarismos que compõem o número.
'''
numero = int(input("Digite um número entre 100 e 9999: "))
if 100 <= numero <= 9999: 
    numero_str = str(numero)
    for algarismo in numero_str:
        print(algarismo)
else:
    print("Número fora do intervalo permitido. Tente novamente.")
'''
# 20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser
# informado o número de dados lidos e número de valores pares. O processo termina quando for
# digitado o número 0.
'''
naopar = 0
par = 0
terminar = False
while terminar == False:
    numero = int(input("Digite um numero (ou 0 para terminar): "))
    if numero == 0:
        terminar = True
    else:
        if numero % 2 == 0:
            par += 1
        else:
            naopar += 1
print(f"Numeros lidos: {naopar}")
print(f"Numeros pares: {par}")
'''
# 21. Crie um programa que receba dois números. Calcule e mostre:
# a soma dos números pares desse intervalo de números, incluindo os números digitados;
# a multiplicação dos números ímpares desse intervalo, incluindo os digitados;
'''
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
pares = 0
impares = 1
for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        pares += i
    else:
        impares = impares * i
print(pares)
print(impares)
'''
# 22. Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
# como nota de aprovação.
'''
terminar = False
notas = []
while terminar == False:
    nota = int(input("Digite um numero: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        terminar = True
print(f"A média é: {sum(notas) / len(notas)}")
'''
# 23. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse
# número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
# 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
'''
numero = int(input("Digite um numero: "))
soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma += i
print(soma)
'''
# 24. Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3
# ou 5.
'''
soma = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(soma)
'''
# 25. Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando
# for informada a idade 0), e calcule a idade média desse grupo.
'''
terminar = False
idades = []
while terminar == False:
    idade = int(input("Digite a idade: "))
    if idade > 0:
        idades.append(idade)
    elif idade == 0:
        terminar = True
print(f"A média é: {sum(idades) / len(idades)}")
'''
# 26. Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3
# x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente
# (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para
# resolver o problema utilize estrutura de repetição.
'''
base = int(input("Digite a base: "))
expo = int(input("Digite o expoente: "))
resultado = 1
i = 0
while i < expo:
    resultado *= base
    i += 1
print(resultado)
'''
# 27. Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do
# Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
'''
num = int(input("Digite um numero: "))
soma = 1
for i in range(1,num+1):
    soma *= i
print(soma)
'''
# 28. Escreva um programa que calcule e escreva o valor de S.
# da nãokkkkkkk entendi nada

# 29. Crie um programa que calcule o menor número divisível por cada um dos números de 1 a 20?
# Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
#desisto

# 30. QUE?