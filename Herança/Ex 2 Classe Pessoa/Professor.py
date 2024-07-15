from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,materia,horas,salario):
        super().__init__(matricula, nome, idade)
        self.horas = horas
        self.materia = materia
        self.cargahoras = horas
        self.salario = salario

    def lecionar(self):
        print(f"O professor {self.nome} esta dando aula sobre {self.materia}")

    def GetDados(self):
        print(self.matricula)
        print(self.nome)
        print(self.idade)
        print(self.horas)
        print(self.materia)
        print(self.salario)