# CTRL + K + CTRL + C > comenta o bloco de código selecionado
# CTRL + K + CTRL + U > descomenta o bloco de código
# que preguiça de fazer isso KKKK pqp 😭😢

# exercicio 1: Faça um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro
# com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número
# digitado ao cubo.
'''
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
n3 = float(input("Digite um numero real: "))

print(n1 * (n2 / 2))
print((n1 * 3) + n3)
print(n3 ** 3)
'''
# exercicio 2: "Crie um programa que receba um número inteiro e verifique se ele é maior que 10 se sim,
# imprima: é maior que 10, senão imprima: é menor que 10."
    # Numero = int(input("Digite um numero intero: "))
    # if Numero > 10 or Numero == 10:
    #     print("É maior ou igual a dez!!!")
    # else:
    #     print("É MENOR QUE DEZ")

# exercicio 3: "Crie um programa que receba dois números e mostre qual deles é o maior.""
    # numero1 = int(input("Digite o primeiro numero: "))
    # numero2 = int(input("Digite o segundo numero: "))
    # if numero1 > numero2:
    #     print(f"{numero1} é o maior numero.")
    # else:
    #     print(f"{numero2} é o maior numero.")

# exercicio 4 "Crie um programa que receba três números e mostre-os em ordem crescente."
'''
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

numero_ordenado = sorted([n1, n2, n3])
print(numero_ordenado)
'''
# exercicio 5 "Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F
# - Feminino, M – Masculino ou Sexo Inválido."
'''
sexo = input("Digite o seu SEXO. F ou M: ")
sexo = sexo.lower() # a função ".lower()" converte o texto digitado para minusculo.
if sexo == "f":
    print("você é mujer 👩")
elif sexo == "m":
    print("tu eres hombrer 🧔")
else:
    print("Sexo invalido")
'''
# exercicio 6 "Faça um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou
# V- Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso."
'''
turno = input("Digite qual turno você estuda: M (matutino) V (verspertino) ou N (noturno): ")
turno = turno.lower()

if turno == "m":
    print("Bom dia!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("ERRO")
'''
''' exercicio 7: Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor
de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser
vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, faça um
algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda'''

'''
preco_aquisicao = float(input("Digite o preço de aquisição: "))
if preco_aquisicao < 50:
    preco_venda = preco_aquisicao * 1.45
else:
    preco_venda =  preco_aquisicao * 1.30

print(f"O valor de venda é: {preco_venda}")
'''

# exercicio 8: Faça um Programa que receba 3 entradas de dados e informe qual tipo de dados está
# armazenado na variável se é do tipo: int, float ou string
''' isso aqui foi tudo chatgpt professor, me perdoa kkkkkkk
entrada1 = input("Digite o primeiro valor: ")
entrada2 = input("Digite o segundo valor: ")
entrada3 = input("Digite o terceiro valor: ")

tipo_entrada1 = "int" if entrada1.isdigit() else ("float" if entrada1.replace('.', '', 1).isdigit() else "str")
tipo_entrada2 = "int" if entrada2.isdigit() else ("float" if entrada2.replace('.', '', 1).isdigit() else "str")
tipo_entrada3 = "int" if entrada3.isdigit() else ("float" if entrada3.replace('.', '', 1).isdigit() else "str")

print("O tipo de dado armazenado na primeira variável é:", tipo_entrada1)
print("O tipo de dado armazenado na segunda variável é:", tipo_entrada2)
print("O tipo de dado armazenado na terceira variável é:", tipo_entrada3)
'''

# exercicio 9: Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
# número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

'''import math
numero = float(input("Digite um numero: "))

if numero >= 1:
    numero = math.sqrt(numero)
    print(numero)
else:
    print("NUMERO INVALIDO")'''

# exercicio 10: Leia um número real. Se o número for positivo imprima a raiz quadrada. Caso contrário imprima
# o número ao quadrado.

'''import math

numero = float(input("Digite um numero: "))
if numero >= 0:
    numero = math.sqrt(numero)
    print(numero)
else:
    numero = (numero * numero)
    print(numero)'''

