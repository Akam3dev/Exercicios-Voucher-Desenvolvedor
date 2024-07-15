# 30. Elabore um programa que faça leitura de vários números inteiros, até que se digite um número
# negativo. O programa tem que retornar o maior e o menor número lido.
'''
numeros = []
terminar = False
while terminar == False:
    numero = int(input("Digite um numero: "))
    if numero >= 0:
        numeros.append(numero)
    else:
        terminar = True
print(f"Maior: {max(numeros)}, Menor: {min(numeros)}")
'''
# 31. Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020
# recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do 
# ano anterior. Faça um programa que determine o salário atual do funcionário.
'''
salario = 4000
aumento = salario * 0.015 
salario += aumento

for i in range(4):
    aumento *= 2
    salario += aumento
print(salario)
'''
# 32. Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório 
# desses números na tela. Após exibir a soma, o programa deve mostrar também os números que 
# o usuário digitou, um por linha.
'''
num = []
cont = 0

while cont < 5:
    num.append(int(input("Digite um numero: ")))
    cont += 1
print(f"Soma: {sum(num)}")

for i in range(5):
    print(num[i])
'''
# 33. Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida 
# receba um novo valor do usuário e verifique se este valor se encontra no vetor
'''
import random

vetor = []
cont = 0

while cont < 10:
    vetor.append(random.randint(0,100))
    cont += 1

cont = 0
while True:
    num = int(input("Digite um numero entre 0 - 100: "))
    if cont >= 10:
        cont = 0
    if vetor[cont] == num:
        print("se encontra no vetor!")
        cont += 1
    else:
        cont += 1
        print("não se encontra no vetor")
'''
# 34. Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os 
# números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores
'''
pares = []
impar = []
numeros = []
i = 0

while i < 20:
    num = int(input("Digite um numero: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
        i += 1
    else:
        impar.append(num)
        i += 1
print(numeros)
print(impar)
print(pares)
'''
# 35. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.
'''
consoantes = 0
caracteres = []
vogais = ["a", "e", "i", "o","u"]
i = 0
while i < 10:
    caracter = input("Digite um caractere: ")
    if caracter not in vogais:
        caracteres.append(caracter)
        consoantes += 1
        i += 1
    else:
        caracteres.append(caracter)
        i += 1

print(f"consoantes: {consoantes}")

for i in caracteres:
    if i not in vogais:
        print(i)
'''
# 36. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# 37. Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número
# fornecido é primo ou não.
'''
num = int(input("Digite um numero: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo!")
            break
    else:
        print("É primo!")
else:
    print("Não é primo!")
'''

# 38. Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos. 

# 39. Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário.

# 40. Crie um programa que some os números ímpares em um intervalo definido pelo usuário.
# Se o valor inicial for maior que o valor final, exiba "Intervalo de valores inválido" e termine o programa.
'''
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
soma = 0

if inicio > fim:
    print("Intervalo de valores invalido")
else:
    for i in range(inicio, fim):
        if i % 2 != 0:
            soma += i
    print(f"soma dos impares neste intervalo: {soma}")
'''
# 41. Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos
# pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
# entre com um valor para resistência igual a zero. R = (R1 * R2) / (R1 + R2)
'''
while True:
    r1 = int(input("Digite a resistencia 1: "))
    r2 = int(input("Digite a resistencia 2: "))
    r = (r1 * r2) / (r1 + r2)
    print(r)
    if r1 == 0 or r2 == 0:
        break
print("fim")
'''
# 42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
# escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada
# de dados com um valor negativo ou zero.
'''
import math
val = []

while True:
    num = int(input("Digite um valor: "))
    if num <= 0:
        break
    else:
        val.append(num)
# que codigo mizeravel
for i in range(len(val)):
    print(f"Numero: {val[i]}")
    print(f"    Quadrado: {val[i] * val[i]}")
    print(f"    Cubo: {val[i] * val[i] * val[i]}")
    print(f"    Raiz quadrada: {math.sqrt(val[i])}")
'''
# 43. Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar acertar
# qual o número foi gerado, a cada tentativa o programa deverá informar se o chute e menor ou
# maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O
# programa deve informar em quantas tentativas o número foi descoberto.
'''
import random
att = 0
x = random.randint(1,100)

while True:
    guess = int(input("Digite um numero: "))
    att += 1
    if guess == x:
        break
    elif guess > x:
        print("Maior que o numero")
    else:
        print("Menor que o numero")

print(f"Numero descoberto! em {att} tentativas")
'''
# 44. Crie um programa que apresente um menu de opções para o cálculo das seguintes operações 
# entre dois números. [...]
while True:
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Sair")
    operacao = int(input("Escolha a operação: "))
    if operacao == 5:
        break
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if operacao == 1:
        print(f"resultado: {num1 + num2}")
    elif operacao == 2:
        print(f"resultado: {num1 - num2}")
    elif operacao == 3:
        print(f"resultado: {num1 * num2}")
    elif operacao == 4:
        print(f"resultado: {num1 / num2}")
    else:
        print("numero invalido")
print("Saiu")
