class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def GetDados(self):
        print(self.matricula)
        print(self.nome)
        print(self.idade)