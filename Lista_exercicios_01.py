pi = 3.1415
# Exercício 1: Faça um programa que leia um número inteiro e o imprima
num = int(input("Digite um número inteiro: "))
print(num)

# Exercício 2: Faça um programa que leia um número real e o imprima
num = float(input("Digite um número real: "))
print(num)

# Exercício 3: Peça ao usuário para digitar três valores inteiros e imprima a soma deles
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
z = int(input("Digite mais um número: "))
print(x + y + z)

# Exercício 4: Leia um número real e imprima o resultado do quadrado desse número
n1 = float(input("Digite um número real: "))
print(f"O quadrado é: {n1 ** 2}")

# Exercício 5: Leia um número real e imprima a quinta parte deste número
n1 = float(input("Digite um número real: "))
print("A quinta parte deste número é: ", n1 * 1/5)

# Exercício 6: Leia um número inteiro e imprima o seu antecessor e o seu sucessor
n1 = int(input("Digite um número inteiro: "))
print("Antecessor: ", n1 - 1)
print("Sucessor: ", n1 + 1)

# Exercício 7: Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
n1 = int(input("Digite um número inteiro: "))
antecessor = (n1 * 2) - 1
sucessor = (n1 * 3) + 1
print(antecessor + sucessor)

# Exercício 8: Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = ano_atual - idade
print(f"Seu ano de nascimento: {ano_nascimento}")

# Exercício 9: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit
temperaturac = float(input("Digite a temperatura em Celsius: "))
temperaturaf = (temperaturac * 1.8) + 32
print(temperaturaf)

# Exercício 10: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius
tempfahr = float(input("Digite a temperatura em Fahrenheit: "))
tempcelsius = (tempfahr - 32) * 5.0 / 9.0
print(tempcelsius)

# Exercício 11: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius
tempkelvin = float(input("Digite a temperatura em Kelvin: "))
tempcelsius = tempkelvin - 273.15
print(f"A temperatura em Celsius é: {tempcelsius}")

# Exercício 12: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin
tempcelsius = float(input("Digite a temperatura em Celsius: "))
tempkelvin = tempcelsius + 273.15
print(f"A temperatura convertida para Kelvin é: {tempkelvin}")

# Exercício 13: Leia uma velocidade em km/h e apresente-a convertida em m/s
km_hora = float(input("Digite a velocidade em km/h: "))
mt_porsegundo = km_hora / 3.6
print(f"A velocidade em metros/s é: {mt_porsegundo}")

# Exercício 14: Leia uma velocidade em m/s e apresente-a convertida em km/h
metrosporsegundo = float(input("Digite a velocidade em m/s: "))
kilometrosporhora = metrosporsegundo * 3.6
print(f"A velocidade convertida em quilômetros por hora é: {kilometrosporhora}")

# Exercício 15: Leia uma distância em milhas e apresente-a convertida em quilômetros
milhas = float(input("Digite a quantidade de milhas: "))
quilometros = 1.61 * milhas
print(f"A quantidade de milhas convertida para quilômetros é: {quilometros}")

# Exercício 16: Leia uma distância em quilômetros e apresente-a convertida em milhas
quilometros = float(input("Digite a distância em quilômetros: "))
milhas = quilometros / 1.61
print(f"{quilometros} km convertidos em milhas são: {milhas}")

# Exercício 17: Leia um ângulo em graus e apresente-o convertido em radianos
angulo = float(input("Digite o ângulo em graus: "))
radiano = (angulo * pi) / 180
print(f"O ângulo em radianos é: {radiano}")

# Exercício 18: Leia um ângulo em radianos e apresente-o convertido em graus
angulorad = float(input("Digite um ângulo em radianos: "))
graus = (angulorad * 180) / pi
print(f"O ângulo em graus é: {graus}")

# Exercício 19: Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros
polegadas = float(input("Digite o comprimento em polegadas: "))
centimetros = polegadas * 2.54
print(f"O comprimento em centímetros é: {centimetros}")

# Exercício 20: Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas
valorcm = float(input("Digite o valor em centímetros: "))
valorpol = (valorcm / 2.54)
print(f"O valor convertido para polegadas é: {valorpol}")

# Exercício 21: Leia um valor de volume em metros cúbicos e apresente-o convertido em litros
metros = float(input("Digite o valor em metros cúbicos: "))
litros = 1000 * metros
print(f"O valor convertido em litros é: {litros}")

# Exercício 22: Leia um valor de volume em litros e apresente-o convertido em metros cúbicos
litros = float(input("Digite o valor em litros: "))
metros = (litros / 1000)
print(f"O valor em metros cúbicos é: {metros}")

# Exercício 23: Leia um valor de massa em quilogramas e apresente-o convertido em libras
quilos = float(input("Digite o valor em quilogramas: "))
libras = quilos / 0.45
print(f"O valor convertido em libras é: {libras}")

# Exercício 24: Leia um valor de massa em libras e apresente-o convertido em quilogramas
libras = float(input("Digite o valor em libras: "))
quilos = libras * 0.45
print(f"O valor convertido em quilogramas é: {quilos}")

# Exercício 25: Leia um valor de comprimento em jardas e apresente-o convertido em metros
jardas = float(input("Digite o valor em jardas: "))
metros = 0.91 * jardas
print(f"O valor convertido em metros é: {metros}")

# Exercício 26: Leia um valor de comprimento em metros e apresente-o convertido em jardas
metros = float(input("Digite o valor em metros: "))
jardas = (metros / 0.91)
print(f"O valor convertido em jardas é: {jardas}")

# Exercício 27: Leia um valor de área em metros quadrados e apresente-o convertido em hectares
mtquadrado = float(input("Digite o valor em metros quadrados: "))
hectares = mtquadrado * 0.0001
print(f"O valor convertido em hectares é: {hectares}")

# Exercício 28: Leia um valor de área em hectares e apresente-o convertido em metros quadrados
hectares = float(input("Digite o valor em hectares: "))
mtquadrado = hectares * 10000
print(f"O valor convertido em metros quadrados é: {mtquadrado}")

# Exercício 29: Leia três valores e apresente como resultado a soma dos quadrados dos três valores lidos
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
res = (n1 * n1) + (n2 * n2) + (n3 * n3)
print(f"A soma dos quadrados dos três valores é: {res}")

# Exercício 30: Leia quatro notas, calcule a média aritmética e imprima o resultado
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média das notas é: {media}")

# Exercício 31: Leia um valor em reais e a cotação do dólar. Imprima o valor correspondente em dólares
real = float(input("Digite o valor em reais: "))
dollar = float(input("Digite a cotação do dólar: "))
print(f"O valor convertido é: {real * dollar}")

# Exercício 32: Leia o valor do raio de um círculo e calcule a área do círculo correspondente
raio = float(input("Digite o raio do círculo: "))
area = pi * raio * raio
print(f"A área do círculo é: {area}")
