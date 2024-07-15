class Pessoa:
    def __init__(self, nome: str, tel: int, email: str,ende: str):
        self.nome = nome
        self.telefone = tel
        self.email = email
        self.endereco = ende

    def negociar(self):
        print(f"{self.nome} esta negrociando 🤑🤑🤑🤑")