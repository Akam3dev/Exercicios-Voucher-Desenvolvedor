from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)

        self.senha = senha

    def homens(self):
        print(f"o {self.nome} gerenciou 2050 homens o diferentes, o {self.nome} vai bater o recorde mundial em gerenciar homens")