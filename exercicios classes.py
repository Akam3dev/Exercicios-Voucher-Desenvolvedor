#1
'''
class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def MostrarNome(self):
        print(self.nome)

    def MudarIdade(self):
        novaidade = int(input("Digite a nova idade: "))
        self.idade = novaidade
        print(f"Nova idade: {self.idade}")

    def MostrarEndereco(self):
        print(self.endereco)

joao = Pessoa("Joao", 17, "Santo Angelo")
joao.MostrarNome()
joao.MudarIdade()
'''
#2
'''
class Livro:
    def __init__(self, nome: str, autor: str, editora: str, paginas: int):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def AlterarEditora(self):
        neweditora = input("Digite a nova editora: ")
        self.editora = neweditora
        print(self.editora)

    def QntPaginas(self):
        print("Paginas: ",self.paginas)

main_kampf = Livro("Main Kampf", "Adolf", "Auschwitz", 239)

main_kampf.AlterarEditora()
main_kampf.QntPaginas()
'''
# 3 
'''
class Aluno:
    def __init__(self, nome,ra,n1,n2,n3,n4):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def mostrarSituacao(self):
        soma = (self.n1 + self.n2 + self.n3 + self.n4) / 4
        print(soma)
        if soma >= 7:
            return "Aprovado"
        elif soma < 5:
            return "Reprovado"
        else:
            return "De exame"

joao = Aluno("Joao", 43, 1,1,6,8)
print(joao.mostrarSituacao())
'''
# 4
'''
class Banco:
    def __init__(self, nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self,quantidade):
        self.saldo = self.saldo + quantidade
        print(f"Novo saldo: {self.saldo}")

    def sacar(self, quantidade):
        if quantidade > self.saldo:
            print("Não é possivel sacar mais do que a quantidade na conta")
        else:
            if self.saldo > 0:
                self.saldo = self.saldo - quantidade
                print(f"Novo saldo: {self.saldo}")
            else:
                print("Não ha saldo suficiente para saque")

    def mostrarsaldo(self):
        print(f"Saldo da conta: {self.saldo}")
    
joao = Banco(None, None, None, 200)
joao.depositar(500)
joao.sacar(500)
joao.mostrarsaldo()
'''
#4 dois
'''
class Funcionario:
    def __init__(self, nome: str, sobrenome: str, horas_worked: int, valor_hora: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_worked = horas_worked
        self.valor_hora = valor_hora

    def NomeCompleto(self):
        print(f"{self.nome} {self.sobrenome}")

    def CalcularSalario(self):
        print(f"Salario: {self.horas_worked * self.valor_hora}R$")

    def IncrementarHora(self, hour: int):
        self.valor_hora = self.valor_hora + hour
        print("Novo valor por hora:",self.valor_hora)

joao = Funcionario("Joao", "Almeida", 10, 10)

joao.NomeCompleto()
joao.CalcularSalario()
joao.IncrementarHora(20)
'''
#5
'''
class Circulo:
    def __init__(self,raio: int):
        self.raio = raio

    def ValorRaio(self):
        print(self.raio)

    def CalcArea(self):
        area = 3.1415 * self.raio * self.raio
        print(f"Area: {area}")

    def CalcCircuferencia(self):
        circuferencia = self.raio * (2 * 3.1415)
        print(circuferencia)

blanda = Circulo(13)
blanda.CalcArea()
blanda.CalcCircuferencia()
'''
#6
'''
class Agenda:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = ""

        
    def anotar_tarefa(self, tarefa):
        if self.dia <= 30 and self.mes <= 12:
            self.anotacao = tarefa
            print(f"Tarefa anotada para {self.dia}/{self.mes}/{self.ano}: {tarefa}")
        else:
            print("da naokkkkkkkk")

    def mostrar_anotacao(self):
        if self.anotacao:
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            print(f"Nenhuma anotação para {self.dia}/{self.mes}/{self.ano}")

minha_agenda = Agenda(dia=12, mes=4, ano=2024)
minha_agenda.anotar_tarefa("Reunião às 14h")
minha_agenda.mostrar_anotacao()
'''
#7
'''
class Triangulo:
    def  __init__(self, lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def GetMaior(self):
        maior = max(self.lado1, self.lado2, self.lado3)
        print(f"Maior lado: {maior}")

    def CalcPerimetro(self):
        print(f"Perimetro: {self.lado1 + self.lado2 + self.lado3}")

ladoa = int(input("Digite o lado A: "))
ladob = int(input("Digite o lado B: "))
ladoc = int(input("Digite o lado C: "))

triangulo = Triangulo(ladoa, ladob, ladoc)
triangulo.CalcPerimetro()
triangulo.GetMaior()
'''
#8
'''
class Academia:
    def __init__(self,nome: str,idade: int,peso: float, mensalidade = 120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.mensalidade = mensalidade

        if self.idade < 18:
            self.mensalidade = 60
            print(f"{self.nome} é menor de idade e pagara {self.mensalidade}R$ por mes")
        else:
            print(f"{self.nome} pagara {self.mensalidade}$ por mes.")
    
    def CalcImc(self):
        altura = float(input("Digite a altura: "))
        imc = self.peso / (altura * altura)
        print(f"O imc de {self.nome} é: {round(imc, 2)}") # round arredonda os numero :d
aluno = Academia("joao", 16, 56,)
aluno.CalcImc()
'''
#9
'''
class Carro:
    def __init__(self, modelo: str, marca: str, cor: str, ano: int, valor: int, nivel: int, consumo = 0):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo

    def abastecer(self):
        novogas = int(input("Digite quantos litros de gasolina: "))
        self.nivel += novogas
        print(f"Novo valor: {self.nivel}L")

    def andar(self):
        andou = int(input("Digite quantos km o carro andou: "))
        valorkm = float(input("Digite o valor de gasolina por km: "))
        valorkm = valorkm * andou
        self.nivel -= valorkm
        print(f"O carro andou {andou} KM e gastou {valorkm}L de gasolina")
        print(f"Gasolina atual: {self.nivel}L")

    def calcimposto(self):
        ipva = self.valor * 2.5 / 100
        print(f"Ipva: {ipva}")


prismao = Carro("Prisma", "Chevrolet", "Preto", 2018, 63000, 100,)
prismao.calcimposto()
prismao.andar()
prismao.abastecer()
'''
'''
#10
class Notafiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0  # inicialmente o valor total é 0
        
    def obterNumero(self):
        return self.numero
    
    def obterDataEmissao(self):
        return self.data
    
    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social
        print(f"Razão social alterada para: {self.razao_social}")
    
    def calcularValorTotal(self):
 
        self.valor_total = self.valor_produtos + self.icms + self.frete + self.ipi
        print(f"Valor total da NF calculado: R$ {self.valor_total:.2f}")
'''