# exercicio 11: Crie um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# O número digitado ao quadrado;
# A raiz quadrada do número digitado;
'''import math

numero = float(input("Digite a desgraça de um numero rapai vagabundo sem vergonha: "))

if numero >= 0:
    print("Numero digitado ao quadrado: ", numero * numero)
    print("Raiz quadrada do numero digitado: ",math.sqrt(numero))
else:
    print("o numero não é positivo.")'''

# exercicio 12: Crie um programa que receba um número inteiro e verifique se este número é par ou ímpar.
'''
numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero digitado é par.")
else:
    print("O numero digitado é impar.")
'''
# exercicio 13: Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim
# como a diferença existente entre ambos.
'''
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior que {numero2}.")
    print(f"A diferença entre eles é: {numero1 - numero2}")
elif numero2 > numero1:
    print(f"O numero {numero2} é maior que {numero1}.")
    print(f"A diferença entre eles é: {numero2 - numero1}")
else:
    print("numero invalido.")
'''

# exercicio 14: Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números
# forem iguais, imprima a mensagem: Números iguais.
'''
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior que {numero2}.")
elif numero2 > numero1:
    print(f"O numero {numero2} é maior que {numero1}.")
elif numero1 == numero2 or numero2 == numero1:
    print("Os dois numeros são iguais.")
else:
    print("ERRO")
'''

# exercicio 15: Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem
# crescente. Caso contrário, imprima não está em ordem crescente.
'''
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite mais um numero: "))

crescente = sorted([numero1,numero2,numero3])
dados = [numero1, numero2, numero3]

if dados == crescente:
    print("Esta em ordem crescente.")
else:
    print("Não esta em ordem crescente.")
'''

# exercicio 16: Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela
# a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
# onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o
# programa termina
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10: # que negocio feio.
    print("não possui um valor valido")
else:
    media = (nota1 + nota2) / 2
    print(f"A media das notas é: {media}")
'''

# exercicio 17: Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários
# acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor
# do seu salário líquido
'''
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
salario = horas_trabalhadas * 40.50

if salario > 2500:
    imposto = salario * 0.11
    salario = salario - imposto
    print(f"Salario depois do imposto: {salario}R$")
else:
    print(f"salario sem imposto: {salario}")
'''

# exercicio 18: Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de
# acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de
# um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não
# concedido, caso contrário imprima: Empréstimo concedido.
'''
salario = float(input("Digite o salario: "))
prestacao = float(input("Digite o valor da prestação do impréstimo: "))
salario = salario * 0.20

if prestacao >= salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido!")
'''

# exercicio 19: Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes formulas (onde h corresponde à altura):
'''
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo. H ou M: ")
sexo = sexo.lower()

if sexo == "h":
    peso_ideal = (72.7 * altura) - 58
    print(f"seu peso ideal é: {peso_ideal}")
elif sexo == "m":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"seu peso ideal é: {peso_ideal}")
else:
    print("altura ou sexo invalidos.")
'''

# exercicio 20: Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”
'''
numero = input("Digite um numero de 3 caracteres: ")
a = numero[0]
b = numero[1]
c = numero[2]

soma = int(a) + int(b) + int(c)
print(f"A soma dos algoritmos é: {soma}")
'''
# exercicio 21: A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0
# até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
# final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de
# Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela
# se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi
# aprovado. Faça todas as verificações necessárias.
'''
nota_laboratorio = float(input("Digite a nota de laboratorio: "))
nota_semestral = float(input("Digite a nota de avaliação semestral: "))
nota_exame = float(input("Digite a nota do exame final: "))
media = (nota_laboratorio + nota_semestral + nota_exame) / 3

print(f"A media do aluno é: {media}")
if media < 3:
    print("O aluno esta reprovado.")
elif media >= 3 and media < 6:
    print("O aluno esta de recuperação.") 
else:
    print("O aluno esta aprovado.")
'''

# exercicio 22: Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente
# a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.
'''
dia = int(input("Digite um numero correspondente a um dia da semana: "))

if dia == 1:
    print("O dia é domingo")
elif dia  == 2:
    print("O dia é segunda")
elif dia  == 3:
    print("O dia é terça")
elif dia  == 4:
    print("O dia é quarta")
