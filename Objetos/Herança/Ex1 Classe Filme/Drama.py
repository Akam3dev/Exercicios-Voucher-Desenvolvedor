from Filme import Filme

class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def chorar(self):
        print(f"Assistiu o filme: {self.nome} e chorou!")

    def play(self): # polimorfismo
        print(f"O filme de drama: {self.nome} esta tocando")