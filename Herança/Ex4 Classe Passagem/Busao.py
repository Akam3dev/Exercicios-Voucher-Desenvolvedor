from Passagem import Passagem

class Busao(Passagem):
    def __init__(self, preco, assento, placa, leitor):
        super().__init__(preco, assento)

        self.placa = placa
        self.leitor = leitor

    def viajar(self):
        print(f"Busão esta viajando")

    