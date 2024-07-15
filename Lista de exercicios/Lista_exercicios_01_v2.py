# exercicio 33 "Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: h = √ 𝑎 2 + 𝑏 2
# Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa e imprima o resultado dessa 
# operação"
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
x = (a * a) + (b * b)
hipotenusa = x ** 0.5
print(f"Valor da hipotenusa: {hipotenusa}")

# exercicio 34 "Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um
# cilindro circular é calculado por meio da seguinte fórmula V = π ∗ raio² ∗ altura, onde π = 3.141592."
raio = float(input("Digite o valor do raio: "))
altura = float(input("Digite o valor da altura: "))
pi = 3.141592
volume = pi * (raio * raio) * altura
print(volume)

# exercicio 35 "Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em
# vista que o desconto foi de 12%"
valor = float(input("Digite o valor: "))
desconto = valor * 0.12
valor_com_desconto = valor - desconto
print(f"O valor com desconto é: {valor_com_desconto}")

# exercicio 36 "Leia o salário de um funcionário. Calcule e imprima o valor do novo salario, sabendo que ele
# recebeu um aumento de 25%."
salario = float(input("Digite o salario: "))
aumento = salario * 0.25
salario_aumentado = salario + aumento
print(salario_aumentado)

# exercicio 37 "A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que
# da quantia total: O primeiro ganhador receberá 46%; O segundo receberá 32%; O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores."
total = 780000.00
primeiro = 0.46 * total
segundo = 0.32 * total
terceiro = total - primeiro - segundo
print(f"Quantia ganhada pelo primeiro ganhador: {primeiro}")
print(f"Quantia ganhada pelo segundo ganhador: {segundo}")
print(f"Quantia ganhada pelo terceiro ganhador: {terceiro}")

# exercicio 38 "Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o
# número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se 
# que são descontados 8% para imposto de renda."
dias_trabalhados = int(input("Digite a quantia de dias trabalhados: "))
salario = dias_trabalhados * 30
imposto = salario * 0.08
salario_com_desconto = salario - imposto
print(f"O salario com desconto é: {salario_com_desconto}")

# exercicio 39 "Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas
# no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado."
valor_hora = float(input("Digite o valor de cada hora trabalhada: "))
hora_trabalhada = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario = hora_trabalhada * valor_hora
bonus = salario * 0.10
print(f"O valor pago ao funcionario sera: {salario + bonus}")

# exercicio 40 "Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que
# esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto 
# sobre o salário-base."
salario_base = float(input("Digite a desgraça do salario do filho da puta do funcionario: "))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_base = salario_base + gratificacao - imposto
print(f"O salario do arrombado é: {salario_base}")

# exercicio 41 "Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# o total a pagar com desconto de 10%; o valor de cada parcela, no parcelamento de 3× sem juros;
# a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)"
valor_total = float(input("Digite o valor total da venda: "))
desconto = valor_total * 0.10
valor_semdesconto = valor_total
valor_total = valor_total - desconto
valor_parcela = valor_total / 3
comissao_vista = valor_total * 0.05
comissao_parcelada = valor_semdesconto * 0.05
print(f"O valor de cada parcela é: {valor_parcela}")
print(f"Valor total a ser pago com desconto: {valor_total} ")
print(f"Comissão do vendedor caso a venda for a vista: {comissao_vista}")
print(f"Comissão do vendedor caso a venda for parcelada: {comissao_parcelada}")

# exercicio 42 "Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a
# escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo."
altura_degrau = int(input("Digite a altura de cada degrau em CM: "))
altura_usuario = int(input("Digite a altura que você quer subir em CM: "))
print(f"Você precisa subir {int(altura_usuario / altura_degrau)} degraus da escada.")

# exercicio 43 "Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto
# arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança 
# (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono."
vendaspao = int(input("Digite a quantidade de pãozinhos vendidos no dia: "))
vendasbroa = int(input("Digite a quantiade de broas vendidas no dia: "))
vendaspao = vendaspao * 0.12
vendasbroa = vendasbroa * 1.50
valortotal = vendaspao + vendasbroa
print(f"Valor arrecadado com as vendas = {valortotal}R$")
poupanca = valortotal * 0.10
print(f"O valor que devera ir pra poupança: {poupanca}")

