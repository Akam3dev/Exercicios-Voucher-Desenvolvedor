from Filme import Filme

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def explodir(self):
        print(f"O filme {self.nome} teve uma explosão :0")

    def play(self): # polimorfismo
        print(f"O filme de ação: {self.nome} esta tocando")