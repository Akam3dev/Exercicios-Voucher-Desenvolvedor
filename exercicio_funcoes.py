'''
def produto(num1,num2,num3):
    soma = (num1 * num2 * num3)
    return soma

x = produto(12,12,12)
print(x)

#2
def potencia(base, expo):
    return base ** expo

y = potencia(int(input("Num1: ")), int(input("Num2: ")))
print(y)

#3 tbm
def digitos(num):
    contagem = 0
    for i in str(num):
        contagem += 1
    return contagem
print(digitos(100))

#3
def contardigito(num):
    return len(str(num))

print(contardigito(int(input("Digite o numero: "))))

#4
def iciente(x):
    if x > 0:
        return "P"
    else:
        return "N"
    
print(iciente(100))
'''
'''
#5
def somaimposto(taxa, valor):
    taxa = taxa / 100
    imposto = taxa * valor
    return valor + imposto

taxa = int(input("Digite o valor do imposto em %: "))
valor = int(input("Digite o valor: "))

print(somaimposto(taxa, valor))
'''
'''
#6
def tabelopreco(itens):
    valor = 0
    for i in range(1, itens + 1):
        valor += 1.99
        print(f"{i} - R${valor:.2f}")
    return "--- tabela de preços ---"

print(tabelopreco(50))
'''
#7 
'''
def calcsalario(valor, horas):
    if horas <= 40:
        salario = valor * horas
    else:
        salario_base = valor * 40
        salario_extra = (valor + 0.50) * (horas - 40)
        salario = salario_base + salario_extra
    return salario

print(calcsalario(1.50, 40))
'''
#8
'''
def calcular_excesso_e_multa(peso):
    excesso = peso - 50
    multa = excesso * 4
    if peso > 50:
        return(f"excesso: {excesso} kilos, multa: {multa}R$")
    else:
        return "não há excesso nem multa"
    
peso = float(input("Digite o peso: "))
print(calcular_excesso_e_multa(peso))
'''
#9

#10

#11
def mostrar(lista):
    cont = 1
    for i in lista:
        print(f"{cont}, {i}")
        cont += 1

frutas = ["pera", "uva", "maça", "mel", "banana"]
mostrar(frutas)

#12

def calcula_media(lista):
    return sum(lista) / len(lista)
 
numeros = [6,5,7,19,5,29,10,2,1,3,5,6]
x = calcula_media(numeros)
print(x)