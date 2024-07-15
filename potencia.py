def calc_valor(consumo,preco):
    valor = consumo * preco
    return valor

def calc_consumo(potencia, horas,preco):
    consumo = potencia * horas / 1000
    return calc_valor(consumo, preco)

pot = int(input("Digite a potencia em KWh: "))
horas = int(input("Digite a quantidade de horas: "))
preco = float(input("Digite o preço do kwh: "))

hora = calc_consumo(pot,horas,preco)
print(hora)