elif dia  == 5:
    print("O dia é quinta")
elif dia  == 6:
    print("O dia é sexta")
elif dia  == 7:
    print("O dia é sabado")
else:
    print("numero invalido")
'''

# exercicio 23: Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este
# número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.
'''
mes = int(input("Digite o valor do mes: "))

if mes == 1:
    print("O mes é janeiro")
elif mes == 2:
    print("O mes é fevereiro")
elif mes == 3:
    print("O mes é março")
elif mes == 4:
    print("O mes é abril")
elif mes == 5:
    print("O mes é maio")
elif mes == 6:
    print("O mes é junho")
elif mes == 7:
    print("O mes é julho")
elif mes == 8:
    print("O mes é agosto")
elif mes == 9:
    print("O mes é setembro")
elif mes == 10:
    print("O mes é outubro")
elif mes == 11:
    print("O mes é novembro")
elif mes == 12:
    print("O mes é dezembro")
else:
    print("erro")
'''

# exercicio 24: Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que: area = basemaior + basemenor * altura /  2
'''
basemaior = float(input("Digite a base maior do trapézio: "))
basemenor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))
area = ((basemaior + basemenor) * altura) / 2
print(area)
'''

# exercicio 25: Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas
# (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois
# valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.
'''
operacao = input("Escolha a operação: +, -, *, /: ")
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

if operacao == "+":
    print(n1 + n2)
elif operacao == "-":
    print(n1 - n2)
elif operacao == "*":
    print(n1 * n2)
elif operacao == "/":
    print(n1 / n2)
else:
    print("Operação ou numeros invalidos.")
'''
# exercicio 26: . Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se
# forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
# Chama-se equilátero o triângulo que tem três lados iguais.
# Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
'''
A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))

if A + B > C and A + C > B and B + C > A:
    print("Os valores podem formar um triângulo.")
else:
    print("Os valores não podem formar um triangulo.")

if A == B == C:
    print("O triangulo é Equilátero")
elif A == B or A == C or B == C:
    print("O triangulo é isósceles.")
elif A != B or A != C or B != C:
    print("O triangulo é escaleno.")
else:
    pass
'''
# exercicio 27: Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
# Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero)
'''print("--- Escolha uma opção ---")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números.")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números.")    
operacao = input("Digite a opçao: ")

if operacao == "1":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    print(f"O resultado é: {num1 + num2}")
elif operacao == "2":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    if num1 > num2:
        print(f"A diferença entre os numeros é: {num1 - num2}")
    else:
        print(f"A diferença entre os numeros é: {num2 - num1}")
elif operacao == "3":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    print(f"O produto entre os dois numeros é: {num1 * num2}")
elif operacao == "4":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    if num1 or num2 == 0:
        print("O denominador não pode ser zero.")
    else:
        print(f"O resultado é: {num1 / num2}")
else:
    print("opção invalida")
'''
# exercicio 28: Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
# As condições para aposentadoria são:
# Ter pelo menos 65 anos,
# Ou ter trabalhado pelo menos 30 anos,
# Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
'''
idade = int(input("Digite sua idade: "))
tempo_trabalhado = int(input("Digite a quantidade de anos trabalhados: "))

if idade >= 65 or tempo_trabalhado >= 30:
    print("Você pode se aposentar! ")
else:
    print("Você nao pode se aposentar")
'''
# exercicio 29: Determine se um determinado ano lido é bissexto. Sendo que um ano e bissexto se for divisível
# por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996
'''
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")
'''
# exercicio 30: Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
# taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado
# não for válido, mostrar uma mensagem de erro.
'''
valor = float(input("Digite o valor do produto: "))
estado = input("Selecione o estado: MS, MG, SP, RJ: ")
estado = estado.lower()

if estado == "ms":
    imposto = valor * 0.08
    valor = valor + imposto
    print(f"O valor do produto + imposto: {valor}")
elif estado == "mg":
    imposto = valor * 0.07
    valor = valor + imposto
    print(f"O valor do produto + imposto: {valor}")
elif estado == "sp":
    imposto = valor * 0.12
    valor = valor + imposto
    print(f"O valor do produto + imposto: {valor}")
