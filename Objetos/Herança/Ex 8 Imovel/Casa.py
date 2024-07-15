from Imovel import Imovel

class Casa(Imovel):
    def __init__(self, inscricao, aluguel, iptu, quartos, quintal = bool):
        super().__init__(inscricao, aluguel, iptu)