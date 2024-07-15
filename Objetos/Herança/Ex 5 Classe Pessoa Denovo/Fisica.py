from Pessoa import Pessoa
class Fisica(Pessoa):
    def __init__(self, nome: str, tel: int, email: str, ende: str, cpf, cnpj):
        super().__init__(nome, tel, email, ende)
        
        self.cpf = cpf
        self.cnpj = cnpj

    def aplicargolpe(self):
        print(f"{self.nome} virou estelionatario e ganhou muito dinheiro")