elif estado == "rj":
    imposto = valor * 0.15
    valor = valor + imposto
    print(f"O valor do produto + imposto: {valor}")
else:
    print("Estado inserido errado.")
'''
# exercicio 31: Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
# percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
'''
kilometros = int(input("Digite a distancia percorrida em quilometros: "))
consumidos = int(input("Digite a quantidade de gasolina consumida nesse percurso: "))
kmlitro = kilometros / consumidos

if kmlitro < 8:
    print("Venda o carro!")
elif kmlitro >= 8 and kmlitro <= 14:
    print("Êconomico!")
elif kmlitro > 12:
    print("Super economico")
else:
    print("erro sei la")
'''
# exercicio 32: Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes
# categorias: Categoria Idade
'''
idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("O nadador é da categoria Infantil A")
elif idade >= 8 and idade <= 10:
    print("O nadador é da categoria Infantil B")
elif idade >= 11 and idade <= 13:
    print("O nadador é da categoria Juvenil A")
elif idade >= 14 and idade <= 17:
    print("O nadador é da categoria Juvenil A")
elif idade > 18:
    print("O nadador é senior")
else:
    print("idade invalida")
'''

# exercicio 33: Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e
# a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
# cada execução somente será calculado um pedido.
'''
print("Digite o código do produto: ")
print("Hot Dog[100], Bauru[101], X-Salada[102], X-Bacon[103], X-Burguer[104]")
print("Suco De Laranja[105], Refrigerante[106]")
codigo = int(input())
print("Selecione a quantidade: ")
quantidade = int(input())

if codigo == 100:
    print(f"Valor total a ser pago: {1.20 * quantidade}R$")
elif codigo == 101:
    print(f"Valor total a ser pago: {1.30 * quantidade}R$")
elif codigo == 102:
    print(f"Valor total a ser pago: {1.50 * quantidade}R$")
elif codigo == 103:
    print(f"Valor total a ser pago: {1.20 * quantidade}R$")
elif codigo == 104:
    print(f"Valor total a ser pago: {17.00 * quantidade}R$")
elif codigo == 105:
    print(f"Valor total a ser pago: {9.50 * quantidade}R$")
elif codigo == 106:
    print(f"Valor total a ser pago: {6.00 * quantidade}R$")
else:
    print("Codigo de produto invalido.")
'''
# exercicio 34: Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e
# escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a
# segunda tabela).
'''
preco_antigo = float(input("Digite o preço antigo: "))

if preco_antigo <= 50:
    aumento1 = preco_antigo * 0.05
    preco_antigo = preco_antigo + aumento1
    print(f"Valor novo: {preco_antigo}")
elif preco_antigo > 50 and preco_antigo <= 100:
    aumento2 = preco_antigo * 0.10
    preco_antigo = preco_antigo + aumento2
    print(f"Valor novo: {preco_antigo}")
elif preco_antigo > 100:
    aumento3 = preco_antigo * 0.15
    preco_antigo = preco_antigo + aumento3
    print(f"Valor novo: {preco_antigo}")
else:
    print("erro")
'''

# exercicio 35: Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao
# vendedor. Para calcular a comissão, considere a tabela abaixo:
'''
vendas = float(input("Digite o valor da venda: "))

if vendas >= 100000:
    comissao = vendas * 0.16
    print(f"Valor da comissão: {700 + comissao}R$")
elif vendas < 100000 and vendas >= 80000:
    comissao = vendas * 0.14
    print(f"Valor da comissão: {650 + comissao}R$")
elif vendas < 80000 and vendas >= 60000:
    comissao = vendas * 0.14
    print(f"Valor da comissão: {600 + comissao}R$")
elif vendas < 60000 and vendas >= 40000:
    comissao = vendas * 0.14
    print(f"Valor da comissão: {550 + comissao}R$")
elif vendas < 40000 and vendas >= 20000:
    comissao = vendas * 0.14
    print(f"Valor da comissão: {500 + comissao}R$")
elif vendas < 20000:
    comissao = vendas * 0.14
    print(f"Valor da comissão: {400 + comissao}R$")
else:
    print("erro")
