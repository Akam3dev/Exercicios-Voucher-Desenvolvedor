from Fisica import Fisica
class Juridica(Fisica):
    def __init__(self, nome: str, tel: int, email: str, ende: str, cpf, cnpj):
        super().__init__(nome, tel, email, ende, cpf, cnpj)

    def clonarcartao(self):
        print(f"{self.nome} clonou 2050 cartões diferentes, no matagal, {self.nome} clono o cartão de 2050 homens")