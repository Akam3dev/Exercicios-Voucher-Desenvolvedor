from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas=list):
        super().__init__(matricula, nome, idade)

        self.notas = notas

    def media(self):
        media = sum(self.notas) / len(self.notas)
        print(f"Media do aluno = {media}")

    def estudar(self):
        print(f"O aluno {self.nome} esta estudando.")