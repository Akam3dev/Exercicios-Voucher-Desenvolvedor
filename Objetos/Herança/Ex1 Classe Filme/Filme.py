class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"O filme: {self.nome} esta tocando!")