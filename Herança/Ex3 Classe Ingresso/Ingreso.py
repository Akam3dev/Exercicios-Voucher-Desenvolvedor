class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def AlterarPreco(self,novo):
        self.preco = novo
        print(f"Preço novo: {self.preco}")

    def MostrarSetor(self):
        print(f"Setor: {self.setor}")