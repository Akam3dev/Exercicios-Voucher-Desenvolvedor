class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def bater_ponto(self):
        lista = []
        while True:
            num = int(input("Deseja bater o ponto? 1 ou 0: "))
            if num == 1 or num == 0:
                lista.append(num)
            else:
                break
vitor = Funcionario("Vitolas", 134124, 250000)
vitor.bater_ponto()