'''

# exercicio 36: Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que
# considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
# salário terão um aumento proporcionalmente maior do que os funcionários com um salário
# maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
# adicional de salário.
'''
salario_atual = float(input("Digite o valor atual do salario do funcionario: "))
anos_trabalhados = int(input("Digite a quantidade de anos trabalhados: "))

if salario_atual <= 500:
    reajuste = salario_atual * 0.25
    salario_atual = salario_atual + reajuste
    print(f"O salario novo é: {salario_atual}R$")
elif salario_atual > 500 and salario_atual <= 1000:
    reajuste = salario_atual * 0.20
    salario_atual = salario_atual + reajuste
    print(f"O salario novo é: {salario_atual}R$")

    if anos_trabalhados >= 1 and anos_trabalhados <= 3:
        print("Bonus salarial = 100R$")
    else:
        print("sem bonus")
elif salario_atual > 1000 and salario_atual <= 1500:
    reajuste = salario_atual * 0.15
    salario_atual = salario_atual + reajuste
    print(f"O salario novo é: {salario_atual}R$")

    if anos_trabalhados >= 4 and anos_trabalhados <= 6:
        print("Bonus salarial = 200R$")
    else:
        print("sem bonus")
elif salario_atual > 1500 and salario_atual <= 2000:
    reajuste = salario_atual * 0.10
    salario_atual = salario_atual + reajuste
    print(f"O salario novo é: {salario_atual}R$")

    if anos_trabalhados >= 7 and anos_trabalhados <= 10:
        print("Bonus salarial = 300R$")
    else:
        print("sem bonus")
elif salario_atual > 2000:
    print("Sem reajuste de salario.")
    print("Bonus salarial = 500R$")
else:
    print("erro")
'''
# exercicio 37: O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do
# distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
# de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
'''
custo_de_fabrica = float(input("Digite o valor de fabrica: "))

if custo_de_fabrica <= 12000:
    comissao = custo_de_fabrica * 0.05
    custo_de_fabrica = custo_de_fabrica + comissao
    print(f"O custo ao consumidor é: {custo_de_fabrica}")
elif custo_de_fabrica > 12000 and custo_de_fabrica <= 25000:
    comissao = custo_de_fabrica * 0.10
    imposto = custo_de_fabrica * 0.15
    custo_de_fabrica = custo_de_fabrica + comissao + imposto
    print(f"O custo ao consumidor é: {custo_de_fabrica}")
else:
    comissao = custo_de_fabrica * 0.15
    imposto = custo_de_fabrica * 0.20
    custo_de_fabrica = custo_de_fabrica + comissao + imposto
    print(f"O custo ao consumidor é: {custo_de_fabrica}")
'''

# exercicio 38: Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a
# tabela abaixo:
'''
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print("Saudável")
elif imc >= 25 and imc <= 29.9:
    print("Peso em excesso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade Grau I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade Grau II (Severa)")
else:
    print("Obesidade Grau III (Mórbida)")
'''
# exercicio 39:
'''   
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
area *= 1.1 # 10% de folga

tinta_necessaria = area / 6

latas = -(-tinta_necessaria // 18)

galoes = -(-tinta_necessaria // 3.6)

preco_latas = latas * 80
preco_galoes = galoes * 25
preco_mistura = (latas // 1) * 80 + (-(-tinta_necessaria % 18) // 3.6) * 25

print(f"Compre {latas} latas de 18 litros. Preço: R${preco_latas:.2f}")
print(f"Compre {galoes} galões de 3,6 litros. Preço: R${preco_galoes:.2f}")
print(f"Compre {int(latas)} latas e {-(-tinta_necessaria % 18) // 3.6} galões. Preço: R${preco_mistura:.2f}")
'''
# exercicio 40

valor_hora = float(input("Digite o valor que você recebe por hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario_bruto = horas * valor_hora

print(f"Salario bruto: {salario_bruto}R$")
inss = salario_bruto * 0.08
imposto = salario_bruto * 0.11
sindi  = salario_bruto * 0.05
salario_liquido = (salario_bruto - inss - imposto - sindi)
print(f"Salario liquido: {salario_liquido}R$ \nValor inss: {inss}R$ \nValor imposto de renda: {imposto}R$ \nValor sindicato: {sindi}R$")