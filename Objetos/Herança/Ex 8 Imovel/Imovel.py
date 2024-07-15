class Imovel:
    def __init__(self, inscricao, aluguel, iptu):
        self.inscricao = inscricao
        self.aluguel = aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        return self.iptu
    
    def set_aluguel(self,valor):
        self.aluguel = valor
        return self.aluguel