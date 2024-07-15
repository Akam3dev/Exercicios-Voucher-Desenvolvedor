# 1
def potencia(num1,num2):
    for i in range(num2 + 1):
        print(f"{num1 ** i}")

potencia(2,3)

# 2
def data():
    meses = ["nada", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    day = input('Digite o dia: ')
    mes = int(input('Digite o mes: '))
    ano = input('Digite o ano: ')

    print(f"{day} de {meses[mes]} de {ano}")

data()
# 3
def negroativo(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
    
print(negroativo(-100))

# 4
def horas(seg,min,horas):
    print(f"{seg + (min * 60) + ((horas * 60) * 60)}")

horas(10, 1, 1)

# 5
def maior(num1,num2,num3):
    numeros = [num1,num2,num3]
    print(max(numeros))

maior(5,10,15)
# 6
def reverso(num):
    num = str(num)
    invertido = "".join(reversed(num))
    print(invertido)

reverso(102)

# 7
def esfera(raio):
    vol = 4 / 3 * 3.14159 + raio ** 3
    print(vol)

esfera(5)

# 8

def cilindro(alt,raio):
    volume = 3.141592 * (raio * raio) * alt
    print(volume)

cilindro(10,2)

# 9

def convertertemp(temp):
    graus = (9 / 5) * temp + 32
    print(graus)

convertertemp(70)
# 10

def media(num1, num2, num3, letra):
    if letra == "A":
        print(f"Media aritimetica: {(num1 + num2 + num3) / 3}")
    elif letra == "P":
        print(f"Media ponderada: {(5*num1 + 3*num2 + 2*num3) / (5+3+2)}")

media(5,3,2,"A")

# 11

def calcular(num1, num2, operador):
    if operador == "+":
        print(f"{num1 + num2}")
    elif operador == "-":
        print(f"{num1 - num2}")
    elif operador == "*":
        print(f"{num1 * num2}")
    elif operador == "/":
        print(f"{num1 / num2}")
    else:
        print("erro sei la")

calcular(5,5, "+")

# 12

def existentes(num1,num2):
    numeros = 0
    for i in range(num1, num2):
        numeros += i

    print(numeros)

existentes(1,5)

# 13
def exponente(num1, num2):
    resultado = 1
    for i in range(num2):
        resultado *= num1
    print(resultado)

exponente(3,3)

# 14
def carro(kilometros, consumidos):
    kmlitro = kilometros / consumidos

    if kmlitro < 8:
        print("Venda o carro!")
    elif kmlitro >= 8 and kmlitro <= 15:
        print("Êconomico!")
    elif kmlitro > 15:
        print("Super economico")
    else:
        print("erro sei la")

# 15
import random
def embaralhar(palavra):
    aleatorio = list(palavra)
    random.shuffle(aleatorio)
    aleatorio = "".join(aleatorio)
    print(aleatorio)

embaralhar("Toxicysm")

# 16
def exclamacao(num):
    for i in range(num+1):
        print("!" * i)

exclamacao(5)

# 17
def trianlateral(num):
    num -= 1
    for i in range(num + 2):
        print("*" * i)

    for i in range(num):
        print("*" * (num - i))

trianlateral(4)


# 18
import random

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)

def sorteia():
    numeros = []

    for i in range(5):
        numeros.append(random.randint(1,100))
    return somapar(numeros)

sorteia()

# 19
def triangulo(num):
    for i in range(num + 1):
        print(" " * (num - i) + "*" * (i*2 - 1))

triangulo(4)

# 20
import random
def sorteiaaluno(num):
    alunos = []
    while len(alunos) < num:
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
    x = len(alunos)
    escolher = random.randint(0, x)
    print(alunos[escolher])

sorteiaaluno(4)