class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self):
        novo = float(input("Digite o novo preço: "))
        self.preco = novo
        print(f"Novo preço: {self.preco}")

    def escolher_assento(self):
        novo = int(input("Digite o novo assento: "))
        self.assento = novo
        print(f'Novo assento: {self.assento}')

    def viajar(self):
        print("Veiculo esta viajando")