# exercicio 44 "O restaurante a kilo Bem-Bão cobra R$57,00 por cada quilo de refeição. Escreva um algoritmo
# que leia o peso do prato montado pelo cliente (em gramas) e imprima o valor a pagar. Assuma que
# a balança já desconte o peso do prato."
pratogramas = float(input("Digite a quantidade de gramas do prato: "))
pratogramas = pratogramas - 100
valor = pratogramas * (0.57 / 10)
print(f"O valor a ser pago será: {valor}R$")

# exercicio 45 "Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
# vendida respectivamente por 35, 45 e 55 reais. Construa um algoritmo em que o usuário forneça
# a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina
# informe quanto será o valor arrecadado."
camisapequena = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
camisamedia = int(input("Digite a quantidade de camisetas medias vendidas: "))
camisagrande = int(input("Digite a quantidade de camisetas grandes vendidas: "))
valor = (camisapequena * 35) + (camisamedia * 45) + (camisagrande * 55)
print(f"O valor arrecadado é: {valor}R$")

# exercicio 46 "A lanchonete do Gauchão vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias
# de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo
# ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo
# em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades
# (em quilos) de queijo, presunto e carne necessários para compra."
PESO_QUEIJO = 50
PESO_PRESUNTO = 50
PESO_HAMBURGUER = 100
quantidade_sanduiches = int(input("Quantidade de sanduíches: "))
queijo = quantidade_sanduiches * 2 * PESO_QUEIJO / 1000
presunto = quantidade_sanduiches * PESO_PRESUNTO / 1000
hamburguer = quantidade_sanduiches * PESO_HAMBURGUER / 1000
print(f"Queijo: {queijo:.2f} kg, Presunto: {presunto:.2f} kg, Hambúrguer: {hamburguer:.2f} kg")

# exercicio 47 "Uma Indústria de Peças automotivas paga R$32,50 por hora normal trabalhada, e R$44,50 por
# hora extra. Faça um algoritmo que leia a quantidade de horas normais trabalhas e a quantidade
# de horas extras. Calcule e imprima o salário bruto e o salário líquido de um determinado
# funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 11%
# do INSS."
horasnormais = int(input("Digite a quantidade de horas normais trabalhadas: "))
horasextras = int(input("Digite a quantidade de horas extras trabalhadas: "))
horasnormais = horasnormais * 32.50
horasextras = horasextras * 44.50
salario_bruto = horasnormais + horasextras
inss = salario_bruto * 0.11
salario_liquido = salario_bruto - inss
print(f"O salario bruto é: {salario_bruto}R$")
print(f"O salario liquido é: {salario_liquido}R$")
print(f"Valor do inss a pagar: {inss}")

# exercicio 48 "A granja Frangofit possui um controle automatizado de cada frango da sua produção. No pé
# direito do frango há um anel com um chip de identificação; no pé esquerdo são dois
# anéis para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa
# R$4,00 e o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da granja
# para marcar todos os seus frangos."
frangos = int(input("Digite a quantidade de frangos: "))
frangos = frangos * 11
print(f"A quantidade gasta com os frangos é: {frangos}R$")

# exercicio 49 "A fábrica de refrigerantes Frutuba vende seu produto em três formatos: lata de 350 ml,
# garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada
# quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou."
lata = int(input("Digite a quantidade de latas compradas (350 ml): "))
garrafa = int(input("Digite a quantidade de garrafas compradas (600 ml): "))
garrafonakk = int(input("Digite a quantidade de garronas compradas (2000 ml): "))
lata = lata * 350
garrafa = garrafa * 600
garrafonakk = garrafonakk * 2000
print(f"Total de ML comprados: {lata + garrafa + garrafonakk}ML")

import math
# DESAFIO 50!

x1 = int(input("Digite o ponto x1: "))
y1 = int(input("Digite o ponto y1: "))
x2 = int(input("Digite o ponto x2: "))
y2 = int(input("Digite o ponto y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"A distancia entre os pontos é: {distancia}")

if distancia > 10:
    print("Longe")
else:
    print("Perto") 
