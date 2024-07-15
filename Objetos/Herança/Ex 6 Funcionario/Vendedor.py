from Funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)

        self.comissao = comissao

    def bater_meta(self,vendas, meta):
        if vendas < meta:
            print(f"Você ainda precisa de {meta - vendas} vendas para bater a meta")
        else:
            print("Você ja bateu a meta")