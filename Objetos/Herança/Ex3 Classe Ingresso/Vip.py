from Ingreso import Ingresso

class Vip(Ingresso):
    def __init__(self, preco, setor, open_bar = bool, open_food = bool, estacionamento = bool):
        super().__init__(preco, setor)

        self.openbar = open_bar
        self.openfood = open_food
        self.estacionamento = estacionamento

    def PegarBebida(self):
        if self.openbar == True:
            print("Você pegou uma bebida")
        else:
            print("Você não pode pegar bebidas")

    def camarote(self):
        print("Você acessou o camarote")